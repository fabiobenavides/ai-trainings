"""Lab 02: multi-step prompt for a beach vacation plan."""

from __future__ import annotations

from client import get_response, require_api_key


def main() -> None:
    require_api_key()
    prompt = """
Plan beach vacations by following these steps in order. Respond in Spanish.

Step 1 — Destinations:
Propose exactly four possible beach destinations.

Step 2 — Lodging:
For each destination, suggest a few lodging options (budget, mid-range, and nicer if useful).

Step 3 — Activities:
For each destination, list some activities suitable for a beach trip.

Step 4 — Pros and cons:
For each destination, give a short pros and cons evaluation.

Use clear headings per destination and keep the answer organized by the steps above.
""".strip()
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
