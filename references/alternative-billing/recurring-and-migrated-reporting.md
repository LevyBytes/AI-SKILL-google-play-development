### Report subsequent transactions for a purchase

In some cases, there is more than one user payment associated with the same external purchase, for example subscription renewals or prepaid plan top-ups. You can report these subsequent transactions by using the same API in `Externaltransactions`. As described in [Report a new purchase](<https://developer.android.com/google/play/billing/outside-gpb-backend?hl=en#report-new>), the `externalTransactionToken` isn't necessary for subsequent transactions. Instead, a new unique `externalTransactionId` is sent as the query parameter for each renewal or top-up transaction, with the ID of the initial transaction included in the `initialExternalTransactionId` field.

**Following the previous example**:

1. User 1's first renewal occurs on the alternative billing system. The initial transaction ID was *123-456-789*.
2. The developer reports the transaction recurrence in the URL query parameter as the external transaction ID for this new transaction, while referencing the external transaction ID of the initial transaction in the `initialExternalTransactionId` field.

**Example request**:

[Complete text example: Report subsequent transactions for a purchase](<https://developer.android.com/google/play/billing/outside-gpb-backend#report-subsequent>).

### Report an upgrade or downgrade

To report an upgrade or a downgrade when the user owns a subscription in the alternative billing system you use the same endpoint and function in the `Externaltransactions` API, sending the `externalTransactionToken` that was provided to the app for the upgrade or downgrade transaction. This works similarly to [reporting a new purchase](<https://developer.android.com/google/play/billing/outside-gpb-backend?hl=en#report-new>).

### Report an app download

To report an app install in the external offers billing system, you must call `Externaltransactions.createexternaltransaction`, sending the `externalTransactionToken` that was provided to the app. Report this as a zero-cost, one-time transaction; this process is similar to reporting an [initial transaction](<https://developer.android.com/google/play/billing/outside-gpb-backend?hl=en#report-new>). Be sure to include [`ExternalOfferDetails`](<https://developer.android.com/google/play/billing/outside-gpb-backend?hl=en#external-offer-details>) in the request body.

**Example request**:

[Complete text example: Report an app download](<https://developer.android.com/google/play/billing/outside-gpb-backend#report-app-download>).

### Migrate from manual reporting of alternative billing transactions

> **Note:** Manual reporting of alternative billing only and user choice billing is being discontinued. For more details about migration deadlines, see [Understanding user choice billing on Google Play](<https://support.google.com/googleplay/android-developer/answer/13821247>). Be sure to migrate all active subscriptions that started while you were offering alternative billing without automated reporting through the `externaltransactions` API before manual reporting is disabled.

To migrate active subscriptions that started while you were offering alternative billing without automated reporting, create a new zero-cost transaction using the `migratedTransactionProgram` field instead of specifying an `initialExternalTransactionId` or `externalTransactionToken`. Set the `transactionTime` to the time when the user initially signed up for each active subscription. Afterwards, report each subsequent transaction for these subscriptions as normal through the APIs, providing the `initialExternalTransactionId` used earlier to create the renewal transactions. Once the subscription is migrated, you will no longer need to manually report the subsequent transactions for the subscription, provided they are being reported through the automated methods described in [transaction reporting](transaction-reporting.md).

While migrating subscriptions, be mindful of the [quota limits](<https://developer.android.com/google/play/billing/alternative/backend#api-quotas>) in place to verify the migration does not cause a quota outage. If many subscriptions need to be migrated, spread them out across multiple days or [request for an increase in quota](<https://support.google.com/googleplay/android-developer/contact/apiqr>).

> **Note:** Only developers who have offered alternative billing without automated reporting will be able to set the `migratedTransactionProgram` field. If you previously offered alternative billing without automation and are getting an error when attempting to make a request to migrate the subscription, you can [contact our support team](<https://support.google.com/googleplay/android-developer/contact/additional_billing_system_q>) for help.

The `migratedTransactionProgram` field can only be used when migrating from manual reporting. It will be deprecated when manual reporting is no longer supported.

**Example request**:

[Complete text example: Migrate from manual reporting of alternative billing transactions](<https://developer.android.com/google/play/billing/outside-gpb-backend#migrating-manual>).

### Requirements for Play partner programs

Developers participating in partner programs such as the [Play Media Experience Program](<https://google.play/business/programs/mediaprogram/>) must provide the [`transaction_program_code`](<https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions>) when reporting external transactions. If you are an eligible developer, contact your Business Development Manager for more information on how to set this field.

## Report purchase refunds to Google Play

Integrate with the `externaltransactions` API to report transactions refunded to users outside Google Play's billing system. For Play to correctly identify which transaction has been refunded, you should include the corresponding `externalTransactionId` for the previously reported transaction as part of the URL parameters.

When reporting refunds of subscription purchases, reference the `externalTransactionId` of the specific recurrence of the subscription that is being refunded.

**Example**: Suppose a subscription has the following transactions:

- An initial transaction with external transaction ID *ABC.1234-5678-9012-34567*
- The first recurring transaction with external transaction ID *ABC.1234-5678-9012-34567..0*
- The second recurring transaction with external transaction ID *ABC.1234-5678-9012-34567..1*

To report a refund of all transactions for the subscription, you need to make three separate refund requests: one for the initial transaction and two for the subsequent transactions.

This method accepts both [full refunds](<https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction#fullrefund>) (where the amount is the same amount that the user paid in the original external transaction) and [partial refunds](<https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction#partialrefund>) (where the amount is smaller than what the user paid in the original external transaction). For partial refunds, you need to specify the pre-tax amount that was refunded.

## API quotas

The `Externaltransactions` API is subject to [API quotas](<https://developers.google.com/android-publisher/quotas>) for all calls, just like any other endpoint in the Google Play Developer API.

Additionally, the `Externaltransactions` API has a 1,200 Queries Per Minute (QPM) limit on calls to `Externaltransactions.createexternaltransaction` or `Externaltransactions.refundexternaltransaction`. Calls to `Externaltransactions.getexternaltransaction` don't count toward this 1,200 QPM limit.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/outside-gpb-backend).
