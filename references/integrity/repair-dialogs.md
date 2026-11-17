### [GET_INTEGRITY](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_INTEGRITY>) (Type Code 4)

#### Verdict issue

This dialog is appropriate for any of the following issues:

- **Weak device integrity**: When the `deviceRecognitionVerdict` does not contain `MEETS_DEVICE_INTEGRITY`, the device might not be a genuine and certified Android-powered device. This can happen, for example, if the device's bootloader is unlocked or its loaded Android OS is not a certified manufacturer image.
- **Unauthorized access**: `appLicensingVerdict: "UNLICENSED"`. This means the user account does not have an entitlement for your app, which can happen if the user sideloaded it or acquired it from a different app store than Google Play.
- **Tampered app**: `appRecognitionVerdict: "UNRECOGNIZED_VERSION"`. This means that your app's binary has been modified or is not a version recognized by Google Play.
- **Client side exceptions**: When a remediable exception occurs during an Integrity API request. Remediable exceptions are Integrity API exceptions with error codes like `PLAY_SERVICES_VERSION_OUTDATED`, `NETWORK_ERROR`, `PLAY_SERVICES_NOT_FOUND`, etc. You can use the [`exception.isRemediable()`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#isRemediable()>) method to check if an exception is fixable by the dialog.

#### Remediation

The `GET_INTEGRITY` dialog is designed to streamline the user's experience by handling multiple remediation steps within a single, continuous flow. This prevents the user from having to interact with multiple separate dialogs to fix different issues.

When you request the dialog, it automatically detects which of the targeted verdict issues are present and provides the appropriate remediation steps. This means a single dialog request can address multiple problems at once, including:

- **Device integrity**: If a device integrity issue is detected, the dialog will guide the user to improve the device's security status to meet the requirements for a `MEETS_DEVICE_INTEGRITY` verdict.
- **App integrity**: If issues like unauthorized access or app tampering are detected, the dialog will direct users to acquire the app from the Play Store to fix them.

> **Note:** `GET_INTEGRITY` dialog automatically detects and tries to resolve multiple verdict issues when requested. To remediate only issues with account licensing or app integrity, we recommend using the [`GET_LICENSED`](<https://developer.android.com/google/play/integrity/remediation#get-licensed-dialog>) dialog.

- **Client-side exceptions**: The dialog checks for and attempts to resolve any underlying issues that caused an Integrity API exception. For example, it might prompt the user to update an outdated version of Google Play services.

#### Example UX

![Image](<https://developer.android.com/static/images/google/play/integrity/get_integrity_network_error_ux.gif>)

**Figure 4.** GET_INTEGRITY dialog network error remediation flow

### [GET_STRONG_INTEGRITY](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_STRONG_INTEGRITY>) (Type Code 5)

#### Verdict issue

This dialog is designed to fix all of the same issues that [GET_INTEGRITY](<https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog>) addresses, with the added capability of fixing problems that prevent a device from receiving a `MEETS_STRONG_INTEGRITY` verdict and fixing Play Protect verdict issues.

> **Note:** [MEETS_STRONG_INTEGRITY](<https://developer.android.com/google/play/integrity/verdicts#optional-device-labels>) and [playProtectVerdict](<https://developer.android.com/google/play/integrity/verdicts#environment-details-field>) are optional verdicts and, you should only check for them if you've [opted in to receive additional labels](<https://developer.android.com/google/play/integrity/setup#configure-api>).

#### Remediation

`GET_STRONG_INTEGRITY` is designed to streamline the user's experience by handling multiple remediation steps within a single, continuous flow. The dialog automatically checks for an address applicable integrity problems, including:

- **Device integrity**: If a device integrity issue is detected, the dialog will guide the user to improve the device's security status to meet the requirements for a `MEETS_STRONG_INTEGRITY` verdict.
- **Play protect status**: If the `playProtectVerdict` indicates an issue, the dialog will guide the user to fix it:

  - If Play Protect is disabled (`playProtectVerdict == POSSIBLE_RISK`), the dialog will prompt the user to enable it and perform a scan of all apps on the device.
  - If harmful apps are detected (`playProtectVerdict == MEDIUM_RISK` or `HIGH_RISK`), the dialog will direct the user to uninstall them using Google Play Protect.
- **App integrity**: If issues like unauthorized access or app tampering are detected, the dialog will prompt the user to acquire the app from the Play Store to fix the problem.
- **Client-side exceptions**: The dialog also attempts to resolve any underlying issues that caused an Integrity API exception. For example, it may prompt the user to enable Google Play services if it's found to be disabled. Remediable exceptions are Integrity API exceptions with error codes like `PLAY_SERVICES_VERSION_OUTDATED`, `NETWORK_ERROR`, or `PLAY_SERVICES_NOT_FOUND`. You can use the [`exception.isRemediable()`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#isRemediable()>) method to check if an error is fixable by the dialog.

#### Example UX

![Image](<https://developer.android.com/static/images/google/play/integrity/get_strong_integrity_update_play_services_ux.gif>)

**Figure 5.** GET_STRONG_INTEGRITY dialog updating Play services.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
