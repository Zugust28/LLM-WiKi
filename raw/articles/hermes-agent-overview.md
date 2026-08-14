---
source_url: https://github.com/NousResearch/hermes-agent
ingested: 2026-08-14
sha256: b3ad253d9c698fe3abd7b6f59003f641ea0b76adfd66f6118597c7d1cd45d524
source_type: note
sensitivity: normal
---

# Hermes Agent source notes

Curated from the Hermes Agent repository README, pyproject metadata, developer documentation, and the local checkout at `/home/codex/.hermes/hermes-agent` on 2026-08-14.

## Identity

Hermes Agent is an MIT-licensed self-improving AI agent by Nous Research. The repository currently reports version 0.20.0 in `pyproject.toml`. The project supports local and remote deployment, including a low-cost VPS, GPU infrastructure, and serverless terminal backends.

## User-facing capabilities

- Interactive CLI/TUI with multiline editing, slash-command autocomplete, history, interruption, and streaming tool output.
- Messaging gateway integrations including Telegram, Discord, Slack, WhatsApp, Signal, and email.
- Persistent memory, session search, skill creation and improvement, scheduled cron jobs, and isolated subagent delegation.
- Multiple model providers and user-selectable models without changing application code.
- Terminal backends including local, Docker, SSH, Singularity, Modal, Daytona, and Vercel Sandbox.
- Research workflows including batch trajectory generation and trajectory compression.

## Core architecture facts

- The agent core is centered around `run_agent.py`, with tool discovery and dispatch in `model_tools.py`, toolset definitions in `toolsets.py`, and state persistence in `hermes_state.py`.
- Context management has two layers: gateway session hygiene at roughly 85% of context and the in-loop agent compressor at a configurable default of 50%.
- Prompt caching is treated as a core invariant. Past context, toolsets, and system prompt must remain stable during a conversation except during context compression.
- In-place compression is the default: the live session keeps one durable ID while the summarized middle replaces older context and the old turns remain searchable.

## Extension model

Hermes favors extension at the edges. Native plugins can register tools, hooks, CLI commands, and bundled skills. Separate extension surfaces exist for model providers, memory providers, context engines, image/video generation, browser/search backends, desktop, dashboard, and MCP servers.

## Operational references

- Official docs: https://hermes-agent.nousresearch.com/docs/
- Repository: https://github.com/NousResearch/hermes-agent
- Local checkout: `/home/codex/.hermes/hermes-agent`
- User configuration: profile-scoped Hermes home, normally `~/.hermes/`

This note is a curated source record. It is not a copy of the upstream repository and contains no credentials or secret configuration.
