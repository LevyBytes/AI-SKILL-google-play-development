### Replacement examples and behaviors

Samwise subscribes to Country Gardener's text-only **Tier 1** for **$2 per month**. Halfway through a monthly billing period, he switches to the video-enabled annual **Tier 2** at **$36 per year**. The developer selects a replacement mode.

`WITH_TIME_PRORATION`

Tier 1 ends immediately. Its unused half-month is a $1 credit. In this worked example, that credit buys 10 days at the new annual rate. After those days, Samwise pays $36 and begins a new annual billing cycle; subsequent annual renewals also cost $36.

`CHARGE_PRORATED_PRICE`

This mode is available because Tier 2's price per time unit ($36/year = $3/month) exceeds Tier 1's $2/month. Tier 1 ends immediately. Its unused half-month contributes $1, while the remaining 15 days at the new rate cost $1.50. Samwise pays the $0.50 difference immediately. At the existing renewal boundary he pays $36, and subsequent annual renewals cost $36.

`WITHOUT_PRORATION`

Tier 2 becomes active immediately without an extra charge. Samwise pays $36 at the existing renewal boundary and $36 at each subsequent annual renewal.

For these three immediate replacements, the Billing Library delivers the successful purchase through the registered [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener). The new purchase is available through [`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)), and the backend immediately receives `SUBSCRIPTION_PURCHASED`.

`DEFERRED`

Tier 1 continues through its current paid period. Tier 2 takes effect at the next renewal, when Samwise pays $36.

The Billing Library reports the successful purchase through `PurchasesUpdatedListener`, the new purchase appears in `queryPurchasesAsync()`, and the backend immediately receives `SUBSCRIPTION_PURCHASED`. [Process and acknowledge the new purchase](https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto) at that point. Its `startTime` is populated when replacement becomes effective and the old subscription expires; the new plan then produces `SUBSCRIPTION_RENEWED`. See [deferred replacement](https://developer.android.com/google/play/billing/subscriptions?hl=en#handle-deferred-replacement) for the full contract.

`CHARGE_FULL_PRICE`

Tier 1 ends immediately. Tier 2 starts immediately and Samwise pays $36. His unused Tier 1 credit is $1, worth 1/36th of a year at the new rate (about 10 days). His next $36 charge is therefore one year and 10 days after the switch; subsequent renewals cost $36 each year.

Review the [replacement recommendations](https://developer.android.com/google/play/billing/subscriptions?hl=en#replacement-recommendations) before selecting a mode.

`KEEP_EXISTING`

Samwise has monthly Plan 1 at an introductory $2 per month for three months, followed by $4 per month. Halfway through its first monthly period, he adds Plan 2 at $3 per month while keeping Plan 1. His payment schedule is:

- An immediate prorated $1.50 for Plan 2.
- $5.00 per month for the next two months, covering Plan 1's introductory price and Plan 2's regular price.
- $7.00 per month thereafter.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
