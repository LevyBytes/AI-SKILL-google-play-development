### Configure the build process to automatically sign your app

In Android Studio, you can configure your project to sign the release version of your app automatically during the build process by creating a signing configuration and assigning it to your release build type. A signing configuration consists of a keystore location, keystore password, key alias, and key password. To create a signing configuration and assign it to your release build type using Android Studio, complete the following steps:

1. In the **Project** window, right click on your app and click **Open Module Settings**.
2. On the **Project Structure** window, under **Modules** in the left panel, click the module you would like to sign.
3. Click the **Signing** tab, then click **Add** ![Image](<https://developer.android.com/static/studio/images/publish/add-signing-config_2-1_2x.png>).
4. Select your keystore file, enter a name for this signing configuration (as you may create more than one), and enter the required information.

   ![Image](<https://developer.android.com/static/studio/images/publish/project-structure-signing_2-1_2x.png>)

   **Figure 7**. The window for creating a new signing configuration.
5. Click the **Build Types** tab.
6. Click the **release** build.
7. Under **Signing Config**, select the signing configuration you just created.

   ![Image](<https://developer.android.com/static/studio/images/publish/project-structure-build-types_2-1_2x.png>)

   **Figure 8**. Select a signing configuration in Android Studio.
8. Click **OK**.

Now every time you build your release build type by selecting an option under **Build > Build Bundle(s) / APK(s)** in Android Studio, the IDE will sign your app automatically, using the signing configuration you specified. You can find your signed APK or app bundle in the `build/outputs/` directory inside the project directory for the module you are building.

When you create a signing configuration, your signing information is included in plain text in your Gradle build files. If you are working in a team or sharing your code publicly, you should keep your signing information secure by removing it from the build files and storing it separately. You can read more about how to remove your signing information from your build files in [Remove Signing Information from Your Build Files](<https://developer.android.com/studio/publish/app-signing?hl=en#secure-shared-keystore>). For more about keeping your signing information secure, see [Keep your key secure](<https://developer.android.com/studio/publish/app-signing?hl=en#secure_key>), below.

### Sign each product flavor differently

If your app uses product flavors and you would like to sign each flavor differently, you can create additional signing configurations and assign them by flavor:

1. In the **Project** window, right click on your app and click **Open Module Settings**.
2. On the **Project Structure** window, under **Modules** in the left panel, click the module you would like to sign.
3. Click the **Signing** tab, then click **Add** ![Image](<https://developer.android.com/static/studio/images/publish/add-signing-config_2-1_2x.png>).
4. Select your keystore file, enter a name for this signing configuration (as you may create more than one), and enter the required information.

   ![Image](<https://developer.android.com/static/studio/images/publish/project-structure-signing_2-1_2x.png>)

   **Figure 10**. The window for creating a new signing configuration.
5. Repeat steps 3 and 4 as necessary until you have created all your signing configurations.
6. Click the **Flavors** tab.
7. Click the flavor you would like to configure, then select the appropriate signing configuration from the **Signing Config** dropdown menu. ![Image](<https://developer.android.com/static/studio/images/publish/project-structure-flavors_2-1_2x.png>)

   **Figure 11**. Configure signing settings by product flavor.

   Repeat to configure any additional product flavors.
8. Click **OK**.

You can also specify your signing settings in Gradle configuration files. For more information, see [Configuring Signing Settings](<https://developer.android.com/studio/build/build-variants#signing>).

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
