#!/usr/bin/env python3
"""Validate the shared catalogue manifest and its artifact hashes."""

import argparse
import hashlib
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--check-files", action="store_true")
    args = parser.parse_args()
    payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1 or not payload.get("items"):
        raise SystemExit("invalid manifest")
    for item in payload["items"]:
        artifact = item["artifact"]
        if args.check_files:
            path = args.manifest.parent / artifact["path"]
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != artifact["sha256"]:
                raise SystemExit(f"hash mismatch: {artifact['path']}")
    print(f"valid content manifest: {payload['catalog_version']} ({len(payload['items'])} items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

