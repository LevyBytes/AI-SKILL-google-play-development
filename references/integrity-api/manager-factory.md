```text
public class IntegrityManagerFactory
```

---

Creates instances of `IntegrityManager`.

## Summary

### Public methods

| Declaration | Description |
| --- | --- |
| `static` [`IntegrityManager`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager>) | [`create`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManagerFactory#create(android.content.Context)>)`(`[`Context`](<https://developer.android.com/reference/android/content/Context.html>) `applicationContext)`<br> Creates a Classic Integrity Manager. |
| `static` [`StandardIntegrityManager`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager>) | [`createStandard`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManagerFactory#createStandard(android.content.Context)>)`(`[`Context`](<https://developer.android.com/reference/android/content/Context.html>) `applicationContext)`<br> Creates a Standard Integrity Manager. |

## Public methods

### create

```text
public static IntegrityManager create(Context applicationContext)
```

Creates a Classic Integrity Manager.

### createStandard

```text
public static StandardIntegrityManager createStandard(Context applicationContext)
```

Creates a Standard Integrity Manager.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManagerFactory).
