import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from asset_manifest import schema
from test_manifest import manifest


class PolicyTests(unittest.TestCase):
    def cli(self, command):
        script = Path(__file__).resolve().parents[1] / "play_assets.py"
        with tempfile.TemporaryDirectory(prefix="policy-test-") as folder:
            result = subprocess.run([sys.executable, "-I", "-B", str(script), command], cwd=folder,
                                    capture_output=True, text=True, encoding="utf-8", timeout=15,
                                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def test_emitted_profile_has_no_calendar_date(self):
        for command in ("guide", "template"):
            with self.subTest(command=command):
                self.assertNotRegex(json.dumps(self.cli(command)), r"\b\d{4}-\d{2}-\d{2}\b")

    def test_emitted_profile_matches_manifest_contract(self):
        guide, template = self.cli("guide"), self.cli("template")
        self.assertEqual(guide["version"], template["policy"])
        approved = manifest()
        approved["policy"] = template["policy"]
        self.assertIs(schema(approved), approved)
        approved["policy"] = "unknown-policy"
        with self.assertRaises(ValueError):
            schema(approved)
