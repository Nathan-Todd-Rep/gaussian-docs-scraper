from __future__ import annotations

import time

import requests
from bs4 import BeautifulSoup

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


def fetch_page_text(url: str) -> tuple[str | None, int | None]:
    """
    Fetch a URL and return its visible text content as a plain string,
    along with the HTTP status code for logging purposes.

    Steps:
    - Wait briefly between requests to avoid rate limiting
    - Make an HTTP GET request with a realistic browser User-Agent header
    - Parse the HTML with BeautifulSoup
    - Extract text only from content-bearing tags
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
