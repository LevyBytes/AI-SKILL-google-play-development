# Screenshot requirements

Choose the requested languages, supported device categories, views and orientation before capture. Compare the target app's current Play Console fields with [Google's preview-asset guidance](https://support.google.com/googleplay/android-developer/answer/9866151). Record which requirements govern the requested delivery; do not silently replace a supplied Console specification with a conflicting help-page value.

## Bundled Console preset

The validator implements `play-console-v1`. This is an explicit requirements preset, not a live policy service. Counts below apply independently to each requested language/category.

| Category | Filename suffix | Count | Each side, px | Maximum bytes | Maximum portrait, px |
| --- | --- | --- | --- | --- | --- |
| Phone | `_phone` | 2-8 | 320-3840 | 8,000,000 | 2160 x 3840 |
| Tablet 7-inch | `_tablet7` | Up to 8 | 320-3840 | 8,000,000 | 2160 x 3840 |
| Tablet 10-inch | `_tablet10` | Up to 8 | 1080-7680 | 8,000,000 | 4320 x 7680 |
| Desktop | `_desktop` | 4-8 | 1080-7680 | 8,000,000 | 4320 x 7680 |
| Android XR | `_xr` | 4-8 | 720-7680 | 15,000,000 | 4320 x 7680 |

Every preset category requires exact 16:9 or 9:16. Landscape swaps the portrait dimensions. Byte limits use decimal MB. Maximum dimensions are a saved quality requirement; smaller compliant images fail unless the caller explicitly requests `--allow-submax`.

Opaque RGB PNG is the preset default. JPEG auditing requires an explicit manifest setting, `png_only: false`. Still images, matching extensions, localized stems, recorded hashes and source-render evidence are required. Keep tablet sizes distinct even when their layouts resemble one another.

Optional categories may be omitted from `categories`. When included, every declared view must have an asset in every requested language/category. The tablet preset has no positive count minimum; that does not establish current large-screen listing readiness.

## Current documentation boundary

The linked public guidance specifies 4-8 XR images at 8:5, up to 8 MB, with 1920 x 1200 minimum and 3840 x 2400 recommended. Those values conflict with this XR preset. Public large-screen guidance also calls for at least four images, while the tablet count gate permits fewer.

General phone publication rules and recommendation eligibility are separate in that guidance; the saved exact aspect ratios and maximum-resolution gate should not be described as universal Google requirements. The script's `desktop` category is its saved Console label, not proof of Windows support.

If the current Console differs, retain the captured requirements and report the mismatch. Do not relabel a saved-preset result as a current-policy result or change `asset_rules.py` merely to make a delivery pass. An updated validator profile needs its own reviewed requirements and boundary checks.

Wear OS, Android TV, Automotive, icons, feature graphics and videos have separate requirements and are outside this validator. Use their current official guidance when requested instead of coercing them into these five categories.
