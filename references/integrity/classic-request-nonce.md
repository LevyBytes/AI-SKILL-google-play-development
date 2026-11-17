## Generate a nonce

When you protect an action in your app with the Play Integrity API, you can leverage the `nonce` field to mitigate certain types of attacks, such as person-in-the-middle (PITM) tampering attacks and replay attacks. The Play Integrity API returns the value you set in this field inside the signed integrity response.

The value set in the `nonce` field must be correctly formatted:

- `String`
- URL-safe
- Encoded as Base64 and non-wrapping
- Minimum of 16 characters
- Maximum of 500 characters

The following are some common ways to use the `nonce` field in the Play Integrity API. To get the strongest protection from the `nonce`, you can combine the methods below.

### Include a request hash to protect against tampering

You can use the `nonce` parameter in a classic API request similarly to the `requestHash` parameter in a standard API request to protect the contents of a request against tampering.

When you request an integrity verdict:

1. Compute a digest of all critical request parameters (e.g. SHA256 of a stable request serialization) from the user action or server request that is happening.
2. Use `setNonce` to set the `nonce` field to the value of the computed digest.

When you receive an integrity verdict:

1. Decode and verify the integrity token, and obtain the digest from the `nonce` field.
2. Compute a digest of the request in the same manner as in the app (e.g. SHA256 of a stable request serialization).
3. Compare the app-side and server-side digests. If they don't match, the request is not trustworthy.

> **Note:** You should also verify both the device and app integrity signals to ensure that the results of the high-value action were created by your untampered app on an untampered device.

### Include unique values to protect against replay attacks

In order to prevent malicious users from reusing previous responses from the Play Integrity API, you can use the `nonce` field to uniquely identify each message.

When you request an integrity verdict:

1. Obtain a globally unique value in a way that malicious users cannot predict. For example, a cryptographically-secure random number generated on the server side can be such a value, or a pre-existing ID, such as a session or a transaction ID. A simpler and less secure variant is to generate a random number on the device. We recommend creating values 128 bits or larger.
2. Call `setNonce()` to set the `nonce` field to the unique value from step 1.

When you receive an integrity verdict:

1. Decode and verify the integrity token, and obtain the unique value from the `nonce` field.
2. If the value from step 1 was generated on the server, check that the received unique value was one of the generated values, and that it's being used for the first time (your server will need to keep a record of generated values for a suitable duration). If the received unique value has been used already or does not appear in the record, reject the request
3. Otherwise, if the unique value was generated on the device, check that the received value is being used for the first time (your server needs to keep a record of already seen values for a suitable duration). If the received unique value has been used already, reject the request.

### Combine both protections against tampering and replay attacks (recommended)

It is possible to use the `nonce` field to protect against both tampering and replay attacks at the same time. To do so, generate the unique value as described above, and include it as part of your request. Then compute the request hash, making sure to include the unique value as part of the hash. An implementation that combines both approaches is as follows:

When you request an integrity verdict:

1. The user initiates the high-value action.
2. Obtain a unique value for this action as described in the [Include unique values to protect against replay attacks](<https://developer.android.com/google/play/integrity/classic?hl=en#include-unique>) section.
3. Prepare a message you want to protect. Include the unique value from step 2 in the message.
4. Your app calculates a digest of the message it wants to protect, as described in the [Include a request hash to protect against tampering](<https://developer.android.com/google/play/integrity/classic?hl=en#include-request>) section. Since the message contains the unique value, the unique value is part of the hash.
5. Use `setNonce()` to set the `nonce` field to the computed digest from the previous step.

When you receive an integrity verdict:

1. Obtain the unique value from the request
2. Decode and verify the integrity token, and obtain the digest from the `nonce` field.
3. As described in the [Include a request hash to protect against tampering](<https://developer.android.com/google/play/integrity/classic?hl=en#include-request>) section, recompute the digest on the server side, and check that it matches the digest obtained from the integrity token.
4. As described in the [Include unique values to protect against replay attacks](<https://developer.android.com/google/play/integrity/classic?hl=en#include-unique>) section, check the validity of the unique value.

The following sequence diagram illustrates these steps with a server-side `nonce`:

![Image](<https://developer.android.com/static/images/google/play/integrity/play-integrity-api-nonce-content-binding.svg>)

**Figure 2.** Sequence diagram that shows how to protect against both tampering and replay attacks.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
