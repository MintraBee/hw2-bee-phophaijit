import os
import argparse
from datetime import datetime
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("Missing ANTHROPIC_API_KEY in .env file")

client = anthropic.Anthropic(api_key=api_key)

PROMPT = """
You are a compliance operations assistant.

Convert the input into the following sections:
1. Risk
2. Action Items
3. Owner
4. Escalation Level (Low, Medium, or High)
5. Notes

Rules:
- Do not guess missing information.
- If an owner is not provided, write "Unclear".
- If the information is ambiguous, say so clearly.
- Do not provide legal advice.
- If legal confirmation is needed, state that human review is required.
"""

def analyze_note(user_input: str) -> str:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=PROMPT,
        messages=[{"role": "user", "content": user_input}]
    )
    return response.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Compliance Risk Translator")
    parser.add_argument("--input", type=str, help="Compliance note to analyze")
    parser.add_argument("--file", type=str, help="Path to a .txt file containing the note")
    parser.add_argument("--save", action="store_true", help="Save output to a file")
    args = parser.parse_args()

    if args.input:
        user_input = args.input
    elif args.file:
        with open(args.file, "r") as f:
            user_input = f.read()
    else:
        user_input = """
        We may have gaps in state-level compliance for remote employees in California and New York.
        Need to confirm payroll tax handling before next payroll cycle.
        """
        print("No input provided. Running with sample input.\n")

    result = analyze_note(user_input)

    print("\n=== INPUT ===\n")
    print(user_input.strip())
    print("\n=== OUTPUT ===\n")
    print(result)

    if args.save:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("=== INPUT ===\n\n")
            f.write(user_input.strip())
            f.write("\n\n=== OUTPUT ===\n\n")
            f.write(result)
        print(f"\nOutput saved to {filename}")

if __name__ == "__main__":
    main()