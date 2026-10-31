---
name: review-checklist
description: Review a diff, branch or pull request for bugs before it merges. Use when asked to review code, check a PR, or look over changes before committing.
---

# Review checklist

Review the change itself, not the whole codebase. Start from the diff
(`git diff`, `git diff main...HEAD`, or `gh pr diff <number>`), then read
enough of the surrounding code to judge each hunk.

## What to check, in order

1. **Correctness.** Does the code do what the change claims? Look for
   off-by-one errors, wrong conditions, unhandled `null`/`None`, swapped
   arguments and missing `await`s.
2. **Edge cases.** Empty input, very large input, unicode, concurrent
   callers, a network or disk call that fails.
3. **Security.** User input reaching a shell, SQL query, file path or HTML
   without escaping. Secrets in code or logs. New permissions.
4. **Tests.** Is the new behaviour tested? Would the tests fail if the fix
   were reverted?
5. **Readability.** Names, dead code, comments that no longer match.

## How to report

- List findings worst first. For each: file and line, what is wrong, why it
  matters, and a concrete fix.
- Mark each one as a bug, a risk or a nit. Leave nits out unless asked.
- If you found nothing, say so in one line. Do not invent findings.
