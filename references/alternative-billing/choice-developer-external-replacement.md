The developer renders the choice screen and alternative payment happens outside the app (Scenario 2B). The connected flow includes [setup and eligibility](choice-developer-external-setup.md), [choice-screen information](choice-developer-external-ui.md), [reporting token](choice-developer-external-reporting.md), [external purchase](choice-developer-external-purchase.md).

#### Subscription replacement in Scenario 2B

The steps to handle subscription replacement in this scenario are similar to the steps described in **Subscription replacement in Scenario 2A**. The only difference is that after generating the transaction token, instead of calling the [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) method, you must call the launchExternalLink to show the linkout disclaimer dialog. In this scenario, user choice is preserved, and you don't have to show the choice screen for upgrade or downgrade.

For sample integration code, see [step 6 in Scenario 2B: Developer renders the choice screen and the alternate billing is handled within your app](<https://developer.android.com/google/play/billing/billingchoice/integration?hl=en#scenario-2b>).

When the upgrade or downgrade is complete, you need to [report a new transaction](<https://developer.android.com/google/play/billing/outside-gpb-backend>) using the external transaction token obtained through the previous call for the new subscription purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
