The developer renders the choice screen and alternative payment happens inside the app (Scenario 1B). The connected flow includes [setup and eligibility](choice-developer-in-app-setup.md), [choice-screen information](choice-developer-in-app-ui.md), [reporting token and purchase handling](choice-developer-in-app-reporting.md).

#### Subscription replacement in Scenario 1B

In this scenario, a new external transaction token must be generated. The only difference from a normal purchase is that, in this scenario, user choice is preserved, and you don't have to show the choice screen for upgrade or downgrade. However you must show the one-time information dialog and the parental acknowledgement.

For sample integration code, see [step 4 in Scenario 1B: Developer renders the choice screen and the alternate billing is handled within your app](<https://developer.android.com/google/play/billing/billingchoice/integration?hl=en#scenario-1b>).

When the upgrade or downgrade is complete, you need to [report a new transaction](<https://developer.android.com/google/play/billing/alternative#report-new>) using the external transaction token obtained through the previous call for the new subscription purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
