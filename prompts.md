# Prompt Iteration

## Initial Version
You are a compliance assistant. Summarize the risk described in the input and suggest next steps.

What changed:
I started with a simple baseline prompt to see how the model would respond with minimal structure.

What improved, stayed the same, or got worse:
The output was readable, but it was too general and did not consistently separate risks, actions, owners, or escalation clearly.

---

## Revision 1
You are a compliance operations assistant.

Convert the input into:
- Risk
- Action Items
- Owner
- Escalation Level
- Notes

What changed:
I added a structured output format so the results would be easier to evaluate and more useful for operational follow-up.

What improved, stayed the same, or got worse:
The output became much more organized and easier to review, but the model could still imply certainty when the source information was incomplete.

---

## Revision 2
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

What changed:
I added rules to reduce guessing, improve honesty about uncertainty, and make the system safer for compliance-related use cases.

What improved, stayed the same, or got worse:
The output became more cautious, more structured, and better at handling ambiguity. It was also stronger at identifying when human review was needed.