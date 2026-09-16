#!/usr/bin/env python3
"""Static server for the FlashCard page.

Usage:  python3 serve.py [port]     (default port 8477)
Then open  http://127.0.0.1:8477/thanks.html
"""

import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent

MIME_OVERRIDES = {
    ".woff2": "font/woff2",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
    ".js": "text/javascript; charset=utf-8",
}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def guess_type(self, path):
        suffix = Path(path).suffix.lower()
        if suffix in MIME_OVERRIDES:
            return MIME_OVERRIDES[suffix]
        return super().guess_type(path)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8477
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"FlashCard running at http://127.0.0.1:{port}/thanks.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
