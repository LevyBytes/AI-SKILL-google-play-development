#### Play Protect verdict

Once enabled, the `environmentDetails` field in the [Play Integrity API payload](<https://developer.android.com/google/play/integrity/verdict#returned-payload-format>) will contain the Play Protect verdict:

```json
"environmentDetails": {
  "playProtectVerdict": "NO_ISSUES"
}
```

`playProtectVerdict` can have one of the following values:

**`NO_ISSUES`**

Play Protect is turned on and did not find any app issues on the device.

**`NO_DATA`**

Play Protect is turned on but no scan has been performed yet. The device or the Play Store app may have been recently reset.

**`POSSIBLE_RISK`**

Play Protect is turned off.

**`MEDIUM_RISK`**

Play Protect is turned on and has found potentially harmful apps installed on the device.

**`HIGH_RISK`**

Play Protect is turned on and has found dangerous apps installed on the device.

**`UNEVALUATED`**

The Play Protect verdict was not evaluated.

This could happen for several reasons, including the following:

- The device is not trustworthy enough.
- The user account does not have a Play license.

#### Guidance on using the Play Protect verdict

Your app's backend server can decide how to act based on the verdict based on your risk tolerance. Here are some suggestions and potential user actions:

**`NO_ISSUES`**

Play Protect is on and hasn't found any issues so no user action is required.

**`POSSIBLE_RISK` and `NO_DATA`**

When receiving these verdicts, ask the user to check that Play Protect is on and has performed a scan. `NO_DATA` should appear only in rare circumstances.

**`MEDIUM_RISK` and `HIGH_RISK`**

Depending on your risk tolerance, you can ask the user to launch Play Protect and take action on the Play Protect warnings. If the user can't fulfill these requirements you could block them from the server action.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
