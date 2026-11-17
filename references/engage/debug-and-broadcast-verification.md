This guide presents a step-by-step workflow for integrating the Engage SDK into your app.

## Shared resources

The following resources are available to assist with integration:

### Verification app

A [verification app](<https://developer.android.com/guide/playcore/engage/workflow?hl=en#lightbox-trigger>) used to verify content publishing in the UI.

### Content publishing guidelines

[Documentation](<https://developer.android.com/guide/playcore/engage/publish>) providing guidelines on how to effectively publish content using the APIs.

> **Note:** Download the latest version of the integration resources.

## Step 1: Develop with the SDK debug mode

Add the Engage SDK in the `build.gradle` file and follow the appropriate vertical-specific integration guide to complete your integration.

```groovy
dependencies {
    // Make sure you also include the repository in your project's
    // build.gradle file.
    implementation 'com.google.android.engage:engage-core:1.6.0'
}
```

## Step 2: Install the verification app

The verification app is an Android application that you can use to verify that the integration is working. The app includes capabilities to help developers verify data and broadcast intents.

## Step 3: Verify that data is visible in the verification app

The verification app should display each cluster as a separate row.

- Enter the name of the developer package that is publishing the data.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/workflow-data-1.png>)

**Figure 1**: Enter package name

- Verify that all entities in the cluster are published.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/workflow-data-2.png>)

**Figure 2**: Confirm all entities in the cluster are published

- Verify that all fields in the entity are published. For each item in the row, you can click the poster image to verify the intent.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/workflow-data-3.png>)

**Figure 3**: Verify entity fields and poster image

- Review the summaries for the app, cluster, and entity levels that indicate the count of validation errors. Review the validation error messages that appear in red beneath each relevant field. Validation errors occur when required fields are missing or have incorrect values.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/workflow-data-4.png>)

**Figure 4**: Validation error summary and details

- Verify that all validation errors have been resolved. Sample state:

![Image](<https://developer.android.com/static/images/guide/playcore/engage/workflow-data-5.png>)

**Figure 5**: Verify validation errors are resolved

## Step 4: Verify the broadcast intent flow

> **Note:** The verification app doesn't support testing broadcast intent with permission. You must remove permissions while testing and add them back before proceeding to [Step 6](<https://developer.android.com/guide/playcore/engage/workflow?hl=en#switch-to-prod>).

To verify the broadcast intent, click the button at the top of the UI to trigger the logic for sending broadcasts.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/workflow-intent.png>)

**Figure 6**: Verify broadcast intent

Once steps 1 through 4 are complete, you have finished testing the integration on your end.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/workflow).
