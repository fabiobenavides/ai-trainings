"""Lab 02: one-shot sentiment classification of a Spanish product review."""

from __future__ import annotations

from client import get_response, require_api_key

# Same review as zero_shot.py and few_shot.py, so you can compare outputs.
# One-shot: a single example teaches the label format. Here the example is
# clearly positive, so the mixed target review may still be labeled inconsistently.
REVIEW = (
    "El teléfono llegó rápido y la pantalla se ve increíble, "
    "pero la batería apenas dura medio día y el cargador no estaba en la caja. "
    "No sé si lo recomendaría."
)


def main() -> None:
    require_api_key()
    prompt = f"""
Clasifica el sentimiento de la reseña. Usa exactamente este formato:

SENTIMIENTO: positivo|negativo|mixto
CONFIANZA: alta|media|baja
MOTIVO: una frase corta

Ejemplo:
Reseña: La cafetera es fácil de usar y el café queda riquísimo. Lleva un mes conmigo y no he tenido ningún problema.
SENTIMIENTO: positivo
CONFIANZA: alta
MOTIVO: Elogia el uso y el sabor, y no reporta fallas.

Ahora clasifica esta reseña. No agregues ningún otro texto.
Reseña: {REVIEW}
""".strip()
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
