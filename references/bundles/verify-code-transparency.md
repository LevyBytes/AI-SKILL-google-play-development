## Verify code transparency of an app

There are different methods for verifying code against the code transparency file, depending on whether you have the APKs installed on a device that runs Android or downloaded locally to your computer.

> **Important:** To verify that the signature comes from the original developer, the printed fingerprint from one of the following methods must be compared with the public key communicated by the developer through a trusted channel. For example, the developer can host their public certificate on a secure website that is known to belong to them. To ensure no other changes have been made to the app, checking the APK signature is also necessary and recommended.

### Using Bundletool to check an app bundle or APK set

You can use bundletool to verify code transparency in an app bundle or an APK set. Use the `check-transparency` command to print the public certificate fingerprint:

```text
# For checking a bundle:
bundletool check-transparency \
  --mode=bundle \
  --bundle=/MyApp/my_app_with_transparency.aab

No APK present. APK signature was not checked.
Code transparency signature is valid. SHA-256 fingerprint of the code transparency key certificate (must be compared with the developer's public key manually): 01 23 45 67 89 AB CD EF ..
Code transparency verified: code related file contents match the code transparency file.


# For checking a ZIP containing app's APK splits:
bundletool check-transparency \
  --mode=apk \
  --apk-zip=/MyApp/my_app_with_transparency.zip

APK signature is valid. SHA-256 fingerprint of the apk signing key certificate (must be compared with the developer's public key manually): 02 34 E5 98 CD A7 B2 12 ..
Code transparency signature is valid. SHA-256 fingerprint of the code transparency key certificate (must be compared with the developer's public key manually): 01 23 45 67 89 AB CD EF ..
Code transparency verified: code related file contents match the code transparency file.
```

You can optionally specify the public certificate that you want to verify the bundle or APK set against, so that you don't have to compare the hashes manually:

```text
bundletool check-transparency \
  --mode=bundle \
  --bundle=/MyApp/my_app_with_transparency.aab \
  --transparency-key-certificate=/MyApp/transparency.cert

No APK present. APK signature was not checked.
Code transparency signature verified for the provided code transparency key certificate.
Code transparency verified: code related file contents match the code transparency file.


bundletool check-transparency \
  --mode=apk \
  --apk-zip=/MyApp/my_app_with_transparency.zip \
  --apk-signing-key-certificate=/MyApp/apk.cert \
  --transparency-key-certificate=/MyApp/transparency.cert

APK signature verified for the provided apk signing key certificate.
Code transparency signature verified for the provided code transparency key certificate.
Code transparency verified: code related file contents match the code transparency file.
```

### Using Bundletool to check an app installed on a device

To check an app installed on a device that runs Android, make sure the device is connected to your computer using ADB, and run the following command:

```text
bundletool check-transparency \
  --mode=connected_device \
  --package-name="com.my.app"

APK signature is valid. SHA-256 fingerprint of the apk signing key certificate (must be compared with the developer's public key manually): 02 34 E5 98 CD A7 B2 12 ..
Code transparency signature is valid. SHA-256 fingerprint of the code transparency key certificate (must be compared with the developer's public key manually): 01 23 45 67 89 AB CD EF ..
Code transparency verified: code related file contents match the code transparency file.
```

The connected device transparency check can also optionally verify the signature against a public key that you specify:

```text
bundletool check-transparency \
  --mode=connected-device \
  --package-name="com.my.app" \
  --apk-signing-key-certificate=/MyApp/apk.cert \
  --transparency-key-certificate=/MyApp/transparency.cert

APK signature verified for the provided apk signing key certificate.
Code transparency signature verified for the provided code transparency key certificate.
Code transparency verified: code related file contents match the code transparency file.
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/code-transparency).
