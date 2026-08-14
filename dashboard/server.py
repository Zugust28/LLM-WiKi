#!/usr/bin/env python3
"""Small dependency-free server for the LLM Wiki knowledge graph."""
from __future__ import annotations

import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

WIKI_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_ROOT = Path(__file__).resolve().parent
PAGE_DIRS = ("entities", "concepts", "comparisons", "queries")
LINK_RE = re.compile(r"\[\[([^]|#]+)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    values: dict[str, str] = {}
    for line in parts[0][4:].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values, parts[1]


def list_values(value: str) -> list[str]:
    value = value.strip().strip("[]")
    return [item.strip().strip("'\"") for item in value.split(",") if item.strip()]


def build_graph() -> dict:
    pages: dict[str, dict] = {}
    paths: dict[str, Path] = {}
    for directory in PAGE_DIRS:
        for path in sorted((WIKI_ROOT / directory).glob("*.md")):
            frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
            if frontmatter.get("sensitivity") == "restricted":
                continue
            slug = path.stem
            pages[slug] = {
                "id": slug,
                "title": frontmatter.get("title", slug.replace("-", " ").title()),
                "type": frontmatter.get("type", directory.rstrip("s")),
                "domain": frontmatter.get("domain", "unknown"),
                "tags": list_values(frontmatter.get("tags", "")),
                "confidence": frontmatter.get("confidence", ""),
                "path": str(path.relative_to(WIKI_ROOT)),
                "excerpt": re.sub(r"\s+", " ", body.replace("#", "")).strip()[:220],
            }
            paths[slug] = path

    links: list[dict[str, str]] = []
    for slug, page_path in paths.items():
        if slug not in pages:
            continue
        text = page_path.read_text(encoding="utf-8")
        _, body = parse_frontmatter(text)
        seen: set[str] = set()
        for target in LINK_RE.findall(body):
            target = target.strip()
            if target in pages and target not in seen and target != slug:
                links.append({"source": slug, "target": target})
                seen.add(target)
    return {
        "pages": list(pages.values()),
        "links": links,
        "meta": {"wiki": str(WIKI_ROOT), "page_count": len(pages), "link_count": len(links)},
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        route = urlparse(self.path).path
        if route == "/api/graph":
            payload = json.dumps(build_graph(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        if route in ("/", "/index.html"):
            payload = (DASHBOARD_ROOT / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        self.send_error(404)

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Serve the LLM Wiki graph dashboard")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"LLM Wiki dashboard: http://{args.host}:{args.port}", flush=True)
    server.serve_forever()
