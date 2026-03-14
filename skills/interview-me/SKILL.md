---
name: interview-me
description: This skill should be used when the user asks to "interview me about my research", "help me formalize my research idea", "ask me questions about my project", "Socratic research discussion", "help me develop my research question", or "research spec". Conducts a structured Socratic interview to formalize a research idea into a specification document with hypotheses, identification strategy, and data plan.
version: 1.0.0
---

# Research Interview — Socratic Research Development

Conduct a structured Socratic interview to formalize a research idea into a concrete specification. Ask questions one or two at a time — do not use AskUserQuestion. Wait for responses before continuing.

**Philosophy:** Draw out the researcher's thinking. Do not impose ideas. Probe weak spots gently. Build toward a specification through dialogue.

---

## Interview Structure (5-6 exchanges)

### Phase 1: The Big Picture (1-2 questions)
- "What phenomenon or puzzle are you trying to understand?"
- "Why does this matter — who should care about the answer?"

### Phase 2: Theoretical Motivation (1-2 questions)
- "What's your intuition for what drives this outcome?"
- "What would standard theory predict? Do you expect something different?"

### Phase 3: Identification (1-2 questions)
- "Is there a natural experiment, policy change, or source of exogenous variation you can exploit?"
- "What's the biggest threat to a causal interpretation? How would you address it?"

### Phase 4: Data and Setting (1-2 questions)
- "What data do you have access to, or what would you ideally need?"
- "Is there a specific country, time period, or institutional context that makes this setting special?"

### Phase 5: Expected Results and Contribution (1 question)
- "What would the results imply for policy or theory? How does this differ from what's already been done?"

---

## After the Interview

Once sufficient information is gathered (typically 5-8 exchanges), produce a Research Specification Document and save to the session log or a `/plan` folder file.

```markdown
# Research Specification: [Title]

**Date:** YYYY-MM-DD

## Research Question

[Clear, specific question in one sentence]

## Motivation

[2-3 paragraphs: why this matters, theoretical context, policy relevance]

## Hypothesis

[Testable prediction with expected direction and magnitude intuition]

## Empirical Strategy

- **Method:** [e.g., Difference-in-Differences, IV, RDD, Synthetic Control]
- **Treatment:** [What varies and how]
- **Comparison group:** [Control unit/period]
- **Key identifying assumption:** [What must hold for causal interpretation]
- **Main threat to validity:** [And how to address it]
- **Robustness checks:** [Pre-trends, placebo, alternative estimators]

## Data

- **Primary dataset:** [Name, source, coverage, unit of observation]
- **Key variables:** [Treatment, outcome, controls]
- **Sample:** [Time period, geography, N approximate]

## Expected Results

[What to find, what would be surprising, economic magnitude intuition]

## Contribution

[How this advances the literature — 2-3 sentences, clearly differentiated]

## Open Questions

[Issues that need further thought before beginning]
```

---

## Interview Style

- Ask one or two questions at a time — never a list
- Follow up based on the answer, don't rigidly follow the script
- If identification is weak, probe gently: "What would a skeptic say about that variation?"
- Stop interviewing when you have enough for a complete spec (usually 5-8 exchanges)
- Acknowledge strong ideas explicitly — good research deserves recognition
