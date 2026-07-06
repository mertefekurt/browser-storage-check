# Browser Storage Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Browser Storage Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-7c3aed?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-0891b2?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-b45309?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-be185d?style=flat-square)

Check frontend storage usage for sensitive data and expiry gaps.

## The short version

`browser-storage-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `token-storage` | high | token stored in localStorage |
| `no-expiry` | medium | expiry missing |
| `pii-storage` | low | PII stored client-side |

## Usage

```bash
python -m pip install -e ".[dev]"
browser-storage-check examples/sample.txt
browser-storage-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m browser_storage_check --help
```
