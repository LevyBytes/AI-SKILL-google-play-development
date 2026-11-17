# Manifest contract

Keep a JSON manifest beside the exported files or above their language/category directories. Generate the bundled starter with `play_assets.py template`; its approvals, hashes and source-render flags are intentionally incomplete. Do not run the starter as if it were an approved delivery.

## Fields and relationships

| Field | Contract |
| --- | --- |
| `policy` | Exact preset identifier, `play-console-v1` |
| `png_only` | Boolean; defaults to `true`; explicitly `false` permits RGB JPEG |
| `locales` | Nonempty list of unique language strings |
| `categories` | Unique requested categories: `phone`, `tablet7`, `tablet10`, `desktop`, `xr` |
| `views` | Nonempty map of stable view IDs to exactly the requested locale records |
| Localized record | `stem`, `approved: true`, nonblank `approval_ref` |
| Asset identity | `file`, `view`, `locale`, `category`; one asset per combination |
| Asset integrity | Lowercase 64-character `sha256` of the final file bytes |
| Capture attestation | `rendered_from_source: true`, nonblank `render_evidence` |

Each asset path is relative to the manifest directory and uses forward slashes. Absolute paths, drive-qualified paths, backslashes, traversal and resolved paths outside that directory are rejected. The basename must equal its localized `stem` plus the category suffix; the extension must match the decoded format.

## Unapproved example

This single-language, single-category example illustrates the structure. Its zero hash and false flags are placeholders; use actual final-file hashes and actual authorization before validation.

```json
{
  "policy": "play-console-v1",
  "png_only": true,
  "locales": ["en-US"],
  "categories": ["phone"],
  "views": {
    "schedule": {
      "en-US": {
        "stem": "schedule",
        "approved": false,
        "approval_ref": ""
      }
    }
  },
  "assets": [
    {
      "file": "en-US/schedule_phone.png",
      "view": "schedule",
      "locale": "en-US",
      "category": "phone",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
      "rendered_from_source": false,
      "render_evidence": ""
    }
  ]
}
```

## Matrix and evidence

Every declared view requires an image in every requested language/category. Use separate manifests when views intentionally target different category subsets. For final delivery, also validate an aggregate manifest for each intended category subset so counts are checked across its complete set of views; separate passing batches do not establish complete counts.

Compute SHA-256 after the final export or authorized pixel-preserving conversion. Re-exporting changes the file identity, even if its appearance seems unchanged. Update the manifest from reviewed final bytes rather than bypassing hash failures.

`approval_ref` and `render_evidence` are human attestations, not fetched or authenticated evidence. Retain the actual decision and capture receipt outside the skill, including source/fixture hashes, dimensions and the capture method. The validator cannot infer translation quality, source fidelity or non-upscaling from a file alone.

Use [validation commands](validation-commands.md) for batch and complete-set checks. Keep report paths separate from the manifest and every image.
