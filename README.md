# Hermes Agent Factory

**A meta-agent that builds other agents.** Describe what you need in plain language — the agent interviews you and generates a complete, ready-to-run Hermes profile.

```bash
hermes plugins install github.com/bonaventuratommasosam-bot/hermes-agent-factory --enable
hermes -s agent-factory
```

## What it generates

```
~/.hermes/profiles/<your-agent>/
├── SOUL.md              # Identity, personality, skills
├── GOAL.md              # Objectives, metrics, constraints
├── skills/              # 3-5 domain-specific skills
│   └── <skill>/SKILL.md
├── config.yaml          # Provider, gateway, model config
├── cron/jobs.json       # Scheduled tasks (if needed)
└── .env.EXAMPLE        # Required environment variables
```

## How it works

1. Load the skill: `hermes -s agent-factory`
2. Describe your agent: "I need a GitHub code review bot that checks security and style"
3. Answer 5-7 quick questions (domain, personality, triggers)
4. Watch it generate all files automatically
5. Start it: `hermes -p <name> gateway start`

## Example

```
$ hermes -s agent-factory

> Create an agent for restaurant inventory tracking.
  It should monitor stock levels, calculate food cost,
  and send alerts when items run low.

[Agent Factory Interview]
Q1: What's the ONE main thing this agent should do?
> Track inventory in real-time and alert on low stock

Q2: Personality & tone?
> Professional but friendly, like a maître d'

Q3: Skills needed?
> Inventory tracking, cost calculation, Telegram alerts

[... 3 more questions ...]

✓ Profile generated: ~/.hermes/profiles/groot-brigata/
✓ 4 skills created
✓ 2 cron jobs scheduled
✓ .env.EXAMPLE ready

Start with: hermes -p groot-brigata gateway start
```

## Requirements

- Hermes Agent v0.16.0+
- DeepSeek API key (or any LLM provider)

## License

MIT — use it, fork it, ship it.

## Built by

[HermesBro](https://hermesbro.cloud) — open-source AI agents for business.
