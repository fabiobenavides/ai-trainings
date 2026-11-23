"""Lab 02: self-consistency over several chain-of-thought samples."""

from __future__ import annotations

import re
from collections import Counter

from client import get_response, require_api_key

# Self-consistency: sample the same CoT prompt several times at a higher
# temperature, then majority-vote the final answers. One noisy chain can
# be wrong; the most frequent answer is usually more reliable.
N_SAMPLES = 5
TEMPERATURE = 0.7

# A slightly tricky well problem: the last day it climbs out and does not
# slip. A common mistake is dividing depth by the net daily gain (13 / 2).
PROMPT = """
Solve this step by step. Show your reasoning before the final answer.
Respond in Spanish.

Problem:
A snail is at the bottom of a 13-meter well.
Each day it climbs 5 meters, but at night it slips 3 meters back.
How many days does it take to get out of the well?

Think through each day carefully. The snail does not slip once it has reached or passed the top.
End with a single line in this exact format, and nothing after it:
RESPUESTA FINAL: <número>
""".strip()

ANSWER_RE = re.compile(r"RESPUESTA FINAL:\s*(-?\d+)", re.IGNORECASE)


def extract_final_answer(text: str) -> str | None:
    """Return the last ``RESPUESTA FINAL: <n>`` value in the model output."""
    matches = list(ANSWER_RE.finditer(text))
    if not matches:
        return None
    return matches[-1].group(1)


def majority_vote(answers: list[str | None]) -> tuple[str | None, list[tuple[str, int]]]:
    """Return the majority answer and the (answer, count) tallies."""
    counts = Counter(answer for answer in answers if answer is not None)
    if not counts:
        return None, []
    return counts.most_common()[0][0], counts.most_common()


def main() -> None:
    require_api_key()
    print(f"Prompt: {PROMPT}")
    print(f"Samples: {N_SAMPLES}  Temperature: {TEMPERATURE}\n")

    answers: list[str | None] = []
    for i in range(1, N_SAMPLES + 1):
        response = get_response(PROMPT, temperature=TEMPERATURE)
        answer = extract_final_answer(response)
        answers.append(answer)
        print(f"--- Muestra {i} ---")
        print(response)
        print(f"Respuesta extraída: {answer if answer is not None else '(no se pudo leer)'}\n")

    winner, tallies = majority_vote(answers)
    print("Votos:")
    if not tallies:
        print("  (ninguna respuesta parseable)")
        print("Ganador (mayoría): (empate / sin votos)")
        return

    for answer, count in tallies:
        print(f"  {answer}: {count}")

    top_count = tallies[0][1]
    winners = [answer for answer, count in tallies if count == top_count]
    if len(winners) > 1:
        print(f"Ganador (mayoría): empate entre {', '.join(winners)}")
    else:
        print(f"Ganador (mayoría): {winner}")


if __name__ == "__main__":
    main()
