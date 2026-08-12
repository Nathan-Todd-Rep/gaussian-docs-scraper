from __future__ import annotations

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_HEALTH_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3"

# CPU-only local inference is slow and varies a lot run to run -- real testing
# against a freshly-pulled llama3 model saw single summarization calls take
# anywhere from ~23s to ~32s, with a cold model load alone taking ~27s. A
# short timeout here doesn't fail loudly, it fails *silently*: summarize_passages()
# catches the timeout and returns None, so a slow-but-working Ollama looks
# identical to a broken one ("SKIPPED - no response from Ollama"). 120s gives
# real CPU inference enough headroom without waiting forever on a genuinely
# hung request.
REQUEST_TIMEOUT_SEC = 120

# Maximum number of passages to include in a single summarization prompt.
# The extractor already ranks passages by keyword-match score, so the top
# 5 are the most keyword-dense. Keeping prompts short improves summary
# quality and reduces Ollama response time.
MAX_PASSAGES_TO_SUMMARIZE = 5

# This data feeds a scientific HPC assistant, so the prompt explicitly
# forbids adding anything not present in the passages. A summary that
# sounds confident but includes fabricated details (a made-up flag, a
# wrong default value) is worse than no summary at all -- accuracy over
# fluency is the priority here.
_PROMPT_TEMPLATE = """\
You are a precise technical summarizer. Summarize ONLY the information \
explicitly stated in the passages below, from {source}, in 2-3 sentences.

Rules:
- Do not add any fact, detail, or context that is not directly stated in the passages.
- Do not rely on outside knowledge about this topic, even if you believe it to be correct.
- If the passages do not contain enough information for a useful summary, say so plainly rather than guessing.
- Focus on what a researcher would find practically useful (e.g. commands, settings, requirements).

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
    timeout: float = REQUEST_TIMEOUT_SEC,
) -> str | None:
    """
    Send passages to a local Ollama instance and return a short summary.

    Args:
        passages: List of text passages to summarize.
        label: Source label included in the prompt so Ollama has context
               about where the passages came from.
        model: Ollama model to use.
        timeout: Seconds to wait for a response before giving up. CPU-only
                 inference can be slow (see REQUEST_TIMEOUT_SEC) -- too short
                 a value here means a slow-but-working Ollama silently looks
                 identical to a broken one.

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
            timeout=timeout,
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
