# Google Play screenshot tools

Portable Python checklist and image-conformance CLI. Keep this complete directory together: `play_assets.py`, its `asset_*.py` modules, `requirements.txt`, the fixture runner and `tests/`. It has no browser dependency, credentials or upload capability. Python 3.10+ is required; checks and tests need Pillow 10.4+.

The preset is `play-console-v1`. It is not fetched or silently updated. Run `guide` to inspect its limits and reminders. Public XR and large-screen guidance differs; see [screenshot requirements](../../references/screenshot-requirements.md) before interpreting a pass as release readiness.

## Run from any directory

Replace the absolute-path placeholders with the selected interpreter, this directory and a caller-owned work folder:

```powershell
& '<PYTHON>' -I -B '<TOOLS>/play_assets.py' guide
& '<PYTHON>' -I -B '<TOOLS>/play_assets.py' template
& '<PYTHON>' -I -B '<TOOLS>/play_assets.py' check '<WORK>/manifest.json' --report '<WORK>/batch-checks.json'
& '<PYTHON>' -I -B '<TOOLS>/play_assets.py' check '<WORK>/manifest.json' --complete --report '<WORK>/complete-checks.json'
& '<PYTHON>' -I -B '<TOOLS>/test_assets.py' --tmp '<WORK>/fixture-scratch'
```

`template` prints an unapproved starter. Save UTF-8 JSON without a BOM, then record actual localized stems, approvals, final-file hashes and source-render evidence. Paths stay below the manifest directory. See [the complete manifest contract](../../references/manifest-contract.md).

`check` audits the declared batch and matrix. `--complete` additionally checks saved minimum counts per language/category. Both enforce the eight-image maximum. `--allow-submax` explicitly relaxes the saved maximum-resolution quality gate. A passing batch can still have `PARTIAL` count results.

Exit `0` indicates the requested operation passed; `1` indicates a reported failure; parser errors use `2`. Inspect both top-level and per-file errors. `--report` writes or replaces only its explicit output path, and refuses the manifest or an inspected image. Other input files are read only. See [validation commands](../../references/validation-commands.md) and [failure diagnoses](../../references/validation-failures.md).

## Capture and review

The tools decode and inspect images; they do not generate or resize them. Render from source at the requested final dimensions, keep tablet sizes distinct, use approved localized stems and review the actual pixels. PNG-only is the saved default; JPEG auditing requires `png_only: false` in the manifest.

Approval references and source-render evidence are attestations. File checks cannot certify language, legibility, device support, non-upscaling or current Play acceptance. Use [source rendering](../../references/source-rendering.md), [localization](../../references/localized-content.md) and [delivery review](../../references/review-and-delivery.md) for those decisions.

The fixture runner creates and cleans its own files beneath `--tmp`. Its tests cover all categories, metadata boundaries, decoded images, corrupt files, naming, hashes, path escapes, transparency, approvals, matrix completeness, duplicates and batch/complete counts. [Evaluation instructions](../../evals/EVALS.md) distinguish those checks from model and native-device testing.

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://support.google.com/googleplay/android-developer/answer/9866151) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
