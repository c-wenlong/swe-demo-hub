# Quiver demo hub

A starter hub for [Quiver](https://github.com/c-wenlong/quiver). A hub is a git
repository that Quiver clones as `~/.quiver` and shares with every coding
agent on your machine: one `AGENTS.md`, one skills folder, your plugin
marketplaces, hook scripts and MCP server list.

## Start here

1. **Fork this repo, or click "Use this template"** to make your own copy.
   A template copy can be private, which is a good idea: your hub will hold
   your own instructions and notes.
2. Paste **your copy's** URL into setup:

   ```bash
   swe setup --hub=https://github.com/<you>/<your-hub>.git
   ```

   Or paste it into the hub URL field on the Setup page (web app or Mac app).
   Do not point setup at this repo directly: you could not push your changes
   back to it.

Setup clones your hub as `~/.quiver`, links `AGENTS.md` and `skills/` into
each coding agent it finds, and registers the plugin marketplaces in
`plugins/`. Run `swe init` any time to repair or refresh the links.

## What each folder holds

| Path | What it is |
|---|---|
| `AGENTS.md` | Instructions every agent reads. Linked into each harness as `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` and so on. |
| `skills/<name>/SKILL.md` | Shared skills, linked into every harness's skills folder. Three samples: `review-checklist`, `debug-systematically`, `write-pr-description`. |
| `plugins/<marketplace>/` | Plugin marketplaces. Each has `.claude-plugin/marketplace.json` listing its plugins. The sample `starter` marketplace holds one plugin, `git-helpers`. |
| `hooks/<harness>/` | Hook scripts, linked into that one harness only. The sample `hooks/claude/block-force-push.py` is off: `hooks/claude/.disabled` lists it. |
| `mcp.json` | MCP servers to sync into each harness. Secrets are `${NAME}` references, never values. |
| `mcp/` | Local checkouts of MCP servers go in `mcp/servers/`, which git ignores. |
| `.gitignore` | Keeps caches, usage data and `secrets/` out of git. Keep it. |
| `.linkignore` | Paths in your home folder that `swe init` should never link. |

## Make it yours

- **Rewrite `AGENTS.md`** with the rules you want every agent to follow.
- **Skills:** delete the samples you do not want, and add a folder per skill
  with a `SKILL.md` (front matter `name` and `description`, then the
  instructions).
- **Plugins:** rename `plugins/starter` and its `"name"`, or add another
  marketplace folder beside it. List each plugin in `marketplace.json` with a
  relative `"source"` such as `"./my-plugin"`.
- **MCP:** add servers with `swe mcp add <name> -- <command>` or
  `swe mcp add <name> --url=<url>`. Store a credential with
  `swe mcp secret set GITHUB_TOKEN`; the value goes in `secrets/`, which is
  never committed, and `mcp.json` keeps only `${GITHUB_TOKEN}`. Then
  `swe mcp sync` writes each harness's config.
- **Hooks:** `swe hooks enable block-force-push.py` links the sample, and
  you declare it in `~/.claude/settings.json` (its docstring shows how).
- **Commit and push** from `~/.quiver` like any repo. On another machine,
  `swe setup --hub=<your URL>` brings the same setup over.

## Sample MCP servers

| Name | What it does | Needs |
|---|---|---|
| `context7` | Up-to-date library documentation | Node.js (`npx`) |
| `github` | GitHub's hosted MCP server | `swe mcp secret set GITHUB_TOKEN` with a personal access token |

Remove either one from `mcp.json` if you do not use it.

## License

MIT, see [LICENSE](LICENSE).
