"""Check Markdown-local links and fragments offline; do not infer remote availability."""
from __future__ import annotations

from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)
            if key == "id" and value:
                self.ids.add(value)


def parse_document(path: Path):
    text = path.read_text(encoding="utf-8")
    # Fenced examples should not be interpreted as document links or headings.
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)
    html = References()
    html.feed(text)
    counts = {}
    for title in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text):
        title = re.sub(r"[`*_]", "", unescape(title)).lower()
        slug = re.sub(r"[^\w\- ]", "", title).strip().replace(" ", "-")
        suffix = counts.get(slug, 0)
        html.ids.add(slug + (f"-{suffix}" if suffix else ""))
        counts[slug] = suffix + 1
    markdown = re.findall(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+\"[^\"]*\")?\)", text)
    return html.links + [angle or plain for angle, plain in markdown], html.ids


def check(root: Path):
    root = root.resolve()
    failures = []
    checked = 0
    documents = sorted(root.glob("*.md"))
    for document in documents:
        links, _ = parse_document(document)
        for href in links:
            try:
                url = urlsplit(unescape(href))
            except ValueError:
                failures.append(f"{document.name}: malformed link {href}")
                continue
            if url.scheme in {"https", "http", "mailto", "tel"}:
                continue
            if url.scheme or url.netloc:
                failures.append(f"{document.name}: unsupported link {href}")
                continue
            checked += 1
            target = (document.parent / unquote(url.path)).resolve() if url.path else document
            if not target.is_relative_to(root):
                failures.append(f"{document.name}: target escapes repository: {href}")
            elif not target.is_file():
                failures.append(f"{document.name}: missing file: {href}")
            elif url.fragment:
                if target.suffix.lower() not in {".md", ".html", ".svg"}:
                    failures.append(f"{document.name}: unsupported fragment target: {href}")
                elif unquote(url.fragment) not in parse_document(target)[1]:
                    failures.append(f"{document.name}: missing fragment: {href}")
    return failures, len(documents), checked


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures, documents, checked = check(root)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"LOCAL_LINKS_PASS documents={documents} local_links={checked}; remote HTTP status not checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
