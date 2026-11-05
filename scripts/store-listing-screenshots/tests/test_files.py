import hashlib
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from asset_image import check_image
from asset_manifest import asset_path


class FileTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(prefix="asset-test-")
        self.addCleanup(self.folder.cleanup)
        self.base = Path(self.folder.name)
        self.path = self.base / "día-de-visitas_phone.png"
        Image.new("RGB", (576, 1024), "white").save(self.path)
        self.item = {"file": self.path.name, "view": "visits", "locale": "es-419", "category": "phone",
                     "sha256": hashlib.sha256(self.path.read_bytes()).hexdigest()}
        self.translation = {"stem": "día-de-visitas"}

    def check(self):
        return check_image(self.base, self.item, self.translation, maximum=False)["errors"]

    def test_rgb_png_and_unicode_localized_name(self):
        self.assertEqual(self.check(), [])

    def test_wrong_suffix(self):
        self.translation["stem"] = "wrong-name"
        self.assertTrue(any(e.startswith("NAME") for e in self.check()))

    def test_wrong_hash(self):
        self.item["sha256"] = "0" * 64
        self.assertTrue(any(e.startswith("HASH") for e in self.check()))

    def test_corrupt_and_truncated_images(self):
        original = self.path.read_bytes()
        for content in (b"not an image", original[:40]):
            self.path.write_bytes(content)
            self.assertTrue(any(e.startswith("DECODE") for e in self.check()))

    def test_mismatched_extension(self):
        renamed = self.path.with_suffix(".jpg")
        self.path.rename(renamed)
        self.item["file"] = renamed.name
        self.assertTrue(any(e.startswith("EXTENSION") for e in self.check()))

    def test_missing_file_and_escape_paths(self):
        self.item["file"] = "missing.png"
        self.assertTrue(any(e.startswith("DECODE") for e in self.check()))
        for value in ("../escape.png", "C:/escape.png", "/escape.png", "folder\\escape.png"):
            with self.assertRaises(ValueError):
                asset_path(self.base, value)

    def test_alpha_and_palette_transparency(self):
        Image.new("RGBA", (576, 1024)).save(self.path)
        self.assertTrue(any(e.startswith("COLOR") for e in self.check()))
        Image.new("P", (576, 1024)).save(self.path, transparency=0)
        self.assertTrue(any(e.startswith("COLOR") for e in self.check()))
