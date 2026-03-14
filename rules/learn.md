# Continuous Learning Protocol

When corrected, discover a non-obvious pattern, or notice something that would save time next session — save it immediately.

## [LEARN] Tag Format

Append to `~/.claude/projects/-Users-xuhaiping-Desktop/memory/MEMORY.md`:

```
[LEARN:category] <what was wrong or discovered> → <correct behavior or when to apply>
```

**Categories:**

| Category | When to use |
|----------|-------------|
| `workflow` | Workflow patterns, tool sequences, process improvements |
| `writing` | Academic writing rules, journal conventions, section structures |
| `python` | Python/pyfixest/pandas patterns, package preferences, traps |
| `stata` | Stata-specific behaviors, version differences, package quirks |
| `data` | Data handling patterns, format-specific quirks |
| `rules` | Claude Code rules, hook behaviors, path-scoped conditions |
| `skills` | Skill trigger phrases, when to use which skill |
| `identity` | User preferences, communication style, workflow habits |

## Triggers for Writing a [LEARN] Entry

Write an entry when:
- The user corrects an assumption ("actually this should be...")
- A previously failed approach is discovered to be wrong
- A pattern is confirmed across 2+ interactions
- A non-obvious dependency or ordering is discovered
- A quality gate failure reveals a recurring issue
- The user explicitly asks to remember something

Do NOT write entries for:
- Single-use context (current task details)
- Things already in CLAUDE.md
- Speculative conclusions from reading one file

## At Session End

Before stopping, scan the session for:
1. Any corrections the user made → write [LEARN] entry
2. Any non-obvious decisions made → log in session log
3. Any rules-worthy patterns confirmed → consider adding to a rule file
4. CLAUDE.zh-CN.md out of sync with CLAUDE.md → update it

## Reading Memory

At start of complex tasks, read the relevant section of MEMORY.md:
- Starting a paper → read `## Research Writing`
- Starting analysis → read `## Python Causal Inference Stack`
- Modifying workflow → read `## Workflow Architecture`
