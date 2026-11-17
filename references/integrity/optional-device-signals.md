### Optional device information and device recall

You can opt in to receive optional device labels as part of a [tiered enforcement strategy](<https://developer.android.com/google/play/integrity/overview#have-tiered>). If you [opt in to receive additional labels](<https://developer.android.com/google/play/integrity/setup#configure-api>) in the integrity verdict, `deviceRecognitionVerdict` can contain the following additional labels:

**`MEETS_BASIC_INTEGRITY`**

The app is running on a device that passes basic system integrity checks. The device bootloader can be locked or unlocked, and the boot state can be verified or unverified. The device may not be certified, in which case Google cannot provide any security, privacy, or app compatibility assurances. On Android 13 and higher, the `MEETS_BASIC_INTEGRITY` verdict requires only that the attestation [root of trust](<https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate>) is provided by Google.

**`MEETS_STRONG_INTEGRITY`**

The app is running on a genuine and certified Android device with a recent security update.

- On Android 13 and higher, the `MEETS_STRONG_INTEGRITY` verdict requires `MEETS_DEVICE_INTEGRITY` and security updates in the last year for all partitions of the device, including an Android OS partition patch and a vendor partition patch.
- On Android 12 and lower, the `MEETS_STRONG_INTEGRITY` verdict only requires hardware-backed proof of boot integrity and **does not** require the device to have a recent security update. Therefore, when using the `MEETS_STRONG_INTEGRITY`, it is recommended to also take into account the Android SDK version in the `deviceAttributes` field.

A single device will return multiple device labels in the device integrity verdict if each of the label's criteria is met.

> **Note:** On Android 13 and higher, the optional `MEETS_BASIC_INTEGRITY` and `MEETS_STRONG_INTEGRITY` device labels are returned only if the requesting app is licensed (installed or updated by Google Play). If the app isn't licensed, these optional labels are omitted from `deviceRecognitionVerdict`. Any other labels that the device meets, such as `MEETS_DEVICE_INTEGRITY`, are still returned. If no labels remain, `deviceRecognitionVerdict` is omitted.

#### Device attributes

You can also opt in to device attributes, which tells the Android SDK version of the Android OS running on the device. The Android SDK version is useful for differentiating between devices running Android 13 and higher and devices running lower Android SDK versions as part of a [tiered enforcement strategy](<https://developer.android.com/google/play/integrity/overview#have-tiered>). In the future, it might be extended with other device attributes.

The SDK version value is the Android SDK version number defined in [`Build.VERSION_CODES`](<https://developer.android.com/reference/android/os/Build.VERSION_CODES>). The SDK version is not evaluated if a necessary requirement was missed. In this case, the `sdkVersion` field is unset; thus, the `deviceAttributes` field is empty. This could happen because:

- The device is not trustworthy enough.
- There were technical issues on the device.

If you opt in to receive `deviceAttributes`, the `deviceIntegrity` field will have the following extra field:

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "deviceAttributes": {
    // 33 is one possible value, which represents Android 13 (Tiramisu).
    "sdkVersion": 33
  }
}
```

In case the SDK version is not evaluated, the `deviceAttributes` field will be set as the following:

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "deviceAttributes": {}  // sdkVersion field is not set.
}
```

#### Recent device activity

You can also opt in to recent device activity, which tells you how many times your app requested an integrity token on a specific device in the last hour. You can use recent device activity to protect your app against unexpected, hyperactive devices that could be an indication of an active attack. You can decide how much to trust each recent device activity level based on how many times you expect your app installed on a typical device to request an integrity token each hour.

If you opt in to receive `recentDeviceActivity` the `deviceIntegrity` field will have two values:

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "recentDeviceActivity": {
    // "LEVEL_2" is one of several possible values.
    "deviceActivityLevel": "LEVEL_2"
  }
}
```

The `deviceActivityLevel` definitions differ between modes and can have one of the following values:

| **Recent device activity level** | **Standard API integrity token requests on this device in the last hour per app** | **Classic API integrity token requests on this device in the last hour per app** |
| --- | --- | --- |
| `LEVEL_1` (lowest) | 10 or fewer | 5 or fewer |
| `LEVEL_2` | Between 11 and 25 | Between 6 and 10 |
| `LEVEL_3` | Between 26 and 50 | Between 11 and 15 |
| `LEVEL_4` (highest) | More than 50 | More than 15 |
| `UNEVALUATED` | Recent device activity was not evaluated. This could happen because: The device is not trustworthy enough.<br> The version of your app installed on the device is unknown to Google Play.<br> The requesting app is not licensed (on Android 13 and higher).<br> Technical issues on the device.<br>  | Recent device activity was not evaluated. This could happen because: The device is not trustworthy enough.<br> The version of your app installed on the device is unknown to Google Play.<br> The requesting app is not licensed (on Android 13 and higher).<br> Technical issues on the device.<br>  |

> **Note:** Level definitions are approximate.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
