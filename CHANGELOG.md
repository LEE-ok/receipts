# Changelog

Versions follow [SemVer](https://semver.org). Bump `version` in `.claude-plugin/plugin.json` with every release; Claude Code uses it to detect plugin updates.

- **MAJOR**: the report contract changes shape (markers, summary line).
- **MINOR**: new rules or sections agents must follow.
- **PATCH**: wording, examples, README/assets.

## [0.2.0] - 2026-10-05

- SKILL.md trimmed 459 → 361 words (−21%).
- New: never run destructive or production-facing commands just to earn a receipt (a trimmed draft ran a prod deploy script in 2/3 test runs; 0/3 after this rule).
- Tally now spells out `verified (✅+❌) · unverified (⚠️)`; fixed ❌ being dropped from the count.
- Hearsay ("someone else ran it") is explicitly not a receipt.
- Scope rule now says to describe what the code does (`.strip()` = trims ends). The first trimmed draft lost this and over-claimed "removes spaces" in 3/3 runs; 0/3 after the fix.
- Routine ✅ may share one line. A hard 5-line cap was tested and dropped: agents ignored it or crammed claims to satisfy it.

## [0.1.0] - 2026-10-05

- Report contract: ✅ verified / ❌ verified-broken / ⚠️ unverified, closing `receipts:` tally line.
- Receipt definition (observed this session, after the last edit) and claim-scoping rules.
- EN/KO READMEs with animated demo SVGs.
