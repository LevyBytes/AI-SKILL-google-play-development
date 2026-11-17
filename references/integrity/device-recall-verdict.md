#### Device recall (beta)

You can also opt in to [device recall](<https://developer.android.com/google/play/integrity/device-recall>), which lets you store some custom, per-device data with specific devices that you can reliably retrieve when your app is installed again later on the same device. After requesting an integrity token, you make a separate server-to-server call to [modify device recall values](<https://developer.android.com/google/play/integrity/device-recall#modify-recall>) for a specific device.

If you opt in to `deviceRecall`, the `deviceIntegrity` field will contain the device recall information that you set for the specific device:

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "deviceRecall": {
    "values": {
      "bitFirst": true,
      "bitSecond": false,
      "bitThird": true
    },
    "writeDates": {
      // Write time in YYYYMM format in UTC.
      "yyyymmFirst": 202401,
      // Note that yyyymmSecond is not set because bitSecond is false.
      "yyyymmThird": 202310
    }
  }
}
```

The `deviceRecall` is split in two fields:

- `values`: Recall the bit values that you previously set for this device.
- `writeDates`: Recall the bit write dates in UTC accurate to the year and month. The write date of a recall bit will be updated every time the bit is set to `true` and will be removed when the bit is set to `false`.

In the case when device recall information is unavailable, the device recall value will be empty:

```json
"deviceIntegrity": {
  "deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"],
  "deviceRecall": {
    "values": {},
    "writeDates": {}
  }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
