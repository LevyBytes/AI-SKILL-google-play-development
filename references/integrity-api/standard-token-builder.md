```text
public abstract class StandardIntegrityManager.StandardIntegrityTokenRequest.Builder
```

---

Builder for `StandardIntegrityTokenRequest`.

## Summary

### Public constructors

| Entry |
| --- |
| [`Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder#Builder()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`StandardIntegrityManager.StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>) | [`build`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder#build()>)`()`<br> Builds a [`StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>). |
| `abstract` [`StandardIntegrityManager.StandardIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder>) | [`setRequestHash`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder#setRequestHash(java.lang.String)>)`(`[`String`](<https://developer.android.com/reference/java/lang/String.html>) `value)`<br> A request hash to bind the integrity token to. |
| `abstract` [`StandardIntegrityManager.StandardIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder>) | [`setVerdictOptOut`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder#setVerdictOptOut(java.util.Set%3Cjava.lang.Integer%3E)>)`(`[`Set`](<https://developer.android.com/reference/java/util/Set.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`> value)`<br> A set of verdicts that should be opted out when requesting the token. |

## Public constructors

### Builder

```text
public Builder()
```

## Public methods

### build

```text
public abstract StandardIntegrityManager.StandardIntegrityTokenRequest build()
```

Builds a `StandardIntegrityTokenRequest`.

### setRequestHash

```text
public abstract StandardIntegrityManager.StandardIntegrityTokenRequest.Builder setRequestHash(String value)
```

A request hash to bind the integrity token to.

It is a recommended and not required field.

### setVerdictOptOut

```text
public abstract StandardIntegrityManager.StandardIntegrityTokenRequest.Builder setVerdictOptOut(Set<Integer> value)
```

A set of verdicts that should be opted out when requesting the token.

Any verdicts specified here will be unevaluated. See `StandardIntegrityVerdictOptOut` for the list of verdicts that can be opted out.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder).
