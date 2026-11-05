import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from asset_check import validate
from asset_manifest import schema
from asset_rules import POLICY


def manifest(count=1, category="phone"):
    views = {f"view-{i}": {loc: {"stem": f"visit-{i}", "approved": True, "approval_ref": "Owner approval"}
                           for loc in ("en-US", "es-419")} for i in range(count)}
    assets = [{"view": view, "locale": loc, "category": category, "file": f"{loc}/{view}_{category}.png",
               "sha256": f"{i:064x}", "rendered_from_source": True, "render_evidence": "capture.json"}
              for i, view in enumerate(views) for loc in ("en-US", "es-419")]
    return {"policy": POLICY["version"], "locales": ["en-US", "es-419"], "categories": [category],
            "views": views, "assets": assets}


class ManifestTests(unittest.TestCase):
    def check(self, data, complete=False):
        with tempfile.TemporaryDirectory(prefix="manifest-test-") as folder:
            path = Path(folder) / "assets.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with patch("asset_check.check_image", side_effect=lambda base, item, *a: {**item, "errors": []}):
                return validate(path, complete=complete)

    def test_batch_not_mistaken_for_listing_ready(self):
        data = manifest()
        self.assertEqual(self.check(data)["status"], "PASSED")
        self.assertTrue(all(c["status"] == "PARTIAL" for c in self.check(data)["counts"]))
        self.assertEqual(self.check(data, True)["status"], "FAILED")
        self.assertEqual(self.check(manifest(2), True)["status"], "PASSED")

    def test_count_boundaries_per_category_and_language(self):
        for category, minimum in (("phone", 2), ("tablet7", 1), ("tablet10", 1), ("desktop", 4), ("xr", 4)):
            self.assertEqual(self.check(manifest(minimum, category), True)["status"], "PASSED")
            self.assertEqual(self.check(manifest(8, category), True)["status"], "PASSED")
            self.assertEqual(self.check(manifest(9, category))["status"], "FAILED")
        self.assertEqual(self.check(manifest(3, "desktop"), True)["status"], "FAILED")
        self.assertEqual(self.check(manifest(3, "xr"), True)["status"], "FAILED")

    def test_missing_localization_and_duplicates(self):
        data = manifest(2)
        data["assets"].pop()
        self.assertTrue(any(e.startswith("MISSING") for e in self.check(data)["errors"]))
        data = manifest()
        data["assets"].append(copy.deepcopy(data["assets"][0]))
        self.assertTrue(any(e.startswith("DUPLICATE") for e in self.check(data)["errors"]))
        data = manifest(2)
        for asset in data["assets"]:
            asset["sha256"] = "0" * 64
        self.assertTrue(any(e.startswith("DUPLICATE") for e in self.check(data)["errors"]))

    def test_missing_approval_and_source_attestation(self):
        for changes in ({"approved": False}, {"approval_ref": ""}):
            data = manifest()
            data["views"]["view-0"]["es-419"].update(changes)
            with self.assertRaises(ValueError):
                schema(data)
        data = manifest()
        data["assets"][0]["rendered_from_source"] = False
        with self.assertRaises(ValueError):
            schema(data)

    def test_malformed_schema(self):
        for change in ({"locales": []}, {"categories": ["tablet"]}, {"views": []}, {"png_only": "yes"},
                       {"assets": []}, {"policy": "outdated"}, {"categories": ["phone", "phone"]}):
            with self.assertRaises(ValueError):
                schema({**manifest(), **change})
        data = manifest()
        data["assets"][0]["sha256"] = 123
        with self.assertRaises(ValueError):
            schema(data)
