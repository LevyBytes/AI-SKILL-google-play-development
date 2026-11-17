Conditional delivery lets you set certain device configuration requirements for feature modules to be downloaded automatically during app install. For example, you can configure a feature module that includes functionality for augmented reality (AR) to be available at app install for only devices that support AR.

This delivery mechanism currently supports controlling the download of a module at app install-time based on the following device configurations:

- [Device hardware and software features](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#new-conditional>), including OpenGL ES version
- [User country](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#country-condition>)
- [API level](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#minapi-condition>)
- [Device model](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#device-targeting-condition>)
- [Device RAM](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#device-targeting-condition>)
- [System features](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#device-targeting-condition>)
- [System on Chip](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#device-targeting-condition>) (for devices with API level at least 31)

If a device does not meet all the requirements you specify, the module is not downloaded at app install-time. However, your app may later request to [download the module on demand](<https://developer.android.com/guide/app-bundle/playcore>) using the Play Core SDK.

Before you get started, make sure you're using Android Studio 3.5 or higher. Create a new conditional module using the procedure below. [Existing-module manifest and country rules](conditional-manifest-and-country-rules.md) and [API-level or device conditions](api-level-and-device-conditions.md) complete conditional delivery.

## Add a new module with conditional delivery options

The easiest way to create a new feature module with conditional delivery is through the **New Module** wizard, as follows:

1. To open the **New Module** dialog, select **File > New > New Module** from the menu bar.
2. In the New Module dialog, select **Dynamic Feature Module** and click **Next**.
3. Configure your module as you normally would and click **Next**.
4. In the **Module Download Options** section, complete the following:

   1. Specify the **Module title** using up to 50 characters. The platform uses this title to identify the module to users when, for example, confirming whether the user wants to download the module. For this reason, your app's base module must include the module title as a [string resource](<https://developer.android.com/guide/topics/resources/string-resource>), which you can translate. When creating the module using Android Studio, the IDE adds the string resource to the base module for you and injects the following entry in the feature module's manifest:

      ```xml
      <dist:module
          ...
          dist:title="@string/feature_title">
      </dist:module>
      ```

      > **Note:** If you enable resource shrinking, such as for your release builds, the shrinker may remove the module title string resource if code in your base module does not reference it. To make sure the string resource remains in the build output, include the resource in a [custom resource keep file](<https://developer.android.com/studio/build/shrink-code#keep-resources>).
   2. In the drop-down menu under **Install-time inclusion**, select **Only include module at app install for devices with specified features**, which creates a module that's included with your app at app install-time on only devices with certain configurations that you can specify, such as device features or country. Android Studio injects the following in the module's manifest to reflect your choice:

      ```xml
      <dist:module ... >
        <dist:delivery>
            <dist:install-time>
                <dist:conditions>
                    <!-- If you specify conditions, as described in the steps
                         below, the IDE includes them here. -->
                </dist:conditions>
            </dist:install-time>
        </dist:delivery>
      </dist:module>
      ```
   3. If you want to limit automatic download of the module to certain countries or a minimum API level, click **Finish** to complete creating the module and then read the section about how to [specify conditions based on country](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#country-condition>) or [minimum API level](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#minapi-condition>). Otherwise, click **+ device feature** to add a feature that a device requires in order to download the module at install-time.
   4. Next to **device-feature**, select one of the following options from the drop-down menu and specify its value:

      - **Name:** Lets you specify a hardware or software feature that a device requires in order to download the module at install-time. The features that conditional delivery supports are the same as those listed as `FEATURE_*` constants by [`PackageManager`](<https://developer.android.com/reference/android/content/pm/PackageManager#constants>). If you select this option, start typing any part of the constant value of the feature, such as "bluetooth", in the field next to the drop-down menu, and select one of the suggestions that appear.
      - **OpenGL ES Version:** Lets you specify a version of OpenGL ES that a device requires in order to download the module at install time. If you select this option, start typing the version, such as "0x00030001", in the field next to the drop-down menu, and select one of the suggestions that appear.
   5. If you want to add multiple conditions based on available device features, click **+ device feature** for each device feature condition you want to specify.
   6. Check the box next to **Fusing** if you want this module to be available to devices running Android 4.4 (API level 20) and lower and included in multi-APKs. This means you can enable on demand behavior for this module and disable fusing to omit it from devices that don't support downloading and installing split APKs. Android Studio injects the following in the module's manifest to reflect your choice:

      ```xml
      <dist:module ...>
          <dist:fusing dist:include="true | false" />
      </dist:module>
      ```
5. When you're done configuring module download options, click **Finish**.

Note that the Android Gradle plugin does not support running [lint](<https://developer.android.com/studio/write/lint>) from dynamic-feature modules. Running lint from the corresponding application module will run lint on its dynamic-feature modules and include all issues in the app's lint report.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/conditional).
