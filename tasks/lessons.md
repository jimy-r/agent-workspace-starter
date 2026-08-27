# Lessons learned

> Patterns and corrections to avoid repeating mistakes. Updated after every user correction — **before** other work continues. Sessions read this file at start (orient does it automatically) and apply every rule.
>
> Format: newest first. `## YYYY-MM-DD — Short title`, then what went wrong and the rule that prevents it recurring.

---

## 2026-06-11 — Example: verify the artifact, not the report

A command exited 0 but the expected output file was never created; the next step then failed confusingly. Exit code 0 plus no error message is not the same as "the operation produced its artifact."

Rule: after any generation step (export, build, render), check that the artifact exists before depending on it or deleting inputs. *(Replace this example with your own first lesson — then keep the habit.)*
