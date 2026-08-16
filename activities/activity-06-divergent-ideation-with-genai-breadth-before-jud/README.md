<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 6 — Divergent Ideation with GenAI (Breadth Before Judgement)

**Topic 2** · A5 · K4 — Generate a wide solution set using appropriate problem-solving techniques.

| Field | Detail |
|---|---|
| Case study | Meridian Health — solving the retention root cause |
| Duration | 45 minutes |
| Grouping | Teams of 3-5 |
| Tools | ChatGPT / Copilot / Gemini, Pinboard |
| Ed-tool | [Pinboard](https://alfredang.github.io/pinboard/) |

---

## The Scenario

Your 5 Whys in Activity 2 established the root cause at Meridian Health: a workforce retention and onboarding failure that leaves 40% of the 07:00 roster staffed by untrained relief phlebotomists at 14 minutes per draw instead of 6.

The Clinical Director has accepted the analysis and killed the S$1.2m seventh-centre proposal. She now wants options — and she has been explicit: "Don't bring me three sensible ideas. Bring me twenty, including the ones that sound ridiculous, and then tell me which four are real."

Budget guidance: up to S$250,000 over 12 months. Constraint: MOH clinical protocols on phlebotomy competency cannot be relaxed under any circumstances.

## The Evidence

*Meridian Health — solution constraints and context*

| Constraint | Detail |
|---|---|
| Budget | Up to S$250,000 over 12 months |
| Clinical | MOH phlebotomy competency standards are non-negotiable |
| Contract | 07:00-09:30 fasting draw window is contractual with corporate clients |
| Courier | Lab courier at 09:45 is fixed by the external lab partner |
| Workforce | Permanent phlebotomist turnover 44%/yr; relief pool is agency-supplied |
| Training | Current onboarding is 2 days shadowing, no structured sign-off |
| Market | Phlebotomist salaries are within 5% of the market median |
| Shift | Early shift (06:30 start) attracts no differential pay |

## Step-by-Step

1. Restate the Meridian root cause from Activity 2 in one sentence so the whole team is solving the same thing.
2. MANUAL ROUND FIRST — set a 7-minute timer. Each person writes ideas silently on post-its. No discussion, no evaluation, no 'that won't work'.
3. Post all ideas to the wall at https://alfredang.github.io/pinboard/ and count them.
4. Now run the GenAI divergent ideation prompt from the slide.
5. Add every AI idea your team did not already have to the board, in a different colour.
6. Count the two groups. Discuss: which AI ideas would nobody in your team have proposed in a real meeting, and what stopped them?
7. Run the SCAMPER section of the prompt against the '07:00-09:30 at the centre' assumption.
8. For each SCAMPER letter, add the resulting idea to the board.
9. Go through the board and mark each idea HARD CONSTRAINT (genuinely ruled out by MOH or contract) or HABIT (only feels fixed).
10. Do NOT rank or cost anything yet — carry the full board forward to Activity 7.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as an innovation consultant running a divergent ideation session. Do NOT evaluate or filter yet.

Root cause to solve: A Singapore health-screening operator has 44% annual turnover among permanent phlebotomists. Vacancies are backfilled by agency relief staff who take 14 min per blood draw versus 6 min for trained staff. 40% of the 07:00 roster is relief staff, causing 31% of morning appointments to overrun and 23% of samples to miss the fixed 09:45 lab courier.

Constraints: S$250k over 12 months; MOH phlebotomy competency standards cannot be relaxed; the 07:00-09:30 fasting window and the 09:45 courier are both fixed.

Generate 20 distinct solutions grouped under:
- People & Retention
- Training & Onboarding
- Process & Scheduling
- Technology & Automation
- Customer/Client Experience

Rules:
- Include at least 4 ideas that would normally be dismissed as unrealistic
- Include at least 2 ideas borrowed from a COMPLETELY different industry (say which)
- One line each, phrased as an action
- Do NOT rank, cost or evaluate them

Then, separately: apply SCAMPER (Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse) to the single assumption that 'every draw must be done by a phlebotomist at the centre between 07:00 and 09:30' and give one idea per SCAMPER letter.
```

## Discussion Questions

1. Your team generated ideas manually first, then with GenAI. Compare the two lists — how many did the AI produce that your team would never have said out loud, and why not?
2. The AI was asked for two ideas borrowed from another industry. Which cross-industry idea is most transferable to Meridian, and what would have to be true for it to work?
3. Apply SCAMPER's 'Reverse' and 'Eliminate' to the fixed 07:00-09:30 window. Which supposedly fixed constraint turns out to be an assumption rather than a real constraint?
4. Identify one idea on your list that is genuinely ruled out by the MOH clinical constraint. How do you tell a hard constraint from a habit?
5. Cognitive fixedness is the tendency to reach for the familiar solution. Find one idea on your list that only appeared because you deliberately broke fixedness — what triggered it?

## Self-Check — Is Your Output Finished?

Your divergence is sufficient when: you have at least 20 distinct ideas spanning all five groups; at least 4 would raise an eyebrow in a management meeting; at least 2 are borrowed from another industry and you can name it; you have one idea per SCAMPER letter; and you have correctly separated at least one HARD CONSTRAINT from at least one HABIT. If every idea on your board is comfortable, you have not diverged — you have listed.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
