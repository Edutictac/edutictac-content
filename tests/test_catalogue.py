import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_manifest_builder_generates_valid_hashes():
    payload = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    assert payload["catalog_version"] == "2026.09.1"
    assert {item["channel"] for item in payload["items"]} == {"resources", "eduhoot"}
    for item in payload["items"]:
        artifact = item["artifact"]
        digest = hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest()
        assert artifact["sha256"] == digest


def test_validator_checks_published_manifest():
    result = subprocess.run(
        ["python3", "scripts/validate-manifest.py", "manifest.json", "--check-files"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr

