from __future__ import annotations

from browser_storage_check.models import Rule

PROJECT_NAME = 'browser-storage-check'
SUMMARY = 'Check frontend storage usage for sensitive data and expiry gaps.'
SAMPLE_RISK = 'localStorage token expiry none pii true'
SAMPLE_CLEAN = 'sessionStorage nonce expiry 15m pii false'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='token-storage',
        severity='high',
        pattern='localStorage\\s+token',
        message='token stored in localStorage',
        recommendation='use secure cookie or safer storage',
    ),
    Rule(
        code='no-expiry',
        severity='medium',
        pattern='expiry\\s+(none|missing|unknown)',
        message='expiry missing',
        recommendation='define expiry',
    ),
    Rule(
        code='pii-storage',
        severity='low',
        pattern='pii\\s+true',
        message='PII stored client-side',
        recommendation='minimize and protect stored data',
    ),
)
