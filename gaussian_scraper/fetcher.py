from __future__ import annotations

import time
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

# How long to wait for a page to respond before giving up.
REQUEST_TIMEOUT_SEC = 10

# Seconds to wait between fetching pages to avoid rate limiting.
REQUEST_DELAY_SEC = 2

# Realistic browser User-Agent to avoid bot detection on documentation sites.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

# Tags that contain visible documentation content.
# skip nav, header, footer, and script tags as they contain UI noise.
CONTENT_TAGS = ["p", "li", "pre", "code", "h1", "h2", "h3", "h4"]


def _extract_pdf_text(pdf_bytes: bytes) -> str | None:
    """
    Extract text from a PDF's raw bytes, one line per extracted text
    fragment -- mirrors fetch_page_text's HTML behavior of one line per
    content piece, so downstream keyword-density scoring works the same
    way regardless of where the text came from.

    Returns None if extraction fails or yields nothing -- e.g. a
    scanned/image-only PDF with no embedded text layer, the PDF
    equivalent of a JS-rendered page BeautifulSoup can't see into.

    Naive extraction like this can produce out-of-reading-order text for
    multi-column layouts and repeated page headers/footers. Not solved
    here -- extract_relevant_passages's per-line keyword scoring still
    surfaces genuinely relevant lines regardless of overall document
    coherence, the same way it already tolerates messy HTML extraction.
    """
    try:
        reader = PdfReader(BytesIO(pdf_bytes))
        text = "\n".join(page.extract_text() for page in reader.pages)
    except Exception:
        return None
    return text if text.strip() else None


def fetch_page_text(url: str) -> tuple[str | None, int | None]:
    """
    Fetch a URL and return its visible text content as a plain string,
    along with the HTTP status code for logging purposes. Handles both
    HTML pages and PDF documents transparently -- callers don't need to
    know which one a URL points to.

    Steps:
    - Wait briefly between requests to avoid rate limiting
    - Make an HTTP GET request with a realistic browser User-Agent header
    - If the response is a PDF (by Content-Type or .pdf URL suffix),
      extract its text directly from the raw bytes
    - Otherwise, parse the HTML with BeautifulSoup and extract text only
      from content-bearing tags
    - Return a single string with one line per extracted piece

    Returns (None, None) if the request fails due to a network error.
    Returns (None, status_code) if the server responds with a non-200 status.
    Returns (text, 200) on success.
    """
    time.sleep(REQUEST_DELAY_SEC)

    try:
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"User-Agent": USER_AGENT},
        )
    except requests.RequestException:
        return None, None

    if response.status_code != 200:
        return None, response.status_code

    content_type = response.headers.get("Content-Type", "")
    if "application/pdf" in content_type or url.lower().endswith(".pdf"):
        return _extract_pdf_text(response.content), 200

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove script and style tags so their text doesn't pollute the output.
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    lines = []
    for tag in soup.find_all(CONTENT_TAGS):
        text = tag.get_text(separator=" ", strip=True)
        if text:
            lines.append(text)

    return ("\n".join(lines) if lines else None), 200
