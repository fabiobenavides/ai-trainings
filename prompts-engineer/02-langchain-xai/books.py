"""Lab 02: ask Grok for a structured list of Christian books."""

from __future__ import annotations

from client import get_response, require_api_key


def main() -> None:
    require_api_key()
    prompt = (
        "List the 10 best Christian books. "
        "Respond in English. "
        "For each book include title, author, and year. "
        "Use a numbered list."
    )
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
