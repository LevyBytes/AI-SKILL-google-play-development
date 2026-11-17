### Opt-out price change example

AltoStrat changes its premium video subscription from $1 to $1.30, immediately ends the legacy price cohort and specifies an opt-out migration. This case assumes a region requiring at least 30 days of opt-out notice; the migration becomes effective after that minimum period.

Alice has a monthly renewal before the notice period is complete and pays the old $1 price. Play begins notifying her 30 days before her next renewal, which is charged at $1.30.

### Price step-up consent examples

These [price step-up consent](https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-stepup-consent) cases apply only to South Korea (KR).

#### Consent during signup

A user signs up with a 10-day free trial and consents to the price step-up during signup. Play applies the step-up when the trial ends.

#### No consent during the free trial

A user signs up with a 10-day free trial and gives no consent during signup or the trial. The consent period runs for the 10-day trial; Play cancels the subscription when the trial ends. [Primary no-consent diagram](https://developer.android.com/static/images/google/play/billing/price-stepup-example-2.png).

A consent period can last at most 30 days before the step-up takes effect. If a free trial lasts 40 days, the consent period starts 10 days after signup and covers the final 30 days of the trial.

#### Consent during the free trial

A user signs up with a 10-day free trial and consents during the trial. Play applies the step-up at the end of the trial. [Primary trial-consent diagram](https://developer.android.com/static/images/google/play/billing/price-stepup-example-3.png).

#### No consent for an introductory offer

A user signs up with a 60-day introductory-price period and does not consent during signup. The consent window starts after the first 30 days and lasts for the remaining 30 days. If the user still has not consented, Play cancels the subscription at the end of the introductory period. [Primary introductory-offer diagram](https://developer.android.com/static/images/google/play/billing/price-stepup-example-4.png).

#### Consent for both trial and introductory offer

For a 10-day free trial followed by a 30-day introductory-price period, Play requests consent separately for the two transitions:

1. During the free trial, it requests consent to move from free access to the introductory price. If the user consents, Play applies this first step-up when the trial ends.
2. During the introductory period, it requests consent to move from the introductory price to the regular price. If the user consents, Play applies this second step-up when the introductory period ends.

The example's user consents during both periods. [Primary two-transition diagram](https://developer.android.com/static/images/google/play/billing/price-stepup-example-5.png).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/price-changes).
