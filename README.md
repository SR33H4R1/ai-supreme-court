# AI Supreme Court

A small LangChain project that turns a topic into a short courtroom-style debate:

- one AI argument for the topic
- one AI argument against the topic
- one judge-style verdict in structured output

The original idea started as a notebook experiment in `AI_Supreme_Court.ipynb`. This repository adds a reusable Python entrypoint so the project is easier to run, share, and understand on GitHub.

## What this project shows

This is a beginner portfolio project focused on applied LLM engineering. It shows:

- prompt chaining with LangChain
- multi-step reasoning flow
- structured output using a schema
- local model usage with Ollama
- moving from notebook prototype to a simple runnable project

## Tech stack

- Python
- LangChain
- Ollama
- Jupyter Notebook

## Project structure

```text
.
|-- AI_Supreme_Court.ipynb
|-- main.py
|-- requirements.txt
|-- README.md
`-- src/
    |-- __init__.py
    `-- ai_supreme_court.py
```

## Setup

1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure [Ollama](https://ollama.com/) is installed and the model is available locally:

```bash
ollama pull llama3.1
```

## Run

```bash
python main.py --topic "Artificial intelligence in healthcare"
```

If you want machine-readable output:

```bash
python main.py --topic "AI in education" --json
```

## Example use cases

- Should AI be used in healthcare?
- Should social media be regulated more heavily?
- Should coding be taught in school from an early age?

## Why this is on GitHub

This is not a large production system. It is a clean learning project that demonstrates how to build a small LLM application with structure instead of a single prompt.

## Next improvements

- add a small Streamlit interface
- support multiple rounds of debate
- save verdict history
- add tests around topic normalization and result formatting
- compare outputs across different Ollama models
