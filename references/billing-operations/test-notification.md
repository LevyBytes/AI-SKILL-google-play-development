## TestNotification

A `TestNotification` contains the following fields:

```json
{
  "version": string
}
```

| version | string | The version of this notification. Initially, this is "1.0". This version is distinct from other version fields. |
| --- | --- | --- |

### Example

Here's an example of a test notification:

```json
{
  "version":"1.0",
  "packageName":"com.some.thing",
  "eventTimeMillis":"1503350156918",
  "testNotification":
  {
    "version":"1.0"
  }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/rtdn-reference).
