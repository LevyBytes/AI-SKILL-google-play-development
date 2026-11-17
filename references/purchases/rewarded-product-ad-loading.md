## Load video ads

Before showing your user an option to watch a video ad in order to receive a rewarded product, you need to load the video. To do so, create a `RewardLoadParams` object, associating it with the `SkuDetails` object that represents the rewarded product. Then, call your billing client's `loadRewardedSku()` method, passing in the `RewardLoadParams` object and a `RewardResponseListener` object.

> **Note:** Video ads associated with rewarded products aren't always available for loading. Also, depending on the user's bandwidth, available videos could take some time to load.

The `RewardResponseListener` listener is notified when the video has finished loading. The listener is also notified if the video is unavailable or if another error, such as a server timeout, occurs.

To maintain device performance when loading the videos associated with your app's rewarded products, keep the following best practices in mind:

- Load at most three rewarded product SKUs at a time.
- Attempt to load the videos whenever the user enters your app. This step helps you check whether the videos are still loaded and available.
- When deciding when to load the videos, choose the balance between bandwidth usage and app responsiveness that works best for your use case:

  - At the earliest, load the videos after you call `getSkuDetails()` for the associated rewarded product. Your app remains very responsive, but you might waste network data loading a video that the user never watches.
  - At the latest, load the video when the user navigates to the page where the video is to be displayed. Your app rarely wastes bandwidth in this case, but the user might have to wait a few moments before the button for watching the video becomes clickable.

The following code snippet demonstrates the process for loading a video ad that plays before the user receives the rewarded product:

**Kotlin**

```kotlin
if (skuDetails.isRewarded()) {
    val params = RewardLoadParams.Builder()
            .setSkuDetails(skuDetails)
            .build()
    mBillingClient.loadRewardedSku(params.build(),
            object : RewardResponseListener {
        override fun onRewardResponse(@BillingResponse responseCode : Int) {
            if (responseCode == BillingResponse.OK) {
                // Enable the reward product, or make
                // any necessary updates to the UI.
            }
        }
    })
}
```

**Java**

```java
if (skuDetails.isRewarded()) {
    RewardLoadParams.Builder params = RewardLoadParams.newBuilder();
    params.setSkuDetails(skuDetails);
    mBillingClient.loadRewardedSku(params.build(),
        new RewardResponseListener() {
            @Override
            public void onRewardResponse(int responseCode) {
                if (responseCode == BillingResponse.OK) {
                      // Enable the reward product, or make
                      // any necessary updates to the UI.
                  }
            }
        });
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billing_rewarded_products).
