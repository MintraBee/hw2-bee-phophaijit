import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env file")

client = genai.Client(api_key=api_key)

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
    full_prompt = f"{PROMPT}\n\nInput:\n{user_input}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    return response.text

if __name__ == "__main__":
    sample_input = """
    We may have gaps in state-level compliance for remote employees in California and New York.
    Need to confirm payroll tax handling before next payroll cycle.
    """

    result = analyze_note(sample_input)

    print("\n=== INPUT ===\n")
    print(sample_input.strip())

    print("\n=== OUTPUT ===\n")
    print(result)