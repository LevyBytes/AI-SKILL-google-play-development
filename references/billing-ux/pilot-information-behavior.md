## Information for users

The information screen helps users understand the context of the change and gives more information to help them make an informed choice.

### When to display

The information screen must be shown to users at the start of their first purchase after you add an alternative billing system. This message does not need to be displayed on subsequent purchases by the same user. Display the information screen immediately after a user has taken explicit action to initiate a purchase.

### When to display price

The purchase price must be visible and obvious to users before they are shown either the information screen or the billing choice screen.

### How to display

The information screen must be displayed in a modal bottom sheet. A modal bottom sheet is similar to a modal dialog that animates up from the bottom of the screen and stays pinned to the bottom. It is elevated above all UI elements on the underlying screen. The underlying screen is obscured behind a dark scrim to indicate that it will not respond to user interaction.

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

Example: When the user taps to purchase in your app, the button will trigger the information screen.

![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-info-flow.png>)

### Design specifications

The information screen is divided into three components: title, message, and buttons. All three components are required and must contain the exact text and UI elements defined in these guidelines. Do not include any additional text or imagery on this screen, but you are free to include additional text and imagery on other screens.

![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-info-specs.png>)

1. Title
2. Text 1
3. Text 2
4. Buttons
5. Bottom sheet
6. Background scrim

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/user-choice).
