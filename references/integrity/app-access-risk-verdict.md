### Environment details field

You can also opt in to additional signals about the environment. App access risk tells your app if there are other apps running that could be used to capture the screen, display overlays, or control the device. The Play Protect verdict tells you if Google Play Protect is enabled on the device and whether it has found known malware.

If you have opted in to the App Access Risk verdict or the Play Protect verdict in your Google Play Console, then your API response will include the `environmentDetails` field. The `environmentDetails` field can contain two values, `appAccessRiskVerdict` and `playProtectVerdict`.

#### App access risk verdict

Once enabled, the `environmentDetails` field in the [Play Integrity API payload](<https://developer.android.com/google/play/integrity/verdict#returned-payload-format>) will contain the new app access risk verdict.

```json
{
  "requestDetails": { ... },
  "appIntegrity": { ... },
  "deviceIntegrity": { ... },
  "accountDetails": { ... },
  "environmentDetails": {
      "appAccessRiskVerdict": {
          // This field contains one or more responses, for example the following.
          "appsDetected": ["KNOWN_INSTALLED", "UNKNOWN_INSTALLED", "UNKNOWN_CAPTURING"]
      }
 }
}
```

> **Note:** In standard requests, the app access risk verdict is only available when using Play Integrity API library version [1.4.0](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-4-0>) or higher for Kotlin or Java. App access risk increases the latency of standard requests, but latency-sensitive standard requests that don't require the app access risk verdict can use the `verdictOptOut` parameter to opt out of this verdict on a per-request basis. App access risk also requires the device to be running Android Marshmallow (API level 23) or higher.

If app access risk was evaluated, `appAccessRiskVerdict` contains the field `appsDetected` with one or more responses. These responses fall into one of the following two groups depending on the install source of the detected apps:

- **Play or system apps**: Apps that are installed by Google Play or preloaded by the device manufacturer on the device's system partition (identified with [`FLAG_SYSTEM`](<https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_SYSTEM>)). Responses for such apps are prefixed by `KNOWN_`.
- **Other apps**: Apps that are not installed by Google Play. This excludes apps preloaded on the system partition by the device manufacturer. Responses for such apps are prefixed by `UNKNOWN_`.

> **Note:** Detected apps that are **only** installed in another profile on the device, such as a [work profile](<https://support.google.com/work/android/answer/6191949>), will have the `UNKNOWN_` response prefix regardless of their install source. For example, if the app requesting the app access risk verdict is in a work profile and an app installed by Google Play in the user profile is running that could capture the screen, it will return `UNKNOWN_CAPTURING` instead of `KNOWN_CAPTURING`.

The following responses can be returned:

**`KNOWN_INSTALLED`, `UNKNOWN_INSTALLED`**

There are apps installed that match the corresponding install source.

**`KNOWN_CAPTURING`, `UNKNOWN_CAPTURING`**

There are apps running that have permissions enabled that could be used to view the screen while your app is running. This excludes any verified accessibility services known to Google Play running on the device.

**`KNOWN_CONTROLLING`, `UNKNOWN_CONTROLLING`**

There are apps running that have permissions enabled that could be used to control the device and directly control inputs into your app and could be used to capture inputs and outputs of your app. This excludes any verified accessibility services known to Google Play running on the device.

**`KNOWN_OVERLAYS`, `UNKNOWN_OVERLAYS`**

There are apps running that have permissions enabled that could be used to display overlays on your app. This excludes any verified accessibility services known to Google Play running on the device.

**Empty (a blank value)**

App access risk is not evaluated if a necessary requirement was missed. In this case the `appAccessRiskVerdict` field is empty. This could happen for several reasons, including the following:

- The device is not trustworthy enough.
- The device form factor is not a phone, tablet, or foldable.
- The device is not running Android 6 (API level 23) or higher.
- The version of your app installed on the device is unknown to Google Play.
- The version of the Google Play Store on the device is outdated.
- The user account does not have a Play license.
- A standard request was used with the `verdictOptOut` parameter.
- A standard request was used with a Play Integrity API library version that doesn't yet support app access risk for standard requests.

App access risk automatically excludes verified accessibility services that have been through an enhanced Google Play accessibility review (installed by any app store on the device). "Excluded" means that verified accessibility services running on the device won't return a capturing, controlling, or overlays response in the app access risk verdict. To request an enhanced Google Play accessibility review for your accessibility app, publish it on Google Play ensuring that your app has the `isAccessibilityTool` flag set to true in your app's manifest, or [request a review](<https://issuetracker.google.com/issues/new?component=1152695&template=1949138>).

##### Example app access risk verdicts

The following table gives some examples of app access risk verdicts and what they mean (this table does not list every possible result):

| Example app access risk verdict response | Interpretation |
| --- | --- |
| `appsDetected:`<br> `["KNOWN_INSTALLED"]` | There are only apps installed that are recognized by Google Play or preloaded on the system partition by the device manufacturer.<br>There are no apps running that would result in the capturing, controlling, or overlays verdicts. |
| `appsDetected:`<br> `["KNOWN_INSTALLED",`<br> `"UNKNOWN_INSTALLED",`<br> `"UNKNOWN_CAPTURING"]` | There are apps installed by Google Play or preloaded on the system partition by the device manufacturer.<br>There are other apps running and have permissions enabled that could be used to view the screen or capture other inputs and outputs. |
| `appsDetected:`<br> `["KNOWN_INSTALLED",`<br> `"KNOWN_CAPTURING",`<br> `"UNKNOWN_INSTALLED",`<br> `"UNKNOWN_CONTROLLING"]` | There are Play or system apps running that have permissions enabled that could be used to view the screen or capture other inputs and outputs.<br> There are also other apps running that have permissions enabled that could be used to control the device and directly control inputs into your app. |
| `appAccessRiskVerdict: {}` | App access risk is not evaluated because a necessary requirement was missed. For example, the device was not trustworthy enough. |

Depending on your risk level, you can decide what combination of verdicts are acceptable to proceed and what verdicts you want to take action on. The following code snippet illustrates an example of verifying that there are no apps running that could capture the screen or control your app:

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
