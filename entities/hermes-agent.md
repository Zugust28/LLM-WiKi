---
title: Hermes Agent
author: Nous Research
created: 2026-08-14
updated: 2026-08-14
type: entity
domain: ai-llm
tags: [ai, llm, hermes-agent, agent-architecture, knowledge-management]
sources: [raw/articles/hermes-agent-overview.md]
confidence: high
sensitivity: normal
contested: false
contradictions: []
---

# Hermes Agent

## ภาพรวม

Hermes Agent คือ AI agent แบบ self-improving ของ Nous Research ที่ทำงานได้ทั้ง CLI/TUI, messaging gateway และ desktop application จุดเด่นคือมี learning loop ในตัว: ใช้ memory ข้าม session, สร้างและปรับปรุง skills จากประสบการณ์, ค้นบทสนทนาเก่า และรองรับการทำงานต่อเนื่องบน VPS หรือ infrastructure อื่น ๆ [[hermes-architecture]]

## ความสามารถหลัก

- เลือก model/provider ได้หลายแบบโดยไม่ต้องแก้ application code
- CLI/TUI ที่มี multiline editing, slash-command autocomplete, history, interrupt และ streaming tool output
- Gateway สำหรับ Telegram, Discord, Slack, WhatsApp, Signal และช่องทางอื่น
- Persistent memory, session search, skills และ scheduled cron jobs
- Delegation สำหรับสร้าง isolated subagents และทำงานหลาย workstream พร้อมกัน
- Terminal backends หลายแบบ เช่น local, Docker, SSH, Singularity, Modal, Daytona และ Vercel Sandbox
- รองรับงานวิจัย เช่น batch trajectory generation และ trajectory compression

## จุดที่เกี่ยวข้องกับ Wiki นี้

Hermes สามารถทำหน้าที่เป็นผู้ดูแล Wiki ได้โดยอ่าน source, สังเคราะห์ข้อมูล, สร้างหน้าที่เชื่อมด้วย wiki links, ตรวจความขัดแย้ง และอัปเดต index/log ตาม schema ของ Wiki นี้ [[llm-wiki]]

## การติดตั้งและใช้งานโดยย่อ

- Linux, macOS, WSL2 และ Termux: ใช้ installer ของ Hermes
- Windows native: ใช้ PowerShell installer
- เริ่มสนทนา: `hermes`
- เลือก model: `hermes model`
- ตั้งค่า tools: `hermes tools`
- ตั้งค่า config: `hermes config set`
- เริ่ม gateway: `hermes gateway`
- ตรวจปัญหา: `hermes doctor`

คำสั่งและรายละเอียดควรตรวจจากเอกสารทางการรุ่นปัจจุบันก่อนใช้งานจริง เพราะ CLI และ provider เปลี่ยนแปลงได้

## แหล่งข้อมูล

- [Hermes Agent repository](https://github.com/NousResearch/hermes-agent)
- [Hermes documentation](https://hermes-agent.nousresearch.com/docs/)
