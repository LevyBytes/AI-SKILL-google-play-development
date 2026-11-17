The values below are loaded by [external signing credentials](external-signing-credentials.md); keep that file outside version control.

4. You can refer to properties stored in `keystoreProperties` using the syntax `keystoreProperties['propertyName']`. Modify the `signingConfigs` block of your module's `build.gradle` file to reference the signing information stored in `keystoreProperties` using this syntax.

   **Groovy**

   ```groovy
   android {
       signingConfigs {
           config {
               keyAlias keystoreProperties['keyAlias']
               keyPassword keystoreProperties['keyPassword']
               storeFile file(keystoreProperties['storeFile'])
               storePassword keystoreProperties['storePassword']
           }
       }
       ...
     }
   ```

   **Kotlin**

   ```kotlin
   android {
       signingConfigs {
           create("config") {
               keyAlias = keystoreProperties["keyAlias"] as String
               keyPassword = keystoreProperties["keyPassword"] as String
               storeFile = file(keystoreProperties["storeFile"] as String)
               storePassword = keystoreProperties["storePassword"] as String
           }
       }
       ...
     }
   ```
5. Open the **Build Variants** tool window and ensure that the release build type is selected.
6. Select an option under **Build > Build Bundle(s) / APK(s)** to build either an APK or app bundle of your release build. You should see the build output in the `build/outputs/` directory for your module.

Because your build files no longer contain sensitive information, you can now include them in source control or upload them to a shared codebase. Be sure to keep the `keystore.properties` file secure. This may include removing it from your source control system.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
