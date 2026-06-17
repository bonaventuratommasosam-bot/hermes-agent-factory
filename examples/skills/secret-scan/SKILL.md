---
name: secret-scan
description: "Scan repo for accidentally committed secrets: API keys, tokens, passwords."
---

# Secret Scan

## When to Use
- Scheduled scan (every 6h)
- Post-commit hook trigger

## Steps
1. Fetch latest repo
2. Run regex patterns for common secret formats
3. Check git history for past secrets
4. Generate report (NO secret values in log)

## Pitfalls
- Non committare report con secret reali
- Escalation immediata per secret in produzione
