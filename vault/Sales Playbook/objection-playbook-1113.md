---
title: "Objection and booking playbook (13 Nov 2026)"
tags: [medwave, brain, sales-playbook, objections, booking]
source: "Davide 13 Nov 10:18 SAST; objection bot v1.4; reels DfnTwRinBWf, Dfm-f1fznqw, DduWil6J55E"
date: 2026-11-13
---


# Objection and booking playbook (13 Nov 2026)

Machine-readable twin: `/workspace/objections/playbook_1113.json`. Follow-ups: [[follow-up-cadence]]. Principles: [[jeremy-miner-nepq]], [[alex-hormozi]]. Outcomes: [[learning-log]].

## Message format (Davide, 13 Nov)

- Every lead message is short, succinct lines. **Send each numbered line as its own text, one after the next.** No paragraphs.

## Hard rules

- CPD-tagged doctors: no pricing at all; only variants with cpd_safe=true
- Only approved figures: practitioner cash line and finance monthly line, verbatim
- Provider in my area is an objection, never a disqualifier, never DND
- No medical cure or outcome claims; say 'red light (PBM)'
- No links in lines; the watcher adds the Meet link only in the booking confirmation
- No repeated wording across variants; rotate, never resend a variant to the same lead
- Max 3 automated touches/day 06:00-22:00; booked leads never messaged; hard stops unchanged

## Approved figures (verbatim only)

- Practitioner cash line: Our entry system is R100,000 and goes up to R350,000, excluding VAT. Most practices pay this off in 2–3 months.
- Finance line: It works out to about R2,174/month for the Neuro Mobile and R4,131/month for the Neuro 100-S. That's 11% over 60 months, no deposit, excl. VAT.
- Neither ever goes to a CPD-tagged doctor (incl. 'cpd - attended').

## Placeholders

- `{slot1}`, `{slot2}`: two free :00/:30 slots with 45 min free, on the right calendar (Davide → Elmien → Andries order per ownership rules; never Andries 09:00–10:00). `{first_name}` where used.

## Objections

### Too expensive / price (`too_expensive_price`)

> CPD-tagged: use variant 3 only (no figures).

**Variant 1** — **practitioners only, never CPD-tagged**  
Principles: `H-stakes` Hormozi reel: high stakes and hard to un-make means best, not cheapest; `H-analogy` Hormozi reel: answer objections with an analogy, not an explanation; `M-isolate` Miner NEPQ: isolate the real reason (money vs belief vs timing); `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Totally fair, it's a big decision 🙂
2. Nobody picks the cheapest surgeon for their own knee.
3. When it's hard to undo, you want the one that works.
4. Is it the total amount, or how it's paid that worries you?
5. Happy to unpack it on a short call, {slot1} or {slot2}?

**Variant 2** — **practitioners only, never CPD-tagged**  
Principles: `T-invest` Thiago Reis reel, door 3 investment: is the investment smaller than the cost of keeping the problem?; `M-consequence` Miner NEPQ: soft consequence question (what happens if nothing changes); `H-value` Hormozi value equation: raise perceived value (outcome, likelihood) before price; `M-commit` Miner NEPQ: commitment question as a choice of two times
_Note: Practitioners only. Never to CPD-tagged doctors._
1. I hear you.
2. It works out to about R2,174/month for the Neuro Mobile and R4,131/month for the Neuro 100-S.
3. That's 11% over 60 months, no deposit, excl. VAT.
4. What does it cost you each month to keep turning those patients away?
5. Shall we run your numbers together {slot1}, or is {slot2} better?

**Variant 3**  
Principles: `D-system` Davide (objection bot): we don't sell a box, we sell a system around your practice; `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `H-whole` Hormozi reel: 'what's the most important part of a car?' sell the whole system, not a part; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Makes sense to check that properly.
2. We don't sell a box, we set up a whole system around your practice.
3. Install, training for your team, and support after go-live.
4. Expensive compared to what you had in mind, or to another quote?
5. Let me show you what's included, would {slot1} or {slot2} suit?

### Asks for the cash / full price (`cash_price`)

> CPD-tagged: never quote. Use variant 3.

**Variant 1** — **practitioners only, never CPD-tagged**  
Principles: `H-stakes` Hormozi reel: high stakes and hard to un-make means best, not cheapest; `M-solution` Miner NEPQ: solution-awareness question, let them picture the outcome; `M-commit` Miner NEPQ: commitment question as a choice of two times
_Note: Approved practitioner cash line only (Davide 13 Nov)._
1. Sure, straight answer.
2. Our entry system is R100,000 and goes up to R350,000, excluding VAT.
3. Most practices pay this off in 2–3 months.
4. What are you hoping it will do for your practice?
5. I can map the right option for you {slot1} or {slot2}, which works?

**Variant 2** — **practitioners only, never CPD-tagged**  
Principles: `T-invest` Thiago Reis reel, door 3 investment: is the investment smaller than the cost of keeping the problem?; `M-problem` Miner NEPQ: problem-awareness question, let them say the problem in their words; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Happy to share.
2. Our entry system is R100,000 and goes up to R350,000, excluding VAT.
3. Most practices pay this off in 2–3 months.
4. Which patients would you want to help first with it?
5. Quick Meet to pick the right size, {slot1} or {slot2}?

**Variant 3**  
Principles: `D-system` Davide (objection bot): we don't sell a box, we sell a system around your practice; `T-clarity` Thiago Reis reel, door 2 clarity: can you see the solution solving your problem?; `M-commit` Miner NEPQ: commitment question as a choice of two times
_Note: CPD-safe: no figures._
1. Good question, it depends on the setup you'd need.
2. Room size, patient load and which system all change it.
3. Rather than guess, let's get you the right answer.
4. Fifteen minutes on Google Meet, {slot1} or {slot2}?

### No time / too busy (`no_time_busy`)

**Variant 1**  
Principles: `M-neutral` Miner NEPQ: neutral, detached tone, no pressure, give them the out; `H-time` Hormozi reel: you can't build muscle in a week; results take the time they take; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Completely get it, practices are flat out.
2. That's actually why most owners look at this.
3. It's 20 minutes, no prep needed.
4. Could you squeeze in {slot1}, or would {slot2} be kinder to your diary?

**Variant 2**  
Principles: `M-consequence` Miner NEPQ: soft consequence question (what happens if nothing changes); `T-priority` Thiago Reis reel, door 1 priority: is this a priority now? if not, close the door without pushing; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. No stress at all.
2. Quick one though, if your week stays this packed, what gives first?
3. If it's not a priority right now, just say so and I'll step back.
4. If it is, I've held {slot1} and {slot2} for you.

**Variant 3**  
Principles: `S-human` Jordan Stupar reel: humanise, put a face to the name (selfie video after the call), stand out from other vendors; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Busy is a good sign 🙂
2. I'll keep it tight and to the point, promise.
3. Phone or Meet, whatever's easier.
4. Does {slot1} work, or {slot2}?

### Send me info first (`send_info_first`)

**Variant 1**  
Principles: `S-value` Jordan Stupar reel: offer something of value to send ('a video that shows what we do') to earn the next step; `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Of course, I'll send the brochure here.
2. So I send the right bits, what made you look at this?
3. Easier still, I can walk you through it live.
4. Are you free {slot1} or {slot2}?

**Variant 2**  
Principles: `H-value` Hormozi value equation: raise perceived value (outcome, likelihood) before price; `T-clarity` Thiago Reis reel, door 2 clarity: can you see the solution solving your problem?; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Sending it over now.
2. Info only tells half the story though.
3. Seeing it fitted to your practice is where it clicks.
4. Grab 20 minutes with me, {slot1} or {slot2}?

**Variant 3**  
Principles: `M-problem` Miner NEPQ: problem-awareness question, let them say the problem in their words; `T-ready` Thiago Reis reel: don't convince anyone; advance only those ready to buy; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Will do 🙂
2. Out of interest, what would you need to see to know it's right for you?
3. I'll make sure we cover exactly that.
4. Could we pencil in {slot1}, or is {slot2} easier?

### Already a provider in my area (`provider_in_area`)

> Objection, never a disqualifier. Demand far outstrips supply. Never set DND for this.

**Variant 1**  
Principles: `D-demand` Davide rule: a provider nearby is never a disqualifier; demand far outstrips supply; `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Good to know, thanks for telling me.
2. Honestly, demand is far bigger than what providers can handle right now.
3. Most areas have room for several.
4. Let's look at your area together, {slot1} or {slot2}?

**Variant 2**  
Principles: `H-analogy` Hormozi reel: answer objections with an analogy, not an explanation; `D-demand` Davide rule: a provider nearby is never a disqualifier; demand far outstrips supply; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Think of it like physios, one in a suburb never fills the need.
2. Patients pick the practice they already trust, that's you.
3. Want to see how it'd sit alongside yours?
4. I'm free {slot1} and {slot2}.

**Variant 3**  
Principles: `M-problem` Miner NEPQ: problem-awareness question, let them say the problem in their words; `T-clarity` Thiago Reis reel, door 2 clarity: can you see the solution solving your problem?; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Fair point.
2. Are your own patients already asking about it?
3. If they are, they'd rather stay with you than go elsewhere.
4. Can I show you how others handle that, {slot1} or {slot2}?

### Need to think about it (`need_to_think`)

**Variant 1**  
Principles: `H-water` Hormozi reel: the water won't get warmer; waiting doesn't improve the decision; `M-isolate` Miner NEPQ: isolate the real reason (money vs belief vs timing); `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Of course, it's a real decision.
2. Just so I help you think it through, what's the part you're unsure of?
3. The water won't get warmer while we wait 🙂
4. Let's clear it up together, {slot1} or {slot2}?

**Variant 2**  
Principles: `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `T-priority` Thiago Reis reel, door 1 priority: is this a priority now? if not, close the door without pushing; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Totally fair.
2. Is it the fit for your practice, or the timing?
3. Either way, I'd rather you decide with all the facts.
4. Would {slot1} or {slot2} give you enough time to chat it through?

**Variant 3**  
Principles: `M-consequence` Miner NEPQ: soft consequence question (what happens if nothing changes); `M-neutral` Miner NEPQ: neutral, detached tone, no pressure, give them the out; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. No rush from my side.
2. What would need to be true for this to be a clear yes?
3. And if it's a no, that's fine too.
4. Short call to land it, {slot1} or {slot2}?

### Need to talk to my partner (`talk_to_partner`)

**Variant 1**  
Principles: `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Makes total sense.
2. What do you think their main question will be?
3. Easiest is if they join us, then nothing gets lost.
4. Could you both do {slot1} or {slot2}?

**Variant 2**  
Principles: `M-isolate` Miner NEPQ: isolate the real reason (money vs belief vs timing); `T-ready` Thiago Reis reel: don't convince anyone; advance only those ready to buy; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Of course.
2. Just between us, are you keen on it yourself?
3. If you are, I'll help you show them the numbers.
4. Shall I book the three of us for {slot1}, or {slot2}?

**Variant 3**  
Principles: `S-human` Jordan Stupar reel: humanise, put a face to the name (selfie video after the call), stand out from other vendors; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Great, let's include them.
2. I'll keep it simple, a quick walk-through for both of you.
3. Which suits better, {slot1} or {slot2}?

### Not interested now / next year (`not_interested_now`)

> A plain 'stop'/opt-out is a hard stop, not an objection.

**Variant 1**  
Principles: `D-humour` Davide (objection bot): light humour then an isolating question ('we can talk in 2029 🙂'); `M-isolate` Miner NEPQ: isolate the real reason (money vs belief vs timing); `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Sure, we can talk in 2029 if that helps 🙂
2. Out of curiosity, is it doubt about the tech or more the budget right now?
3. Either one I can help with.
4. Ten minutes, {slot1} or {slot2}?

**Variant 2**  
Principles: `D-blame` Davide (objection bot): take the blame, 'I haven't given you anything to be interested in'; `H-blame` Hormozi CLOSER (objection bot v1.4): peel the onion of blame, circumstances, others, self; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. That's my fault, I haven't given you a reason to be interested yet.
2. Let me fix that properly.
3. A quick look at what it does for a practice like yours.
4. Is {slot1} or {slot2} open?

**Variant 3**  
Principles: `T-priority` Thiago Reis reel, door 1 priority: is this a priority now? if not, close the door without pushing; `M-neutral` Miner NEPQ: neutral, detached tone, no pressure, give them the out; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. No problem at all.
2. When would it become a priority for you?
3. If anything shifts sooner, I'm here.
4. Or we can lock in a no-pressure chat now, {slot1} or {slot2}?

### Does it work? / evidence (`does_it_work_evidence`)

> No cure or medical outcome claims. Say red light (PBM).

**Variant 1**  
Principles: `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `T-clarity` Thiago Reis reel, door 2 clarity: can you see the solution solving your problem?; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Great question, you should be sceptical.
2. What would good evidence look like for you?
3. I'll walk you through the published research on red light (PBM) properly.
4. Does {slot1} or {slot2} work?

**Variant 2**  
Principles: `H-recipe` Hormozi reel: follow the recipe and you get the cake; the steps work regardless of who you are; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Fair to ask.
2. Same recipe, same steps, that's how our practices get consistent results.
3. We train your team on the exact protocol.
4. Happy to show you the steps, {slot1} or {slot2}?

**Variant 3**  
Principles: `M-problem` Miner NEPQ: problem-awareness question, let them say the problem in their words; `M-solution` Miner NEPQ: solution-awareness question, let them picture the outcome; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Which patients were you thinking of using it with?
2. Then I can show you the research that matches.
3. Let's go through it together, {slot1} or {slot2}?

### How does it work? (`how_does_it_work`)

**Variant 1**  
Principles: `H-whole` Hormozi reel: 'what's the most important part of a car?' sell the whole system, not a part; `D-system` Davide (objection bot): we don't sell a box, we sell a system around your practice; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. It's red light (PBM) with a vibration plate, run in your rooms.
2. We install it, train your team and support you after.
3. Much easier to show than type 🙂
4. Quick screen-share, {slot1} or {slot2}?

**Variant 2**  
Principles: `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Love that you asked.
2. Are you asking for your patients, or for running it in the practice?
3. I'll tailor the walk-through to that.
4. Free at {slot1} or {slot2}?

**Variant 3**  
Principles: `H-analogy` Hormozi reel: answer objections with an analogy, not an explanation; `T-clarity` Thiago Reis reel, door 2 clarity: can you see the solution solving your problem?; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Think of it as a full setup, not just a device.
2. Light panel, plate, protocols and training all working together.
3. Can I show you how a session runs?
4. Pick one, {slot1} or {slot2}.

### Where are you? / online or in person (`location_online`)

**Variant 1**  
Principles: `M-neutral` Miner NEPQ: neutral, detached tone, no pressure, give them the out; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. We're national, and the first chat is on Google Meet.
2. So it doesn't matter where you're based.
3. Shall I send a link for {slot1} or {slot2}?

**Variant 2**  
Principles: `S-human` Jordan Stupar reel: humanise, put a face to the name (selfie video after the call), stand out from other vendors; `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Good question.
2. Where's your practice based?
3. We'll start on a video call, then install on site.
4. Would {slot1} or {slot2} be better for the call?

### Already have similar equipment (`already_have_similar`)

**Variant 1**  
Principles: `M-problem` Miner NEPQ: problem-awareness question, let them say the problem in their words; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Nice, so you know the space already.
2. How's it going for you so far?
3. What would you want more of from it?
4. Worth a comparison call, {slot1} or {slot2}?

**Variant 2**  
Principles: `H-whole` Hormozi reel: 'what's the most important part of a car?' sell the whole system, not a part; `D-system` Davide (objection bot): we don't sell a box, we sell a system around your practice; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Makes sense.
2. The device is only one part, the protocols and support are what make it pay.
3. Let me show you how ours fits around what you've got.
4. Have you got {slot1} or {slot2}?

**Variant 3**  
Principles: `M-consequence` Miner NEPQ: soft consequence question (what happens if nothing changes); `T-invest` Thiago Reis reel, door 3 investment: is the investment smaller than the cost of keeping the problem?; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Interesting.
2. Is it busy enough, or are some sessions sitting empty?
3. Either way, there may be a gap we can fill.
4. Quick look together, {slot1} or {slot2}?

### Patient vs practitioner (who is asking) (`patient_vs_practitioner`)

> Patients: no equipment pricing; patient price line stays notify-only; hand to owner.

**Variant 1**  
Principles: `M-clarify` Miner NEPQ: clarify the objection with a soft question before answering it; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Thanks for reaching out!
2. Is this for your practice, or are you looking for treatment yourself?
3. If it's for your practice, I have {slot1} or {slot2} to walk you through it.

**Variant 2**  
Principles: `M-neutral` Miner NEPQ: neutral, detached tone, no pressure, give them the out; `M-commit` Miner NEPQ: commitment question as a choice of two times
1. Quick check so I point you the right way.
2. Are you a practitioner, or a patient looking for sessions?
3. Practitioners, I'd love to show you the setup {slot1} or {slot2}.

## Principle key

- `M-clarify`: Miner NEPQ: clarify the objection with a soft question before answering it
- `M-isolate`: Miner NEPQ: isolate the real reason (money vs belief vs timing)
- `M-consequence`: Miner NEPQ: soft consequence question (what happens if nothing changes)
- `M-problem`: Miner NEPQ: problem-awareness question, let them say the problem in their words
- `M-solution`: Miner NEPQ: solution-awareness question, let them picture the outcome
- `M-neutral`: Miner NEPQ: neutral, detached tone, no pressure, give them the out
- `M-commit`: Miner NEPQ: commitment question as a choice of two times
- `H-stakes`: Hormozi reel: high stakes and hard to un-make means best, not cheapest
- `H-analogy`: Hormozi reel: answer objections with an analogy, not an explanation
- `H-water`: Hormozi reel: the water won't get warmer; waiting doesn't improve the decision
- `H-recipe`: Hormozi reel: follow the recipe and you get the cake; the steps work regardless of who you are
- `H-time`: Hormozi reel: you can't build muscle in a week; results take the time they take
- `H-whole`: Hormozi reel: 'what's the most important part of a car?' sell the whole system, not a part
- `H-blame`: Hormozi CLOSER (objection bot v1.4): peel the onion of blame, circumstances, others, self
- `H-value`: Hormozi value equation: raise perceived value (outcome, likelihood) before price
- `T-priority`: Thiago Reis reel, door 1 priority: is this a priority now? if not, close the door without pushing
- `T-clarity`: Thiago Reis reel, door 2 clarity: can you see the solution solving your problem?
- `T-invest`: Thiago Reis reel, door 3 investment: is the investment smaller than the cost of keeping the problem?
- `T-ready`: Thiago Reis reel: don't convince anyone; advance only those ready to buy
- `S-human`: Jordan Stupar reel: humanise, put a face to the name (selfie video after the call), stand out from other vendors
- `S-value`: Jordan Stupar reel: offer something of value to send ('a video that shows what we do') to earn the next step
- `D-system`: Davide (objection bot): we don't sell a box, we sell a system around your practice
- `D-humour`: Davide (objection bot): light humour then an isolating question ('we can talk in 2029 🙂')
- `D-blame`: Davide (objection bot): take the blame, 'I haven't given you anything to be interested in'
- `D-demand`: Davide rule: a provider nearby is never a disqualifier; demand far outstrips supply
- `D-lines`: Davide 13 Nov: short succinct lines, each sent as its own text
