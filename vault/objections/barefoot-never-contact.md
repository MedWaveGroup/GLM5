---
title: Barefoot list never contact
---

## Barefoot list = never contact (Davide, 12 Nov 2026 14:34 SAST)
Doctors from the Barefoot list spreadsheet (Barefoot-List-Match-Workbook) must NEVER be messaged by any bot: no WhatsApp, SMS or email, any send kind (blast, reactivation, quiet-lead, sequence, re-touch, reply). They are data only, kept in the Business Intelligence Suite. Hard block in send_filters.py (`barefoot_never_contact`), matched on contactId, phone or email from /workspace/team/outreach-control/barefoot_no_contact_2026-11-12.csv (reloaded whenever the file changes). Webinar attendees and 10 Nov no-shows are NOT on this block; they follow normal rules (CPD no-pricing hold, 24h gap).
