"""Lab 02: send a prompt to xAI Grok via LangChain and return the text reply."""

from __future__ import annotations

import os
import sys

from langchain_xai import ChatXAI

DEFAULT_MODEL = "grok-4"


def get_response(prompt: str) -> str:
    """Call Grok through LangChain ChatXAI and return the reply text."""
    llm = ChatXAI(
        model=os.getenv("LAB_MODEL", DEFAULT_MODEL),
        temperature=0,
    )
    message = llm.invoke(prompt)
    content = message.content
    if isinstance(content, list):
        return "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in content
        )
    return content or ""


def main() -> None:
    if not os.environ.get("XAI_API_KEY", "").strip():
        print(
            "XAI_API_KEY is required. Set it in your environment and try again.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    prompt = "Say hello in one short sentence."
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
