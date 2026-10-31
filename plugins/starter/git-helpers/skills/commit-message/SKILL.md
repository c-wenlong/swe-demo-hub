---
name: commit-message
description: Write a commit message for the staged changes. Use when asked to commit, or to suggest a commit message.
---

# Commit message

1. Read what is staged: `git diff --cached`. If nothing is staged, say so
   and stop. Do not stage files the user did not ask for.
2. Read `git log --oneline -10` and follow the style the repository already
   uses (Conventional Commits, an `area:` prefix, or plain sentences).
3. Write the message:
   - A subject line under 72 characters, in the imperative ("Fix", "Add",
     "Remove"), with no trailing period.
   - A blank line, then a short body saying why the change was made, when
     the subject alone does not make that clear.
4. Show the message, then commit only if the user asked you to commit.
