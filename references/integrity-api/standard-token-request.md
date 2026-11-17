```text
public abstract class StandardIntegrityManager.StandardIntegrityTokenRequest
```

---

Request for `StandardIntegrityTokenProvider#request(StandardIntegrityTokenRequest)`.

## Summary

### Nested types

| Entry |
| --- |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder>)<br> Builder for [`StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>). |

### Public constructors

| Entry |
| --- |
| [`StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest#StandardIntegrityTokenRequest()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `static` [`StandardIntegrityManager.StandardIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder>) | [`builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest#builder()>)`()`<br> Creates [`StandardIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder>). |
| `abstract` [`String`](<https://developer.android.com/reference/java/lang/String.html>) | [`requestHash`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest#requestHash()>)`()`<br> The request hash provided to the API. |
| `abstract` [`Set`](<https://developer.android.com/reference/java/util/Set.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | [`verdictOptOut`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest#verdictOptOut()>)`()`<br> Set of integrity token verdicts that should be opted-out. |

## Public constructors

### StandardIntegrityTokenRequest

```text
public StandardIntegrityTokenRequest()
```

## Public methods

### builder

```text
public static StandardIntegrityManager.StandardIntegrityTokenRequest.Builder builder()
```

Creates `StandardIntegrityTokenRequest.Builder`.

### requestHash

```text
public abstract String requestHash()
```

The request hash provided to the API.

See the details `Builder#setRequestHash(String)`.

### verdictOptOut

```text
public abstract Set<Integer> verdictOptOut()
```

Set of integrity token verdicts that should be opted-out.

See the details `Builder#setVerdictOptOut(Set)`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest).
