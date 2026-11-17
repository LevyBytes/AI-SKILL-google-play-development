This guide describes how to integrate your app with the Play Billing Library APIs so that you can offer [billing choice](<https://developer.android.com/google/play/billing/billingchoice>) to your users.

## Integration with PBL

You can integrate billing choice with the PBL in four scenarios. The scenarios differ based on who renders the choice screen and where the payment will happen. The following table outlines the integration scenarios:

| Entry | Details | Details | Details |
| --- | --- | --- | --- |
|  |  | Which billing choice screen do you want to render? | Which billing choice screen do you want to render? |
|  |  | Google Play's | Your own (in accordance with the UX guidelines) |
| Where does the payment happen? | In-app | **Scenario 1A** Google renders the choice screen and the **alternate billing is handled within your app**. | **Scenario 1B** App developer renders the choice screen and the **alternate billing is handled within your app**. |
| Where does the payment happen? | External web link | **Scenario 2A** Google renders the choice screen and the user is **linked outside of your app to your own websites** for purchases. | **Scenario 2B** App developer renders the choice screen and the user is **linked outside of your app to your own websites** for purchases. |

The following illustration elaborates the billing choice flow for each of these scenarios:

![The billing choice flow showing the sequence of API calls and user interactions for the four integration scenarios.](<https://developer.android.com/static/images/google/play/billing/billingchoice/billing-choice-3.png>)

**Figure 1.** Billing choice integration scenarios

![The billing choice flow showing the sequence of API calls and user interactions for the four integration scenarios.](<https://developer.android.com/static/images/google/play/billing/billingchoice/billing-choice-3.png>)

## PBL integration scenarios

Depending on your integration scenario, follow the steps in this section to implement billing choice in your app.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
