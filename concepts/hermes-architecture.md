---
title: Hermes Architecture And Invariants
created: 2026-08-14
updated: 2026-08-14
type: concept
domain: ai-llm
tags: [hermes-agent, agent-architecture, llm, architecture, knowledge-management]
sources: [raw/articles/hermes-agent-overview.md]
confidence: high
sensitivity: normal
contested: false
contradictions: []
---

# Hermes Architecture And Invariants

## Core structure

Hermes ใช้ core agent ที่เชื่อมกับ provider, tool registry, toolsets, session state, memory, compression และ gateway/platform adapters การเพิ่ม capability ควรเริ่มจากการขยาย code ที่มีอยู่ แล้วพิจารณา CLI + skill, service-gated tool, plugin, MCP และ core tool ตามลำดับ เพื่อลด schema footprint ที่ถูกส่งไปกับทุก model call [[hermes-agent]]

จุดอ้างอิงสำคัญใน checkout คือ `run_agent.py` สำหรับ conversation loop, `model_tools.py` สำหรับ discovery/dispatch, `toolsets.py` สำหรับการจัดกลุ่ม tools และ `hermes_state.py` สำหรับ session storage

## Context management

มี compression สองชั้น:

1. Gateway session hygiene เป็น safety net ก่อนเข้า agent โดยทำงานราว 85% ของ context และใช้ token ที่ API รายงานเมื่อมี หรือ rough estimate เป็น fallback
2. Agent ContextCompressor ทำงานใน tool loop โดยค่าเริ่มต้นราว 50% ของ context และใช้ token count ที่แม่นกว่า

ค่า compression อยู่ใน `config.yaml` ใต้ `compression` และสามารถเลือก context engine แบบ plugin ได้ผ่าน `context.engine` โดย plugin ไม่ถูกเปิดใช้อัตโนมัติ ต้องตั้งค่าอย่างชัดเจน

ค่าเริ่มต้น `compression.in_place: true` ทำให้ conversation ใช้ session ID เดิมตลอดอายุ session: ส่วนกลางที่ถูกสรุปจะถูกแทนที่ ขณะที่ turn เดิมถูกเก็บเป็น compacted และยังค้นคืนได้ ไม่ได้ถูกลบ

## Prompt caching invariant

ระบบต้องรักษา system prompt, toolsets และ past context ให้คงที่ตลอด conversation การเปลี่ยนสิ่งเหล่านี้กลาง session ทำให้ prompt cache เสียและเพิ่มค่าใช้จ่าย การเปลี่ยนแปลงที่มีผลต่อ system-prompt state ควร deferred ไป session ถัดไป เว้นแต่ผู้ใช้เลือก immediate invalidation อย่างชัดเจน

## Plugin compatibility

Native plugin contract เน้น additive compatibility: ไม่ลบหรือ rename `PluginContext` methods, เพิ่ม hook payload เป็น keyword fields, ให้ provider methods ใหม่มี default implementation และตรวจ signature ก่อนส่ง optional kwargs การ version ควรใช้เฉพาะ wire/persisted contract ที่มี migration หรือ compatibility requirement จริง

Third-party product integrations ควรอยู่ใน standalone plugin repository และติดตั้งผ่าน user plugin path หรือ package entry point ไม่ควรเพิ่มภาระ maintenance เข้า core tree

## Related pages

- [[hermes-agent]]
- [[llm-wiki]]
