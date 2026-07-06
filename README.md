# Browser Storage Check

| | |
| --- | --- |
| Focus | browser data |
| Command | `browser-storage-check` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Browser Storage Check cover](assets/readme-cover.svg)

Check frontend storage usage for sensitive data and expiry gaps. The idea is simple: give Browser Storage Check the local file or fixture, get a readable result, and decide what needs attention before the next handoff.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `token-storage` | high | token stored in localStorage |
| `no-expiry` | medium | expiry missing |
| `pii-storage` | low | PII stored client-side |

## Local run

```bash
git clone https://github.com/mertefekurt/browser-storage-check.git
cd browser-storage-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
browser-storage-check examples/sample.txt
browser-storage-check examples/sample.txt --json
```

## Why the sample fails

`localStorage token expiry none pii true` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
