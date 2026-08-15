# LLM Wiki Knowledge Graph Dashboard

แดชบอร์ดแบบ local สำหรับดูความสัมพันธ์ระหว่างหน้า Markdown ใน Wiki

## Run

จาก root ของ Wiki:

```bash
python3 dashboard/server.py --host 127.0.0.1 --port 8765
```

เปิด `http://127.0.0.1:8765/`

## VPS access through SSH tunnel

The server intentionally binds to localhost. From your own computer, keep the SSH session open and run:

```bash
ssh -N -L 8765:127.0.0.1:8765 codex@YOUR_VPS_IP
```

Then open `http://127.0.0.1:8765/` in your local browser. In this URL, `127.0.0.1` means your own computer because SSH forwards it to the VPS. Do not open the port publicly without adding authentication.

## User service

Install the included `llm-wiki-dashboard.service` into `~/.config/systemd/user/`, then run:

```bash
systemctl --user daemon-reload
systemctl --user enable --now llm-wiki-dashboard.service
```

ระบบจะอ่านหน้า `.md` จาก `entities/`, `concepts/`, `comparisons/` และ `queries/` ทุกครั้งที่โหลด `/api/graph` แล้วสร้าง:

- โหนดจากหน้า Wiki
- เส้นจาก `[[wikilinks]]`
- สีแยกตาม page type
- ค้นหาและกรองตาม domain/type
- Node inspector แสดง tags, confidence, excerpt และหน้าที่เชื่อมโยง

หน้า `sensitivity: restricted` จะไม่ถูกส่งออกโดย API
