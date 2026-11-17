## Query user's billing configuration

[`getBillingConfigAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#getBillingConfigAsync(com.android.billingclient.api.GetBillingConfigParams,%20com.android.billingclient.api.BillingConfigResponseListener)>) provides the country the user uses for Google Play.

> **Note:** Don't store any data that `getBillingConfigAsync()` returns; this data is designed to be used only once and can change at any time. You may not use `getBillingConfigAsync()` data to create or enhance a user profile or to target or track customers for advertising or marketing purposes.

You can query the user's billing configuration after creating a [`BillingClient`](<https://developer.android.com/google/play/billing/integrate?hl=en#initialize>). The following code snippet describes how to make a call to `getBillingConfigAsync()`. Handle the response by implementing the `BillingConfigResponseListener`. This listener receives updates for all billing config queries initiated from your app.

If the returned `BillingResult` contains no errors, you can then check the `countryCode` field in the `BillingConfig` object to obtain the user's Play Country.

> **Note:** The country code format is based on ISO-3166-1 alpha2 (UN country codes). See the [Territory Containment table](<https://unicode.org/cldr/charts/latest/supplemental/territory_containment_un_m_49.html>) for more details.

**Kotlin**

```kotlin
// Use the default GetBillingConfigParams.
val getBillingConfigParams = GetBillingConfigParams.newBuilder().build()
billingClient.getBillingConfigAsync(
    getBillingConfigParams,
    object : BillingConfigResponseListener {
        override fun onBillingConfigResponse(
            billingResult: BillingResult,
            billingConfig: BillingConfig?
        ) {
            if (billingResult.responseCode == BillingResponseCode.OK &&
                billingConfig != null
            ) {
                val countryCode = billingConfig.countryCode
                // ...
            } else {
                // Handle errors
            }
        }
    }
)
```

**Java**

```java
GetBillingConfigParams getBillingConfigParams = GetBillingConfigParams.newBuilder().build();
billingClient.getBillingConfigAsync(
        getBillingConfigParams,
        (billingResult, billingConfig) -> {
            if (billingResult.getResponseCode() == BillingResponseCode.OK && billingConfig != null) {
                String countryCode = billingConfig.getCountryCode();
            } else {
                // TODO: Handle errors
            }
        });
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
