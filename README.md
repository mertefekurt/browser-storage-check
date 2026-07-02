# browser-storage-check

> Check frontend storage usage for sensitive data and expiry gaps.

## Review card Overview

Check frontend storage usage for sensitive data and expiry gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts browser storage review. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
browser-storage-check examples/sample.txt
browser-storage-check examples/sample.txt --json --fail-on medium
python -m browser_storage_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `token-storage` | high | token stored in localStorage |
| `no-expiry` | medium | expiry missing |
| `pii-storage` | low | PII stored client-side |

## Validation Notes

```bash
ruff check .
pytest
python -m browser_storage_check --help
```

Example risky input:

```text
localStorage token expiry none pii true
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
