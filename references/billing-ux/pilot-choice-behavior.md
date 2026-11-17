## Billing choice screen

The billing choice screen presents users with two checkout options to complete their purchase. To help users make an informed decision, each billing service option also displays their available forms of payment. Once users make their choice, they will continue to complete their purchase through that billing system.

### When to display

If the user has already seen the information screen during a previous purchase, the billing choice screen should appear immediately after the user has taken explicit action to initiate a purchase.

### How to display

The billing choice screen must be displayed in a modal bottom sheet and follow the same specifications as the information screen.

### Equal visual representation

The buttons for the alternative billing system and Google Play’s billing system should be represented in a fair and equal manner. This includes but is not limited to equal button sizes, text size/style, tap targets, and icon sizes. Please do not add any additional text, images, or style changes not defined in these guidelines.

Example: When a user taps to purchase in your app, the button will trigger the billing choice screen, only if the user has already seen the information screen during a previous purchase.

![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-choice-flow.png>)

### Design specifications

The billing choice screen has four distinct components: title, description, developer button, and the Google Play button. All components must be used, and must contain the exact text and UI elements defined in these guidelines. We ask you not to include any additional text or imagery on this screen, but you are free to include additional text and imagery on other screens owned by you.

Visual assets for Google Play and payment icons are available through the links provided below.

Example: In portrait view, the bottom sheet should span 100% of the total screen width.

![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-choice-specs.png>)

1. Title
2. Description
3. Developer button
4. Google Play button
5. Bottom sheet
6. Background scrim

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/user-choice).
