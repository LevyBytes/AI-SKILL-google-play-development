#### New way to query available products

Arguments for [`queryPurchaseHistoryAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.html#queryPurchaseHistoryAsync(java.lang.String,%0Acom.android.billingclient.api.PurchaseHistoryResponseListener)>) and [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.html#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%0Acom.android.billingclient.api.SkuDetailsResponseListener)>) methods were wrapped into a Builder pattern:

**Kotlin**

```kotlin
val params = SkuDetailsParams.newBuilder()
params.setSkusList(skuList)
        .setType(itemType)
billingClient.querySkuDetailsAsync(params.build(), object : SkuDetailsResponseListener() {
    ...
})
```

**Java**

```java
SkuDetailsParams.Builder params = SkuDetailsParams.newBuilder();
params.setSkusList(skuList)
        .setType(itemType);
billingClient.querySkuDetailsAsync(params.build(), new SkuDetailsResponseListener() {...})
```

The result is now returned via result code and a list of [`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails.html>) objects instead of previous wrapper class for your convenience and to be consistent across our API:

**Kotlin**

```kotlin
fun onSkuDetailsResponse(@BillingResponse responseCode: Int, skuDetailsList: List<SkuDetails>)
```

**Java**

```java
public void onSkuDetailsResponse(@BillingResponse int responseCode, List<SkuDetails> skuDetailsList)
```

#### Parameters order changed on `onConsumeResponse()` method

The order of arguments for [`onConsumeResponse`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeResponseListener#onConsumeResponse(com.android.billingclient.api.BillingResult,java.lang.String)>) from the [`ConsumeResponseListener`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeResponseListener.html>) interface has changed to be consistent across our API:

**Kotlin**

```kotlin
fun onConsumeResponse(@BillingResponse responseCode: Int, outToken: String)
```

**Java**

```java
public void onConsumeResponse(@BillingResponse int responseCode, String outToken)
```

#### Unwrapped PurchaseResult object

[`PurchaseResult`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchasesResult.html>) has been unwraped to be consistent across our API:

**Kotlin**

```kotlin
fun onPurchaseHistoryResponse(@BillingResponse responseCode: Int, purchasesList: List<Purchase>)
```

**Java**

```java
void onPurchaseHistoryResponse(@BillingResponse int responseCode, List<Purchase> purchasesList)
```

### Bug fixes

- [No response code in PURCHASES_UPDATED Bundle](<https://issuetracker.google.com/issues/64075043>)
- [Fix ProxyBillingActivity and PurchasesUpdatedListener issues during device rotation](<https://issuetracker.google.com/issues/63266562>)

## Developer Preview 1 Release

Developer preview launched, aimed to simplify the development process when it comes to billing, allowing developers to focus their efforts on implementing logic specific to the Android app, such as application architecture and navigation structure.

The library includes several convenient classes and features for you to use when integrating your Android apps with the Google Play Billing API. The library also provides an abstraction layer on top of the Android Interface Definition Language (AIDL) service, making it easier for developers to define the interface between the app and the Google Play Billing API.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
