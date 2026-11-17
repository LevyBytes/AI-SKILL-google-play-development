#### Remove signing information from your build files

When you create a signing configuration, Android Studio adds your signing information in plain text to the module's `build.gradle` files. If you are working with a team or open-sourcing your code, you should move this sensitive information out of the build files so it is not easily accessible to others. To do this, you should create a separate properties file to store secure information and refer to that file in your build files as follows:

1. Create a signing configuration, and assign it to one or more build types. These instructions assume you have configured a single signing configuration for your release build type, as described in [Configure the build process to automatically sign your app](<https://developer.android.com/studio/publish/app-signing?hl=en#sign-auto>), above.
2. Create a file named `keystore.properties` in the root directory of your project. This file should contain your signing information, as follows:

   ```text

   storePassword=myStorePassword
   keyPassword=mykeyPassword
   keyAlias=myKeyAlias
   storeFile=myStoreFileLocation
   ```
3. In your module's `build.gradle` file, add code to load your `keystore.properties` file before the `android {}` block.

   **Groovy**

   ```groovy
   ...

   // Create a variable called keystorePropertiesFile, and initialize it to your
   // keystore.properties file, in the rootProject folder.
   def keystorePropertiesFile = rootProject.file("keystore.properties")

   // Initialize a new Properties() object called keystoreProperties.
   def keystoreProperties = new Properties()

   // Load your keystore.properties file into the keystoreProperties object.
   keystoreProperties.load(new FileInputStream(keystorePropertiesFile))

   android {
       ...
   }
   ```

   **Kotlin**

   ```kotlin
   ...
   import java.util.Properties
   import java.io.FileInputStream

   // Create a variable called keystorePropertiesFile, and initialize it to your
   // keystore.properties file, in the rootProject folder.
   val keystorePropertiesFile = rootProject.file("keystore.properties")

   // Initialize a new Properties() object called keystoreProperties.
   val keystoreProperties = Properties()

   // Load your keystore.properties file into the keystoreProperties object.
   keystoreProperties.load(FileInputStream(keystorePropertiesFile))

   android {
       ...
   }
   ```

   **Note:** You could choose to store your `keystore.properties` file in another location (for example, in the module folder rather than the root folder for the project, or on your build server if you are using a continuous integration tool). In that case, you should modify the code above to correctly initialize `keystorePropertiesFile` using your actual `keystore.properties` file's location.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
