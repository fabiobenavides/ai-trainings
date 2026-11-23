"""Lab 02: zero-shot sentiment classification of a Spanish product review."""

from __future__ import annotations

from client import get_response, require_api_key

# Same review as one_shot.py and few_shot.py, so you can compare outputs.
# Zero-shot: only the instruction and the input. No examples of the expected format.
REVIEW = (
    "El teléfono llegó rápido y la pantalla se ve increíble, "
    "pero la batería apenas dura medio día y el cargador no estaba en la caja. "
    "No sé si lo recomendaría."
)


def main() -> None:
    require_api_key()
    prompt = f"""
Clasifica el sentimiento de esta reseña de producto (positivo, negativo o mixto).
Responde en español.

Reseña:
{REVIEW}
""".strip()
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
