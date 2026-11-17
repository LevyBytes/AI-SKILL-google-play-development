# Google Play skill evaluation

Use [activation cases](activation-cases.json) for intended selection and first-reference checks. Run them in fresh contexts with the skill's actual discovery metadata, and retain the model/version, chosen route, result and unauthorized side effects outside this skill. The cases describe expected behavior; they are not recorded model-evaluation results.

Run the existing fixture suite with an explicitly selected Python 3.10+ interpreter and Pillow 10.4+. Replace the absolute-path placeholders:

```powershell
& '<PYTHON>' -I -B '<SKILL_ROOT>/scripts/store-listing-screenshots/test_assets.py' --tmp '<WORK>/fixture-scratch'
```

The suite checks category dimensions and byte boundaries, actual image decoding, formats and transparency, localized names, hashes, path containment, approvals, matrix coverage, duplicates and batch versus complete counts. CLI regressions check date-free guide/template output, matching manifest identity and unknown-policy rejection. Metadata/count fixtures use mocks where noted in their source; file fixtures decode real generated images.

For a task evaluation, supply independent approved synthetic content and capture receipts in an isolated work directory. Have the agent construct the manifest and run the CLI from another working directory. Check actual pixels, names, hashes, output status, report contents and unchanged input bytes.

Exercise a one-view phone batch that passes while `--complete` fails, then a distinct two-view phone set that passes complete mode. Include a missing translation, a changed file hash and an unapproved record as negative cases. Verify that `--report` cannot replace the manifest or an asset.

Evaluate current-policy reasoning separately: a successful saved XR preset must not be described as validation of the current public XR specification. Review routing, truthful capture claims, source fidelity and owner approval manually. Deterministic checks do not measure model activation or native device support.

Development routing cases cover release signing, billing, integrity, asset and feature delivery, review and update flows, cross-device prompts, Engage verticals and Developer API selection. Trace each case from its expected first reference to the actual contract or complete procedure. Include the negative cases for unrelated Android UI, unrelated Google APIs and non-listing screenshots.

For fidelity review, compare retained code blocks separately from prose and inline API identifiers. Check exact owners, version restrictions, prerequisites, callbacks, return values, counts, localized UI text, negation and timing. A linked long example must lead to the complete upstream example. Release-history statements and deprecated integrations require an eligibility check before use.

For task evaluation, review an integration plan against primary SDK contracts before selecting a bounded build or strict mock. Record static review, compilation, native execution and Play/backend behavior separately. The references do not contain SDK dependencies, credentials or a live Android test app; reading them cannot establish device behavior or program acceptance.
