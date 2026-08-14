# Wiki Log

> Append-only record of wiki actions.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete.
> Rotate to `log-YYYY.md` after 500 entries.

## [2026-08-14] create | Multi-domain LLM Wiki initialized

- Owner: P'Su
- Domains: clinic, automation, AI/LLM/Hermes, projects, and personal knowledge
- Created the three-layer structure: immutable raw sources, maintained wiki pages, and schema
- Created `SCHEMA.md`, `index.md`, and `log.md`
- Initial content pages: 0

## [2026-08-14] ingest | Hermes Agent

- Source captured: `raw/articles/hermes-agent-overview.md`
- Pages created: `entities/hermes-agent.md`, `concepts/hermes-architecture.md`, `concepts/llm-wiki.md`
- Updated: `index.md`
- Covered Hermes capabilities, architecture, context compression, prompt caching, plugin compatibility, and the Wiki operating workflow
- No secrets or patient-identifying information included
