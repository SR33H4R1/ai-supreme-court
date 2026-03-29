# AI Supreme Court

AI Supreme Court is a small LangChain project that takes a topic, generates one argument for it, one argument against it, and returns a judge-style verdict in structured output.

The project began as a notebook prototype in `AI_Supreme_Court.ipynb` and is also available as a simple Python script through `main.py`.

## How it works

1. Accept a topic as input.
2. Normalize the topic text.
3. Generate a brief argument for the topic.
4. Generate a brief argument against the topic.
5. Pass both sides to a judge chain.
6. Return a verdict and reasoning as a structured object.

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

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure [Ollama](https://ollama.com/) is installed and the model is available locally:

```bash
ollama pull llama3.1
```

## Run

```bash
python main.py --topic "Artificial intelligence in healthcare"
```

For JSON output:

```bash
python main.py --topic "AI in education" --json
```

## Example output

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

## Notes

- The script uses a local Ollama model.
- The default model is `llama3.1`.
- Output quality depends on the model used.

## Possible improvements

- add multi-round debate
- store verdict history
- add a small web interface
- compare outputs across different local models
