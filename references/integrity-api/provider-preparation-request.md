```text
public abstract class StandardIntegrityManager.PrepareIntegrityTokenRequest
```

---

Request for `prepareIntegrityToken`.

## Summary

### Nested types

| Entry |
| --- |
| `public abstract class` [`StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder>)<br> Builder for [`PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>). |

### Public constructors

| Entry |
| --- |
| [`PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest#PrepareIntegrityTokenRequest()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `static` [`StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder>) | [`builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest#builder()>)`()`<br> Creates [`PrepareIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder>). |
| `abstract long` | [`cloudProjectNumber`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest#cloudProjectNumber()>)`()`<br> The cloud project number provided to the API. |
| `abstract int` | [`webViewRequestMode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest#webViewRequestMode()>)`()`<br> The WebView request mode provided to the API. |

## Public constructors

### PrepareIntegrityTokenRequest

```text
public PrepareIntegrityTokenRequest()
```

## Public methods

### builder

```text
public static StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder builder()
```

Creates `PrepareIntegrityTokenRequest.Builder`.

### cloudProjectNumber

```text
public abstract long cloudProjectNumber()
```

The cloud project number provided to the API.

See the details `Builder#setCloudProjectNumber(long)`.

### webViewRequestMode

```text
public abstract int webViewRequestMode()
```

The WebView request mode provided to the API.

See the details `Builder#setWebViewRequestMode(int)`.

This parameter is only used for advanced system use cases and must be left unspecified by app, game, or SDK developers.

Since 1.6.0

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest).
