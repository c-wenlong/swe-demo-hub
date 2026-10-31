---
name: debug-systematically
description: Find the root cause of a bug step by step instead of guessing. Use when a test fails, an error appears, or behaviour does not match what was expected.
---

# Debug systematically

Fix the cause, not the symptom. Work through these steps and do not skip
ahead to editing code.

1. **Reproduce.** Find the smallest command, test or input that shows the
   bug. If you cannot reproduce it, say so and ask for more detail.
2. **Read the evidence.** Read the full error message and stack trace. Check
   the logs. Note the exact file and line where it fails.
3. **Form one hypothesis.** Write down what you think is wrong and what you
   would expect to see if you are right.
4. **Test the hypothesis.** Add a print, a breakpoint or a failing test that
   proves or disproves it. Change one thing at a time.
5. **Fix.** Make the smallest change that removes the cause.
6. **Verify.** Run the reproduction again, then the related tests. Add a
   regression test when the project has a test suite.

If three hypotheses in a row are wrong, stop and summarise what you have
ruled out before trying a fourth.
