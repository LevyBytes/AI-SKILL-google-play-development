"""Portable, relative-path manifest contract; no project paths or machine configuration."""
import re
from pathlib import Path
from asset_rules import POLICY, RULES


def schema(data):
    if not isinstance(data, dict) or data.get("policy") != POLICY["version"]:
        raise ValueError("Manifest must name policy " + POLICY["version"])
    for key in ("locales", "categories"):
        values = data.get(key)
        if not isinstance(values, list) or not values or any(not isinstance(v, str) for v in values):
            raise ValueError(key + " must be a nonempty list of strings")
        if len(set(values)) != len(values):
            raise ValueError(key + " contains duplicates")
    if any(c not in RULES for c in data["categories"]):
        raise ValueError("Unknown category; use phone, tablet7, tablet10, desktop or xr")
    if type(data.get("png_only", True)) is not bool:
        raise ValueError("png_only must be boolean")
    views = data.get("views")
    if not isinstance(views, dict) or not views:
        raise ValueError("views must map view IDs to approved, localized naming records")
    for view, translations in views.items():
        if not isinstance(translations, dict) or set(translations) != set(data["locales"]):
            raise ValueError("Each view needs exactly the requested locales: " + view)
        for locale, item in translations.items():
            if not isinstance(item, dict):
                raise ValueError("Each localized view must be an object")
            stem = item.get("stem", "")
            if not isinstance(stem, str) or not re.fullmatch(r"[^\W_][\w-]*", stem, re.UNICODE):
                raise ValueError("Use a localized basename without a path, suffix or extension")
            if item.get("approved") is not True or not isinstance(item.get("approval_ref"), str):
                raise ValueError("Explicit prose approval and its reference are required: " + view + "/" + locale)
            if not item["approval_ref"].strip():
                raise ValueError("approval_ref cannot be blank")
    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        raise ValueError("assets must be a nonempty list")
    for item in assets:
        if not isinstance(item, dict):
            raise ValueError("Each asset must be an object")
        if any(not isinstance(item.get(key), str) for key in ("view", "locale", "category")):
            raise ValueError("Asset view, locale and category must be strings")
        if item.get("view") not in views or item.get("locale") not in data["locales"]:
            raise ValueError("Asset has an unknown view or locale")
        if item.get("category") not in data["categories"]:
            raise ValueError("Asset category is not requested by this manifest")
        if not isinstance(item.get("file"), str) or not item["file"].strip():
            raise ValueError("Asset needs a relative file path")
        if not isinstance(item.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"]):
            raise ValueError("Asset needs its lowercase SHA-256")
        if item.get("rendered_from_source") is not True or not isinstance(item.get("render_evidence"), str):
            raise ValueError("Record source-render attestation and evidence; bitmap enlargement is not approved")
        if not item["render_evidence"].strip():
            raise ValueError("render_evidence cannot be blank")
    return data


def asset_path(base, value):
    relative = Path(value)
    if relative.is_absolute() or relative.drive or ".." in relative.parts or "\\" in value or ":" in value:
        raise ValueError("Use portable forward-slash paths contained below the manifest directory")
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError("Asset resolves outside the manifest directory")
    return path
