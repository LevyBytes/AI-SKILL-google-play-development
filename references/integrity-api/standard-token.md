```text
public abstract class StandardIntegrityManager.StandardIntegrityToken
```

---

Response of `StandardIntegrityTokenProvider#request(StandardIntegrityTokenRequest)`.

## Summary

### Public constructors

| Entry |
| --- |
| [`StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken#StandardIntegrityToken()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | [`showDialog`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken#showDialog(android.app.Activity,int)>)`(`[`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) `activity, int typeCode)`<br> **This method is deprecated.** <br>Use [`StandardIntegrityManager#showDialog(StandardIntegrityDialogRequest)`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager#showDialog(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest)>) instead. |

            </td>
          </tr>
          <tr>
            <td><code translate="no" dir="ltr">abstract <a href="https://developer.android.com/reference/java/lang/String.html">String</a></code></td>
            <td>
              <div><code translate="no" dir="ltr"><a href="https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken#token()">token</a>()</code></div>
              <p>A token which contains the response for the integrity related enquiries.</p>
            </td>
          </tr>
        </tbody>
      </table>

## Public constructors

### StandardIntegrityToken

```text
public StandardIntegrityToken()
```

## Public methods

### showDialog

```text
public abstract Task<Integer> showDialog(Activity activity, int typeCode)
```

> **This method is deprecated.**<br>
>
> Use `StandardIntegrityManager#showDialog(StandardIntegrityDialogRequest)` instead.

Displays a dialog to the user.

This method can only be called once per Integrity API response.

| Parameters |  |
| --- | --- |
| `int typeCode` | determines which Integrity Dialog type should be shown. See [`IntegrityDialogTypeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode>) for the supported types. |

| Returns |  |
| --- | --- |
| [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | A [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) that completes with a [`IntegrityDialogResponseCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode>) the showDialog flow succeeded or failed. |

### token

```text
public abstract String token()
```

A token which contains the response for the integrity related enquiries.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken).
