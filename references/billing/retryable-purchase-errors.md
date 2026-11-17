### [SERVICE_UNAVAILABLE](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE>) (Error Code 2)

#### Important Note:

Starting in Google Play Billing Library 6.0.0, `SERVICE_UNAVAILABLE` is no longer returned for network issues. It is returned when the billing service is unavailable and the deprecated `SERVICE_TIMEOUT` case scenarios.

#### Problem

This transient error indicates the Google Play Billing service is currently unavailable. In most cases, this means there is a network connection issue anywhere between the client device and Google Play Billing services.

#### Possible resolution

This is usually a transient issue. Retry the request using either a simple or exponential backoff strategy, depending on which action returned the error.

Unlike [`SERVICE_DISCONNECTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED>), the connection to the Google Play Billing service is not severed, and you need to retry whatever operation is being attempted.

### [BILLING_UNAVAILABLE](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#BILLING_UNAVAILABLE>) (Error Code 3)

#### Problem

This error indicates that a user billing error occurred during the purchase process. Examples of when this can occur include:

- The Play Store app on the user's device is out of date.
- The user is in an unsupported country.
- The user is an enterprise user, and their enterprise admin has disabled users from making purchases.
- Google Play is unable to charge the user's payment method. For example, the user's credit card might have expired.
- The Play Store app is blocked by the system (for example, in an OEM-customized kids mode). In this case, the `BillingResult` includes the *Play Store is blocked* debug message.

#### Possible resolution

- Automatic retries are unlikely to help in this case. However, a manual retry can help if the user addresses the condition that caused the issue. For example, if the user updates their Play Store version to a supported version, then a manual retry of the initial operation could work.
- If this error occurs when the user is not in session, retrying might not make sense. When you receive a [`BILLING_UNAVAILABLE`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#BILLING_UNAVAILABLE>) error as a result of the purchase flow, it's very likely the user received feedback from Google Play during the purchase process and might be aware of what went wrong. In this case, you could show an error message specifying something went wrong and offer a **Try again** button to give the user the option of a manual retry after they address the issue.

### [ERROR](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ERROR>) (Error Code 6)

#### Problem

This is a fatal error that indicates an internal problem with Google Play itself.

#### Possible resolution

Sometimes internal Google Play problems that lead to [`ERROR`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ERROR>) are transient, and a retry with an exponential backoff can be implemented for mitigation. When users are in session, a simple retry is preferable.

### [ITEM_ALREADY_OWNED](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_ALREADY_OWNED>)

#### Problem

This response indicates that the Google Play user already owns the subscription or one-time purchase product they are attempting to purchase. In most cases, this is not a transient error, except when it is caused by a stale Google Play's cache.

#### Possible resolution

To avoid this error happening when the cause is not a cache issue, don't offer a product for purchase when the user already owns it. Make sure you check the user's entitlements when you show the products available for purchase, and filter what the user can purchase accordingly. When the client app receives this error due to a cache issue, the error triggers Google Play's cache to get updated with the latest data from Play's backend. Retrying after the error should resolve this specific transient instance in this case. Call [`BillingClient.queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) after getting an [`ITEM_ALREADY_OWNED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_ALREADY_OWNED>) to check if the user has acquired the product, and if it's not the case implement a simple retry logic to reattempt the purchase.

### [ITEM_NOT_OWNED](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_NOT_OWNED>)

#### Problem

This purchase response indicates that the Google Play user does not own the subscription or one-time purchase product the user is attempting to replace, acknowledge or consume. This is not a transient error in most cases except when it is caused by Google Play's cache getting into a stale state.

#### Possible resolution

When the error is received because of a cache issue, the error triggers Google Play's cache to get updated with the latest data from Play's backend. Retrying with a simple retry strategy after the error should resolve this specific transient instance. Call [`BillingClient.queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) after getting an [`ITEM_NOT_OWNED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_NOT_OWNED>) to check if the user has acquired the product. If they have not, use simple retry logic to reattempt the purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/errors).
