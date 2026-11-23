"""Lab 02: few-shot sentiment classification of a Spanish product review."""

from __future__ import annotations

from client import get_response, require_api_key

# Same review as zero_shot.py and one_shot.py, so you can compare outputs.
# Few-shot: several examples cover positivo, negativo, and mixto, so the model
# can copy both the strict format and the mixed-review case.
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

Ejemplo 1:
Reseña: La cafetera es fácil de usar y el café queda riquísimo. Lleva un mes conmigo y no he tenido ningún problema.
SENTIMIENTO: positivo
CONFIANZA: alta
MOTIVO: Elogia el uso y el sabor, y no reporta fallas.

Ejemplo 2:
Reseña: El auricular se rompió a la semana y el soporte no responde los correos.
SENTIMIENTO: negativo
CONFIANZA: alta
MOTIVO: Falló pronto y no hubo soporte.

Ejemplo 3:
Reseña: La mochila es muy cómoda y se ve bien, aunque la cremallera se atora un poco.
SENTIMIENTO: mixto
CONFIANZA: media
MOTIVO: Valora comodidad y diseño, pero critica la cremallera.

Ahora clasifica esta reseña. No agregues ningún otro texto.
Reseña: {REVIEW}
""".strip()
    print(f"Prompt: {prompt}")
    print(f"Response: {get_response(prompt)}")


if __name__ == "__main__":
    main()
