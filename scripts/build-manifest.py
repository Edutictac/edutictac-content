#!/usr/bin/env python3
"""Build the static manifest for the shared EduTicTac content catalogue."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).parents[1]
ITEMS = [
    {
        "id": "eduhoot:repas-sostenibilitat",
        "channel": "eduhoot",
        "title": "Repàs de sostenibilitat digital",
        "description": "Preguntes breus per revisar hàbits digitals sostenibles.",
        "language": "va",
        "license": "CC BY-SA 4.0",
        "revision": 1,
        "artifact": {"path": "activities/eduhoot/repas-sostenibilitat.json", "media_type": "application/json"},
        "metadata": {"subject": "competència digital", "educational_stage": "general", "tags": ["sostenibilitat"]},
    },
    {
        "id": "resources:guia-reparacio-dispositius",
        "channel": "resources",
        "title": "Guia breu: abans de substituir un dispositiu",
        "description": "Activitat de reflexió sobre reparació i reutilització.",
        "language": "va",
        "license": "CC BY-SA 4.0",
        "revision": 1,
        "artifact": {"path": "activities/resources/guia-reparacio-dispositius.md", "media_type": "text/markdown"},
        "metadata": {"subject": "sostenibilitat", "educational_stage": "general", "tags": ["reparació", "reutilització"]},
    },
]


def main() -> None:
    for item in ITEMS:
        path = ROOT / item["artifact"]["path"]
        item["artifact"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    payload = {
        "schema_version": 1,
        "catalog_version": "2026.09.1",
        "published_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": "edutictac-content",
        "items": ITEMS,
    }
    (ROOT / "manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

