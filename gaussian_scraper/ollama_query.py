from __future__ import annotations

import requests

from gaussian_scraper.sources import GAUSSIAN_KEYWORDS

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"
REQUEST_TIMEOUT_SEC = 30

_PROMPT_TEMPLATE = """\
You are a concise technical assistant specializing in Gaussian and HPC environments. \
Answer the following question in 2-4 sentences. Focus on practical, accurate information \
a computational chemistry researcher would find useful.

Question: {topic}

Answer:"""


def is_gaussian_query(text: str) -> bool:
    """
    Return True if the given text appears to be asking about Gaussian
    or a related HPC/computational chemistry topic.

    Uses the same keyword list as the scraper so the two stay in sync.
    """
    lower = text.lower()
    return any(kw.lower() in lower for kw in GAUSSIAN_KEYWORDS)


def query_gaussian(topic: str, model: str = OLLAMA_MODEL) -> str | None:
    """
    Ask a local Ollama instance a direct question about Gaussian and return
    its answer as a plain string.

    Intended as a live fallback for when the scraped JSON does not contain
    a good match for the user's query. Returns None if Ollama is not reachable
    or returns an unexpected response.
    """
    if not topic or not topic.strip():
        return None

    prompt = _PROMPT_TEMPLATE.format(topic=topic.strip())

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=REQUEST_TIMEOUT_SEC,
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    answer = data.get("response", "").strip()
    return answer if answer else None
