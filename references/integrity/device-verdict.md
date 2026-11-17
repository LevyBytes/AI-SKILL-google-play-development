### Device integrity field

The `deviceIntegrity` field can contain a single value, `deviceRecognitionVerdict`, that has one or more labels representing how well a device can enforce app integrity. If a device does not meet the criteria of any labels, then the `deviceIntegrity` field omits `deviceRecognitionVerdict`.

```json
"deviceIntegrity": {
  // "MEETS_DEVICE_INTEGRITY" is one of several possible values.
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"]
}
```

By default, `deviceRecognitionVerdict` can contain the following:

**`MEETS_DEVICE_INTEGRITY`**

The app is running on a genuine and certified Android device. On Android 13 and higher, there is hardware-backed proof that the device bootloader is locked and the loaded Android OS is a certified device manufacturer image.

**Empty (a blank value)**

The app is running on a device that has signs of attack (such as API hooking) or system compromise (such as being rooted), or the app is not running on a physical device (such as an emulator that does not pass Google Play integrity checks).

To ensure that the token came from a trustworthy device, verify the `deviceRecognitionVerdict` is as expected, as shown in the following code snippet:

**Kotlin**

```kotlin
val deviceIntegrity =
    JSONObject(payload).getJSONObject("deviceIntegrity")
val deviceRecognitionVerdict =
    if (deviceIntegrity.has("deviceRecognitionVerdict")) {
        deviceIntegrity.getJSONArray("deviceRecognitionVerdict").toString()
    } else {
        ""
    }

if (deviceRecognitionVerdict.contains("MEETS_DEVICE_INTEGRITY")) {
    // Looks good!
}
```

**Java**

```java
JSONObject deviceIntegrity =
    new JSONObject(payload).getJSONObject("deviceIntegrity");
String deviceRecognitionVerdict =
    deviceIntegrity.has("deviceRecognitionVerdict")
    ? deviceIntegrity.getJSONArray("deviceRecognitionVerdict").toString()
    : "";

if (deviceRecognitionVerdict.contains("MEETS_DEVICE_INTEGRITY")) {
    // Looks good!
}
```

If you are having problems with your testing device meeting device integrity, make sure the factory ROM is installed (for example, by resetting the device) and that the bootloader is locked. You can also [create Play Integrity API tests in your Play Console](<https://developer.android.com/google/play/integrity/additional-tools#create-tests>).

### Conditional device labels

If your app is being released to [Google Play Games for PC](<https://developer.android.com/games/playgames/overview>), the `deviceRecognitionVerdict` can also contain the following label:

**`MEETS_VIRTUAL_INTEGRITY`**

The app is running on an Android-powered emulator with Google Play services. The emulator passes system integrity checks and meets core Android compatibility requirements.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
