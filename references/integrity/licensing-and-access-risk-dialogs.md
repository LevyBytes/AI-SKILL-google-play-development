## Integrity dialog codes

### [GET_LICENSED](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_LICENSED>) (Type Code 1)

#### Verdict issue

This dialog is appropriate for two issues:

- **Unauthorized access**: `appLicensingVerdict: "UNLICENSED"`. This means the user account does not have an entitlement for your app, which can happen if the user sideloaded it or acquired it from a different app store than Google Play.
- **Tampered app**: `appRecognitionVerdict: "UNRECOGNIZED_VERSION"`. This means that your app's binary has been modified or is not a version recognized by Google Play.

> **Note:** The [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation?hl=en#get-integrity-dialog>) dialog addresses the same issues as `GET_LICENSED` in addition to addressing device integrity issues and remediable error codes.

#### Remediation

You can show the `GET_LICENSED` dialog to prompt the user to acquire the genuine app from Google Play. This single dialog addresses both scenarios:

- For an *unlicensed* user, it grants them a Play license. This enables the user to receive app updates from Google Play.
- For a user with a *tampered* app version, it guides them to installing the unmodified app from Google Play.

When the user completes the dialog, subsequent integrity checks return `appLicensingVerdict: "LICENSED"` and `appRecognitionVerdict: "PLAY_RECOGNIZED"`.

#### Example UX

![Image](<https://developer.android.com/static/images/google/play/integrity/get_licensing_ux.png>)

**Figure 1.** GET_LICENSED Play dialog.

### [CLOSE_UNKNOWN_ACCESS_RISK](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#CLOSE_UNKNOWN_ACCESS_RISK>) (Type Code 2)

#### Verdict issue

When `environmentDetails.appAccessRiskVerdict.appsDetected` contains `"UNKNOWN_CAPTURING"` or `"UNKNOWN_CONTROLLING"`, it means there are other apps (not installed by Google Play or preloaded on the system partition by the device manufacturer) running on the device that could be capturing the screen or controlling the device.

#### Remediation

You can show the `CLOSE_UNKNOWN_ACCESS_RISK` dialog to prompt the user to close all unknown apps which could be capturing the screen or controlling the device. If the user taps the `Close all` button, all such apps are closed.

#### Example UX

![Image](<https://developer.android.com/static/images/google/play/integrity/close_unknown_access_risk_ux.png>)

**Figure 2.** Dialog for close unknown access risk.

### [CLOSE_ALL_ACCESS_RISK](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#CLOSE_ALL_ACCESS_RISK>) (Type Code 3)

#### Verdict issue

When `environmentDetails.appAccessRiskVerdict.appsDetected` contains any of `"KNOWN_CAPTURING"`, `"KNOWN_CONTROLLING"`,`"UNKNOWN_CAPTURING"` or `"UNKNOWN_CONTROLLING"`, it means there are apps running on the device that could be capturing the screen or controlling the device.

#### Remediation

You can show the `CLOSE_ALL_ACCESS_RISK` dialog to prompt the user to close all the apps which could be capturing the screen or controlling the device. If the user taps the `Close all` button, all such apps are closed on the device.

#### Example UX

![Image](<https://developer.android.com/static/images/google/play/integrity/close_unknown_access_risk_ux.png>)

**Figure 3.** Dialog for close all access risk.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
