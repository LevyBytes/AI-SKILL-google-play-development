"""File conformance and listing-count readiness are separate results."""
import itertools
import json
from collections import Counter
from pathlib import Path
from asset_image import check_image
from asset_manifest import schema
from asset_rules import POLICY, RULES


def validate(manifest, complete=False, maximum=True):
    manifest = Path(manifest).resolve()
    data = schema(json.loads(manifest.read_text(encoding="utf-8")))
    files, errors, seen_paths, seen_keys, seen_hashes = [], [], set(), set(), set()
    for item in data["assets"]:
        key = (item["view"], item["locale"], item["category"])
        path_key = item["file"].casefold()
        if key in seen_keys or path_key in seen_paths:
            errors.append("DUPLICATE: repeated view/locale/category or filename: " + item["file"])
        seen_keys.add(key)
        seen_paths.add(path_key)
        localized = data["views"][item["view"]][item["locale"]]
        result = check_image(manifest.parent, item, localized, data.get("png_only", True), maximum)
        files.append(result)
        digest_key = (item["locale"], item["category"], result.get("sha256"))
        if result.get("sha256") and digest_key in seen_hashes:
            errors.append("DUPLICATE: same image repeated within one locale/category")
        seen_hashes.add(digest_key)
    expected = set(itertools.product(data["views"], data["locales"], data["categories"]))
    for key in sorted(expected - seen_keys):
        errors.append("MISSING: approved view/locale/category: " + "/".join(key))
    counts = Counter((a["locale"], a["category"]) for a in data["assets"])
    readiness = []
    for locale, category in itertools.product(data["locales"], data["categories"]):
        rule, count = RULES[category], counts[locale, category]
        enough = rule.minimum_count <= count <= rule.maximum_count
        readiness.append({"locale": locale, "category": category, "count": count,
                          "minimum": rule.minimum_count, "maximum": rule.maximum_count,
                          "status": "PASSED" if enough else "PARTIAL"})
        if count > rule.maximum_count or (complete and not enough):
            errors.append(f"COUNT: {locale}/{category}: {count}; expected {rule.minimum_count}-{rule.maximum_count}")
    passed = not errors and not any(f["errors"] for f in files)
    return {"status": "PASSED" if passed else "FAILED", "scope": "complete-set" if complete else "batch",
            "policy": POLICY["version"], "maximum_resolution_required": maximum,
            "files": files, "counts": readiness, "errors": errors,
            "human_review": "Not machine-verified: prose approval, language, legibility, fidelity, device support.",
            "publication": "Not performed; passing this check does not guarantee Play acceptance."}
