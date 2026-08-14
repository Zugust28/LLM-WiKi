---
title: LLM Wiki Workflow For Hermes
created: 2026-08-14
updated: 2026-08-14
type: concept
domain: ai-llm
tags: [llm, hermes-agent, knowledge-management, prompting, process]
sources: [raw/articles/hermes-agent-overview.md]
confidence: medium
sensitivity: normal
contested: false
contradictions: []
---

# LLM Wiki Workflow For Hermes

## วิธีใช้

Hermes ใช้ Wiki นี้เป็น persistent knowledge layer ที่อยู่ระหว่าง raw sources กับบทสนทนา Agent ต้องอ่าน `SCHEMA.md`, `index.md` และ log ล่าสุดก่อนทำงานทุกครั้ง จากนั้นจึงค้นหน้าที่เกี่ยวข้องและสร้าง synthesis ที่อ้างอิงด้วย wiki links [[hermes-agent]] [[hermes-architecture]]

## Ingest

เมื่อมีบทความ เอกสาร หรือข้อมูลใหม่ ให้เก็บ raw source แบบ immutable พร้อม provenance และ hash ก่อน แล้วตรวจหน้าที่มีอยู่เพื่อ update canonical pages แทนการสร้าง duplicate การเปลี่ยนแปลงควรอัปเดต index และ log ในรอบเดียว

## Query

คำตอบที่เป็นการสังเคราะห์และมีประโยชน์ระยะยาวควรถูก file กลับไปที่ `queries/` หรือ `comparisons/` ส่วนคำถาม lookup ชั่วคราวไม่จำเป็นต้องสร้างหน้าใหม่

## Lint

การตรวจสุขภาพควรมองหา broken links, orphan pages, หน้าไม่อยู่ใน index, frontmatter ไม่ครบ, tag ผิด taxonomy, source drift, stale claims, contradictions และหน้า sensitive ที่ตั้งค่าไม่ถูกต้อง

## ขอบเขต

Wiki ไม่ใช่ที่เก็บ API key, token, password หรือสถานะงานชั่วคราว และไม่ควรทำให้ Hermes ต้อง rebuild system prompt กลาง conversation เพราะจะขัดกับ prompt caching invariant
