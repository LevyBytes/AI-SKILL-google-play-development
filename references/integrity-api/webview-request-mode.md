```text
public annotation StandardIntegrityWebViewRequestMode
```

---

Request mode for WebView for Standard Integrity API.

The WebView request mode is only used for advanced system use cases and must be left unspecified by app, game, or SDK developers.

Since 1.6.0

## Summary

### Constants

| Declaration | Description |
| --- | --- |
| `static final int` | [`UNSPECIFIED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityWebViewRequestMode#UNSPECIFIED()>) `= 0`<br> WebView request mode not set. |
| `static final int` | [`WITHOUT_APP_BINDING`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityWebViewRequestMode#WITHOUT_APP_BINDING()>) `= 2`<br> Standard API WebView request mode to return only device integrity verdicts in the final token. |
| `static final int` | [`WITH_APP_BINDING`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityWebViewRequestMode#WITH_APP_BINDING()>) `= 1`<br> Standard API WebView request mode to return device and application integrity verdicts in the final token. |

## Constants

### UNSPECIFIED

```text
public static final int UNSPECIFIED = 0
```

WebView request mode not set. Default value.

Since 1.6.0

### WITHOUT_APP_BINDING

```text
public static final int WITHOUT_APP_BINDING = 2
```

Standard API WebView request mode to return only device integrity verdicts in the final token.

This mode should be used when the application has opted out of providing its identity to the caller.

The WebView request mode is only used for advanced system use cases and must be left unspecified by app, game, or SDK developers.

Since 1.6.0

### WITH_APP_BINDING

```text
public static final int WITH_APP_BINDING = 1
```

Standard API WebView request mode to return device and application integrity verdicts in the final token.

This mode should be used when the application agreed to provide its identity to the caller.

The WebView request mode is only used for advanced system use cases and must be left unspecified by app, game, or SDK developers.

Since 1.6.0

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityWebViewRequestMode).
