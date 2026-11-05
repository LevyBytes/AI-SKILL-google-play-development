import unittest
from asset_image import metadata_errors
from asset_rules import RULES


class MetadataTests(unittest.TestCase):
    def info(self, rule, portrait=True, **changes):
        return {"pixels": rule.pixels(portrait), "bytes": rule.maximum_bytes, "format": "PNG",
                "mode": "RGB", "transparent": False, "frames": 1, **changes}

    def test_all_maximum_sizes_and_exact_byte_boundaries(self):
        for rule in RULES.values():
            for portrait in (True, False):
                with self.subTest(rule=rule, portrait=portrait):
                    self.assertEqual(metadata_errors(self.info(rule, portrait), rule), [])

    def test_size_over_by_one_rejected_in_every_category(self):
        for rule in RULES.values():
            errors = metadata_errors(self.info(rule, bytes=rule.maximum_bytes + 1), rule)
            self.assertTrue(any(e.startswith("SIZE") for e in errors))

    def test_invalid_dimensions_aspect_and_quality(self):
        rule = RULES["phone"]
        for pixels, code in (([100, 100], "DIMENSIONS"), ([2160, 3841], "DIMENSIONS"),
                             ([1080, 1920], "QUALITY"), ([2160, 2160], "ASPECT")):
            with self.subTest(pixels=pixels):
                self.assertTrue(any(e.startswith(code) for e in metadata_errors(self.info(rule, pixels=pixels), rule)))

    def test_minimums_and_legacy_quality_override(self):
        for key, pixels in (("phone", [320, 576]), ("tablet7", [320, 576]),
                            ("tablet10", [1080, 1920]), ("desktop", [1080, 1920]), ("xr", [720, 1280])):
            rule = RULES[key]
            errors = metadata_errors(self.info(rule, pixels=pixels), rule, maximum=False)
            self.assertFalse(any(e.startswith("DIMENSIONS") for e in errors))
            errors = metadata_errors(self.info(rule, pixels=[rule.minimum_side - 1, 2000]), rule, maximum=False)
            self.assertTrue(any(e.startswith("DIMENSIONS") for e in errors))
        self.assertEqual(metadata_errors(self.info(RULES["phone"], pixels=[1080, 1920]),
                                         RULES["phone"], maximum=False), [])

    def test_formats_color_transparency_animation(self):
        rule = RULES["xr"]
        for changes in ({"format": "GIF"}, {"mode": "CMYK"}, {"mode": "RGBA"},
                        {"transparent": True}, {"frames": 2}, {"format": "JPEG"}):
            self.assertTrue(metadata_errors(self.info(rule, **changes), rule))
        self.assertEqual(metadata_errors(self.info(rule, format="JPEG"), rule, png_only=False), [])
