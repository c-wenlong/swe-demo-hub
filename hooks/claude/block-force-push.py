#!/usr/bin/env python3
"""Example Claude Code PreToolUse hook: refuse `git push --force`.

Disabled by default. `hooks/claude/.disabled` lists this file, so
`swe init` does not link it into ~/.claude/hooks. To turn it on:

  1. Run `swe hooks enable block-force-push.py`, which removes its line
     from hooks/claude/.disabled and links it into ~/.claude/hooks.
  2. Declare it in ~/.claude/settings.json. SWE links the script but
     never edits your settings:

     "hooks": {
       "PreToolUse": [{
         "matcher": "Bash",
         "hooks": [{"type": "command",
                    "command": "python3 ~/.claude/hooks/block-force-push.py"}]
       }]
     }

Claude Code sends the tool call as JSON on stdin. Exit 0 lets it run;
exit 2 blocks it and shows stderr to the agent. Standard library only,
no network, no files written.
"""

import json
import re
import sys

FORCE = re.compile(r"\bgit\b.*\bpush\b.*(\s--force(?!-with-lease)\b|\s-f\b)")


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (ValueError, OSError):
        return 0  # never block on input this hook does not understand
    if not isinstance(event, dict):
        return 0
    command = (event.get("tool_input") or {}).get("command") or ""
    if event.get("tool_name") == "Bash" and FORCE.search(command):
        print("Blocked by block-force-push.py: force-push is off. "
              "Use --force-with-lease, or ask the user to run it.",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
