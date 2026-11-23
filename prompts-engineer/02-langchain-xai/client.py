"""Shared xAI Grok helper for lab 02 scripts."""

from __future__ import annotations

import os
import sys

from langchain_xai import ChatXAI

DEFAULT_MODEL = "grok-4"


def require_api_key() -> None:
    """Exit if ``XAI_API_KEY`` is missing."""
    if not os.environ.get("XAI_API_KEY", "").strip():
        print(
            "XAI_API_KEY is required. Set it in your environment and try again.",
            file=sys.stderr,
        )
        raise SystemExit(1)


def get_response(prompt: str, temperature: float = 0) -> str:
    """Call Grok through LangChain ChatXAI and return the reply text.

    ``temperature`` defaults to 0 so existing lab scripts stay deterministic.
    """
    llm = ChatXAI(
        model=os.getenv("LAB_MODEL", DEFAULT_MODEL),
        temperature=temperature,
    )
    message = llm.invoke(prompt)
    content = message.content
    if isinstance(content, list):
        return "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in content
        )
    return content or ""
