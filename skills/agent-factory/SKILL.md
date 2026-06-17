---
name: agent-factory
description: "Use when the user asks to create, generate, or build a new Hermes Agent profile. Interviews the user about domain, personality, and requirements, then generates a complete profile (SOUL, GOAL, skills, cron, config, .env.EXAMPLE). The agent acts as a factory — describe what you need, get a ready-to-run agent."
version: 0.1.0
author: HermesBro
license: MIT
metadata:
  hermes:
    tags: [agent-factory, profile-generation, meta-agent, hermesbro]
    related_skills: [hermes-agent, hermes-agent-skill-authoring]
---

# Agent Factory

Meta-agent that generates complete Hermes Agent profiles. Describe the agent you need in plain language — domain, personality, tasks — and this skill guides the interview and builds all profile files.

## When to Use

- User says "create an agent that...", "build me a bot for...", "I need an agent..."
- User wants to generate a new Hermes profile from scratch
- User wants to clone and customize an existing agent concept

## How It Works

Three phases:
1. **Extract** — Parse the user's initial description. Extract domain, tasks, tone, integrations automatically. Most answers are already in the first message.
2. **Interview** — Only ask what's missing. 2-4 questions max, never 7.
3. **Generate** — Write all profile files with domain-specific knowledge injected.

---

## Phase 1: Extract

Before asking ANY question, extract everything you can from the user's initial message:

- **Domain**: restaurant, legal, finance, coding, content, security, gaming, etc.
- **Core task**: the ONE thing they described
- **Tone**: formal, casual, technical, friendly — infer from domain
- **Integrations**: any service mentioned (GitHub, Google Sheets, Telegram, etc.)
- **Triggers**: scheduled, on-demand, event-driven — infer from task
- **Name**: derive from domain + task if not given (e.g. "restaurant inventory" → `groot-brigata`)

**Fill a mental matrix before proceeding.** Only ask questions for empty cells.

### Domain Knowledge Injection

Based on the extracted domain, pre-load relevant patterns:

| Domain | Skill patterns | Common integrations | Cron examples |
|--------|---------------|---------------------|---------------|
| Restaurant | Inventory tracking, food cost calc, menu analysis, HACCP compliance | Google Sheets, Telegram | Daily inventory check, weekly cost report |
| Legal | Contract review, GDPR check, compliance audit, clause extraction | Email, Google Drive | Weekly compliance scan |
| Finance | Portfolio analysis, risk scoring, market monitoring, P&L calc | APIs, Google Sheets | Daily market open, weekly summary |
| Coding | Code review, PR analysis, security scan, refactoring | GitHub, GitLab | On push trigger, weekly dep audit |
| Content | Post generation, scheduling, engagement tracking, A/B testing | X/Twitter, LinkedIn, Telegram | Daily post, weekly analytics |
| Security | Vulnerability scan, secret detection, dependency audit, pentest report | GitHub, Slack | Every 6h scan, weekly report |
| DevOps | Log monitoring, health check, deploy verification, incident response | SSH, APIs, Slack | Every 5m health, daily backup check |

Use these patterns when generating skills — don't start from scratch. A restaurant agent gets `food-cost` and `inventory-tracker` skills with real formulas. A security agent gets OWASP patterns.

---

## Phase 2: Interview

From the extraction, identify gaps. Ask ONLY for missing info. Maximum 4 questions, ideally 2-3.

### Gap questions (ask only what's missing):

**Missing core task?** → "What's the ONE main thing this agent should do?"

**Missing personality?** → "How should they talk? Pick: professional, casual, technical, or custom."

**Missing name?** → "What should we call this agent? (lowercase, hyphens OK)"

**Missing triggers?** → "Run on schedule, on demand, or both? Any specific timing?"

**STOP after each question.** If user says "just generate it" or shows impatience — generate immediately with what you have. Fill gaps with domain-appropriate defaults.

**Escape hatch:** User gave a full description with name, task, and domain? Skip ALL questions. Go straight to Phase 3.

---

## Phase 3: Generate

After extraction (+ optional interview), generate all files. Use the domain patterns from Phase 1 to make skills realistic and useful.

### Step 0: Detect provider

Check the current user's config before generating:
```bash
hermes config get model.provider 2>/dev/null || echo "deepseek"
hermes config get model.default 2>/dev/null || echo "deepseek-v4-pro"
```

Use these values in the generated `config.yaml` — don't hardcode DeepSeek.

### Step 1: Create directory structure

```bash
mkdir -p ~/.hermes/profiles/<name>/skills/{<skill-1>,<skill-2>,<skill-3>}
mkdir -p ~/.hermes/profiles/<name>/cron
```

### Files to Generate (in order)

**SOUL.md** — Identity. Use the domain to inject realistic competencies. A restaurant agent mentions "food cost %", "par levels", "supplier lead times". A security agent mentions "OWASP", "CVE database", "MITRE ATT&CK".

**GOAL.md** — Objectives with measurable metrics. Not "be helpful" but "reduce food waste by 15%" or "catch 100% of critical CVEs before merge".

**Skills (3-5)** — Each skill MUST have:
- Realistic trigger conditions (not generic "when user asks")
- Concrete steps with actual tools mentioned (`terminal()`, `web_search()`, `read_file()`)
- At least ONE domain-specific pitfall (e.g. "food cost calc doesn't include waste %")
- Related config/env vars referenced

**config.yaml** — Use detected provider/model. Enable appropriate gateway platforms based on integrations mentioned.

**.env.EXAMPLE** — List every env var mentioned in skills, plus provider credentials. Add comments explaining where to get each key.

**cron/jobs.json** (if scheduled) — Use realistic schedules from the domain table above.

---

## Phase 4: Verify & Iterate

1. Validate profile: `hermes profile show <name>`
2. List files: `find ~/.hermes/profiles/<name>/ -type f | sort`
3. Show summary to user:
   - Profile name, path, provider
   - Number of skills (list them)
   - Cron jobs (if any)
   - Env vars needed (count)
   - Start command
4. **Ask once:** "Want to add, remove, or modify any skill? I can also add cron jobs or tweak the personality."
5. If user wants changes, loop back to the relevant generation step. Don't restart the interview.

---

## Common Pitfalls

- **Don't ask all 7 questions when 2 suffice.** Extract first. Interview is the fallback, not the default.
- **Don't generate generic skills.** A "code review" skill without OWASP patterns is useless. A "food cost" skill without the formula (COGS / revenue × 100) is wrong. Inject domain knowledge.
- **Don't hardcode the provider.** Always detect the user's current provider with `hermes config get`.
- **Don't over-engineer SOUL.md.** 3-4 personality traits, 4-5 competencies, 2-3 limits. Brevity = clarity.
- **Profile directory must exist before writing files.** Create all skill subdirectories in one `mkdir -p`.
- **If user interrupts with "just generate it"**, skip remaining questions. Extract what you can, fill gaps with domain defaults, generate.
- **The generation is NOT the end.** Always ask "want to modify anything?" after showing the summary.

## Verification Checklist

- [ ] All files generated under `~/.hermes/profiles/<name>/`
- [ ] SOUL.md has identity, personality, skills, limits
- [ ] GOAL.md has objective, metrics, tasks, constraints
- [ ] 3-5 skills generated with realistic content
- [ ] .env.EXAMPLE lists all needed variables
- [ ] Profile recognized by `hermes profile show`
- [ ] No sensitive data in generated files
