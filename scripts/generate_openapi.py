"""Generate OpenAPI schema for the API.

This script imports the FastAPI app and dumps its schema to `openapi.json`.
"""

from __future__ import annotations

import json
import os
import sys

# Ensure the repository root is on sys.path so `app` can be imported when this
# script is invoked from within the `scripts/` directory.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app.main import create_app


def main() -> None:
    app = create_app()
    with open("openapi.json", "w", encoding="utf-8") as f:
        json.dump(app.openapi(), f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
