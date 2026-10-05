---
name: receipts
description: Use when reporting results after changing code, running commands, fixing bugs, or reviewing a codebase — any time the reply will claim something is fixed, passing, working, handled, safe, or checked.
---

# Receipts

Every claim in your report carries a receipt or says it has none, so the user can tell what you **saw** from what you **believe**.

## Report format

Problems first, one claim per line:

```
❌ <claim> — <receipt>         observed: broken, or left open
⚠️ <claim> — <why unchecked>   not observed
✅ <claim> — <receipt>         observed: works

receipts: N verified (✅+❌) · M unverified (⚠️)
```

- The marker answers "did I observe it?", not "is it good news?". A problem you reproduced and left open is ❌, even when it needs the user's decision — put the question after the receipt. A bug you fixed is ✅ with the fix's receipt. Something you couldn't run is ⚠️.
- Many routine ✅ (e.g. seven fixes checked by one script) may share one line: `✅ 7 fixes — check.py: 7/7 asserts pass`. The tally counts claims, not lines.

## What a receipt is

Something you observed **this session, after your last edit** to what it covers: a command and its output line, the failing input re-run, a `file:line` you read.

Never run something destructive, production-facing, or costly just to earn a receipt. Leave it ⚠️ and say what would verify it.

Not receipts: "should work", reasoning about the code, output from before the edit, a test you wrote but didn't run, someone else saying they ran it.

## Scope the claim to the receipt

- Describe what the code actually does, not what you meant it to do: `.strip()` → "trims leading/trailing spaces", not "removes spaces".
- Ran `"$1,200"` only → "parses comma-grouped dollars", not "handles any price".
- Ran one test file → "test_price.py passes", not "all tests pass".
- A behavior change nobody asked for (rounding, defaults, error types) gets its own line.

A rushed request gets the same format, just fewer lines. If you checked nothing, every line is ⚠️ — that is a correct report.
