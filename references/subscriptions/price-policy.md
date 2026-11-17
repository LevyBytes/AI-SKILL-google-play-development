You can change the prices of your subscription base plans and offers. For example, you might have digital products that need annual price adjustments, or you might change the set of benefits for a product and want to reflect these changes in the price.

For more information about changing subscription prices using the Play Console, see the documentation in the [Play Console Help Center](<https://support.google.com/googleplay/android-developer/answer/140504>).

To programmatically change the subscription base plan price, use the [`monetization.subscriptions.patch`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch>) method. This method receives a [`Subscription`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#resource:-subscription>) object with the subscription product configuration that is being changed. Set the new price in the [`RegionalBasePlanConfig`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#regionalbaseplanconfig>) object under the correct base plan in the subscription's `basePlans` collection. This can be very useful if you have a sizable catalog and you need to make updates to all of your products in a short period of time, or if you have a product catalog management system that automatically makes changes to your Google Play subscription products when changes occur.

> **Note:** Some regions are considered child territories of a parent region for billing purposes. While purchase-status APIs may return the specific `regionCode` of a child territory (e.g., **PR** for Puerto Rico), you must use the **parent region's code** (e.g., **US** for United States) when programmatically updating prices using the Google Play Developer API. Using a child territory code directly will result in an error indicating the region is not billable.

> **Warning:** You shouldn't change the price of a [Subscribe with Google](<https://developers.google.com/news/subscribe>) subscription.

You can visit your Play Console [change log](<https://support.google.com/googleplay/android-developer/answer/6053184>) to look up information about any price changes you have made in the past. The information you can find there includes when the prices were updated, who initiated the change, the regions that were updated, and more. This might assist you in cases where you need to review past price changes or review an accidental price change to assess next steps.

## Price changes for new subscription purchases

When you change the price of a base plan or offer, the new price takes effect within a few hours for all new purchases without you having to take any additional action.

## Price changes for existing subscribers

When you change subscription prices, existing subscribers are unaffected by default; they are placed into a legacy price cohort where they continue to pay their original base plan price when they renew.

If you choose to, you can move existing subscribers to the current base plan price. This action is called [ending a legacy price cohort](<https://developer.android.com/google/play/billing/price-changes?hl=en#end-legacy>). Changes to an offer's pricing phases cannot be applied to existing subscribers. For installment subscriptions, price changes for a legacy cohort happen at the end of the active commitment period. You cannot change the price currently being paid for a user who is in the middle of paying their installments.

## End a legacy price cohort

You can choose to end a legacy price cohort at any time. This can be done independently for each region. To end a legacy price through the Play Console, refer to the [Play Console Help Center](<https://support.google.com/googleplay/android-developer/answer/140504>).

### End a legacy price cohort with the Google Play Developer API

To programmaticaly end a legacy price cohort, use the [`monetization.subscriptions.basePlans.migratePrices`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans/migratePrices>) method. This method migrates subscribers who are receiving a historical subscription price to the current base plan price for the specified regions. The method also triggers price change notifications to be sent to users who are currently receiving a historical price older than the supplied timestamp. When you send this request, you include a list of [`RegionalPriceMigrationConfig`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans/migratePrices#regionalpricemigrationconfig>) objects in the request body to configure the price cohort migration.

For more information on using legacy price cohorts, see the [Play Console Help Center](<https://support.google.com/googleplay/android-developer/answer/140504>).

## Price decreases

When you end a legacy price cohort and the new purchase price is *lower* than the price that users in the cohort are paying, Google Play notifies the users by email and these subscribers begin paying the lower price the next time they pay for their base plan.

**Note:** [Payment authorization](<https://support.google.com/googleplay/answer/2476088>) may be placed up to 48 hours before the start of a user's next renewal period. However, for users in India or Brazil, this period extends to up to 5 days before the next renewal period. Users who have already been authorized at the higher price won't be immediately charged the lower price; they will renew at the lower price on their subsequent renewal.

[License testers](<https://developer.android.com/google/play/billing/test>) also receive email notifications for price decreases.

## Price increases

When ending a legacy price cohort and the new price is *higher* than the price that users in the cohort are paying, a price increase occurs. Price increases may or may not require user action.

By default, price increases are *opt-in* changes for existing subscribers. Users must explicitly accept the higher price before it is first charged, or Google Play automatically cancels their subscription. Users are charged the higher price the next time they pay for their base plan following an advance notification period of 37 days. Starting 30 days before this charge, Play notifies existing subscribers through email and push notifications.

During the first seven days after the cohort migration is triggered, no users receive notifications from Google Play. This means that you have seven days from when you initiate an opt-in price increase to notify your existing subscribers before Google Play begins notifying them directly. During this period, you can effectively cancel a pending price increase by making another price change back to the original price.

After that seven-day period, each user receives automatic notifications from Google Play 30 days before the first renewal with the new price.

In some cases when increasing prices for existing subscribers, you have the option to perform price increases with advance notification to users, but without requiring them to take any action. With this option, unless users *opt-out* by changing subscription plans or canceling their subscription, they'll be charged the new price the next time they pay for their base plan following an advance notification period. This period varies by country and is either 30 days or 60 days. Beginning that number of days before this charge, Play notifies existing subscribers through email and push notification.

Opt-out increases are only available in certain locations with limits on the increase amount and frequency, and are subject to certain developer requirements.

You can mark a legacy price cohort migration as an opt-out increase if it meets those criteria, as shown in figure 1.

![Google Play Console legacy price cohort migration with opt-out increase](<https://developer.android.com/static/images/google/play/billing/opt-out-increase.png>)

**Figure 1.** Using Play Console to specify a legacy price cohort migration as an opt-out increase.

![Google Play Console legacy price cohort migration with opt-out increase](<https://developer.android.com/static/images/google/play/billing/opt-out-increase.png>)

## Communicate your price change to the user

> **Important:** This notice must be displayed on all device types where the app is available, including mobile, TV platforms, and streaming devices. The sole exception is watch devices, for which the notice is recommended but not required.

You should notify existing subscribers whenever you end their legacy price cohort.

For opt-out price increases, you should give users advance notification, and you must show users an in-app notice. Unlike opt-in price increases, there is no seven-day waiting period before Play starts notifying users directly.

For opt-in price increases, give users advance notification and inform them of the need to accept the price increase. When you initiate an opt-in price increase, you have seven days to notify your existing subscribers before Google Play begins to notify them directly. We recommend that you notify affected users in your app and provide a deep link to the Play Store subscription screen to help them review the new price. When users review an opt-in price increase on the Play Store subscription screen, a dialog similar to figure 2 is shown.

![Generic dialog notifying the user of a subscription price change](<https://developer.android.com/static/images/google/play/billing/price-change-1.png>)

**Figure 2.** Example dialog notifying the user of a subscription price change.

## Handle user response to an opt-in price change

After you have notified existing subscribers of a price change and it's an opt-in increase, they may take action before the new price applies to accept or not accept the price increase. If they do, you will receive an RTDN informing you of the outcome. See the [purchase lifecycle guidance](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-changes>) to learn how to handle these notifications.

To notify users of an upcoming opt-in price increase, you can use the [in-app messaging](<https://developer.android.com/google/play/billing/subscriptions#in-app-messaging>) feature. This lets users to confirm the price increase without leaving the app. The message for an outstanding opt-in price increase is shown starting on the first day the user can accept the price increase, and the message is shown a maximum of once every 7 days.

If the user doesn't act and they reach the first renewal that the opt-in price will apply to, their subscription is automatically canceled and expired on that renewal date.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/price-changes).
