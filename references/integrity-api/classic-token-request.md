```text
public abstract class IntegrityTokenRequest
```

---

Request for `IntegrityManager#requestIntegrityToken(IntegrityTokenRequest)`.

## Summary

### Nested types

| Entry |
| --- |
| `public abstract class` [`IntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder>)<br> Builder for [`IntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest>). |

### Public constructors

| Entry |
| --- |
| [`IntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest#IntegrityTokenRequest()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `static` [`IntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder>) | [`builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest#builder()>)`()`<br> Creates an integrity request builder. |
| `abstract` [`Long`](<https://developer.android.com/reference/java/lang/Long.html>) | [`cloudProjectNumber`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest#cloudProjectNumber()>)`()`<br> The cloud project number provided to the API. |
| `abstract` [`String`](<https://developer.android.com/reference/java/lang/String.html>) | [`nonce`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest#nonce()>)`()`<br> Nonce provided to the API. |

## Public constructors

### IntegrityTokenRequest

```text
public IntegrityTokenRequest()
```

## Public methods

### builder

```text
public static IntegrityTokenRequest.Builder builder()
```

Creates an integrity request builder.

### cloudProjectNumber

```text
public abstract Long cloudProjectNumber()
```

The cloud project number provided to the API.

See the details `Builder#setCloudProjectNumber(long)`.

### nonce

```text
public abstract String nonce()
```

Nonce provided to the API.

See the details `Builder#setNonce(String)`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest).
