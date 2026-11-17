The [program-specific client setup](user-choice-client-and-launch.md) establishes the connection and eligibility checks for this flow.

## Handle the user selection

How you handle the rest of the purchase flow differs depending on whether the user selected Google Play's billing system or an alternative billing system.

### When the user selects an alternative billing system

If the user chooses the alternative billing system, Google Play calls the `UserChoiceBillingListener` to notify the app that it needs to launch the purchase flow in the alternative billing system. In particular, the `userSelectedAlternativeBilling()` method is called.

The external transaction token provided in the `UserChoiceDetails` object represents a signature for the user's choice to enter the alternative billing flow. Use this token to report any transaction resulting from this choice as explained in the [backend integration guide](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

The `UserChoiceBillingListener` should perform the following actions:

- Get the product or products being purchased by the user so that they can be presented in the purchase flow in the alternative billing system.
- Collect the string received as the external transaction token and send it to your backend to persist it. This is used later to report the external transaction to Google Play if the user completes this specific purchase.
- Launch the developer's alternative purchase flow.

If the user completes the purchase using the alternative billing system, **you must report the transaction to Google Play by calling the Google Play Developer API from your backend within 24 hours**, providing the `externalTransactionToken` and additional transaction details. See the [backend integration guide](<https://developer.android.com/google/play/billing/outside-gpb-backend>) for more details.

The following example demonstrates how to implement the `UserChoiceBillingListener`:

> **Note:** In Play Billing Library 6.1 alternative billing was renamed to user choice billing to distinguish alternative billing with user choice from alternative billing only (i.e. without user choice). As a result, API and class names such as enableAlternativeBilling have been switched to enableUserChoiceBilling. APIs and classes with the old naming still exist for backwards compatibility and will be removed in a subsequent release.

**Kotlin**

```kotlin
private val userChoiceBillingListener =
    UserChoiceBillingListener { userChoiceDetails ->
        // Get the products being purchased by the user.
        val products = userChoiceDetails.products

        // Send external transaction token to developer backend server
        // this devBackend object is for demonstration purposes,
        // developers can implement this step however best fits their
        // app to backend communication.
        DevBackend.sendExternalTransactionStarted(
            userChoiceDetails.externalTransactionToken,
            user
        )

        // Launch alternative billing
        // ...
        // The developer backend handles reporting the transaction
        // to Google Play's backend once the alternative billing
        // purchase is completed.
    }
```

**Java**

```java
private userChoiceBillingListener userChoiceBillingListener = new UserChoiceBillingListener() {
    @Override
    public void userSelectedAlternativeBilling(
           UserChoiceDetails userChoiceDetails) {
       // Get the products being purchased by the user.
       List<Product> products =
              userChoiceDetails.getProducts();

       // Send external transaction token to developer backend server
       // this devBackend object is for demonstration purposes,
       // developers can implement this step however best fits their
       // app to backend communication.
       devBackend.sendExternalTransactionStarted(
              userChoiceDetails.getExternalTransactionToken(),
              user
       );

       // Launch alternative billing
       // ...
       // The developer backend handles reporting the transaction
       // to Google Play's backend once the alternative billing
       // purchase is completed.
    }
};
```

### When the user selects Google Play's billing system

If the user chooses Google Play's billing system, they continue with the purchase through Google Play.

- See [Processing purchases](<https://developer.android.com/google/play/billing/integrate#process>) in the library integration guide for more information about how to handle new in-app purchases through Google Play's billing system.
- See [New subscriptions](<https://developer.android.com/google/play/billing/subscriptions#new>) in the subscription management guide for additional guidance for subscription purchases.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app).
