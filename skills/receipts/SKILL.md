---
name: receipts
description: Use when reporting results to the user after changing code, running commands, fixing bugs, or reviewing a codebase — any time the reply will claim something is fixed, passing, working, handled, safe, or checked.
---

# Receipts

Every claim in your report carries a receipt, or a label saying it has none. The user should be able to tell what you **saw** from what you **believe** without re-running anything.

## The report contract

End-of-task reports are a list of claims. Each claim is one of:

```
✅ <claim> — <receipt>                      verified, works
❌ <claim> — <receipt>                      verified, still broken / left open
⚠️ <claim> — unverified: <why / how to check>  not observed
```

The marker answers "did I observe it?", not "is it good news?". A problem you reproduced is ❌, not ⚠️ — even when it needs the user's decision; put the question after the receipt.

Then one closing line:

```
receipts: N verified (✅+❌) · M unverified
```

## What counts as a receipt

A receipt is something **you observed in this session, after your last edit** to the thing it covers:

| Claim type | Receipt |
|---|---|
| Tests pass | the command + its summary line (`pytest -q → 4 passed`) |
| Bug fixed | the failing input re-run, with output (`parse_price("$1,200") → 1200`) |
| Code does X | `file:line` you read |
| Command / build works | command + exit code or key output line |
| "Nothing else is broken" | what you actually checked (`grep callers → 2 sites, both updated`) |

Not receipts: "should work", reasoning about the code, output from before your last edit, a test you wrote but didn't run.

## Scope the claim to the receipt

State exactly what the receipt proves, no wider.

- Ran `"$1,200"` only → claim "parses comma-grouped dollars", not "handles any price". `"$1,200.50"` goes under ❌ or ⚠️.
- Ran one test file → "test_price.py passes", not "all tests pass".
- Changed behavior the user didn't ask about (rounding, defaults, error types) → its own line, so it isn't hidden inside "fixed".

## Example

```
✅ parse_price("$1,200") → 1200 — ran it after edit
✅ test_price.py: 4 passed — `python -m pytest -q`
✅ apply_discount now returns int via round() — price.py:6
❌ round() turns $17.991 into $18 — ran it; round to cents instead? your call
❌ "$1,200.50" (cents) still raises ValueError — ran it, left as-is
⚠️ negative prices — not tested

receipts: 5 verified · 1 unverified
```

A short or rushed request still gets the contract — just fewer lines. If you checked nothing, the report is all ⚠️, and that is a correct report.
