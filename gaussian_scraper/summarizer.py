from __future__ import annotations

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"
REQUEST_TIMEOUT_SEC = 30

_PROMPT_TEMPLATE = """\
You are a concise technical assistant. Summarize the following passages from \
HPC documentation about Gaussian in 2-3 sentences. Focus on what a researcher \
would find practically useful.

Passages:
{passages}

Summary:"""


def summarize_passages(passages: list[str], model: str = OLLAMA_MODEL) -> str | None:
    """
    Send passages to a local Ollama instance and return a short summary.

    Returns None if Ollama is not reachable or returns an unexpected response,
    so the caller can store passages without a summary rather than failing.
    """
    if not passages:
        return None

    prompt = _PROMPT_TEMPLATE.format(passages="\n".join(f"- {p}" for p in passages))

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
