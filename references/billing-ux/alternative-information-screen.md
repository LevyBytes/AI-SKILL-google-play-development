> **Note:** Developers offering alternative billing to users in South Korea must use alternative billing APIs. Follow the requirements below and the [alternative billing API integration guide](<https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app>), and verify current program eligibility before implementation.

## Overview

In order to maintain a consistent user experience and to help users make an informed choice, you are required to display an information screen and a separate billing choice screen if you offer an alternative in-app billing system to Google Play’s. The information screen only needs to be shown to each user the first time the user initiates a purchase, while the billing choice screen should be shown before every purchase. The user-facing messages and UI specifications for both screens should be implemented according to the following guidelines.

![Information screen and billing choice screen UI guidelines](<https://developer.android.com/static/images/google/play/billing/ui-guidelines.png>)

## Information for users

The information screen helps users understand the context of the change and gives more information to help them make an informed choice.

### When to display

The information screen should be shown to users at the start of their first purchase after you add an alternative in-app billing system. This message does not need to be displayed on subsequent purchases by the same user. Display the information screen immediately after a user has taken explicit action to initiate a purchase.

### When to display price

The purchase price should be visible and obvious to users before they are shown either the information screen or the billing choice screen.

### How to display

The information screen should be displayed in a modal bottom sheet. A modal bottom sheet is similar to a modal dialog that animates up from the bottom of the screen and stays pinned to the bottom. It is elevated above all UI elements on the underlying screen. The underlying screen is obscured behind a dark scrim to indicate that it will not respond to user interaction.

Refer to Google Material Design for more information on the [design](<https://material.io/components/sheets-bottom#modal-bottom-sheet>) and [implementation](<https://material.io/components/sheets-bottom/android#using-bottom-sheets>) of modal bottom sheets.

### User actions

The bottom sheet should be triggered when a user taps on a button or other UI element in your app that initiates a purchase. The user can take three possible actions from the information screen:

#### Continue

Tapping the “Continue” button dismisses the information screen and launches the billing choice screen.

#### Learn more

Tapping the “Learn more” button launches a Google Help Center article in a web browser.

#### Dismiss

If users want to dismiss the bottom sheet and return to the underlying screen, they can dismiss the bottom sheet by:

- Tapping outside of the bottom sheet container
- Tapping the Android system "Back" button

The information screen does not need to be displayed again after it has been dismissed or after the user has tapped “Continue”.

Example: The purchase price is clearly displayed before the user initiates the purchase. Tapping the “join now” button triggers the information screen.

![user information screen](<https://developer.android.com/static/images/google/play/billing/user-info.png>)

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/billing-choice).
