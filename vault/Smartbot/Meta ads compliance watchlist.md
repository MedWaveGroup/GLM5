---
title: "Smartbot Meta ads compliance watchlist"
tags: [medwave, brain, smartbot, meta, compliance]
source: "MEDWAVE_META_ADS_WATCHLIST_2026-11-02.md (digest of VCA Don't Get Your Ads Banned v1.1 and VCA Meta Ads Playbook v1.1, verified 2 Nov 2026 against Meta Advertising Standards). 6 Nov research: no change to this watchlist."
date: 2026-11-02
updated: 2026-11-18
privacy: "no lead or customer names, phones, emails, HighLevel contact IDs, or deposit-by-person details"
---

# Meta ads compliance watchlist

Digest written by Smartbot on 2 Nov 2026 from two VCA guides. The guides say they were verified that day against Meta's Advertising Standards. They are guidance, not legal advice. Meta changes policy without notice; check [transparency.meta.com](https://transparency.meta.com). Full guide text remains in `/workspace/meta_guides/banned.txt` and `playbook.txt` on the box.

6 Nov research (R9): a third-party blog claimed a July 2026 Meta health-policy rewrite, while Meta's Transparency page still dated 27 Dec 2024. **No change** was made to MedWave rules or this watchlist on the back of that.

No existing vault note was a dedicated copy of this watchlist, so this is the tracked version. Related rules in the brain: [[standing-rules]] · [[products-positioning]] · [[channels]].

Related: [[Smartbot/Smartbot]] · [[Smartbot/Research and competitor learnings]] · [[Smartbot/Improvement Log]]

## How accounts get lost (most important)

- Meta punishes patterns, in steps: one ad rejected, then the ad account, then the whole Business Manager (every account, Page and pixel), then the person's profile.
- Never re-upload a rejected ad or duplicate it into another ad set. Never open new accounts to get around a restriction. Never misspell words or hide text in images to slip past the filters.
- When an ad is rejected: stop, read the policy Meta cites, find the real cause (copy, every video frame, the audio, the landing page), fix it, ask for one review, and log it.
- Check Account Quality (business.facebook.com/accountquality) every Monday. Don't edit a live ad many times in a short period, because each edit triggers a new review.
- The payment method should be in MedWave's name. On 2 Nov the Master Ads account had an unpaid balance after declined payments (morning figure in the source watchlist: $1,807.02; the evening CEO input recorded $1,859.04). Settling it protects the account.

## Medical device rules (red light / PBM)

- The risk is in the claims. Symptom-management wording is allowed ("may help relieve muscle soreness"); cure claims aren't ("cures arthritis").
- Never claim to cure, heal, reverse or eliminate anything on Meta's list: diabetes, thyroid, psoriasis, cancer, autism, Alzheimer's, Parkinson's, ALS, HIV, herpes, Ebola. This matters for MedWave's neurological and metabolic messages, even in SA.
- Use the exact registration wording. "FDA cleared" is not "FDA approved", and never claim SAHPRA registration a device doesn't have. Proof goes on the page.
- Clinical claims need the actual study on the landing page, not "studies show".
- Use real, named practitioners with their consent. No stock "doctor in a white coat", no AI doctors or testimonials.
- Demonstration works best: show the device, the experience, and a practitioner explaining it. This matches Davide's device-as-hero rule.
- No "wear it and it works" claims (Meta rule since July 2026). This matters for any wearable pad or wrap.

## Copy red flags

- "You" plus a condition gets rejected: "Suffering from joint pain?", "Struggling with your back pain?". Describe the product or the practice, not the viewer. B2B framing ("Add a recovery room to your practice") naturally avoids this.
- No absolutes (guaranteed, 100%, permanent, instant, risk-free, no side effects). No set result in a set time. No fake urgency.
- Amber words need proof, a true offer, or 18+ targeting: weight loss, recovery, anti-inflammatory, pain relief, clinically proven, medical-grade, before and after, doctor recommended, limited time.
- Testimonials must be real and typical, or carry "results vary". Prices and offers must match the page exactly.
- Weight-loss, health and cosmetic ads must be targeted 18+.

## Video and creative

- Meta scans every frame, the captions and the audio transcript. Watch the whole video with sound and read the SRT file end to end before upload.
- Never: fat-pinching or body-shaming shots, needles or injection imagery, graphic wounds (watch MedWave wound-care content), fake play buttons or notifications, celebrities without a release, unlicensed music.

## Landing page and the whole site

- A clean ad pointing to a non-compliant page still gets rejected, and every page on the domain counts, including the blog and shop.
- For MedWave this was the biggest live risk on 2 Nov. Legal and QA had flagged the Neuro-100S page (3-4cm and condition claims), `/metabolic-health-mitochondria/`, `/60-day-trial/` and `/roi-calculator/`. `/cpd-event/` still showed a placeholder.
- The page must match the ad's offer, work on mobile, and show a privacy policy and contact details.
- Moderate comments on live ads. A reply like "yes, it cured my client's arthritis" counts as a claim.
- Organic posts on the advertising Page are reviewed too.

## Tracking (UTM and booking-attribution work)

- Meta may limit health and wellness accounts. That strips URL paths and custom parameters and blocks lower-funnel events (Lead, Purchase) for optimisation, on both Pixel and Conversions API. Page View and View Content still work. This explained Meta Ad bot's finding that Meta strips URL paths.
- Keep health terms out of URLs, event names and parameters (no "weight-loss-booking", no "pain_lead"). Keep the pixel off patient and booking-confirmation pages. Use Instant Forms for lead gen. Never disguise health data to get around the limit.
- Health-condition targeting has been gone since 2022, so use broad targeting and let the creative find the audience.
- Custom audiences must not be built from health-condition data or patient lists. Under POPIA, customer lists (for example MedX buyers) may only be uploaded if those people consented to marketing.

## Pre-launch ban test (any "yes" means it doesn't go live)

1. Names a prescription drug, GLP-1 or peptide?
2. Claims to cure, heal, reverse or eliminate?
3. A specific result in a specific time?
4. Implies the viewer has a condition, body issue, age or money problem?
5. A fat pinch or weight-loss before and after in any frame?
6. A needle, vial, pill or prescription pack in any frame?
7. A celebrity, fake doctor, deepfake or fake review?
8. Absolutes (guaranteed, 100%, permanent, instant, no side effects)?
9. Does the landing page or any page on the site say something the ad couldn't?
10. Age targeting under 18 on a health ad?

## Suggested actions (for Master Control to assign, 2 Nov)

- Meta Ad bot: add the 10-question test and a Monday Account Quality check to its routine. Check live ads' landing pages against the flagged page list. Make sure planned UTMs and HighLevel field names use neutral, non-health words.
- Content bot, QA and Legal: add the "you plus condition" rule, the requirement to read the SRT, and the "every page on the domain counts" rule to the shared rules file.
- Davide: approve the website clean-up list (already coming from Legal), because it blocks ads as well as compliance. Settle the Meta balance.

Back to [[Smartbot/Smartbot]].
