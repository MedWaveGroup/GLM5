---
title: "CPD Attendees Dashboard"
tags: [medwave, bi-suite, cpd]
bi_type: dashboard
updated: 2026-11-12
refreshed_sast: "2026-11-12 11:14"
source: "refresh_bi_suite.py (Google Sheets + read-only HighLevel export)"
privacy: "no emails or phone numbers"
attended: 333
attended_booked: 102
registered_no_show: 559
barefoot_only: 10810
unique_doctors: 11702
---
# CPD Attendees Dashboard

Suite: [[Business Intelligence Suite/Home|Home]] · [[Business Intelligence Suite/CPD Attendees Dashboard|CPD dashboard]] · [[Business Intelligence Suite/Pipeline & Conversion|Pipeline]] · [[Business Intelligence Suite/Follow-up Priorities|Follow-ups]] · [[Business Intelligence Suite/Rules - CPD Pricing|Rules]] · [[Business Intelligence Suite/Data Dictionary|Data dictionary]] · [[Business Intelligence Suite/How to Refresh|Refresh]]

## By event / list

| Event or list | Doctors |
|---|---|
| Barefoot list (no event or date in sheet) | 10883 |
| CPD webinar 10 Nov 2026 (registered, did not attend) | 559 |
| CPD webinar 10 Nov 2026 (attended) | 333 |

Doctors on more than one list: 73.

## Webinar audience (attended + registered no-shows, 892 doctors)

### By attendance status
| Attendance Status | Doctors | Share |
|---|---|---|
| Registered - did not attend | 559 | 63% |
| Attended | 312 | 35% |
| Attended (name only, unverified) | 21 | 2% |

### By specialty group
| Specialty Group | Doctors | Share |
|---|---|---|
| Nursing | 182 | 20% |
| Manager / Admin / Non-clinical | 155 | 17% |
| Allied / Other Clinical | 151 | 17% |
| General Practitioner | 96 | 11% |
| Not stated | 70 | 8% |
| Medical Officer | 63 | 7% |
| Doctor - specialty not stated | 48 | 5% |
| Physiotherapy / Rehab | 42 | 5% |
| Psychiatry / Psychology | 36 | 4% |
| Specialist Physician | 26 | 3% |
| Intern / Student | 10 | 1% |
| Surgeon / Orthopaedics | 8 | 1% |
| Paediatrics | 4 | 0% |
| Obstetrics & Gynaecology | 1 | 0% |

### By province
| Province | Doctors | Share |
|---|---|---|
| (blank) | 787 | 88% |
| Gauteng | 26 | 3% |
| KwaZulu-Natal | 23 | 3% |
| Western Cape | 20 | 2% |
| Limpopo | 12 | 1% |
| North West | 8 | 1% |
| Mpumalanga | 6 | 1% |
| Free State | 5 | 1% |
| Eastern Cape | 5 | 1% |

### Booked or not
| Booked | Doctors | Share |
|---|---|---|
| no | 747 | 84% |
| yes | 145 | 16% |

### Owner in HighLevel
| Owner | Doctors | Share |
|---|---|---|
| (blank) | 527 | 59% |
| Erich MedWave | 206 | 23% |
| Elmien Geldenhuys | 111 | 12% |
| Michael Steytler | 22 | 2% |
| Andries Maritz | 11 | 1% |
| Hazel Janecke | 5 | 1% |
| Rozanne Diederichs | 4 | 0% |
| Eddie VDW | 2 | 0% |
| Sterrenberg Smit | 2 | 0% |
| Karin Duranti | 2 | 0% |

### BDR (sheet split or HL bdr tag)
| Bdr | Doctors | Share |
|---|---|---|
| Erich | 85 | 26% |
| Mike | 83 | 25% |
| Hazel | 81 | 24% |
| Eddie | 80 | 24% |
| (blank) | 2 | 1% |
| Hazel, Mike | 1 | 0% |
| Erich, Hazel | 1 | 0% |

### DND
| Dnd | Doctors | Share |
|---|---|---|
| no | 493 | 55% |
| (blank) | 365 | 41% |
| yes | 34 | 4% |

### Pricing hold
| Pricing Hold | Doctors | Share |
|---|---|---|
| YES - no pricing at all | 892 | 100% |

## Barefoot list (10810 doctors)

**Do not contact these 10,810 Barefoot-only doctors.** They are in this suite as data only (Davide, 12 Nov 2026 14:34 SAST). The 73 doctors who also appear on a webinar list are counted with that webinar audience, not in this 10,810, and may be reached.

### By specialty group
| Specialty Group | Doctors | Share |
|---|---|---|
| Not stated | 8308 | 77% |
| General Practitioner | 1104 | 10% |
| Specialist Physician | 341 | 3% |
| Intern / Student | 312 | 3% |
| Medical Officer | 178 | 2% |
| Surgeon / Orthopaedics | 147 | 1% |
| Allied / Other Clinical | 107 | 1% |
| Paediatrics | 74 | 1% |
| Doctor - specialty not stated | 66 | 1% |
| Obstetrics & Gynaecology | 62 | 1% |
| Manager / Admin / Non-clinical | 49 | 0% |
| Psychiatry / Psychology | 49 | 0% |
| Physiotherapy / Rehab | 12 | 0% |
| Nursing | 1 | 0% |

### By province (from home area or landline code; many blank)
| Province | Doctors | Share |
|---|---|---|
| (blank) | 7764 | 72% |
| Gauteng | 932 | 9% |
| KwaZulu-Natal | 705 | 7% |
| Western Cape | 531 | 5% |
| Eastern Cape | 272 | 3% |
| Free State | 152 | 1% |
| Limpopo | 147 | 1% |
| Mpumalanga | 144 | 1% |
| North West | 106 | 1% |
| Northern Cape | 57 | 1% |

### In HighLevel
| In HighLevel | Doctors |
|---|---|
| yes | 476 |
| no | 10334 |

## Dataview

```dataview
TABLE attended, attended_booked, registered_no_show, refreshed_sast
FROM "Business Intelligence Suite"
WHERE bi_type = "dashboard"
```
