# Wiki Schema

## Domain

This is P'Su's multi-domain personal knowledge base. It covers:

- Clinic operations and reusable clinical-business knowledge
- Automation and integrations, including n8n, LINE OA, Google Workspace, and MCS
- AI, LLMs, Hermes Agent, and related research
- Projects, architecture, decisions, and lessons learned
- Personal knowledge that is useful over time

The wiki stores durable knowledge, not temporary task status or a duplicate of chat history.

## Domain Boundaries

Every page must declare exactly one primary `domain`:

- `clinic`
- `automation`
- `ai-llm`
- `project`
- `personal`
- `cross-domain`

Use `cross-domain` only when a page genuinely connects two or more domains. Do not duplicate the same fact across domain-specific pages; link to the canonical page instead.

## Privacy And Safety

- Do not store passwords, API keys, access tokens, credentials, or payment secrets.
- Do not copy `.env` files or credential stores into this wiki.
- Prefer reusable clinic knowledge over patient-level records.
- Patient-identifying information may be stored only when P'Su explicitly requests it and identifies this wiki as the intended destination.
- When patient-level content is permitted, include only necessary facts, mark the page `sensitivity: restricted`, and never infer diagnoses or unstated details.
- Do not publish or sync restricted pages to public repositories or shared services.

## Conventions

- File names use lowercase kebab-case with no spaces.
- Raw sources live under `raw/` and are immutable after ingestion.
- Wiki pages live under `entities/`, `concepts/`, `comparisons/`, or `queries/`.
- Every wiki page starts with YAML frontmatter.
- Every substantive page should have at least two relevant `[[wikilinks]]`. A new wiki may temporarily have fewer until related pages exist.
- Update `updated` whenever page content changes.
- Add every new page to `index.md` under its domain and type.
- Append every ingest, query filed, lint, archive, and structural change to `log.md`.
- On pages synthesizing three or more sources, add provenance markers such as `^[raw/articles/source-file.md]` to sourced claims.
- Write content in Thai by default. Preserve established English technical terms where translation would reduce precision.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
domain: clinic | automation | ai-llm | project | personal | cross-domain
tags: [approved-tag]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
sensitivity: normal | internal | restricted
contested: false
contradictions: []
---
```

Required fields are `title`, `created`, `updated`, `type`, `domain`, `tags`, `sources`, and `sensitivity`. `confidence`, `contested`, and `contradictions` are recommended when claims are uncertain, opinion-heavy, or changing quickly.

## Raw Source Frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: body-sha256
source_type: article | paper | transcript | note | dataset
sensitivity: normal | internal | restricted
---
```

Compute `sha256` over the body after the closing frontmatter delimiter. On re-ingest, skip unchanged content and flag changed content for review. Never silently overwrite a raw source.

## Tag Taxonomy

Only use tags listed below. Add a tag here before using it.

### Clinic

- `clinic-operations`
- `patient-follow-up`
- `procedure`
- `promotion`
- `customer-service`
- `clinic-policy`

### Automation

- `automation`
- `n8n`
- `line-oa`
- `google-workspace`
- `mcs`
- `integration`
- `data-sync`
- `workflow-design`

### AI And LLM

- `ai`
- `llm`
- `hermes-agent`
- `agent-architecture`
- `prompting`
- `knowledge-management`
- `evaluation`
- `research`

### Projects

- `project`
- `architecture`
- `decision`
- `requirement`
- `implementation`
- `incident`
- `lesson-learned`

### Personal And Meta

- `personal`
- `goal`
- `preference`
- `process`
- `comparison`
- `timeline`
- `reference`

## Page Thresholds

- Create a page when a concept or entity appears in at least two sources, or is central to one source.
- Update an existing canonical page when the subject already exists.
- Do not create pages for passing mentions, temporary task progress, or facts likely to expire within a week.
- File a query result only when it contains a substantial synthesis that would be expensive to recreate.
- Split pages longer than roughly 200 lines into linked subtopics.
- Archive fully superseded pages under `_archive/` and repair their inbound links.

## Page Types

### Entity Pages

Use for people, organizations, products, systems, models, and named projects. Include an overview, durable facts, relationships, and sources.

### Concept Pages

Use for methods, workflows, policies, recurring problems, and technical concepts. Include definition, current understanding, practical implications, open questions, and related concepts.

### Comparison Pages

Use for side-by-side evaluations. State the decision context, compare consistent dimensions, identify evidence and uncertainty, and record a scoped conclusion.

### Query Pages

Use for valuable answers or syntheses produced while exploring the wiki. State the question, evidence used, answer, caveats, and follow-up questions.

## Ingest Procedure

1. Read `SCHEMA.md`, `index.md`, and recent `log.md` entries.
2. Capture the source under the correct immutable `raw/` directory with frontmatter and body hash.
3. Search the index and existing pages before creating anything.
4. Discuss key takeaways with P'Su unless the ingest is explicitly automated.
5. Create or update canonical pages, preserve domain boundaries, and add cross-links.
6. Record uncertainty and contradictions instead of silently replacing conflicting claims.
7. Update `index.md` once after all page edits.
8. Append a structured entry to `log.md` listing every file changed.
9. Ask before an ingest that would modify more than ten existing wiki pages.

## Query Procedure

1. Read `index.md` and search all Markdown pages when needed.
2. Read relevant canonical pages and their cited raw sources when precision matters.
3. Answer with `[[wikilink]]` citations to wiki pages.
4. File only substantial, reusable synthesis into `queries/` or `comparisons/`.
5. Update the index and log when a result is filed.

## Lint Procedure

Check for:

- Broken and missing wikilinks
- Orphan pages with no inbound links
- Pages absent from `index.md`
- Missing or invalid frontmatter
- Tags outside this taxonomy
- Raw-source hash drift
- Pages over 200 lines
- Stale claims superseded by newer sources
- `contested: true`, explicit contradictions, and low-confidence claims
- Sensitive pages with incorrect `sensitivity`
- `log.md` exceeding 500 entries; rotate it to `log-YYYY.md`

Report findings by severity and append the lint result to `log.md`.

## Index Scaling

- Keep entries alphabetical within each subsection.
- Each entry contains a wikilink and one-line summary.
- Split a subsection when it exceeds 50 entries.
- When the wiki exceeds 200 pages, maintain `_meta/topic-map.md` to group pages by theme.

## Update Policy

When new information conflicts with existing content:

1. Compare dates, provenance, and source quality.
2. Preserve both claims when the conflict is unresolved.
3. Set `contested: true` and list conflicting pages under `contradictions`.
4. Lower confidence when evidence is weak or single-source.
5. Flag the decision for P'Su rather than inventing a resolution.
