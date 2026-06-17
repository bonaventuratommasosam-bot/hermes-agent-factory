---
name: code-audit
description: "Full security audit of a code diff or file. Checks OWASP Top 10, hardcoded secrets, unsafe patterns."
---

# Code Security Audit

## When to Use
- New PR opened
- User requests security review
- `audit` mentioned in PR comment

## Steps
1. Read the diff or file content
2. Run OWASP Top 10 checklist
3. Flag each finding: severity, file:line, description, fix
4. Post review as PR comment

## Pitfalls
- Non bloccare PR per warning bassa severità
- False positives su stringhe simili a secret
- Non esporre finding in canali pubblici
