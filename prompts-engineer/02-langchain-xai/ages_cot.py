"""Lab 02: chain-of-thought prompt for a simple age reasoning problem."""

from __future__ import annotations

from client import get_response, require_api_key


def main() -> None:
    require_api_key()
    prompt = """
Solve this step by step. Show your reasoning before the final answer.
Respond in Spanish.

Problem:
My friend is 20 years old right now.
His father currently has twice my friend's age.
How old will the father be in 10 years?

Think through each step carefully (friend's current age → father's current age → father's age in 10 years).
End with a single clear final answer.
""".strip()
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
