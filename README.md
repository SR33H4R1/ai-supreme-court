# AI Supreme Court

AI Supreme Court is a small LLM project that turns any topic into a courtroom-style debate:

- one AI argument for the topic
- one AI argument against the topic
- one judge-style verdict with structured reasoning

It started as a notebook experiment and was cleaned up into a simple Python project so it is easier to run, share, and explain on GitHub.

## Why this project is interesting

This is a beginner portfolio project, but it already shows useful applied AI engineering skills:

- prompt chaining instead of a single prompt
- multi-step reasoning flow
- structured output with a schema
- local model usage through Ollama
- moving from notebook prototype to reusable Python code

## Quick demo

Run:

```bash
python main.py --topic "Artificial intelligence in healthcare"
```

Typical output shape:

```text
Topic: Artificial intelligence in healthcare

For:
AI can improve diagnosis speed and help doctors process large amounts of medical data more accurately.

Against:
Heavy reliance on AI can reduce human judgment and create risks when systems are biased or wrong.

Verdict:
AI should be used in healthcare, but only with strong human oversight.

Reasoning:
The benefits are meaningful, but healthcare decisions still need accountability, empathy, and clinical judgment.
```

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
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure [Ollama](https://ollama.com/) is installed and the model is available locally:

```bash
ollama pull llama3.1
```

## Run

Basic run:

```bash
python main.py --topic "Artificial intelligence in healthcare"
```

JSON output:

```bash
python main.py --topic "AI in education" --json
```

## What the code does

1. Normalizes the topic input.
2. Generates one brief argument for the topic.
3. Generates one brief argument against the topic.
4. Sends both sides to a judge chain.
5. Returns a structured verdict and reasoning object.

## Example use cases

- Should AI be used in healthcare?
- Should social media be regulated more heavily?
- Should coding be taught in school from an early age?

## Why this is on GitHub

This is not a large production system. It is a clean learning project that shows how to build a small LLM application with structure, reusable code, and a clearer developer experience than a notebook alone.

## Next improvements

- add a small Streamlit interface
- support multiple rounds of debate
- save verdict history
- add tests around topic normalization and result formatting
- compare outputs across different Ollama models
