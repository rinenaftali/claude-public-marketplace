---
name: conventional-commit
description: Writes a well-formed Conventional Commit message from the currently staged git changes. Use when the user asks to "write a commit message", "commit this", or "generate a conventional commit".
---

# Conventional Commit Helper

Generate a Conventional Commit message that accurately describes the staged changes.

## Steps

1. Inspect what is staged. Run:
   ```bash
   git diff --cached --stat && git diff --cached
   ```
   If nothing is staged, tell the user there are no staged changes and stop (suggest `git add` first). Do not run `git add` yourself.

2. Choose the correct type based on what the diff actually does:
   - `feat` — a new user-facing capability
   - `fix` — a bug fix
   - `docs` — documentation only
   - `refactor` — code change that neither fixes a bug nor adds a feature
   - `perf` — performance improvement
   - `test` — adding or correcting tests
   - `build` / `ci` — build system or CI config
   - `chore` — maintenance, deps, tooling

3. Add a scope in parentheses when the change is clearly confined to one module or area (e.g. `feat(auth):`). Omit it if the change is broad.

4. Write the message in this exact format:
   ```
   <type>(<scope>): <concise summary in imperative mood, <=72 chars, no trailing period>

   <optional body: what changed and why, wrapped at ~72 cols>

   <optional footer: BREAKING CHANGE: ... or issue refs like Refs: IP-123>
   ```

## Rules

- Summary line: imperative mood ("add", not "added"/"adds"), lowercase after the colon, no trailing period.
- Add a `BREAKING CHANGE:` footer if the diff removes or changes a public interface.
- Base the message strictly on the actual staged diff — never invent changes that aren't there.
- Output the commit message in a fenced code block so it is easy to copy. Do not run `git commit` unless the user explicitly asks you to.
