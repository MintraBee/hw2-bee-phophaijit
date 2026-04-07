# Report

## Workflow Summary
This project implements a simple generative AI workflow called a “Compliance Risk Translator.” The system takes unstructured compliance or governance-related notes as input and generates a structured output including risk, action items, ownership, escalation level, and supporting notes.

The goal of this workflow is to improve clarity, consistency, and speed in how compliance-related information is interpreted and communicated across teams.

---

## What the system does well
The system performs well at converting unstructured text into a consistent and structured format. It is able to:
- identify key risks from loosely written notes
- extract actionable next steps
- maintain clarity when ownership is not specified
- apply escalation levels based on urgency and context

The structured output makes it easier to review, compare, and act on compliance-related information.

---

## Where the system struggles
The system can still struggle in situations where the input is ambiguous, incomplete, or highly context-dependent. In particular:
- it may interpret urgency differently depending on wording
- it cannot reliably assign ownership when not explicitly stated
- it requires caution in areas involving legal interpretation

These limitations highlight the importance of human review in compliance workflows.

---

## Role of prompt design
Prompt design played a critical role in improving system performance. Moving from an unstructured prompt to a structured format significantly improved consistency and usability.

Adding explicit rules in later iterations helped reduce hallucination, enforce transparency, and ensure the model handled uncertainty more appropriately.

---

## Role of evaluation
Creating a small evaluation set made it easier to assess performance across different scenarios, including normal cases, edge cases, and situations requiring human review.

This approach ensured that improvements were measured consistently rather than based on a single example.

---

## Conclusion
This exercise demonstrates how generative AI can support operational workflows by providing a structured first-pass interpretation of complex inputs. While the system is not a replacement for human judgment, it can improve efficiency, reduce ambiguity, and support better decision-making when used with appropriate oversight.