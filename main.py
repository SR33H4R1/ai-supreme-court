from __future__ import annotations

import argparse
import json

from src.ai_supreme_court import run_case


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a simple AI courtroom debate and verdict."
    )
    parser.add_argument(
        "--topic",
        required=True,
        help='Debate topic, for example: "AI in education".',
    )
    parser.add_argument(
        "--model",
        default="llama3.1",
        help="Local Ollama model name to use.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full result as JSON.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_case(topic=args.topic, model_name=args.model)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(f"Topic: {result['topic']}")
    print()
    print("For:")
    print(result["pro_argument"])
    print()
    print("Against:")
    print(result["con_argument"])
    print()
    print("Verdict:")
    print(result["verdict_data"]["verdict"])
    print()
    print("Reasoning:")
    print(result["verdict_data"]["reasoning"])


if __name__ == "__main__":
    main()

