## Decrypt and verify the integrity verdict

When you request an integrity verdict, the Play Integrity API provides a signed response token. The `nonce` that you include in your request becomes part of the response token.

### Token format

The token is a nested [JSON Web Token (JWT)](<https://jwt.io/>), that is [JSON Web Encryption (JWE)](<https://tools.ietf.org/html/rfc7516>) of [JSON Web Signature (JWS)](<https://tools.ietf.org/html/rfc7515>). The JWE and JWS components are represented using [compact serialization](<https://datatracker.ietf.org/doc/html/rfc7515#section-3.1>) .

The encryption / signing algorithms are well-supported across various JWT implementations:

- JWE uses A256KW for [alg](<https://tools.ietf.org/html/rfc7516#section-4.1.1>) and A256GCM for [enc](<https://tools.ietf.org/html/rfc7516#section-4.1.2>)
- JWS uses ES256.

### Decrypt and verify on Google's servers (recommended)

The Play Integrity API lets you decrypt and verify the integrity verdict on Google's servers, which enhances your app's security. To do so, complete these steps:

1. [Create a service account](<https://cloud.google.com/iam/docs/service-accounts-create>) within the Google Cloud project that's linked to your app.
2. On your app's server, fetch the access token from your service account credentials using the `playintegrity` scope, and make the following request:

   ```text
   playintegrity.googleapis.com/v1/PACKAGE_NAME:decodeIntegrityToken -d \
   '{ "integrity_token": "INTEGRITY_TOKEN" }'
   ```

   > **Note:** To access the API's REST interface, you can use the [Google API Client Library](<https://developers.google.com/api-client-library>), which is available in many programming languages, [including Java](<https://github.com/googleapis/google-api-java-client-services/tree/main/clients/google-api-services-playintegrity/v1>).
3. Read the JSON response.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
