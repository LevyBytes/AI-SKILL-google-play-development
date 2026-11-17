# Localized content

Choose each screenshot view for the feature it demonstrates, then establish the actual approved copy and example data for every requested language. Existing images, a translated stem or a `true` manifest flag do not independently establish approval.

Keep a stable view ID across languages and categories. For example, view `schedule` may use `schedule_phone.png` in English and `agenda_phone.png` in Spanish. The localized stem comes from the approved language record; `_phone`, `_tablet7`, `_tablet10`, `_desktop` and `_xr` identify the category. Store translations in separate directories when helpful.

Use distinct example content for distinct views. Translations of one view retain its scenario, times, timer state and feature meaning. Do not count copies of the same image as additional views; the validator rejects identical bytes within a language/category but cannot recognize visually repeated content saved with different bytes.

## Localization review

- Review UI labels, navigation, tooltips, native date controls, annotations and example records that appear in the frame. A cropped phone image may hide fallback labels that become visible on desktop.
- Confirm the language actually displayed, including native system controls. An app locale and the device's available system locale may differ; record that difference.
- Check accented characters, punctuation, line breaks, text expansion, clipping and text direction. Review the full-resolution image and a realistic display-size preview.
- Preserve approved phrasing when adapting layout. If a render needs a missing translation or changed claim, recover its approval boundary before using it.
- An approved marketing-only label adjustment belongs in the isolated render. It does not authorize changes to app catalogs, stored values, production data or runtime behavior.

Represent current capabilities accurately. Google’s preview-asset guidance restricts ranking, price/promotional claims and calls to action, and recommends restrained, legible text. Large-screen guidance discourages extra text outside the app experience. Check the current rules for the actual target surface before adding a tagline.

Provide localized screenshot alt text where the Console supports it; public guidance specifies at most 140 characters. Describe the important app state concisely. Alt text and copy quality are human checks; the screenshot manifest does not validate them.

Avoid unapproved third-party characters, logos, store badges and personal data. A story reference or location approved in another app's campaign does not become a reusable approval for this app.

Record the approval reference and source-render evidence in [the manifest](manifest-contract.md). The reference can identify a decision or reviewed copy document; the tool only checks that it is a nonblank string. A native-language reviewer and truthful content review remain separate from filename and pixel checks.
