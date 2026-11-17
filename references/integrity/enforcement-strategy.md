### Have a tiered enforcement strategy

The Play Integrity API's integrity verdict has a range of possible responses making it possible to build an anti-abuse strategy with multiple tiers of enforcement. You can do this by configuring your app's backend server to behave differently depending on each possible response or group of responses.

Before evaluating device trustworthiness, it is essential to check the other core signals in the API response:

- **Request details:** Ensure the `requestDetails` match your expected values, in particular verifying the `requestHash` or `nonce` to prevent replay attacks.
- **App integrity:** Check that `appRecognitionVerdict` is `PLAY_RECOGNIZED`, confirming that the app's signing certificate is recognized by Play and untampered.
- **Account details:** Check that `appLicensingVerdict` is `LICENSED`, confirming that the user installed or updated the app from Google Play.

Your app should be able to handle when these baseline checks fail, for example, using the [in-app Play remediation dialog](<https://developer.android.com/google/play/integrity/remediation>). Additionally, your app should also be able to [handle error codes](<https://developer.android.com/google/play/integrity/error-codes>) that may arise during the request.

Once the baseline checks pass, it's possible to tier your enforcement strategy based on device trustworthiness by [opting in to receive additional device labels](<https://developer.android.com/google/play/integrity/setup#configure-api>) in your API response from the Play Console. Each device will return all the labels whose criteria it satisfies. To obtain the Android SDK version, you should use the `deviceAttributes` field included in the API response. The breadth of device trust tiers ranges from more trusted to less trusted devices:

- `MEETS_STRONG_INTEGRITY` (Android 13+): The highest device trust tier, requiring [hardware-backed security signals](<https://developer.android.com/privacy-and-security/security-key-attestation>) and a recent security patch.
- `MEETS_DEVICE_INTEGRITY` (Android 13+) and `MEETS_STRONG_INTEGRITY` (pre-Android 13): The next trust tier. Both rely on hardware-backed security signals.
- `MEETS_DEVICE_INTEGRITY` (pre-Android 13): The next tier, using hardware-backed attestation when available and software-backed attestation as a fallback.
- `MEETS_BASIC_INTEGRITY`: The weakest trust tier, just before receiving no device labels at all.

For example, after opting in to receive all the device labels, you could choose to trust a device that returns `MEETS_STRONG_INTEGRITY`, `MEETS_DEVICE_INTEGRITY`, and `MEETS_BASIC_INTEGRITY` more than a device that only returns `MEETS_BASIC_INTEGRITY`. You can respond differently from the server in each scenario.

You can then layer in other signals into your tiered enforcement strategy, such as treating devices as less trusted that return higher levels in `recentDeviceActivity`.

> **Tip:** Fewer devices are in the higher trust tiers than the lower device trust tiers, so it's recommended to have a tiered enforcement strategy instead of solely relying on the higher trust tiers to maximize user reach.

### Send a range of responses from your server to your app

Having a range of decision outcomes is harder to replicate than sending a binary "allow" or "deny" response from the server back to the app for each response. For example, you could use a series of related responses such as Allow, Allow with limits, Allow with limits after CAPTCHA completion, and Deny.

### Detect repeat abuse using device recall, while preserving user privacy

[Device recall](<https://developer.android.com/google/play/integrity/device-recall>) gives apps the ability to store and recall some custom data associated with a specific device in a way that preserves user privacy. The data is stored on Google's servers, allowing your app to reliably recall per-device data even after your app is reinstalled or the device is reset. This gives you a reliable way to re-identify a device that you found abusive in the past so that you can take action and stop it from being used for abuse again. You can define your own meaning to the three values that make up device recall data:

- You could use them as up to three separate flags or booleans. For example, values could represent that a device has or hasn't created an account, has or hasn't redeemed a free trial, or has or hasn't been known for high severity abuse.
- Alternatively, you could combine all of the states of the values into up to eight custom labels, for example one label for the default state when all three values are unmodified and seven labels with custom meanings. This lets you segment all devices into up to eight groups based on behaviors or actions that you define. In this scenario, the most recently updated of the three `writeDates` indicates when you last updated the label.

Also keep in mind the [prerequisites and other considerations](<https://developer.android.com/google/play/integrity/device-recall#device-recall-prerequisites>) when working with device recall data.

### Detect large-scale abuse using recent device activity

Use the [recent device activity](<https://developer.android.com/google/play/integrity/setup#optional_device_information>) feature in the Play Integrity API to find devices requesting large numbers of integrity tokens. High-volume-activity abusers commonly generate valid attestation results from real devices and provide them to bots to automate attacks on rooted devices and emulators. You can use the recent device activity level to check how many attestations were generated by your app on that device in the last hour.

### Show actionable error messages

When possible, provide useful error messages to the user and let them know what they can do to fix it; such as retrying, enabling their Internet connection, or checking that the Play Store app is up-to-date.

### Have a plan for unexpected issues or outages

The [Play status dashboard](<https://status.play.google.com>) shows information about the service status of Play Integrity API along with information about any disruptions and outages. You should plan in advance how you want your backend server to function in the unlikely event of a large-scale Play Integrity API outage. Note that your backend server should also be ready to function in the case when Android Platform Key Attestation keys specific for devices are [revoked](<https://developer.android.com/privacy-and-security/security-key-attestation#certificate_status>).

### Consider end to end enterprise fraud solutions

Enterprise customers looking for a complete fraud and bot management solution can purchase [reCAPTCHA Enterprise](<https://cloud.google.com/recaptcha-enterprise>) for mobile, which includes [SDKs for Android](<https://cloud.google.com/recaptcha-enterprise/docs/instrument-android-apps>) that provide fraud risk scores to developers. reCAPTCHA Enterprise automatically includes Play Integrity API signals, and combines them with reCAPTCHA network and application signals for customers, providing a frictionless, invisible fraud management solution out of the box. It can also provide protection for Android apps where Play Integrity API is not available.

### Challenge risky traffic when accessing high value or sensitive features

Identify high value or sensitive actions in your app or game to protect with the Play Integrity API instead of denying access outright. When possible, challenge risky traffic before allowing high-value actions to proceed. For example, when the app access risk indicates that an app is running that could capture the screen, ask the user to disable or uninstall apps that can capture the screen before allowing them to proceed to functionality that you want to protect.

## Terms of service and data safety

By accessing or using the Play Integrity API, you agree to the [Play Integrity API Terms of Service](<https://developer.android.com/google/play/integrity/terms>). Read and understand all applicable terms and policies before accessing the API.

Google Play has a data safety section for developers to disclose their apps' data collection, sharing, and security practices to keep your users informed. To help you complete your data form, see this information on [how the Play Integrity API handles data](<https://developer.android.com/google/play/integrity/terms#data-safety>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/overview).
