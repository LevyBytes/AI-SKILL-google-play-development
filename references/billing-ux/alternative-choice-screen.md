## Billing choice screen

The billing choice screen presents users with two checkout options to complete their purchase. To help users make an informed decision, each billing service option also displays their available forms of payment. Once users make their choice, they will continue to complete their purchase through that billing service.

### When to display

If the user has already seen the information screen, the billing choice screen should appear immediately after the user has taken explicit action to initiate a purchase.

### How to display

The Billing choice screen should be displayed in a modal bottom sheet and follow the same specifications as the information screen.

### Equal visual representation

The buttons for the additional in-app billing service and Google Play’s billing service should be represented in a fair and equal manner. This includes but is not limited to equal button sizes, text size/style, tap targets, and icon sizes. Please do not add any additional text, images, or style changes not defined in these guidelines.

Example: Tapping the “join now” button triggers the billing choice screen.

![the billing choice screen with equal representation for each billing option](<https://developer.android.com/static/images/google/play/billing/equal-representation.png>)

### Design specifications

The billing choice screen has four distinct components: title, description, developer button, and the Google Play button. All components should be used, and should contain the exact text and UI elements defined in these guidelines. We ask you not to include any additional text or imagery on this screen, but you are free to include additional text and imagery on other screens owned by you.

Visual assets for Google Play and payment icons are available through the links provided below.

Example: In portrait view, the bottom sheet should span 100% of the total screen width.

![bottom sheet showing position of required elements](<https://developer.android.com/static/images/google/play/billing/bottom-sheet.png>)

1. Title
2. Description
3. Developer button
4. Google Play button
5. Bottom sheet
6. Background scrim

#### Title

| Text | Choose how to check out |
| --- | --- |
| Font | Roboto (apply to all fonts) |
| Font size | 18sp |
| Font color | #202124 |

#### Description

| Text | Choose who will secure and process your payment and provide customer service. Benefits and available forms of payment may vary. |
| --- | --- |
| Font size | 14sp |
| Font color | #5F6368 |
| Text Link | Learn more |
| Link destination | [Link](<https://support.google.com/googleplay/answer/11174377>) |
| Font size | 14sp |
| Decoration | Underline |
| Font color | #5F6368 |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/billing-choice).
