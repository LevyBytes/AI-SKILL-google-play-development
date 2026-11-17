These constants belong to `IntegrityErrorCode`; [the class summary](classic-error-index.md) lists the full set.

### PLAY_SERVICES_NOT_FOUND

```text
public static final int PLAY_SERVICES_NOT_FOUND = -6
```

Play Services is not available or version is too old.

Recommended actions:

- Ask the user to install or update Play Services.
- For a guided user experience that helps the user to enable, install or update Play Services, you can show either `GET_INTEGRITY` or `GET_STRONG_INTEGRITY` dialog.

### PLAY_SERVICES_VERSION_OUTDATED

```text
public static final int PLAY_SERVICES_VERSION_OUTDATED = -15
```

Play Services needs to be updated.

Recommended actions:

- Ask the user to update Google Play Services.
- For a guided user experience that helps the user to update Play Services, you can show either `GET_INTEGRITY` or `GET_STRONG_INTEGRITY` dialog.

### PLAY_STORE_ACCOUNT_NOT_FOUND

```text
public static final int PLAY_STORE_ACCOUNT_NOT_FOUND = -4
```

No Play Store account is found on device. Note that the Play Integrity API now supports unauthenticated requests. This error code is used only for older Play Store versions that lack support.

Ask the user to authenticate in Play Store.

### PLAY_STORE_NOT_FOUND

```text
public static final int PLAY_STORE_NOT_FOUND = -2
```

No Play Store app is found on device or not official version is installed.

Ask the user to install an official and recent version of Play Store.

### PLAY_STORE_VERSION_OUTDATED

```text
public static final int PLAY_STORE_VERSION_OUTDATED = -14
```

The Play Store needs to be updated.

Ask the user to update the Google Play Store.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode).
