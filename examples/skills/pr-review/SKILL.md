---
name: pr-review
description: "Review PR for code quality, best practices, architecture. Educational tone."
---

# PR Review

## When to Use
- New PR opened
- User mentions `review`

## Steps
1. Fetch PR diff from GitHub
2. Analyze: duplication, complexity, missing tests, naming, error handling
3. Write review as inline comments
4. Summarize: approve / request changes / comment

## Pitfalls
- Non fare nitpick su formattazione
- Non richiedere test per modifiche banali
- Se insicuro, chiedi invece di bloccare
