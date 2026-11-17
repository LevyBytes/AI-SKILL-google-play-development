## How to add code transparency

Before you can add code transparency to your app, make sure that you have a private and public key pair that you can use for code transparency signing. This should be a unique key that is different from the app signing key that you use for Play App Signing, and it must be held securely and never shared outside of your organization.

If you don't have a key, you can follow the instructions in the [Sign your app](<https://developer.android.com/studio/publish/app-signing#generate-key>) guide to generate one on your machine. Code transparency uses a standard keystore file, so even though the guide is for app signing, the key generation process is the same.

### Using Android Gradle plugin

Code transparency support requires Android Gradle plugin version 7.1.0-alpha03 or newer. To configure the key used for code transparency signing, add the following in the `bundle` block.

**Groovy**

```groovy
// In your app module's build.gradle file:
android {
    ...
    bundle {
        codeTransparency {
            signing {
                keyAlias = "ALIAS"
                keyPassword = "PASSWORD"
                storeFile = file("path/to/keystore")
                storePassword = "PASSWORD"
            }
        }
        ...
    }
}
```

**Kotlin**

```kotlin
// In your app module's build.gradle.kts file:
android {
    ...
    bundle {
        codeTransparency {
            signing {
                keyAlias = "ALIAS"
                keyPassword = "PASSWORD"
                storeFile = file("path/to/keystore")
                storePassword = "PASSWORD"
            }
        }
        ...
    }
}
```

The key used must be one that you will only use for code transparency, and not the app signing key that is used by Play App Signing.

### Using `bundletool` on the command line

Code transparency support requires bundletool version 1.7.0 or newer, which you can [download from GitHub](<https://github.com/google/bundletool/releases>).

Run the following command to add code transparency to an Android App Bundle. The key used must be one that you will only use for code transparency, and not the app signing key that is used by Play App Signing.

```text
bundletool add-transparency \
  --bundle=/MyApp/my_app.aab \
  --output=/MyApp/my_app_with_transparency.aab \
  --ks=/MyApp/keystore.jks \
  --ks-pass=file:/MyApp/keystore.pwd \
  --ks-key-alias=MyKeyAlias \
  --key-pass=file:/MyApp/key.pwd
```

Alternatively, if you want to use your own signing tools, you can use bundletool to generate the unsigned code transparency file, sign it in a separate environment and inject the signature into the bundle:

```text
# Generate code transparency file
bundletool add-transparency \
  --mode=generate_code_transparency_file \
  --bundle=/MyApp/my_app.aab \
  --output=/MyApp/code_transparency_file.jwt \
  --transparency-key-certificate=/MyApp/transparency.cert

# Add code transparency signature to the bundle
bundletool add-transparency \
  --mode=inject_signature \
  --bundle=/MyApp/my_app.aab \
  --output=/MyApp/my_app_with_transparency.aab \
  --transparency-key-certificate=/MyApp/transparency.cert \
  --transparency-signature=/MyApp/signature
```

> **Note:** Adding the code transparency file to the bundle invalidates any existing signatures. The resulting bundle (`my_app_with_transparency.aab` in the previous example) must be resigned with the upload key (e.g. using `jarsigner`) before uploading it to the Play Console for distribution.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/code-transparency).
