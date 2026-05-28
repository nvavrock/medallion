# Agent git policy

Project agents follow [.cursor/rules/git-release.mdc](../.cursor/rules/git-release.mdc):

- **Commit and push** after substantive work unless you say otherwise.
- **Tag** `vX.Y.Z` on release bumps (CHANGELOG / `pyproject.toml`), not every commit.

To apply the same behavior in **all** Cursor projects, add equivalent text to **Cursor Settings → Rules → User rules** (global). Project rules apply automatically in this repository.
