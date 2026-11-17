## Add conditional delivery options to an existing feature module

You can add conditional delivery options to an existing feature module through the module's manifest. However, you should first read about the [compatibility of conditional delivery options](<https://developer.android.com/guide/playcore/feature-delivery/conditional?hl=en#dist-compat>) with other delivery options you may already have enabled.

To get started, you need to first migrate your manifest to the new `<dist:delivery>` element. The code snippet below shows an example of the older syntax:

```xml
<!-- This is the old syntax. -->
<dist:module
  dist:title="@string/feature_title" dist:onDemand="true">
  <dist:fusing dist:include="true"/>
</dist:module>
```

The delivery options above are now specified as follows.

```xml
<dist:module
  dist:title="@string/feature_title">
  <dist:delivery>
      <dist:on-demand/>
  </dist:delivery>
  <dist:fusing dist:include="true"/>
</dist:module>
```

You can then include conditional delivery options based on device features as follows.

```xml
<dist:module
    dist:title="@string/feature_title">
    <dist:delivery>
      <dist:on-demand/>
      <dist:install-time>
        <dist:conditions>
          <!-- Requires that the device support AR to download the module at
          app install-time.  -->
          <dist:device-feature dist:name="android.hardware.camera.ar"/>
        </dist:conditions>
      </dist:install-time>
    </dist:delivery>
    <dist:fusing dist:include="true"/>
</dist:module>
```

The sections below discuss other options for conditional delivery, such as by country or minimum API level.

## Compatibility with other module download options

Because feature modules offer multiple options to configure how each feature is delivered to a user's device, it's important to understand how conditional delivery options are affected by other settings. The following table summarizes compatibility of conditional delivery with other module download options.

| Module download option | Compatibility with conditional delivery |
| --- | --- |
| Fusing (`<dist:fusing dist:include="true"/>`) | If a module sets this option to true, Google Play does not respect the conditional delivery options you specify when deploying your app to devices running API level 19 or lower. That is, feature modules that enable fusing are always included at install time for device running API level 19 or lower. |
| Instant-enabled (`<dist:module dist:instant="true"/>`) | Conditional delivery options are not supported for instant-enabled feature modules. |
| On demand (`<dist:on-demand/>`) | By default, if you specify conditional delivery options, the module is also available on demand. |

## Specify conditions based on country

Conditional delivery also lets you specify which countries you want to exclude (or include) from downloading your module at app install-time. Specifying this condition might be useful if, for example, your module implements a payment method that's not available in certain regions.

In this context, the device country is typically determined by the user's billing address registered on their Google Play account.

To specify countries for your module, include the following in the feature module's manifest.

```xml
<dist:conditions>
   <!-- Set to "true" to specify countries to exclude from downloading
   this module at app install-time. By default, modules are available
   for download to all user countries. -->
  <dist:user-countries dist:exclude="true">
    <!-- Specifies the two-letter  CLDR country code for regions that should
    not download the module at app install-time. -->
    <dist:country dist:code="CN"/>
    <dist:country dist:code="HK"/>
  </dist:user-countries>
</dist:conditions>
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/conditional).
