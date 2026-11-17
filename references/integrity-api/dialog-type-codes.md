```text
public annotation IntegrityDialogTypeCode
```

---

Dialog type codes for Integrity API.

## Summary

### Constants

| Declaration | Description |
| --- | --- |
| `static final int` | [`CLOSE_ALL_ACCESS_RISK`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#CLOSE_ALL_ACCESS_RISK()>) `= 3`<br> A dialog prompting users to close all apps which can capture or control the user screen. |
| `static final int` | [`CLOSE_UNKNOWN_ACCESS_RISK`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#CLOSE_UNKNOWN_ACCESS_RISK()>) `= 2`<br> A dialog prompting users to close unknown apps which can capture or control the user screen. |
| `static final int` | [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_INTEGRITY()>) `= 4`<br> A dialog that guides users to achieve a MEETS_DEVICE_INTEGRITY verdict and obtain legitimate app access via the Play Store (e.g., by purchasing or installing) when applicable. |
| `static final int` | [`GET_LICENSED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_LICENSED()>) `= 1`<br> A dialog prompting users to acquire or buy a license for the app from Google Play. |
| `static final int` | [`GET_STRONG_INTEGRITY`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_STRONG_INTEGRITY()>) `= 5`<br> A dialog that guides users to achieve a MEETS_STRONG_INTEGRITY verdict, obtain legitimate app access via the Play Store (e.g., by purchasing or installing), and fix Play Protect issues when applicable. |

## Constants

### CLOSE_ALL_ACCESS_RISK

```text
public static final int CLOSE_ALL_ACCESS_RISK = 3
```

A dialog prompting users to close all apps which can capture or control the user screen.

### CLOSE_UNKNOWN_ACCESS_RISK

```text
public static final int CLOSE_UNKNOWN_ACCESS_RISK = 2
```

A dialog prompting users to close unknown apps which can capture or control the user screen.

### GET_INTEGRITY

```text
public static final int GET_INTEGRITY = 4
```

A dialog that guides users to achieve a MEETS_DEVICE_INTEGRITY verdict and obtain legitimate app access via the Play Store (e.g., by purchasing or installing) when applicable. It can also be used in resolving user-remediable client-side errors.

Since 1.5.0

### GET_LICENSED

```text
public static final int GET_LICENSED = 1
```

A dialog prompting users to acquire or buy a license for the app from Google Play.

### GET_STRONG_INTEGRITY

```text
public static final int GET_STRONG_INTEGRITY = 5
```

A dialog that guides users to achieve a MEETS_STRONG_INTEGRITY verdict, obtain legitimate app access via the Play Store (e.g., by purchasing or installing), and fix Play Protect issues when applicable. It can also be used in resolving user-remediable client-side errors.

Since 1.5.0

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode).
