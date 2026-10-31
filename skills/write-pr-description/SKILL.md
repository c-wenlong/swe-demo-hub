---
name: write-pr-description
description: Write a clear pull request title and description from the current branch. Use when opening a PR or when asked to describe a set of changes.
---

# Write a PR description

Read the branch before writing: `git log main..HEAD --oneline` and
`git diff main...HEAD --stat`, then the diff itself. Use the repository's
default branch if it is not `main`. If the repository has a
`.github/pull_request_template.md`, follow it instead of the shape below.

## Title

One line, under 70 characters, in the imperative: "Add retry to the upload
client", not "Added retries" or "Upload changes".

## Body

```markdown
## What
One or two sentences on what changed.

## Why
The problem this solves, or the issue it closes (`Closes #123`).

## How to test
Commands or steps a reviewer can run to see it work.

## Notes
Anything risky, any follow-up left for later. Omit if empty.
```

Keep it short. Describe behaviour, not every file touched.
