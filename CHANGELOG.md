# Changelog

Versions follow [SemVer](https://semver.org). Bump `version` in `.claude-plugin/plugin.json` with every release; Claude Code uses it to detect plugin updates.

- **MAJOR**: the report contract changes shape (markers, summary line).
- **MINOR**: new rules or sections agents must follow.
- **PATCH**: wording, examples, README/assets.

## [0.1.0] - 2026-10-05

- Report contract: ✅ verified / ❌ verified-broken / ⚠️ unverified, closing `receipts:` tally line.
- Receipt definition (observed this session, after the last edit) and claim-scoping rules.
- EN/KO READMEs with animated demo SVGs.
