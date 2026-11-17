# Review and delivery

Review the final pixels as well as the machine report. Hash matching binds a manifest to bytes; it cannot establish truthful content, approval, translation quality, readability or device compatibility.

## Pixel and source review

- Inspect full-resolution images for text clipping, blur, distorted aspect ratios, missing fields, incorrect orientation and partially loaded fonts. Check realistic display-size previews for legibility.
- Compare the visible fixture against approved copy and intended app state. Confirm dates, time zones, timers, units, names and language fallbacks across every requested category.
- Keep original captures, final exports and thumbnails distinguishable. Supply the category-suffixed full-resolution files as candidates; thumbnails are review aids.
- Review framing and extra annotations against the current requirements of the target surface. Keep controls and core UI visible, and disclose illustrative compositions.

## Native controls and XR

Capture actual native authentication controls when presenting them as system UI. A hand-drawn prompt or an emulator helper does not establish that the production app displayed that prompt. Record the package/build, capture environment and any helper's role accurately.

If an authorized annotation is composited over a native screenshot, verify it does not cover controls. Compare decoded pixels outside the annotation bounds to prove that unrelated native content was preserved. Removing an entirely opaque alpha channel can preserve RGB pixels; verify that property before describing a conversion as lossless.

Keep synthetic credentials and seeded data confined to disposable capture state. Record cleanup of this task's helper, emulator and temporary credentials. Do not change a personal device, production authentication settings or a shared emulator merely to recreate a marketing screenshot.

For XR, separate app execution, native scene capture, headset interaction and physical-headset testing. A successful emulator capture supports only the environment and states actually exercised. A saved `_xr` filename or a browser viewport cannot establish XR support.

## Delivery evidence

Deliver the requested full-resolution files, a final manifest, capture receipts and a review gallery or previews when useful. Run the aggregate saved-preset check with `--complete` for the intended language/category sets. Record any current Console mismatch independently of that result.

Report the following statuses with their actual coverage:

| Status | Useful evidence |
| --- | --- |
| Passed | Named image checks, capture/layout assertions, unchanged protected hashes and completed human review |
| Failed | Every unresolved file, matrix, count, content or runtime failure and its consequence |
| Partial | Passing batches with missing listing views, limited localization review or incomplete target-device coverage |
| Not run | Physical devices, native-language review, broader XR interactions, Console acceptance or upload when absent |

A file pass, a complete saved-preset pass and current Play acceptance are distinct conclusions. Keep uploads and publication within the owner's actual authorization; this skill has no upload capability and grants no permission to publish.
