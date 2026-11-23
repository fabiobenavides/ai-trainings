# 02 — LangChain + xAI Grok

Minimal lab: a Python helper that sends a prompt to Grok via LangChain `ChatXAI`.

```text
02-langchain-xai/
  client.py        # shared get_response(prompt, temperature=0)
  main.py          # hello demo
  books.py         # 10 Christian books (title, author, year)
  vacation.py      # multi-step beach vacation plan
  ages_cot.py      # chain-of-thought age problem
  self_consistency.py  # self-consistency: several CoT samples, majority vote
  zero_shot.py     # zero-shot sentiment of a Spanish review
  one_shot.py      # one-shot version of the same review
  few_shot.py      # few-shot version of the same review
  pyproject.toml
  .env.example
```

The three `*_shot.py` scripts classify the same mixed product review. Run them in order and compare: zero-shot has no examples (free-form answer), one-shot shows a single positive example of a strict label format, and few-shot adds positive, negative, and mixed examples.

`self_consistency.py` complements `ages_cot.py`: it asks the same chain-of-thought question several times at a higher temperature and keeps the majority final answer.

---

## Español

### Requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- Una API key de [xAI](https://console.x.ai/)

### Setup

```bash
cd prompts-engineer/02-langchain-xai
uv sync
```

### Variables de entorno

Copia `.env.example` o exporta la key en tu shell:

```powershell
$env:XAI_API_KEY = "xai-..."
# Opcional:
# $env:LAB_MODEL = "grok-4"
```

```bash
export XAI_API_KEY="xai-..."
# Optional:
# export LAB_MODEL="grok-4"
```

### Ejecutar

```bash
uv run python main.py
uv run python books.py
uv run python vacation.py
uv run python ages_cot.py
uv run python self_consistency.py
uv run python zero_shot.py
uv run python one_shot.py
uv run python few_shot.py
```

`client.get_response(prompt, temperature=0)` usa LangChain `ChatXAI` y lo reutilizan los scripts del lab. El parámetro `temperature` es opcional y no cambia el comportamiento de los demás scripts.

Los scripts `zero_shot.py`, `one_shot.py` y `few_shot.py` clasifican la misma reseña de producto en español. Compáralos: sin ejemplos la respuesta suele ser libre; con un ejemplo (positivo) el modelo copia el formato `SENTIMIENTO` / `CONFIANZA` / `MOTIVO`; con varios ejemplos (positivo, negativo y mixto) también cubre el caso mixto.

`self_consistency.py` complementa `ages_cot.py`: hace la misma pregunta de razonamiento varias veces con temperatura más alta, extrae cada `RESPUESTA FINAL` y se queda con la que más se repite. El problema es un caracol en un pozo (sube de día y resbala de noche); un error común es dividir la profundidad entre el avance neto y olvidar que el último día ya no resbala.

### Si `uv` no se reconoce (Windows)

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
uv run python .\main.py
```

Sin `uv` (después de `uv sync`):

```powershell
.\.venv\Scripts\python.exe .\main.py
```

---

## English

### Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- An [xAI](https://console.x.ai/) API key

### Setup

```bash
cd prompts-engineer/02-langchain-xai
uv sync
```

### Environment variables

Copy `.env.example` or set the key in your shell:

```powershell
$env:XAI_API_KEY = "xai-..."
# Optional:
# $env:LAB_MODEL = "grok-4"
```

```bash
export XAI_API_KEY="xai-..."
# Optional:
# export LAB_MODEL="grok-4"
```

### Run

```bash
uv run python main.py
uv run python books.py
uv run python vacation.py
uv run python ages_cot.py
uv run python self_consistency.py
uv run python zero_shot.py
uv run python one_shot.py
uv run python few_shot.py
```

`client.get_response(prompt, temperature=0)` calls LangChain `ChatXAI` and is shared by the lab scripts. The `temperature` parameter is optional and leaves the other scripts unchanged.

`zero_shot.py`, `one_shot.py`, and `few_shot.py` classify the same Spanish product review. Compare them: with no examples the answer is usually free-form; one positive example teaches the strict `SENTIMIENTO` / `CONFIANZA` / `MOTIVO` format; a few examples (positive, negative, and mixed) also cover the mixed case.

`self_consistency.py` complements `ages_cot.py`: it asks the same reasoning question several times at a higher temperature, extracts each `RESPUESTA FINAL`, and keeps the majority answer. The problem is a snail in a well (it climbs by day and slips at night); a common mistake is dividing depth by the net daily gain and forgetting that it does not slip on the last day.

### If `uv` is not recognized (Windows)

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
uv run python .\main.py
```

Without `uv` (after `uv sync`):

```powershell
.\.venv\Scripts\python.exe .\main.py
```
