Client: `AppEngageShoppingClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

##### For SDK versions prior to v1.6.0 (Deprecated)

**Kotlin**

```kotlin
client.isServiceAvailable.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        // Handle IPC call success
        if(task.result) {
          // Service is available on the device, proceed with content publish
          // calls.
        } else {
          // Service is not available, no further action is needed.
        }
    } else {
      // The IPC call itself fails, proceed with error handling logic here,
      // such as retry.
    }
}
```

**Java**

```java
client.isServiceAvailable().addOnCompleteListener(task -> {
    if (task.isSuccessful()) {
        // Handle success
        if(task.getResult()) {
          // Service is available on the device, proceed with content publish
          // calls.
        } else {
          // Service is not available, no further action is needed.
        }
    } else {
      // The IPC call itself fails, proceed with error handling logic here,
      // such as retry.
    }
});
```

> **Note:** We highly recommend keeping a periodic job running to check if the service becomes available at a later point in time. The availability of the service may change with Android version upgrades, app upgrades, installs, and uninstalls. By ensuring periodic job checks at a certain time interval, data can be published once the service becomes available.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
