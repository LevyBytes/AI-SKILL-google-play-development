# Validation failures

Start with the report's top-level `errors`, then inspect every entry in `files`. Schema errors prevent file inspection and can produce a shorter failure report. Preserve failed evidence before rerendering or replacing a manifest.

| Finding | Diagnose and repair |
| --- | --- |
| `ASPECT` | Confirm the requested orientation and exact preset ratio. Rerender; do not stretch a bitmap. |
| `DIMENSIONS` | Compare decoded pixels with the category bounds and capture framebuffer, not the intended viewport alone. |
| `QUALITY` | Capture from source at maximum preset dimensions. Use `--allow-submax` only for an explicitly requested legacy audit. |
| `SIZE` | Inspect the actual file bytes. Simplify excessive visual noise or use a suitable lossless export; preserve source quality and PNG preference. |
| `FORMAT`, `COLOR`, `ANIMATION` | Export a still opaque RGB image. Inspect palette transparency, alpha channels and animation metadata. |
| `EXTENSION` | Re-export in the intended format; renaming a JPEG to `.png` does not convert it. |
| `NAME` | Match the approved localized stem and the exact category suffix. Keep `_tablet7` and `_tablet10` separate. |
| `HASH` | Compare the final bytes to the reviewed capture. Correct unexpected changes before recording a new digest. |
| `DECODE` | Check missing, truncated or corrupt files, rejected paths and decoder limits. Do not disable image warnings to force a pass. |
| `MISSING` | Complete each declared view/language/category combination or intentionally separate category subsets into manifests. |
| `DUPLICATE` | Remove accidental repeated rows or identical images. Rerender distinct approved views rather than editing metadata to evade detection. |
| `COUNT` | Add distinct views to the affected language/category. Eight is the saved maximum; unrelated categories and languages cannot supply a minimum. |

An unavailable Pillow import requires the declared dependency in an authorized environment. `guide` and `template` do not require Pillow and can help confirm the tool's versioned contract without changing that environment.

A policy mismatch is not an image defect: the manifest must name the bundled preset exactly. If the requested current Console requirements differ, retain that discrepancy and arrange a reviewed profile update; changing a manifest label cannot change the implemented rules.

If a source-rendered image fails human review despite passing the tool, fix the source composition, translation or fixture and recapture. Record new hashes and rerun both the affected batch and aggregate complete-set checks. Detector silence cannot resolve misleading claims, unapproved copy or unsupported device evidence.

Use [review and delivery](review-and-delivery.md) to report remaining limits without presenting a partial technical pass as finished listing approval.
