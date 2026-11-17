# Validation commands

Use an explicitly selected Python 3.10+ interpreter and the complete `scripts/store-listing-screenshots/` directory. `guide` and `template` use the standard library; image checks and fixture tests require the Pillow dependency declared in that directory's `requirements.txt`. Do not install into or change a shared environment without the caller's authorization.

Replace `<PYTHON>`, `<SKILL_ROOT>` and `<WORK>` with absolute paths. Each PowerShell line below is independently copyable after those substitutions; no working-directory or environment activation is required.

```powershell
& '<PYTHON>' -I -B '<SKILL_ROOT>/scripts/store-listing-screenshots/play_assets.py' guide
& '<PYTHON>' -I -B '<SKILL_ROOT>/scripts/store-listing-screenshots/play_assets.py' template
& '<PYTHON>' -I -B '<SKILL_ROOT>/scripts/store-listing-screenshots/play_assets.py' check '<WORK>/manifest.json' --report '<WORK>/batch-checks.json'
& '<PYTHON>' -I -B '<SKILL_ROOT>/scripts/store-listing-screenshots/play_assets.py' check '<WORK>/manifest.json' --complete --report '<WORK>/complete-checks.json'
& '<PYTHON>' -I -B '<SKILL_ROOT>/scripts/store-listing-screenshots/test_assets.py' --tmp '<WORK>/fixture-scratch'
```

`template` prints JSON; save that output as UTF-8 JSON in the intended asset directory, then fill in actual decisions and final-file metadata. The CLI reads UTF-8 without a BOM. In Windows PowerShell 5.1, default redirection and `Set-Content -Encoding UTF8` can produce an unsuitable encoding or BOM; use an explicit BOM-less UTF-8 writer.

## Interpret results

| Mode | Meaning |
| --- | --- |
| Default `check` | Batch conformance, complete declared matrix, no overflow counts; minimum listing counts may still be missing |
| `check --complete` | Same checks plus the saved preset's minimum counts for each requested language/category |
| `check --allow-submax` | Explicit legacy-resolution audit; the report sets `maximum_resolution_required` to `false` |

Neither complete mode nor the quality override updates the saved policy. In particular, a complete tablet or XR preset result does not settle the current-policy differences described in [screenshot requirements](screenshot-requirements.md).

Exit `0` means the selected operation passed. Exit `1` means a reported validation/dependency/file failure. Argument-parser errors use exit `2`. JSON report fields include `status`, `scope`, `policy`, `maximum_resolution_required`, `files`, `counts`, `errors`, `human_review` and `publication` when manifest validation reaches file checking. Early input failures can return only failure details and help.

Inspect both top-level `errors` and each file's `errors`. In batch mode, `counts[].status` may be `PARTIAL` even with top-level `PASSED`. Do not pool counts across languages or categories. Duplicate paths, repeated view/language/category keys and identical image bytes within one language/category fail.

## Writes and portability

Checking leaves input files unchanged. `--report` explicitly writes or replaces the selected JSON report; its parent directory must already exist. The CLI refuses a report path that resolves to the manifest or an inspected asset. Use a dedicated report file, not another source or review document.

The fixture runner creates and cleans its own temporary files beneath the required `--tmp` path. `-B` avoids bytecode caches, and both entrypoints locate sibling modules under `-I`. Copy the entire tool directory when testing portability; copying only `play_assets.py` omits required modules.

After a repair, rerun the affected file checks and the aggregate complete-set check. See [validation failures](validation-failures.md) for diagnoses and [review and delivery](review-and-delivery.md) for the separate human checks.
