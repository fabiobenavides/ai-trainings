"""Intro lab: send a prompt to OpenAI and return the text reply."""

from __future__ import annotations

import os
import sys

from openai import OpenAI

DEFAULT_MODEL = "gpt-4.1-mini"


def get_response(prompt: str) -> str:
    """Call OpenAI Chat Completions with ``prompt`` and return the reply text."""
    client = OpenAI()
    response = client.chat.completions.create(
        model=os.getenv("LAB_MODEL", DEFAULT_MODEL),
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        print(
            "OPENAI_API_KEY is required. Set it in your environment and try again.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    prompt = "Say hello in one short sentence."
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
