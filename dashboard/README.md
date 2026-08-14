# LLM Wiki Knowledge Graph Dashboard

แดชบอร์ดแบบ local สำหรับดูความสัมพันธ์ระหว่างหน้า Markdown ใน Wiki

## Run

จาก root ของ Wiki:

```bash
python3 dashboard/server.py --host 127.0.0.1 --port 8765
```

เปิด `http://127.0.0.1:8765/`

ระบบจะอ่านหน้า `.md` จาก `entities/`, `concepts/`, `comparisons/` และ `queries/` ทุกครั้งที่โหลด `/api/graph` แล้วสร้าง:

- โหนดจากหน้า Wiki
- เส้นจาก `[[wikilinks]]`
- สีแยกตาม page type
- ค้นหาและกรองตาม domain/type
- Node inspector แสดง tags, confidence, excerpt และหน้าที่เชื่อมโยง

หน้า `sensitivity: restricted` จะไม่ถูกส่งออกโดย API
