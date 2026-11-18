---
title: "Pipeline & Conversion"
tags: [medwave, bi-suite, cpd]
bi_type: pipeline
updated: 2026-11-12
refreshed_sast: "2026-11-12 11:14"
source: "refresh_bi_suite.py (Google Sheets + read-only HighLevel export)"
privacy: "no emails or phone numbers"
attended_contacted: 309
attended_replied: 170
attended_booked: 102
attended_sold: 1
---
# Pipeline & Conversion

Suite: [[Business Intelligence Suite/Home|Home]] · [[Business Intelligence Suite/CPD Attendees Dashboard|CPD dashboard]] · [[Business Intelligence Suite/Pipeline & Conversion|Pipeline]] · [[Business Intelligence Suite/Follow-up Priorities|Follow-ups]] · [[Business Intelligence Suite/Rules - CPD Pricing|Rules]] · [[Business Intelligence Suite/Data Dictionary|Data dictionary]] · [[Business Intelligence Suite/How to Refresh|Refresh]]

Funnel per audience. Contacted = any inbound or outbound message on the HighLevel conversation. Booked = a live appointment, a booked tag or stage, or a BDR note saying booked. Sold = an opportunity in a Deposit Received, Cash Collected, Sold/Closed, Financing connected or Existing customer stage (a 'won' status on a booking stage is not counted).

| Audience | Doctors | In HighLevel | Contacted | Replied | Booked | Showed | Sold |
|---|---|---|---|---|---|---|---|
| Attended 10 Nov webinar | 333 | 318 (95%) | 309 (93%) | 170 (51%) | 102 (31%) | 4 (1%) | 1 (0%) |
| Registered, no-show | 559 | 209 (37%) | 208 (37%) | 106 (19%) | 43 (8%) | 8 (1%) | 2 (0%) |
| Barefoot list only | 10810 | 476 (4%) | 364 (3%) | 183 (2%) | 110 (1%) | 27 (0%) | 5 (0%) |

## Attended: current stage
| Stage | Doctors |
|---|---|
| Contacted | 133 |
| Booked | 101 |
| Replied | 74 |
| Not in HighLevel | 15 |
| In HighLevel, no messages found | 9 |
| Sold | 1 |

## Attended: HighLevel pipeline stages (open opportunities)
| Pipeline: stage (status) | Doctors |
|---|---|
| 1.3) Elmien Geldenhuys Sales Superhero: LQ appt booked (open) | 89 |
| Master Pipeline: B1 (open) | 40 |
| 2.1) Erich - CPD: CPD - nurture (open) | 34 |
| 2.1) Erich - CPD: Lost (lost) | 22 |
| Erich - Auto nurture: Booked - Web (open) | 11 |
| 1.1) Davide - MedWave CEO: CPD test leads (open) | 10 |
| 2.1) Erich - CPD: CPD - email only (open) | 7 |
| Erich - Auto nurture: No answer (open) | 4 |
| 2.1) Erich - CPD: Booked - Web (open) | 4 |
| Eddie - Auto nurture: Booked - Web (open) | 3 |
| 1.3) Elmien Geldenhuys Sales Superhero: LQ no show (open) | 3 |
| Mike - Auto nurture: No answer (open) | 3 |
| 2.2) Mike - new cadence: Booked - Web (open) | 3 |
| Erich - Auto nurture: Self booking/conversation (open) | 2 |
| Erich Pipeline: Andries Booked (open) | 2 |
| Mike - Auto nurture: Booked - Web (open) | 2 |
| Mike - Auto nurture: Nurture (open) | 2 |
| 2.2) Mike - new cadence: Day 7 – Call (if no answer - manual move) (open) | 2 |
| Rozanne Outreach: New Lead (open) | 2 |
| 2.1) Erich - CPD: Booked (open) | 2 |

## Attended and booked: by owner
| Owner | Booked | Not booked |
|---|---|---|
| (none) | 0 | 158 |
| Elmien Geldenhuys | 94 | 0 |
| Erich MedWave | 3 | 60 |
| Michael Steytler | 2 | 10 |
| Andries Maritz | 2 | 0 |
| Rozanne Diederichs | 1 | 1 |
| Hazel Janecke | 0 | 1 |
| Eddie VDW | 0 | 1 |

## Sold (attended or registered)
| Name | Practice | Province | Owner | Opportunities | Contactid |
|---|---|---|---|---|---|
| Dr. Ceilia Coetzer | Coetzer Algemene Praktisyns |  | Elmien Geldenhuys | Erich Pipeline: Andries Booked (open); 1.2) Andries Pipeline | eZWPtVjnPVr7q5IU7y7D |
| Mrs Christine Copley | Private Practice |  |  | Karin - Pipeline: (K) Sold/Closed (open); South Africa B2B:  | SZEN7dBbdvGCdV9Nbd9g |
| Ms Mpho Mkutshulwa | Khulani Clinic Mamelodi | Gauteng | Andries Maritz | 1.2) Andries Pipeline: Deposit Received (won); Erich Pipelin | Ja4a2QGzNpZVFVeNHbyX |

Opportunity values in HighLevel are mostly R0, so revenue is not reported here.
