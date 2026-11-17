Use the steps in this guide to access your app's asset packs from your Java code.

## Build for Kotlin and Java

Use the following steps to build Play Asset Delivery into your project's Android App Bundle. You don't need to use Android Studio to perform these steps.

> **Note:** For a guided tutorial, see the [Using Play Asset Delivery in native games Codelab](<https://codelabs.developers.google.com/codelabs/native-gamepad>).

1. Update the version of the Android Gradle plugin in your project's `build.gradle` file to `4.0.0` or later.
2. In the top-level directory of your project, create a directory for the asset pack. This directory name is used as the asset pack name. Asset pack names must start with a letter and can only contain letters, numbers, and underscores.
3. In the asset pack directory, create a `build.gradle` file and add the following code. Make sure to specify the name of the asset pack and only one delivery type:

   **Groovy**

   ```groovy
   // In the asset pack's build.gradle file:
   plugins {
     id 'com.android.asset-pack'
   }

   assetPack {
       packName = "asset-pack-name" // Directory name for the asset pack
       dynamicDelivery {
           deliveryType = "[ install-time | fast-follow | on-demand ]"
       }
   }
   ```

   **Kotlin**

   ```kotlin
   // In the asset pack's build.gradle.kts file:
   plugins {
     id("com.android.asset-pack")
   }

   assetPack {
     packName.set("asset-pack-name") // Directory name for the asset pack
     dynamicDelivery {
       deliveryType.set("[ install-time | fast-follow | on-demand ]")
     }
   }
   ```
4. In the project's app `build.gradle` file, add the name of every asset pack in your project as shown below:

   **Groovy**

   ```groovy
   // In the app build.gradle file:
   android {
       ...
       assetPacks = [":asset-pack-name", ":asset-pack2-name"]
   }
   ```

   **Kotlin**

   ```kotlin
   // In the app build.gradle.kts file:
   android {
       ...
       assetPacks += listOf(":asset-pack-name", ":asset-pack2-name")
   }
   ```
5. In the project's `settings.gradle` file, include all asset packs in your project as shown below:

   **Groovy**

   ```groovy
   // In the settings.gradle file:
   include ':app'
   include ':asset-pack-name'
   include ':asset-pack2-name'
   ```

   **Kotlin**

   ```kotlin
   // In the settings.gradle.kts file:
   include(":app")
   include(":asset-pack-name")
   include(":asset-pack2-name")
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
