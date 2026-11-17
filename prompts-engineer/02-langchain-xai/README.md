# 02 — LangChain + xAI Grok

Minimal lab: a Python helper that sends a prompt to Grok via LangChain `ChatXAI`.

```text
02-langchain-xai/
  client.py        # shared get_response(prompt)
  main.py          # hello demo
  books.py         # 10 Christian books (title, author, year)
  vacation.py      # multi-step beach vacation plan
  pyproject.toml
  .env.example
```

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
```

`client.get_response(prompt)` usa LangChain `ChatXAI` y lo reutilizan `main.py`, `books.py` y `vacation.py`.

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
```

`client.get_response(prompt)` calls LangChain `ChatXAI` and is shared by `main.py`, `books.py`, and `vacation.py`.

### If `uv` is not recognized (Windows)

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
uv run python .\main.py
```

Without `uv` (after `uv sync`):

```powershell
.\.venv\Scripts\python.exe .\main.py
```
