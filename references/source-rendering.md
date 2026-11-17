# Source rendering and capture

Choose a capture method that truthfully represents the app. A browser rendering of the app UI can support a marketing composition; it does not establish APK, physical-device or XR compatibility. Native permission, credential and biometric prompts require authentic system captures when represented as actual system UI.

## Render at the final pixel size

Keep CSS viewport size separate from output pixels. Set a responsive viewport appropriate to the category, then render text, vectors and UI directly at the output density. For a browser renderer, `output width = viewport width * deviceScaleFactor`, and the same relation must hold for height. Assert the actual decoded output size; renderer rounding can differ from the requested size.

| Example layout | CSS viewport | Scale | Output pixels |
| --- | --- | --- | --- |
| Phone portrait | 360 x 640 | 6 | 2160 x 3840 |
| Tablet 7-inch portrait | 720 x 1280 | 3 | 2160 x 3840 |
| Tablet 10-inch portrait | 900 x 1600 | 4.8 | 4320 x 7680 |
| Desktop landscape | 2560 x 1440 | 3 | 7680 x 4320 |

These are composition examples for the saved preset, not device specifications. Use the app's real responsive behavior. Confirm orientation explicitly for each view; do not let a portrait editor preset silently govern a requested landscape desktop or XR image.

Never enlarge an existing bitmap to reach the maximum. If raster source content is too small, recapture or replace it with a suitable original. Keep originals separate from final exports and review thumbnails. Enlarging a thumbnail or changing image metadata does not improve source quality.

## Make capture deterministic

1. Use a dedicated browser profile or disposable emulator state beneath the caller's work directory. Do not seed a personal profile or production records.
2. Load the approved fixture and language. Freeze both the capture instant and time zone when dates, clocks or timers affect the view; use the same scenario across translations.
3. Wait for application readiness, loaded fonts, localized labels and settled layout. Check asynchronous data and animation rather than relying only on an arbitrary delay.
4. Assert all required cards, fields and controls are visible. Check text clipping, horizontal overflow, footer position and requested orientation. Retain runtime errors as evidence.
5. Capture directly at final resolution. Record viewport, output pixels, renderer/version, fixture identity, source hashes, locale and exceptions with the image hash.
6. Compare protected app, language-pack, approved-copy and prior-image hashes. Keep any approved marketing-only presentation changes confined to the isolated rendering.

For native captures, verify the framebuffer's actual dimensions. A logical display-size override may leave the emulator's capture framebuffer unchanged. Configure supported capture dimensions before producing final images, and inspect the output instead of inferring size from the requested setting.

XR framing also needs a settled recenter state and visible scene/window bounds. Record the actual app, emulator and capture method. Avoid carrying device-specific camera coordinates or private ADB endpoints into a generic workflow.

The bundled Python tools perform independent checks after capture; they do not provide a browser renderer, emulator setup or bitmap resizer. Use the caller's existing authorized capture tooling, then follow [the manifest contract](manifest-contract.md).
