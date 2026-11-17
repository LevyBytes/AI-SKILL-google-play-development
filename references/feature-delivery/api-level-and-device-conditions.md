## Specify conditions for API level

Specifying a condition based on a device's API level can be useful if a feature module depends on APIs that are available in only certain versions of the Android platform.

To set a condition based on a minimum or maximum device API level, include the following in your feature module's manifest.

```xml
<dist:conditions>
    <!-- Specifies the minimum API level that the device must satisfy
         in order to download your module at app install-time. The API level you
         specify must be greater or equal to the module's own minSdkVersion. -->
   <dist:min-sdk dist:value="21"/>
    <!-- Specifies the maximum API level that the device cannot exceed
         in order to download your module at app install-time. The API level you
         specify must be less than or equal to the module's own maxSdkVersion. -->
   <dist:max-sdk dist:value="24"/>
</dist:conditions>
```

## Specify conditions for other device properties (beta)

To specify conditions for other device properties, such as model name, RAM, system features, and system on chip, you can use a device targeting configuration file.

To create a device targeting configuration file, see the [documentation for device targeting](<https://developer.android.com/google/play/device-targeting>).

Once you have created the configuration file, you can specify device groups for your module by including the following in the feature module's manifest.

```xml
<dist:conditions>
   <dist:device-groups>
      <dist:device-group dist:name="myCustomGroup1"/>
      <dist:device-group dist:name="myCustomGroup2"/>
   </dist:device-groups>
</dist:conditions>
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/conditional).
