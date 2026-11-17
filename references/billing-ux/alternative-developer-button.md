### Developer button

![ui requirements for a developer button](<https://developer.android.com/static/images/google/play/billing/developer-button.png>)

1. App icon
2. App name
3. Payment method icons

![additional options for the developer button](<https://developer.android.com/static/images/google/play/billing/developer-button-2.png>)

**Payment method icons**
1. Maximum number of payment method icons
2. Payment method names instead of icons
**Scale to screen width**
3. 360dp width
4. 480dp width

#### Button container

| Outline | 1pt, #DADCE0 |
| --- | --- |
| Corner radius | 4dp |
| Inner padding | 16dp, 16dp, 16dp, 16dp, |

#### App icon

| Dimensions | Height: 24dp, Width: variable |
| --- | --- |

#### Title

| Text | {App Name} |
| --- | --- |
| Font size | 14sp |
| Font color | #202124 |

#### Payment methods

| Dimensions | 32dp X 20dp |
| --- | --- |
| Corner radius | 2 |
| Quantity | 5 maximum, if >5 available display additional indicator |
| Additional indicator | + more (wraps to next line on narrow screens) |
| Font size | 12sp |
| Font color | #5F6368 |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/billing-choice).
