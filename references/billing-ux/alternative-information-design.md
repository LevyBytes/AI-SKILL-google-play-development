### Design specifications

The information screen is divided into three components: title, message, and buttons. All three components are required and must contain the exact text and UI elements defined in these guidelines. Do not include any additional text or imagery on this screen, but you are free to include additional text and imagery on other screens.

![checkout options screen showing position of required components](<https://developer.android.com/static/images/google/play/billing/checkout.png>)

1. Title
2. Message
3. Buttons
4. Bottom sheet
5. Background scrim

#### Title

| Text | Changes to your checkout options |
| --- | --- |
| Font | Roboto (apply to all fonts) |
| Font size | 18sp |
| Font color | #202124 |

#### Message

| Text 1 | You now have more options at checkout, due to recent regulatory changes in South Korea. Your choice will determine: Who secures your purchase, processes your payment, and stores any payment information Who provides customer support for the purchase Which forms of payment you can use Which benefits are available with your purchase |
| --- | --- |
| Font size | 14sp |
| Line height | 20 |
| Font color | #5F6368 |
| Text 2 | Only purchases through Google Play are secured by Google. Play features such as Play gift cards, Play Points, purchase controls, and subscription management are only available when you choose Google Play at checkout. |
| Font size | 12sp |
| Line height | 16 |
| Font color | #5F6368 |

#### Button 1

| Text | Learn more |
| --- | --- |
| Text alignment | Centered |
| Font size | 14sp |
| Font weight | Medium |
| Font color | #01875F |
| Background color | #FFFFFF |
| Dimensions | Height:36, Width: scale to container |
| Corner radius | 4dp |
| Outline | 1dp, #DADCE0 |
| Link | [Links to Google Play help article](<https://support.google.com/googleplay/answer/11174377>) |

#### Button 2

| Text | Continue |
| --- | --- |
| Text alignment | Centered |
| Font size | 14sp |
| Font weight | Medium |
| Font color | #FFFFFF |
| Background color | #01875F |
| Dimensions | Height:36, Width: scale to container |
| Corner radius | 4dp |
| Link | Links to Billing choice screen |

#### Bottom sheet

| Dimensions | Height: variable, Width: 100% |
| --- | --- |
| Corner radius | 8dp, 8dp, 0, 0 |
| Background | #FFFFFF |
| Inner padding | Left:24dp, Right:24dp, Top:32dp, Bottom: 24dp |
| Elevation | 8dp |

### Landscape

In landscape view, the bottom sheet is wider than in portrait view, but otherwise follows the same design specifications and functionality.

![checkout options screen in landscape mode](<https://developer.android.com/static/images/google/play/billing/checkout-landscape.png>)

| Bottom sheet | Width: 500dp maximum, Inner padding: 24dp |
| --- | --- |
| Title | Same as portrait view |
| Message | Same as portrait view |
| Buttons | Height:36, Width: scale to container |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/billing-choice).
