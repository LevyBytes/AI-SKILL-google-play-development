> **Note:** Google is sunsetting manual implementation of the interim UX guidelines. Learn more about migration deadlines [here](<https://support.google.com/googleplay/android-developer/answer/13821247#alt_billing_API_migration_deadline>). If you are offering user choice billing through alternative billing APIs, you can meet the user experience requirements by integrating with and using the client-side APIs. In this case, you don't need to separately follow the interim user experience guidelines outlined in this topic.

## Overview

The [user choice billing pilot](<https://support.google.com/googleplay/android-developer/answer/12570971>) allows participating developers to test offering an alternative billing option next to Google Play's billing system and is designed to help us explore offering this choice to users. These UX guidelines aim to maintain a consistent user experience and help users make an informed decision.

You are required to display an information screen and a separate billing choice screen if you are participating in the pilot. The information screen only needs to be shown to each user the first time the user initiates a purchase, while the billing choice screen must be shown before every purchase. The user-facing messages and UI specifications for both screens must be implemented according to the following guidelines.

| ![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-overview-a.png>) Developer app | ![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-overview-b.png>) Information screen for users | ![Image](<https://developer.android.com/static/images/google/play/billing/interim-ucb-overview-c.png>) Billing choice screen |
| --- | --- | --- |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/interim-ux/user-choice).
