"""Lab 02: send a prompt to xAI Grok via LangChain and return the text reply."""

from __future__ import annotations

from client import get_response, require_api_key


def main() -> None:
    require_api_key()
    prompt = "Say hello in one short sentence."
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
