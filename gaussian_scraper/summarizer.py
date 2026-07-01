from __future__ import annotations

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_HEALTH_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3"
REQUEST_TIMEOUT_SEC = 30

# Maximum number of passages to include in a single summarization prompt.
# The extractor already ranks passages by relevance (first match wins),
# so the top 5 are the most useful. Keeping prompts short improves
# summary quality and reduces Ollama response time.
MAX_PASSAGES_TO_SUMMARIZE = 5

_PROMPT_TEMPLATE = """\
You are a concise technical assistant. Summarize the following passages from \
{source} in 2-3 sentences. Focus on what a researcher \
would find practically useful.

Passages:
{passages}

Summary:"""


def is_ollama_available() -> bool:
    """
    Return True if a local Ollama instance is reachable.
    Uses a lightweight GET to the root endpoint rather than a full generate call.
    """
    try:
        response = requests.get(OLLAMA_HEALTH_URL, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def summarize_passages(
    passages: list[str],
    label: str = "HPC documentation about Gaussian",
    model: str = OLLAMA_MODEL,
) -> str | None:
    """
    Send passages to a local Ollama instance and return a short summary.

    Args:
        passages: List of text passages to summarize.
        label: Source label included in the prompt so Ollama has context
               about where the passages came from.
        model: Ollama model to use.

    Returns None if Ollama is not reachable or returns an unexpected response,
    so the caller can store passages without a summary rather than failing.
    """
    if not passages:
        return None

    prompt = _PROMPT_TEMPLATE.format(
        source=label,
        passages="\n".join(f"- {p}" for p in passages[:MAX_PASSAGES_TO_SUMMARIZE]),
    )

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

    summary = data.get("response", "").strip()
    return summary if summary else None
