# Google Play screenshot assets

Portable Python checklist and read-only conformance tool. Copy this entire folder into a future skill's scripts
folder. It has no project paths, browser dependency, account credentials or upload capability.
Python 3.10+ is required. `guide` and `template` use only the standard library; `check` and tests require Pillow.
Use the existing environment when available; `requirements.txt` identifies the dependency for another machine.

## Owner standard, captured November 5, 2026

| Category | Filename suffix | Count per language | Each side | Bytes, maximum | Maximum portrait |
| --- | --- | --- | --- | --- | --- |
| Phone | `_phone` | 2-8 | 320-3840 px | 8,000,000 | 2160 x 3840 |
| Tablet 7-inch | `_tablet7` | up to 8 | 320-3840 px | 8,000,000 | 2160 x 3840 |
| Tablet 10-inch | `_tablet10` | up to 8 | 1080-7680 px | 8,000,000 | 4320 x 7680 |
| Desktop | `_desktop` | 4-8 | 1080-7680 px | 8,000,000 | 4320 x 7680 |
| Android XR | `_xr` | 4-8 | 720-7680 px | 15,000,000 | 4320 x 7680 |

Landscape swaps width and height. Exact 16:9 or 9:16 is required. MB uses conservative decimal bytes.
These are the owner's supplied Console requirements, including XR. They are versioned, not fetched or silently updated.
Recheck the relevant Console category before a future release; this tool cannot guarantee Google acceptance.
[Google's preview asset guidance](https://support.google.com/googleplay/android-developer/answer/9866151).

The owner prefers PNG only. The manifest must explicitly set `png_only: false` to audit JPEGs.
Use opaque RGB. Render fonts, SVGs and UI directly at the target resolution; do not upscale a smaller bitmap.
Keep approved prose and its language-specific basename. For example:
`day-of-visits_tablet7.png`, `dia-de-visitas_tablet7.png`.
Separate 7-inch and 10-inch files even when their composition is similar.

## Commands

Run from this folder, or provide the full path to `play_assets.py` from any directory:

```text
python -B play_assets.py guide
python -B play_assets.py template
python -B play_assets.py check /path/to/manifest.json --report /path/to/checks.json
python -B play_assets.py check /path/to/manifest.json --complete
python -B test_assets.py --tmp /path/to/scratch
```

`template` prints an unapproved example. Save it where the images will live, then fill in actual approvals,
localized stems, paths, SHA-256 hashes and rendering evidence. No approval is inferred from an existing image.
Use forward-slash relative asset paths beneath the manifest folder. No environment variables need configuration.
`-I` is also supported; the entrypoints explicitly locate their sibling modules.

`check` defaults to a batch audit and requires maximum resolution. `--complete` also enforces minimum counts.
Both reject over eight screenshots in any language/category. Counts are never added across languages or categories.
`--allow-submax` permits a legacy-resolution audit; the report explicitly records that the quality gate was relaxed.
Exit 0 means the requested check passed; exit 1 means it failed. A batch pass is not a complete-listing pass.
The report records missing listing counts even when batch checks pass. Optional categories can be omitted entirely.

## Manifest and review contract

`locales` and `categories` define the requested matrix. Each entry in `views` must have an approved localized
basename and an approval reference for every language. Each view requires an image in every requested category
and language. Use separate manifests when particular views intentionally target different category subsets.

The asset list names each file, view, locale and category, its hash, and a `rendered_from_source` attestation with
`render_evidence`. Localized filename language and prose approval are human attestations, not automated judgments.
Hash validation detects changes after the manifest was prepared; it does not independently prove owner approval.
The tool checks actual decoding, exact aspect ratio, dimensions, maximum resolution, size, format/extension,
RGB/transparency, still-image status, names, hashes, duplicate images and matrix completeness.

Review the pixels for clipping, legibility and complete localization. Verify supported device layouts independently.
Never claim a browser render proves a physical device or XR build was tested. Do not count repeated copies as new views.
Use different approved example content for each distinct screenshot; keep translations of that view consistent.
For this project, Karate Kid and Sandlot references remain reserved for the approved feature graphic.
Do not edit the frozen listing draft to store workflow notes. Git commands and publishing belong to the owner.

## Fixture tests

Tests cover all five categories in portrait/landscape, byte boundaries, wrong suffixes/hashes, missing translations,
batch versus complete counts, overflow counts, duplicates, bad manifests, corrupt images, mismatched extensions,
alpha/palette transparency, unsupported formats, animation metadata and path escapes.
Tests create only their own temporary files below the required `--tmp` directory, then clean those files up.
The tool does not generate or resize marketing images; use the source renderer, then run these independent checks.
