**Kotlin**

```kotlin
val environmentDetails =
    JSONObject(payload).getJSONObject("environmentDetails")
val appAccessRiskVerdict =
    environmentDetails.getJSONObject("appAccessRiskVerdict")

if (appAccessRiskVerdict.has("appsDetected")) {
    val appsDetected = appAccessRiskVerdict.getJSONArray("appsDetected").toString()
    if (!appsDetected.contains("CAPTURING") && !appsDetected.contains("CONTROLLING")) {
        // Looks good!
    }
}
```

**Java**

```java
JSONObject environmentDetails =
    new JSONObject(payload).getJSONObject("environmentDetails");
JSONObject appAccessRiskVerdict =
    environmentDetails.getJSONObject("appAccessRiskVerdict");

if (appAccessRiskVerdict.has("appsDetected")) {
    String appsDetected = appAccessRiskVerdict.getJSONArray("appsDetected").toString()
    if (!appsDetected.contains("CAPTURING") && !appsDetected.contains("CONTROLLING")) {
        // Looks good!
    }
}
```

##### Remediate app access risk verdicts

Depending on your risk level, you can decide what app access risk verdicts you want to take action on before letting the user complete a request or action. There are optional Google Play prompts you can show to the user after checking the app access risk verdict. You can show [CLOSE_UNKNOWN_ACCESS_RISK](<https://developer.android.com/google/play/integrity/remediation#close-unknown-access-risk-dialog>) to ask the user to close unknown apps causing the app access risk verdict or you can show [CLOSE_ALL_ACCESS_RISK](<https://developer.android.com/google/play/integrity/remediation#close-all-access-risk-dialog>) to ask the user to close all apps (known and unknown) causing the app access risk verdict.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
