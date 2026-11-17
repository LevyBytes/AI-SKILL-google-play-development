When a Play Billing Library call triggers an action, the library returns a [`BillingResult`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) response to inform developers of the outcome. For example, if you use [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) to get the available offers for the user, the response code either contains an OK code and provides the right [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object, or it contains a different response that indicates the reason why the [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object couldn't be provided.

Not all response codes are errors. The [`BillingResponseCode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode>) reference page provides a detailed description of each of the responses discussed in this guide. Some examples of response codes that don't indicate errors are:

- [`BillingClient.BillingResponseCode.OK`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK>) : the action triggered by the call was completed successfully.
- [`BillingClient.BillingResponseCode.USER_CANCELED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED>) : for actions that display Play Store UI flows to the user, this response indicates the user navigated away from those UI flows without completing the process.

When the response code does indicate an error, the cause is sometimes due to transient conditions, and thus recovery is possible. When a call to a Play Billing Library method returns a [`BillingResponseCode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode>) value that indicates a recoverable condition, you should retry the call. In other cases, conditions are not considered transient and therefore a retry is not recommended.

Transient errors call for different retry strategies depending on factors like whether the error happens when users are in session (for example, when a user is going through a purchase flow) or the error happens in the background (for example, when you're querying the user's existing purchases during [`onResume`](<https://developer.android.com/reference/android/app/Activity#onResume()>)). The [retry strategies](<https://developer.android.com/google/play/billing/errors?hl=en#retry_strategies>) section provides examples of these different strategies, and the section on [`BillingResult`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) [responses you can retry](<https://developer.android.com/google/play/billing/errors?hl=en#retriable_billingresult_responses>) recommends which strategy works best for each response code.

In addition to the response code, some error responses include messages for debugging and logging purposes.

> **Tip:** Before you deploy your app to the production environment, you can test how your app handles the various BillingResult response error codes by using the Response Simulator. For more information, see [Test BillingResult response codes](<https://developer.android.com/google/play/billing/test-response-codes>).

## Retry strategies

### Simple retry

In situations where the user is in session, it's better to implement a simple retry strategy so that the error disrupts the user experience as little as possible. In that case, we recommend a simple retry strategy with a maximum number of attempts as an exit condition.

The following example demonstrates a simple retry strategy to handle an error when establishing a [`BillingClient`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>) connection:

[Complete kotlin example: Simple retry](<https://developer.android.com/google/play/billing/errors#simple_retry>).

### Exponential backoff retry

We recommend using exponential backoff for Play Billing Library operations that happen in the background and don't affect the user experience while the user is in session.

For example, it would be appropriate to implement this when acknowledging new purchases because this operation can happen in the background, and acknowledgment doesn't need to happen in real time if an error occurs.

[Complete kotlin example: Exponential backoff retry](<https://developer.android.com/google/play/billing/errors#exponential_backoff_retry>).

## BillingResult responses you can retry

### [NETWORK_ERROR](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#NETWORK_ERROR>) (Error Code 12)

> **Note:** This error is only returned in Google Play Billing Library 6 and up. Previous versions are not supported.

#### Problem

This error indicates that there was a problem with the network connection between the device and Play systems.

#### Possible resolution

To recover, use simple retries or exponential backoff, depending on which action triggered the error.

### [SERVICE_TIMEOUT](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT>) (Error Code -3)

> **Note:** This error is only returned in Google Play Billing Library 5.2.0 and earlier. Starting with Google Play Billing 6.0.0, [SERVICE_UNAVAILABLE](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE>) is returned for the problem described below, and `SERVICE_TIMEOUT` is deprecated.

#### Problem

This error indicates that the request has reached the maximum timeout before Google Play is able to respond. This could be caused, for example, by a delay in the execution of the action requested by the Play Billing Library call.

#### Possible resolution

This is usually a transient issue. Retry the request using either a simple or exponential backoff strategy, depending on which action returned the error.

Unlike [`SERVICE_DISCONNECTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED>), the connection to the Google Play Billing service is not severed, and you only need to retry whatever Play Billing Library operation was attempted.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/errors).
