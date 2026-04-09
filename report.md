# Report

## Workflow Summary
This project implements a generative AI workflow called a “Compliance Risk Translator.” The system takes unstructured compliance or governance-related notes as input and generates a structured output including risk, action items, ownership, escalation level, and supporting notes.

The goal of this workflow is to improve clarity, consistency, and speed in how compliance-related information is interpreted and communicated across teams.

---

## Business Use Case
In many organizations, compliance and risk-related information is captured in unstructured formats such as meeting notes, emails, or informal documentation. This creates challenges in identifying risks, assigning ownership, and ensuring timely follow-up.

This workflow provides a structured first-pass interpretation of these inputs, helping teams quickly identify key issues and reduce ambiguity in communication while maintaining a human-in-the-loop review process.

---

## Model Choice
This prototype uses Claude Haiku via the Anthropic API. This model was chosen because it provides a strong balance between speed, cost, and performance for structured text generation tasks.

Given that this workflow focuses on transforming relatively short, unstructured notes into structured outputs, a lightweight and fast model is sufficient. More advanced models were not necessary for this use case, as the task does not require deep reasoning or complex multi-step problem solving.

During development, the prototype was initially built using the Google Gemini API, but persistent availability issues with the Gemini 2.5 Flash model required switching to Anthropic's Claude Haiku. This transition was straightforward and resulted in reliable, consistent outputs across all test cases.

---

## Baseline vs Final Design
The initial version of the prompt was simple and unstructured, asking the model to summarize risks and suggest next steps. While the responses were readable, they were inconsistent and lacked clear separation between risk, actions, and ownership.

After introducing a structured output format, the responses became significantly more consistent and easier to evaluate. The final version added explicit rules to prevent guessing, enforce clarity around uncertainty, and avoid inappropriate outputs such as legal advice.

These improvements resulted in outputs that were more reliable, better aligned with real-world compliance workflows, and easier to compare across test cases.

---

## What the system does well
The system performs well at converting unstructured text into a consistent and structured format. It is able to:
- identify key risks from loosely written notes
- extract actionable next steps
- maintain clarity when ownership is not specified
- apply escalation levels based on urgency and context

The structured output makes it easier to review, compare, and act on compliance-related information.

---

## Where the system struggles / human review required
The system can struggle in situations where the input is ambiguous, incomplete, or highly context-dependent. In particular:
- it may interpret urgency differently depending on wording
- it cannot reliably assign ownership when not explicitly stated
- it should not be relied on for legal interpretation or compliance decisions

For these reasons, human review is required, especially for high-risk or legally sensitive scenarios.

---

## Role of evaluation
A small evaluation set was created to test the system across normal cases, edge cases, and scenarios requiring human review. This helped ensure that improvements were measured consistently rather than based on a single example.

The evaluation approach made it easier to identify where the system performed well and where it required additional constraints through prompt design.

---

## Deployment recommendation
This workflow could be deployed as a decision-support tool for internal teams, particularly in operational or compliance-heavy environments. It is best suited for lightweight, high-frequency use cases where teams need quick summaries and structured outputs.

However, it should not be used as a fully automated system. Human oversight is required to validate outputs, particularly in cases involving legal risk or ambiguous inputs. With appropriate review controls in place, this workflow can improve efficiency and reduce ambiguity without replacing human judgment.

---

## Conclusion
This exercise demonstrates how generative AI can support operational workflows by providing a structured first-pass interpretation of complex inputs. While the system is not a replacement for human expertise, it can enhance efficiency, improve communication, and support better decision-making when used with appropriate safeguards.