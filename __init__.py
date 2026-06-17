"""
Hermes Agent Factory Plugin

A meta-agent plugin that interviews users and generates complete Hermes
Agent profiles. Describe what you need in plain language, get a
ready-to-run agent profile.

CLI:
    hermes factory create   — interactive profile generator
    hermes -s agent-factory — same, via skill load

Install:
    hermes plugins install github.com/bonaventuratommasosam-bot/hermes-agent-factory --enable
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def register(ctx) -> None:
    """Register the agent-factory skill and CLI command with Hermes."""
    # Register the skill (loadable via -s agent-factory or /skill agent-factory)
    skill_md = ROOT / "skills" / "agent-factory" / "SKILL.md"
    if skill_md.exists():
        ctx.register_skill("agent-factory", skill_md)

    # Register CLI command: hermes factory create
    ctx.register_cli_command(
        name="factory",
        help="Agent Factory — generate Hermes agent profiles from plain-language descriptions",
        setup_fn=_setup_factory_cli,
        handler_fn=_run_factory,
        description=(
            "Describe what you need in plain language, answer a few quick "
            "questions, and Agent Factory generates a complete, ready-to-run "
            "Hermes profile (SOUL, GOAL, skills, cron, config, .env.EXAMPLE)."
        ),
    )


def _setup_factory_cli(parser) -> None:
    parser.add_argument(
        "action",
        nargs="?",
        default="create",
        choices=["create"],
        help="Action: create a new agent profile",
    )
    parser.add_argument(
        "--name",
        help="Profile name (lowercase, hyphens OK). Auto-derived if not provided.",
    )
    parser.add_argument(
        "--description",
        help="What the agent should do. If omitted, interactive interview starts.",
    )


def _run_factory(args) -> int:
    """Handle 'hermes factory create' by printing a guided start message.

    The actual interview + generation is handled by loading the
    agent-factory skill. This CLI command provides a clean entry point
    and prints instructions.
    """
    if args.action == "create":
        print()
        print("  Agent Factory — build your AI agent")
        print("  ─────────────────────────────────────")
        print()
        print("  Describe what you need and answer a few quick questions.")
        print("  I'll generate a complete Hermes profile ready to run.")
        print()
        print("  To start, load the factory skill:")
        print("    /skill agent-factory")
        print()
        print("  Or restart Hermes with:")
        print("    hermes -s agent-factory")
        print()
        return 0
    return 1
