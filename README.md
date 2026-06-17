# Hermes Agent Factory

**A meta-agent that builds other agents — and entire agent teams.** Describe what you need in plain language. The agent interviews you and generates complete, ready-to-run Hermes profiles.

```bash
hermes plugins install github.com/bonaventuratommasosam-bot/hermes-agent-factory --enable
hermes -s agent-factory
```

## Two Modes

### Single Agent
"Build me a GitHub security reviewer"
→ One profile with SOUL, GOAL, skills, cron, config

### Agent Pack
"Build me a restaurant management system"
→ 3+ agents (inventory, accounting, compliance) with inter-agent bus and coordinator

## What it generates

**Single Agent:**
```
~/.hermes/profiles/<your-agent>/
├── SOUL.md              # Identity, personality
├── GOAL.md              # Objectives, metrics
├── skills/              # 3-5 domain-specific skills
├── config.yaml          # Provider, gateway config
├── cron/jobs.json       # Scheduled tasks
└── .env.EXAMPLE        # Required env vars
```

**Agent Pack:**
```
~/.hermes/packs/<pack-name>/
├── pack.yaml            # Team manifest
├── bus/routes.json      # Inter-agent routing
├── agents/              # 3 profiles (SOUL, GOAL, skills, cron)
└── coordinator/         # Team lead with routing rules
```

## Pre-built Packs

| Pack | Agents | Use |
|------|--------|-----|
| Restaurant | Groot + Contabile + Lawrenzo | Inventory, accounting, HACCP |
| Dev Shop | Frank + Sentinel + Wannabe | Coding, security, R&D |
| Marketing | Wannabe + DesignBro + Ducato | Content, brand, analytics |

## Example

```
$ hermes -s agent-factory

> Build me a dev team for my open source project

[Pack detected — team mode]

Q1: What kind of team? Pick from templates or custom.
> Dev shop — coding, security review, testing

Q2: Any specific roles?
> Same as template, Frank + Sentinel + Wannabe

[Generating 3 agents + coordinator + bus...]

✓ Pack generated: ~/.hermes/packs/dev-shop/
✓ 3 agents: Frank (dev), Sentinel (security), Wannabe (R&D)
✓ Coordinator: Machiavelli
✓ Bus wired with 3 routes
✓ 16 files generated

Deploy with: hermes pack deploy dev-shop
```

## Requirements

- Hermes Agent v0.16.0+
- DeepSeek API key (or any LLM provider)

## License

MIT — use it, fork it, ship it.

## Built by

[HermesBro](https://hermesbro.cloud) — open-source AI agents for business.
