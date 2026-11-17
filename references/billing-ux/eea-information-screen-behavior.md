> **Note:** Google is sunsetting manual implementation of the interim UX guidelines. Learn more about migration deadlines [here](<https://support.google.com/googleplay/android-developer/answer/13821247#alt_billing_API_migration_deadline>). If you are offering user choice billing through alternative billing APIs, you can meet the user experience requirements by integrating with and using the client-side APIs. In this case, you don't need to separately follow the interim user experience guidelines outlined in this topic.

## Overview

These guidelines are provided for developers participating in our [program](<https://support.google.com/googleplay/android-developer/answer/12348241>) for offering users in the European Economic Area (EEA) an alternative billing to Google Play’s billing system without user choice. Developers with users in the EEA who are participating in the [user choice billing pilot](<https://support.google.com/googleplay/android-developer/answer/12570971>) and offering an alternative billing system alongside Google Play’s billing system should use the [user choice billing UX guidelines](<https://developer.android.com/google/play/billing/alternative/interim-ux/user-choice>). These UX guidelines aim to maintain a consistent user experience by requiring developers to display an information screen to each user the first time the user initiates a purchase. The user-facing messages and UI specifications for the information screen should be implemented according to the following guidelines.

| ![Image](<https://developer.android.com/static/images/google/play/billing/interim-eea-overview-a.png>) Developer app | ![Image](<https://developer.android.com/static/images/google/play/billing/interim-eea-overview-b.png>) Information screen for users |
| --- | --- |

## Information for users

The information screen helps users understand the impact of the change.

### When to display

The information screen must be shown to users at the start of their first purchase. This message does not need to be displayed on subsequent purchases by the same user. Display the information screen immediately after a user has taken explicit action to initiate a purchase.

### When to display price

The purchase price should be visible and obvious to users before they are shown the information screen.

### How to display

The information screen must be displayed in a modal bottom sheet. A modal bottom sheet is similar to a modal dialog that animates up from the bottom of the screen and stays pinned to the bottom. It is elevated above all UI elements on the underlying screen. The underlying screen is obscured behind a dark scrim to indicate that it will not respond to user interaction.

Refer to Google Material Design for more information on the [design](<https://material.io/components/sheets-bottom#modal-bottom-sheet>) and [implementation](<https://material.io/components/sheets-bottom/android#using-bottom-sheets>) of modal bottom sheets.

### User actions

The bottom sheet must be triggered when a user taps on a button or other UI element in your app that initiates a purchase. The user can take two possible actions from the information screen:

#### Got it

Tapping the “Got it” button dismisses the information screen and launches the next screen in your payment flow.

#### Learn more

Tapping the “Learn more” button launches a Google Help Center article in a web browser.

#### Dismiss

If users want to dismiss the bottom sheet and return to the underlying screen, they can dismiss the bottom sheet by:

- Tapping outside of the bottom sheet container
- Tapping the Android system "Back" button

The information screen does not need to be displayed again after it has been dismissed or after the user has tapped “Got it”.

Example: When the user taps to purchase in your app, the button will trigger the information screen.

![Interim EEA information screen flow](<https://developer.android.com/static/images/google/play/billing/interim-eea-flow.png>)

### Design specifications

The information screen is divided into three components: title, message, and buttons. All three components are required and must contain the exact text and UI elements defined in these guidelines. Do not include any additional text or imagery on this screen, but you are free to include additional text and imagery on other screens.

![Image](<https://developer.android.com/static/images/google/play/billing/interim-eea-specs.png>)

1. Title
2. Text 1
3. Text 2
4. Buttons
5. Bottom sheet
6. Background scrim

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/alt-billing).
