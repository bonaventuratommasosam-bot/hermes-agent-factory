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

Two phases:
1. **Interview** — 5-8 targeted questions to understand the domain and requirements
2. **Generate** — Write all profile files based on interview answers

---

## Phase 1: Interview

Ask these questions ONE AT A TIME via `clarify()`. Do not ask all at once. Adapt questions based on the user's initial description.

### Q1 — Domain & Core Task
"What's the ONE main thing this agent should do? Be specific — not 'help with marketing' but 'write 3 LinkedIn posts per week and track engagement.'"

### Q2 — Personality & Tone
"How should this agent talk? Pick a vibe: professional/formal, casual/friendly, technical/precise, or something custom. What's their role identity? (e.g. 'senior DevOps engineer', 'creative director', 'legal analyst')"

### Q3 — Skills & Capabilities
"What specific skills does it need? Choose from: writing, coding, data analysis, research, scheduling, monitoring, content creation, calculation, compliance checking, translation, summarization. Or describe custom ones."

### Q4 — Triggers & Automation
"Should this agent run on a schedule (cron), react to triggers (webhooks, messages), or only respond on demand? If scheduled, how often and what triggers it?"

### Q5 — Integrations
"What external services does it connect to? Examples: Google Sheets, GitHub, email, Stripe, Telegram, Slack, Calendly, weather API, custom REST APIs."

### Q6 — Constraints & Boundaries
"Anything this agent should NEVER do? Sensitive data boundaries? Compliance requirements? Specific rules to follow?"

### Q7 — Name
"Pick a name for this agent (lowercase, hyphens OK). This becomes the profile name."

**Smart-skip:** If the user's initial request already answers a question clearly, skip it. Only ask what's not yet clear. If user says "just do it" or shows impatience, do Q1 + Q2 + Q7 minimum, then generate.

**STOP after each question.** Wait for the user's response before asking the next one.

---

## Phase 2: Generate

After the interview, generate these files under the profile directory. Use `terminal()` to create the profile directory, then `write_file()` for each file.

### Profile Path
```
~/.hermes/profiles/<profile-name>/
```

### Files to Generate

#### 1. SOUL.md — Identity & Personality

Template:
```markdown
# <AGENT-NAME> — <ROLE>

## CHI SEI
<One paragraph: who this agent is, its role, its purpose. Include the domain context.>

## PERSONALITÀ
- **<trait>**: <description>
- **<trait>**: <description>
- **<trait>**: <description>

## COMPETENZE
- <skill 1>
- <skill 2>
- <skill 3>
- <skill 4>

## LIMITI
- <boundary 1>
- <boundary 2>
```

#### 2. GOAL.md — Objectives & Success Metrics

```markdown
# <AGENT-NAME> — Goals

## Primary Objective
<One sentence: the core mission>

## Success Metrics
- <metric 1>
- <metric 2>
- <metric 3>

## Recurring Tasks
- <task 1> — <frequency>
- <task 2> — <frequency>

## Constraints
- <constraint 1>
```

#### 3. Skills (3-5 files)

Each skill in `skills/<skill-name>/SKILL.md`. Minimal viable skill:

```markdown
---
name: <skill-name>
description: "<one-line description>"
---

# <Skill Title>

## When to Use
- <trigger 1>
- <trigger 2>

## Steps
1. <step>
2. <step>
3. <step>

## Pitfalls
- <pitfall>
```

Skills should match what was discussed in the interview. Use the domain context to make them realistic.

#### 4. Cron Jobs

If the user wants scheduled tasks, create `cron/jobs.json`:

```json
{
  "jobs": [
    {
      "schedule": "<cron or duration>",
      "prompt": "<what to do>",
      "deliver": "local"
    }
  ]
}
```

#### 5. Config (config.yaml)

```yaml
model:
  default: deepseek-v4-pro
  provider: custom:deepseek

agent:
  max_turns: 60

gateway:
  platforms:
    telegram:
      enabled: true
```

#### 6. .env.EXAMPLE

List all required environment variables with comments:

```bash
# LLM Provider
DEEPSEEK_API_KEY=sk-...

# Telegram
TELEGRAM_TOKEN=123:abc

# <Integration-specific vars>
# GOOGLE_SHEETS_CREDENTIALS=/path/to/credentials.json
```

---

## Phase 3: Verify

After generating all files:
1. Run `hermes profile show <name>` to verify the profile is recognized
2. List the generated files: `find ~/.hermes/profiles/<name>/ -type f`
3. Show a summary to the user:
   - Profile name and path
   - Number of skills generated
   - Cron jobs created
   - Environment variables needed
   - Command to start: `hermes -p <name> gateway start` (or `hermes -p <name>` for CLI)

---

## Common Pitfalls

- **Don't ask too many questions.** Tommy hates walls of text. 5-7 questions max.
- **Don't generate skills that don't match the domain.** A "restaurant inventory agent" doesn't need a "stock trading" skill.
- **Don't over-engineer SOUL.md.** Keep personality traits to 3-4 bullet points.
- **Profile directory must exist before writing files.** Create with `mkdir -p`.
- **If the user interrupts mid-interview with "just generate it"**, skip remaining questions and generate with what you have. Fill gaps with reasonable defaults.

## Verification Checklist

- [ ] All files generated under `~/.hermes/profiles/<name>/`
- [ ] SOUL.md has identity, personality, skills, limits
- [ ] GOAL.md has objective, metrics, tasks, constraints
- [ ] 3-5 skills generated with realistic content
- [ ] .env.EXAMPLE lists all needed variables
- [ ] Profile recognized by `hermes profile show`
- [ ] No sensitive data in generated files
