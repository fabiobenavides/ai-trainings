# 01 — Intro: OpenAI `get_response`

Minimal lab: a Python helper that sends a prompt to OpenAI and returns the text reply.

```text
01-intro/
  main.py          # get_response(prompt) + demo
  pyproject.toml
  .env.example
```

---

## Español

### Requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- Una API key de OpenAI

### Setup

```bash
cd prompts-engineer/01-intro
uv sync
```

### Variables de entorno

Copia `.env.example` o exporta la key en tu shell:

```powershell
$env:OPENAI_API_KEY = "sk-..."
# Opcional:
# $env:LAB_MODEL = "gpt-4.1-mini"
```

```bash
export OPENAI_API_KEY="sk-..."
# Optional:
# export LAB_MODEL="gpt-4.1-mini"
```

### Ejecutar

```bash
uv run python main.py
```

La función `get_response(prompt)` llama a Chat Completions y devuelve el texto de la respuesta.

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
- An OpenAI API key

### Setup

```bash
cd prompts-engineer/01-intro
uv sync
```

### Environment variables

Copy `.env.example` or set the key in your shell:

```powershell
$env:OPENAI_API_KEY = "sk-..."
# Optional:
# $env:LAB_MODEL = "gpt-4.1-mini"
```

```bash
export OPENAI_API_KEY="sk-..."
# Optional:
# export LAB_MODEL="gpt-4.1-mini"
```

### Run

```bash
uv run python main.py
```

`get_response(prompt)` calls Chat Completions and returns the reply text.

### If `uv` is not recognized (Windows)

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
uv run python .\main.py
```

Without `uv` (after `uv sync`):

```powershell
.\.venv\Scripts\python.exe .\main.py
```
