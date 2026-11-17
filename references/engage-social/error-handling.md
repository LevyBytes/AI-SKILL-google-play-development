Client: `AppEngageSocialClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### Error handling

It is highly recommended to listen to the task result from the publish APIs so that a follow-up action can recover and resubmit an unsuccessful task.

```java
client.publishRecommendationClusters(
              new PublishRecommendationClustersRequest.Builder()
                  .addRecommendationCluster(...)
                  .build())
          .addOnCompleteListener(
              task -> {
                if (task.isSuccessful()) {
                  // do something
                } else {
                  Exception exception = task.getException();
                  if (exception instanceof AppEngageException) {
                    @AppEngageErrorCode
                    int errorCode = ((AppEngageException) exception).getErrorCode();
                    if (errorCode == AppEngageErrorCode.SERVICE_NOT_FOUND) {
                      // do something
                    }
                  }
                }
              });
```

The error is returned as an `AppEngageException` with the cause included as an error code.

| Error code | Error name | Note |
| --- | --- | --- |
| `1` | `SERVICE_NOT_FOUND` | The service is not available on the given device. |
| `2` | `SERVICE_NOT_AVAILABLE` | The service is available on the given device, but it is not available at the time of the call (for example, it is explicitly disabled). |
| `3` | `SERVICE_CALL_EXECUTION_FAILURE` | The task execution failed due to threading issues. In this case, it can be retried. |
| `4` | `SERVICE_CALL_PERMISSION_DENIED` | The caller is not allowed to make the service call. |
| `5` | `SERVICE_CALL_INVALID_ARGUMENT` | The request contains invalid data (for example, more than the allowed number of clusters). |
| `6` | `SERVICE_CALL_INTERNAL` | There is an error on the service side. |
| `7` | `SERVICE_CALL_RESOURCE_EXHAUSTED` | The service call is made too frequently. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
