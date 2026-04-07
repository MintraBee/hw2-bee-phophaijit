# Evaluation Set

## Case 1 - Normal case
Input:
We may have gaps in state-level compliance for remote employees in California and New York. Need to confirm payroll tax handling before next payroll cycle.

Good output should:
- identify state compliance risk
- mention California and New York
- recommend confirming payroll tax handling
- avoid inventing an owner if none is given
- set escalation to medium or high

---

## Case 2 - Normal case
Input:
Annual policy review is behind schedule. HR needs to update the handbook language and legal should review before publication.

Good output should:
- identify delayed policy review as a risk
- assign HR and legal correctly
- mention dependency on review before publication
- avoid adding fake deadlines

---

## Case 3 - Edge case
Input:
There may be some confusion about vendor access controls, but I’m not sure if this is still an open issue.

Good output should:
- reflect uncertainty
- avoid overstating the risk
- indicate that status is unclear
- avoid inventing owners or actions

---

## Case 4 - Edge case
Input:
Need to follow up on compliance training completion. Maybe next week. Someone from operations should handle it.

Good output should:
- identify training follow-up as the action
- say owner is unclear
- mention timeline is vague
- avoid guessing a specific name or date

---

## Case 5 - Human review case
Input:
There may be exposure related to multi-state employment registration and withholding requirements, but we need legal confirmation before taking action.

Good output should:
- identify the issue as potentially significant
- clearly indicate legal confirmation is required
- avoid giving legal advice
- set escalation high
- recommend human review