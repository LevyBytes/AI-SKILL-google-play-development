### Opt-in price increase examples

These worked cases use a migration effective 37 days after it is triggered and notifications beginning 30 days before the first renewal charged at the new price. The price-policy contract determines which notice period applies to the actual region and product.

#### Monthly subscription

AltoStrat ends a legacy cohort and moves AltoStrat Pro from $1 to the base-plan price of $2. Alice has two monthly renewals before the effective date, both charged at $1. Her first renewal after the effective date costs $2, and Play starts notifying her 30 days before that charge. [Primary diagram for Alice's monthly renewals](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-1.svg).

Bob has one monthly renewal before the effective date, charged at $1. His next monthly renewal falls after the effective date and costs $2. Play starts notifying him 30 days before the first $2 renewal. [Primary diagram for Bob's monthly renewals](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-2.svg).

#### Three-month subscription

FindMyLove ends a legacy cohort and changes FindMyLove Premium from $1 per three-month period to $2. The migration becomes effective 37 days after it is triggered.

Alice's next renewal precedes the effective date and remains $1. Her following three-month renewal falls after the effective date and costs $2; notification starts 30 days before that renewal. [Primary diagram for Alice's three-month renewal](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-3.svg).

Bob's next renewal falls after the effective date, so it costs $2. His notification starts 30 days before that renewal. [Primary diagram for Bob's three-month renewal](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-4.svg).

#### Weekly subscription

CutePetsNews changes Weekly Dog Alerts from $1 to $2 by ending a legacy cohort. Alice has five weekly renewals before the effective date, all at $1. Her next weekly renewal falls after the effective date and costs $2. Notification begins 30 days before that first $2 charge. [Primary weekly-renewal diagram](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-5.svg).

#### Multiple monthly price changes

AltoStrat first changes AltoStrat Pro from $1 to $2 per month, then triggers a second migration to $3 per month seven days later. Each migration has its own effective time, 37 days after it was triggered.

Alice's next two renewals occur before the applicable effective time and remain $1. Her first renewal after both changes takes effect costs the newest price, $3. In this example, both changes occur within the 7-day freeze period, so she receives only the second change's notifications. Notification starts 30 days before her first $3 renewal. [Primary multiple-change diagram](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-6.svg).

#### Twelve-month installment subscription

AltoStrat ends the $1 legacy cohort and moves subscribers to the $2 base-plan price, with the change effective after 37 days. Alice is still paying installments in an existing 12-month commitment that will be followed by monthly auto-renewal.

Her three remaining installment payments stay at $1. At the first renewal after the commitment ends, she pays $2 and switches to the monthly auto-renewal cadence. Play starts notifying her 30 days before that renewal.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/price-changes).
