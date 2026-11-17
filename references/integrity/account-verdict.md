### Account details field

The `accountDetails` field contains a single value, `appLicensingVerdict`, that represents the app's Google Play licensing status for the user account that's signed in on the device. If the user account has the Play license for the app, that means they downloaded it or bought it from Google Play.

```json
"accountDetails": {
  // This field can be LICENSED, UNLICENSED, or UNEVALUATED.
  "appLicensingVerdict": "LICENSED"
}
```

`appLicensingVerdict` can have one of the following values:

**`LICENSED`**

The user has an app entitlement. In other words, the user installed or updated your app from Google Play on their device.

> **Note:** On some older devices the user keeps the app entitlement after uninstalling the app, so the user account will still be licensed if the user later obtains the same app another way.

**`UNLICENSED`**

The user doesn't have an app entitlement. This happens when, for example, the user sideloads your app or doesn't acquire it from Google Play. You can show the [GET_LICENSED](<https://developer.android.com/google/play/integrity/remediation#get-licensed-dialog>) dialog to users to remedy this.

**`UNEVALUATED`**

Licensing details were not evaluated because a necessary requirement was missed.

This could happen for several reasons, including the following:

- The device is not trustworthy enough.
- The version of your app installed on the device is unknown to Google Play.
- The user is not signed in to Google Play.

To check that the user has an app entitlement for your app, verify that the `appLicensingVerdict` is as expected, as shown in the following code snippet:

**Kotlin**

```kotlin
val accountDetails = JSONObject(payload).getJSONObject("accountDetails")
val appLicensingVerdict = accountDetails.getString("appLicensingVerdict")

if (appLicensingVerdict == "LICENSED") {
    // Looks good!
}
```

**Java**

```java
JSONObject accountDetails =
    new JSONObject(payload).getJSONObject("accountDetails");
String appLicensingVerdict = accountDetails.getString("appLicensingVerdict");

if (appLicensingVerdict.equals("LICENSED")) {
    // Looks good!
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
