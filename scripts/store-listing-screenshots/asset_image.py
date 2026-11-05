"""Decode and inspect images; never change them."""
import hashlib
import warnings
from PIL import Image
from asset_manifest import asset_path
from asset_rules import RULES


def metadata_errors(info, rule, png_only=True, maximum=True):
    errors = []
    width, height = info["pixels"]
    if not (width * 9 == height * 16 or width * 16 == height * 9):
        errors.append("ASPECT: expected exact 16:9 or 9:16")
    if min(width, height) < rule.minimum_side or max(width, height) > rule.maximum_side:
        errors.append("DIMENSIONS: outside this category's per-side limits")
    if maximum and max(width, height) != rule.maximum_side:
        errors.append("QUALITY: rerender from source at the maximum allowed dimensions")
    if info["bytes"] > rule.maximum_bytes:
        errors.append("SIZE: exceeds the category's byte limit")
    allowed = {"PNG"} if png_only else {"PNG", "JPEG"}
    if info["format"] not in allowed:
        errors.append("FORMAT: unsupported format or violates PNG-only preference")
    if info["mode"] != "RGB" or info["transparent"]:
        errors.append("COLOR: use opaque RGB (24-bit PNG or RGB JPEG)")
    if info["frames"] != 1:
        errors.append("ANIMATION: use a single still screenshot")
    return errors


def check_image(base, item, translation, png_only=True, maximum=True):
    result = {k: item[k] for k in ("file", "view", "locale", "category")}
    errors = []
    try:
        path = asset_path(base, item["file"])
        rule = RULES[item["category"]]
        expected = translation["stem"] + "_" + rule.suffix
        if path.stem != expected:
            errors.append("NAME: expected " + expected + ".png (or .jpg when JPEG is enabled)")
        size = path.stat().st_size
        if size > rule.maximum_bytes:
            errors.append("SIZE: exceeds the category's byte limit")
            return {**result, "bytes": size, "errors": errors}
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(path) as image:
                info = {"pixels": list(image.size), "format": image.format, "mode": image.mode,
                        "transparent": "transparency" in image.info or "A" in image.getbands(),
                        "frames": getattr(image, "n_frames", 1), "bytes": size}
                image.verify()
            with Image.open(path) as image:
                image.load()
        errors.extend(metadata_errors(info, rule, png_only, maximum))
        extension_format = {".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG"}.get(path.suffix.lower())
        if extension_format != info["format"]:
            errors.append("EXTENSION: extension does not match the decoded image format")
        info["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        if info["sha256"] != item["sha256"]:
            errors.append("HASH: file changed since manifest creation")
        result.update(info)
    except (OSError, ValueError, SyntaxError, Image.DecompressionBombWarning, Image.DecompressionBombError) as exc:
        errors.append("DECODE: " + str(exc))
    return {**result, "errors": errors}
