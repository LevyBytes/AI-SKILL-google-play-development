The [program-specific client setup](alternative-only-client-setup.md) establishes the connection and eligibility checks for this flow.

## Information dialog for users

> **Note:** See response handling section for instructions on how to handle errors from this API.

> **Note:** If you are offering alternative billing only through alternative billing APIs, the user experience requirements will be met by integrating with and using the client-side APIs. You will not need to separately follow the [interim user experience guidelines](<https://developer.android.com/google/play/billing/alternative/interim-ux/alt-billing>).

To integrate with alternative billing only, your eligible app must show an information screen which helps users understand that billing will not be managed by Google Play. The information screen must be shown to users by calling the [`showAlternativeBillingOnlyInformationDialog`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showAlternativeBillingOnlyInformationDialog(android.app.Activity,%20com.android.billingclient.api.AlternativeBillingOnlyInformationDialogListener)>) API before starting the alternative billing flow each time. If the user has already acknowledged the dialog, using this API will typically not result in the dialog being shown again. There may be times when the dialog is shown again to a user in situations such as if the user clears caches on their device.

**Kotlin**

```kotlin
// An activity reference from which the alternative billing only information
// dialog will be launched.
val activity: Activity = this.activity

val listener: AlternativeBillingOnlyInformationDialogListener =
    AlternativeBillingOnlyInformationDialogListener { billingResult ->
        // check billingResult
    }

val billingResult =
    billingClient.showAlternativeBillingOnlyInformationDialog(
        activity,
        listener
    )
```

**Java**

```java

// An activity reference from which the alternative billing only information
// dialog will be launched.
Activity activity = ...;

AlternativeBillingOnlyInformationDialogListener listener =
    new AlternativeBillingOnlyInformationDialogListener() {
        @Override
        public void onAlternativeBillingOnlyInformationDialogResponse(
            BillingResult billingResult) {
                // check billingResult
            }
    };

BillingResult billingResult =
    billingClient.showAlternativeBillingOnlyInformationDialog(activity,
        listener);
```

If this method returns [BillingResponseCode.OK](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK>) then your app can proceed with the transaction. In the case of [BillingResponseCode.USER_CANCELED](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED>) your app should call showAlternativeBillingOnlyInformationDialog to show the dialog to the user again. For other response codes see the [response handling section](<https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app?hl=en#response-handling>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app).
