"""
Hermes Agent Factory Plugin

A meta-agent plugin that interviews users and generates complete
Hermes Agent profiles. When the agent-factory skill is loaded,
the agent guides the user through a brief interview and then
builds SOUL.md, GOAL.md, skills, cron jobs, config, and .env.EXAMPLE.

Usage:
    hermes plugins install file:///path/to/hermes-agent-factory --enable
    hermes -s agent-factory
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def register(ctx) -> None:
    """Register the agent-factory skill with Hermes."""
    skill_md = ROOT / "skills" / "agent-factory" / "SKILL.md"
    if skill_md.exists():
        ctx.register_skill("agent-factory", skill_md)
