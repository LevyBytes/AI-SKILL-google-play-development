"""Portable CLI: python play_assets.py guide | template | check manifest.json [--complete]."""
import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from asset_rules import POLICY


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("guide", help="Print limits, maximum pixel sizes and owner instructions as JSON")
    sub.add_parser("template", help="Print an intentionally unapproved starter manifest as JSON")
    check = sub.add_parser("check", help="Read-only image and manifest checks (Pillow required)")
    check.add_argument("manifest", type=Path)
    check.add_argument("--complete", action="store_true", help="Also require listing minimum counts")
    check.add_argument("--allow-submax", action="store_true", help="Audit legacy images without the max-quality gate")
    check.add_argument("--report", type=Path, help="Optional explicit JSON output path; existing files are replaced")
    args = parser.parse_args()
    if args.command == "guide":
        report = POLICY
    elif args.command == "template":
        report = {"policy": POLICY["version"], "png_only": True, "locales": ["en-US", "es-419"],
                  "categories": ["phone", "tablet7", "tablet10", "desktop", "xr"],
                  "views": {"day-of-visits": {
                      locale: {"stem": stem, "approved": False, "approval_ref": ""}
                      for locale, stem in (("en-US", "day-of-visits"), ("es-419", "dia-de-visitas"))}},
                  "assets": [{"file": "en-US/day-of-visits_phone.png", "view": "day-of-visits",
                              "locale": "en-US", "category": "phone", "sha256": "",
                              "rendered_from_source": False, "render_evidence": ""}]}
    else:
        try:
            from asset_check import validate
            if args.report and args.report.resolve() == args.manifest.resolve():
                raise ValueError("Report must not overwrite the manifest")
            report = validate(args.manifest, args.complete, not args.allow_submax)
            if args.report:
                assets = {(args.manifest.parent / a["file"]).resolve() for a in report["files"]}
                if args.report.resolve() in assets:
                    raise ValueError("Report must not overwrite an asset")
                args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                       encoding="utf-8", newline="\n")
        except (ValueError, OSError, ImportError) as exc:
            report = {"status": "FAILED", "errors": [str(exc)],
                      "help": "Use guide/template. Check requires Python 3.10+ and Pillow."}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report.get("status") == "FAILED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
