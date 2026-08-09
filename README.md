# IRONSCALES Public Claude Code Marketplace

A public Claude Code plugin marketplace. Add it by URL — no auth, no zip.

## Install

```
/plugin marketplace add rinenaftali/claude-public-marketplace
/plugin install commit-helper@ironscales-public-marketplace
```

## Plugins

- **commit-helper** — the `conventional-commit` skill writes a well-formed
  Conventional Commit message from your staged git changes. Trigger it by asking
  Claude to "write a commit message" once you've staged changes.

## Updating

Plugin versions auto-bump on every push to `main` via GitHub Actions. Users pull
the latest with `/plugin marketplace update ironscales-public-marketplace`.
