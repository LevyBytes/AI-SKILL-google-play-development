The declaring type and inherited API are described in [the exception contract](standard-exception.md).

## Public constructors

### StandardIntegrityException

```text
public StandardIntegrityException(int errorCode)
```

Constructs an `StandardIntegrityException` with the specified error code.

| Parameters |  |
| --- | --- |
| `int errorCode` | the error code. |

## Public methods

### getCause

```text
synchronized public Throwable getCause()
```

### getErrorCode

```text
public int getErrorCode()
```

Returns the error code resulting from the operation. The value is one of the constants in `StandardIntegrityErrorCode`.

### getStatusCode

```text
public int getStatusCode()
```

Returns the error code resulting from the operation. The value is one of the constants in `StandardIntegrityErrorCode`. getStatusCode() is not supported in `StandardIntegrityException`, please use getErrorCode() instead.

### isRemediable

```text
public boolean isRemediable()
```

Returns whether the exception is remediable by the device integrity dialogs. See `IntegrityDialogTypeCode`.

Since 1.5.0

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException).
