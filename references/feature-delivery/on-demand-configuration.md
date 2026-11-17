Feature modules allow you to separate certain features and resources from the base module of your app and include them in your app bundle. Through Play Feature Delivery, users can, for example, later download and install those components on demand after they’ve already installed the base APK of your app.

For example, consider a text messaging app that includes functionality for capturing and sending picture messages, but only a small percentage of users send picture messages. It may make sense to include picture messaging as a downloadable feature module. That way, the initial app download is smaller for all users and only those users who send picture messages need to download that additional component.

Keep in mind, this type of modularization requires more effort and possibly refactoring your app’s existing code, so consider carefully which of your app’s features would benefit the most from being available to users on demand. To better understand optimal use cases and guidelines for on demand features, read [UX best practices for on demand delivery](<https://developer.android.com/studio/projects/dynamic-delivery/ux-guidelines>).

If you want to gradually modularize app features over time, without enabling advanced delivery options, such as on demand deliver, instead [configure install-time delivery](<https://developer.android.com/studio/projects/dynamic-delivery/at-install-delivery>).

This page helps you add a feature module to your app project and configure it for on demand delivery. Before you begin, make sure you're using [Android Studio 3.5](<https://developer.android.com/studio>) or higher and Android Gradle Plugin 3.5.0 or higher.

## Configure a new module for on demand delivery

The easiest way to create a new feature module is by using [Android Studio 3.5](<https://developer.android.com/studio>) or higher. Because feature modules have an inherent dependency on the base app module, you can add them only to existing app projects.

To add a feature module to your app project using Android Studio, proceed as follows:

1. If you haven’t already done so, open your app project in the IDE.
2. Select **File > New > New Module** from the menu bar.
3. In the **Create New Module** dialog, select **Dynamic Feature Module** and click **Next**.
4. In the **Configure your new module** section, complete the following:

   1. Select the **Base application module** for your app project from the dropdown menu.
   2. Specify a **Module name**. The IDE uses this name to identify the module as a Gradle subproject in your [Gradle settings file](<https://developer.android.com/studio/build#settings-file>). When you build your app bundle, Gradle uses the last element of the subproject name to inject the `<manifest split>` attribute in the [feature module’s manifest](<https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest>).
   3. Specify the module’s **package name**. By default, Android Studio suggests a package name that combines the root package name of the base module and the module name you specified in the previous step.
   4. Select the **Minimum API level** you want the module to support. This value should match that of the base module.
5. Click **Next**.
6. In the **Module Download Options** section, complete the following:

   1. Specify the **Module title** using up to 50 characters. The platform uses this title to identify the module to users when, for example, confirming whether the user wants to download the module. For this reason, your app’s base module must include the module title as a [string resource](<https://developer.android.com/guide/topics/resources/string-resource>), which you can translate. When creating the module using Android Studio, the IDE adds the string resource to the base module for you and injects the following entry in the feature module’s manifest:

      ```xml
      <dist:module
          ...
          dist:title="@string/feature_title">
      </dist:module>
      ```

      > **Note:** If you enable resource shrinking, such as for your release builds, the shrinker may remove the module title string resource if code in your base module does not reference it. To make sure the string resource remains in the build output, include the resource in a [custom resource keep file](<https://developer.android.com/studio/build/shrink-code#keep-resources>).
   2. In the dropdown menu under **Install-time inclusion**, select **Do not include module at install-time**. Android Studio injects the following in the module’s manifest to reflect your choice:

      ```xml
      <dist:module ... >
        <dist:delivery>
            <dist:on-demand/>
        </dist:delivery>
      </dist:module>
      ```
   3. Check the box next to **Fusing** if you want this module to be available to devices running Android 4.4 (API level 20) and lower and included in multi-APKs. This means you can enable on demand behavior for this module and disable fusing to omit it from devices that don’t support downloading and installing split APKs. Android Studio injects the following in the module’s manifest to reflect your choice:

      ```xml
      <dist:module ...>
          <dist:fusing dist:include="true | false" />
      </dist:module>
      ```
7. Click **Finish**.

After Android Studio finishes creating your module, inspect its contents yourself from the **Project** pane (select **View > Tool Windows > Project** from the menu bar). The default code, resources, and organization should be similar to those of the standard app module.

Next, you will need to implement the on demand install functionality using the Play Feature Delivery library.

## Include the Play Feature Delivery Library in your project

Before you can start, you need to first [add the Play Feature Delivery Library](<https://developer.android.com/guide/playcore#java-kotlin-feature-delivery>) to your project.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
