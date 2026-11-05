"""Owner's Play Console screenshot specification, captured 2026-11-05; not a live policy fetch."""
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Rule:
    suffix: str
    minimum_side: int
    maximum_side: int
    maximum_bytes: int
    minimum_count: int
    maximum_count: int = 8

    def pixels(self, portrait=True):
        short = self.maximum_side * 9 // 16
        return [short, self.maximum_side] if portrait else [self.maximum_side, short]


RULES = {
    "phone": Rule("phone", 320, 3840, 8_000_000, 2),
    "tablet7": Rule("tablet7", 320, 3840, 8_000_000, 0),
    "tablet10": Rule("tablet10", 1080, 7680, 8_000_000, 0),
    "desktop": Rule("desktop", 1080, 7680, 8_000_000, 4),
    "xr": Rule("xr", 720, 7680, 15_000_000, 4),
}
POLICY = {
    "version": "owner-console-2026-11-05",
    "authority": "Owner-supplied Google Play Console limits; recheck Console before future publication.",
    "reference": "https://support.google.com/googleplay/android-developer/answer/9866151",
    "formats": ["PNG", "JPEG"],
    "aspect_ratios": ["16:9", "9:16"],
    "byte_units": "Decimal MB (conservative); no resizing or lossy recompression by this tool.",
    "rules": {key: asdict(value) for key, value in RULES.items()},
    "maximum_pixels": {key: [value.pixels(), value.pixels(False)] for key, value in RULES.items()},
    "reminders": [
        "Use approved prose for every language; localized stems, suffixes _phone/_tablet7/_tablet10/_desktop/_xr.",
        "Render HTML/SVG/text at target resolution; do not enlarge a previously rendered bitmap.",
        "PNG-only is the owner default. JPEG can be checked only when png_only is explicitly false.",
        "Different views need different approved example content; translations keep the same scenario.",
        "Approval, translation quality, actual device support and source fidelity require human review.",
        "Do not edit approved copy to store instructions. Do not commit, upload or publish assets.",
        "A batch can pass file checks while lacking the minimum screenshot count for a listing.",
    ],
}
