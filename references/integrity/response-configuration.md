## Configure API responses (optional)

The API response includes default verdicts returned in every request. If you have linked your Cloud project in the Play Console or Play SDK Console, you can customize your API response to include additional information.

### Default integrity verdicts

The following integrity verdicts are returned in the Play Integrity API response by default:

| Response field | Value | Description |
| --- | --- | --- |
| Play account details | `LICENSED` | The user has an app entitlement. In other words, the user installed or updated your app from Google Play on their device. |
|  | `UNLICENSED` | The user doesn't have an app entitlement. This happens when, for example, the user sideloads your app or doesn't acquire it from Google Play. |
|  | `UNEVALUATED` | Licensing details were not evaluated because a requirement was missed. This could happen for several reasons, including the following: The device is not trustworthy enough. The user is not signed in to Google Play. The version of your app installed on the device is unknown to Google Play. |
| Application integrity | `PLAY_RECOGNIZED` | The app and certificate match the versions distributed by Google Play. |
|  | `UNRECOGNIZED_VERSION` | The certificate or package name does not match Google Play records. |
|  | `UNEVALUATED` | Application integrity was not evaluated. A necessary requirement was missed, such as the device not being trustworthy enough. |
| Device integrity | `MEETS_DEVICE_INTEGRITY` | The app is running on a genuine and certified Android-powered device. On Android 13 and higher, there is hardware-backed proof that the device bootloader is locked and the loaded Android OS is a certified device manufacturer image. |
|  | Empty (a blank value) | The app is running on a device that has signs of attack (such as API hooking) or system compromise (such as being rooted), or the app is not running on a physical device (such as an emulator that does not pass Google Play integrity checks). |

### Google Play Games for PC

If you distribute to [Google Play Games for PC](<https://developer.android.com/games/playgames/overview>), you will automatically be opted in to receive an additional label in the device integrity verdict:

| Response field | Label | Description |
| --- | --- | --- |
| Device integrity | `MEETS_VIRTUAL_INTEGRITY` | The app is running on an Android emulator powered by Google Play services. The emulator passes system integrity checks and meets core Android compatibility requirements. |

### Optional integrity verdicts

If you have linked your Cloud project in the Play Console or Play SDK Console, you can opt in to receive additional information.

To make changes, visit the Play Console and navigate to **Protected with Play**. Next to **Play Integrity API**, click **[Manage](<https://play.google.com/console/developers/app/app-integrity/integrity-api-settings>)**. Click **Change responses**, edit and save your changes.

> **Caution:** Changes to integrity responses take effect immediately, including for apps and SDKs in production. Make sure your server is prepared to accept new responses before saving changes.

#### Device information

**Additional device labels** in the `deviceIntegrity` verdict tell you more about the device environment the app is running on. A single device returns multiple labels if it meets the criteria for each. You can use these labels to create a tiered enforcement strategy. For example, you might choose to trust a device that returns three labels (`MEETS_STRONG_INTEGRITY`, `MEETS_DEVICE_INTEGRITY`, and `MEETS_BASIC_INTEGRITY`) more than a device that returns only one label (`MEETS_BASIC_INTEGRITY`).

**Device attributes** tells you the Android SDK version of the Android OS on the device. In the future, it may be extended with other device attributes.

**Recent device activity** returns a level ranging from `LEVEL_1` (low number of requests) to `LEVEL_4` (high number of requests). High activity levels may indicate a device being used to generate excessive tokens for abusive distribution to untrusted devices.

**Device recall** lets you store some custom, per-device data with specific devices that you can reliably retrieve when your app is installed again later on the same device.

> **Note:** [Device recall](<https://developer.android.com/google/play/integrity/device-recall>) is available in beta to apps and subject to change. Pricing for high-scale usage may apply after general release. SDKs cannot use device recall.

After you opt in to optional information, your API response will include new fields and responses in the verdict:

| Response field | Label | Description |  |
| --- | --- | --- | --- |
| Device integrity | `MEETS_BASIC_INTEGRITY` | The app is running on a device that passes basic system integrity checks. The device bootloader can be locked or unlocked, and the boot state can be verified or unverified. The device may not be certified, in which case Google cannot provide any security, privacy, or app compatibility assurances. On Android 13 and higher, the `MEETS_BASIC_INTEGRITY` verdict requires that the attestation [root of trust](<https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate>) is provided by Google. | The app is running on a device that passes basic system integrity checks. The device bootloader can be locked or unlocked, and the boot state can be verified or unverified. The device may not be certified, in which case Google cannot provide any security, privacy, or app compatibility assurances. On Android 13 and higher, the `MEETS_BASIC_INTEGRITY` verdict requires that the attestation [root of trust](<https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate>) is provided by Google. |
|  | `MEETS_STRONG_INTEGRITY` | The app is running on a genuine and certified Android-powered device with a recent security update. On Android 13 and higher, the `MEETS_STRONG_INTEGRITY` verdict requires `MEETS_DEVICE_INTEGRITY` and security updates in the last year for all partitions of the device, including an Android OS partition patch and a vendor partition patch.<br> On Android 12 and lower, the `MEETS_STRONG_INTEGRITY` verdict only requires hardware-backed proof of boot integrity and **does not** require the device to have a recent security update. Therefore, when using the `MEETS_STRONG_INTEGRITY`, it is recommended to also take into account the Android SDK version in the `deviceAttributes` field.<br>  | The app is running on a genuine and certified Android-powered device with a recent security update. On Android 13 and higher, the `MEETS_STRONG_INTEGRITY` verdict requires `MEETS_DEVICE_INTEGRITY` and security updates in the last year for all partitions of the device, including an Android OS partition patch and a vendor partition patch.<br> On Android 12 and lower, the `MEETS_STRONG_INTEGRITY` verdict only requires hardware-backed proof of boot integrity and **does not** require the device to have a recent security update. Therefore, when using the `MEETS_STRONG_INTEGRITY`, it is recommended to also take into account the Android SDK version in the `deviceAttributes` field.<br>  |
| Device attributes | `sdkVersion: 19, 20, ..., 37` | The SDK version of the Android OS running on the device. The number returned maps to [`Build.VERSION_CODES`](<https://developer.android.com/reference/android/os/Build.VERSION_CODES>). | The SDK version of the Android OS running on the device. The number returned maps to [`Build.VERSION_CODES`](<https://developer.android.com/reference/android/os/Build.VERSION_CODES>). |
|  | Empty (a blank value) | The SDK version is not evaluated because a necessary requirement was missed. In this case, the `sdkVersion` field is unset; thus, the `deviceAttributes` field is empty. This could happen because: The device is not trustworthy enough.<br> There were technical issues on the device.<br>  | The SDK version is not evaluated because a necessary requirement was missed. In this case, the `sdkVersion` field is unset; thus, the `deviceAttributes` field is empty. This could happen because: The device is not trustworthy enough.<br> There were technical issues on the device.<br>  |
|  |  | **Standard API integrity token requests on this device in the last hour per app** | **Classic API integrity token requests on this device in the last hour per app** |
| Recent device activity | `LEVEL_1` (lowest) | 10 or fewer | 5 or fewer |
|  | `LEVEL_2` | Between 11 and 25 | Between 6 and 10 |
|  | `LEVEL_3` | Between 26 and 50 | Between 11 and 15 |
|  | `LEVEL_4` (highest) | More than 50 | More than 15 |
|  | `UNEVALUATED` | Recent device activity was not evaluated. This could happen because: The device is not trustworthy enough.<br> The version of your app installed on the device is unknown to Google Play.<br> There were technical issues on the device.<br>  | Recent device activity was not evaluated. This could happen because: The device is not trustworthy enough.<br> The version of your app installed on the device is unknown to Google Play.<br> There were technical issues on the device.<br>  |
| Device recall | `values: bitFirst, bitSecond, bitThird` | These are the bit values that you set in the past for the specific device. You decide the meaning of each bit. The three bit values are false by default. | These are the bit values that you set in the past for the specific device. You decide the meaning of each bit. The three bit values are false by default. |
|  | `writeDates: yyyymmFirst, yyyymmSecond, yyyymmThird` | These are the bit value write dates in UTC accurate to the year and month. The write date of a recall bit is updated every time the bit is set to true and is removed when the bit is set to false. | These are the bit value write dates in UTC accurate to the year and month. The write date of a recall bit is updated every time the bit is set to true and is removed when the bit is set to false. |

#### Environment details

**App access risk** tells you whether other apps are running that could be used to capture the screen, display overlays, or control the device. Verified accessibility services that are known to Google Play are automatically excluded from this verdict.

**Play Protect verdict** tells you whether Google Play Protect is enabled on the device and whether it has found known malware.

After you opt in to optional information, your API response will include new fields and responses in the verdict:

| Response field | Value | Description |
| --- | --- | --- |
| App access risk verdict | `KNOWN_INSTALLED` | Apps are installed by Google Play or preloaded on the system partition by the device manufacturer. |
|  | `KNOWN_CAPTURING` | Apps installed by Google Play or preloaded on the device are running that could be used to read or capture inputs and outputs of the requesting app, such as screen recording apps. |
|  | `KNOWN_CONTROLLING` | Apps installed by Google Play or preloaded on the device are running that could be used to control the device and inputs and outputs of the requesting app, such as remote controlling apps. |
|  | `KNOWN_OVERLAYS` | Apps installed by Google Play or preloaded on the device are running that might be displaying overlays on the requesting app. |
|  | `UNKNOWN_INSTALLED` | Other apps are installed, which were not installed by Google Play or preloaded on the system partition by the device manufacturer. |
|  | `UNKNOWN_CAPTURING` | Other apps are running (not installed by Play or preloaded on the device) that could be used to read or capture inputs and outputs of the requesting app, such as screen recording apps. |
|  | `UNKNOWN_CONTROLLING` | Other apps are running (not installed by Play or preloaded on the device) that could be used to control the device and inputs and outputs of the requesting app, such as remote controlling apps. |
|  | `UNKNOWN_OVERLAYS` | Other apps are running (not installed by Play or preloaded on the device) that might be displaying overlays on the requesting app. |
|  | Empty (a blank value) | App access risk is not evaluated if a necessary requirement was missed. In this case the `appAccessRiskVerdict` field is empty. This could happen for several reasons, including the following: The device is not trustworthy enough. The device form factor is not a phone, tablet, or foldable. The device is not running Android 6 (API level 23) or higher. The version of your app installed on the device is unknown to Google Play. The version of the Google Play Store on the device is outdated. **Games only**: The user account does not have a Play license for the game. A standard request was used with the `verdictOptOut` parameter. A standard request was used with a Play Integrity API library version that doesn't yet support app access risk for standard requests. |
| Play Protect verdict | `NO_ISSUES` | Play Protect is turned on and did not find any app issues on the device. |
|  | `NO_DATA` | Play Protect is turned on but no scan has been performed yet. The device or the Play Store app may have been recently reset. |
|  | `POSSIBLE_RISK` | Play Protect is turned off. |
|  | `MEDIUM_RISK` | Play Protect is turned on and has found potentially harmful apps installed on the device. |
|  | `HIGH_RISK` | Play Protect is turned on and has found dangerous apps installed on the device. |
|  | `UNEVALUATED` | The Play Protect verdict was not evaluated. A necessary requirement was missed, such as the device not being trustworthy enough. |

> **Note:** The app access risk verdict automatically exempts verified accessibility services known to Google Play. These services won't trigger a capturing, controlling, or overlay response, meaning legitimate accessibility tools are not flagged as risks.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/setup).
