## Sign your app for release to Google Play

Before publishing, sign your app and upload it to an app store such as Google Play. Publishing a new app to Google Play also requires configuring Play App Signing. Only legacy apps that meet the [documented exemption](<https://developer.android.com/studio/publish/app-signing#app-signing-google-play>) may continue without opting in. The procedures below explain release signing and Play App Signing configuration.

### Generate an upload key and keystore

If you don't already have an upload key, which is useful when configuring Play App Signing, you can generate one using Android Studio as follows:

1. In the menu bar, click **Build > Generate Signed Bundle/APK**.
2. In the **Generate Signed Bundle or APK** dialog, select **Android App Bundle** or **APK** and click **Next**.
3. Below the field for **Key store path**, click **Create new**.
4. On the **New Key Store** window, provide the following information for your keystore and key, as shown in figure 2.

   ![Image](<https://developer.android.com/static/studio/images/publish/keystore-wizard_2x.png>)

   **Figure 2.** Create a new upload key and keystore in Android Studio.
5. **Keystore**

   - **Key store path:** Select the location where your keystore should be created. Also, a file name should be added to the end of the location path with the `.jks` extension.
   - **Password:** Create and confirm a secure password for your keystore.
6. **Key**

   - **Alias:** Enter an identifying name for your key.
   - **Password:** Create and confirm a secure password for your key. This should be the same as your keystore password. (Please refer to the [known issue](<https://developer.android.com/studio/known-issues#ki-key-keystore-warning>) for more information)
   - **Validity (years):** Set the length of time in years that your key will be valid. Your key should be valid for at least 25 years, so you can sign app updates with the same key through the lifespan of your app.
   - **Certificate:** Enter some information about yourself for your certificate. This information is not displayed in your app, but is included in your certificate as part of the APK.
7. Once you complete the form, click **OK**.
8. If you would like to build and sign your app with your upload key, continue to the section about how to [Sign your app with your upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#sign_release>). If you only want to generate the key and keystore, click **Cancel**.

### Sign your app with your key

If you already have an upload key, use it to sign your app. If instead your app is already signed and published to the Google Play store with an existing app signing key, use it to sign your app. You can later [generate and register a separate upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#register_upload_key>) with Google Play to sign and upload subsequent updates to your app.

To sign your app using Android Studio, follow these steps:

1. If you don’t currently have the **Generate Signed Bundle or APK** dialog open, click **Build > Generate Signed Bundle/APK**.
2. In the **Generate Signed Bundle or APK** dialog, select either **Android App Bundle** or **APK** and click **Next**.
3. Select a module from the drop down.
4. Specify the path to your keystore, the alias for your key, and enter the passwords for both. If you haven't yet prepared your upload keystore and key, first [Generate an upload key and keystore](<https://developer.android.com/studio/publish/app-signing?hl=en#generate-key>) and then return to complete this step.

   ![Image](<https://developer.android.com/static/studio/images/publish/generate-signed-apk-wizard_2x.png>)

   **Figure 3**. Sign your app with your upload key.

   > **Note:** For increased security, Google Play is introducing a new process to upload signing keys, and the option **Export encrypted key** in Android Studio is being deprecated. If you're signing an app with an existing app signing key, and you'd like to opt your app in to Play App Signing, see [Opt in an existing app](<https://developer.android.com/studio/publish/app-signing?hl=en#enroll_existing>) for the process to encrypt and export your signing key.
5. Click **Next**.
6. In the next window (shown in figure 4), select a destination folder for your signed app, select the build type, choose the product flavor(s) if applicable.
7. If you are building and signing an APK, you need to select which **Signature Versions** you want your app to support. To learn more, read about [app signing schemes](<https://source.android.com/security/apksigning>)

   > **Note:** Google Play supports [APK Signature Scheme v3](<https://source.android.com/security/apksigning/v3>) for APKs that aren't already published with an existing [signing certificate lineage](<https://developer.android.com/studio/command-line/apksigner#usage-rotate>).
8. Click **Create**.

   > **Note:** If your project uses product flavors, you can select multiple product flavors while holding down the **Control** key on Windows/Linux, or the **Command** key on Mac OSX. Android Studio will generate a separate APK or app bundle for each product flavor you select.

![Image](<https://developer.android.com/static/studio/images/publish/generate_signed_bundle_popup-2x.png>)

**Figure 5.** Click the link in the popup to analyze or locate your app bundle.

After Android Studio finishes building your signed app, you can either **locate** or **analyze** your app by clicking on the appropriate option in the pop-up notification, as shown in figure 5.

Now you’re ready to opt your app in to Play App Signing and upload your app for release. If you’re new to the app publishing process, you may want to read the [Launch overview](<https://developer.android.com/distribute/best-practices/launch>). Otherwise, continue to the page about how to [Upload your app to the Play Console](<https://developer.android.com/studio/publish/upload-bundle>).

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
