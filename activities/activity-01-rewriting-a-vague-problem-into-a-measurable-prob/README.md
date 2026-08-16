<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 1 — Rewriting a Vague Problem into a Measurable Problem Statement

**Topic 1** · A1 · K1 — Identify the type of performance deficiency and express it as a measurable problem statement.

| Field | Detail |
|---|---|
| Case study | ShopFront SG — 'Customers are unhappy and sales are dropping' |
| Duration | 45 minutes |
| Grouping | Teams of 3 |
| Tools | ChatGPT / Copilot / Gemini, CollabNote |
| Ed-tool | [CollabNote](https://alfredang.github.io/collabnote/) |

---

## The Scenario

ShopFront SG is a 42-outlet fashion retailer with an e-commerce site and a mobile app. At the Monday management meeting the Head of Retail Operations opens with one line: "Customers are unhappy and sales are dropping — fix it." No metric, no baseline, no scope. Three departments leave the room with three different interpretations. Marketing books a S$180,000 discount campaign. IT starts an app redesign. Customer Service hires two temps. Ninety days later the complaint rate is unchanged and the budget is gone.

You are the business analyst asked to restate the problem BEFORE any more money is committed. The dashboard extract below is all the evidence you have.

## The Evidence

*ShopFront SG — 90-day performance extract*

| Metric | 12 months ago | Current | Industry benchmark |
|---|---|---|---|
| Average app page load | 2.1 s | 4.8 s | under 2.0 s |
| Checkout completion rate | 68% | 51% | 70% |
| Cart abandonment | 61% | 74% | 60% |
| CSAT (post-purchase) | 84% | 70% | 85% |
| Repeat purchase (90-day) | 38% | 29% | 40% |
| Complaint tickets / week | 120 | 410 | - |
| In-store sales | S$4.2m/mo | S$4.1m/mo | - |
| Online sales | S$2.8m/mo | S$1.9m/mo | - |

## Step-by-Step

1. Read the ShopFront SG scenario and the 90-day evidence table as a team.
2. Individually and in silence, underline the one metric you believe is the real performance deficiency. Do not discuss yet — this prevents anchoring on the loudest voice.
3. Compare choices around the table. Where you disagree, argue from the numbers only.
4. Draft the problem statement on paper with all six elements labelled: Context, Metric, Baseline, Target, Timeframe, Constraints.
5. Open your GenAI tool and run the Problem Statement prompt supplied on the slide.
6. Compare the AI output against your draft. Highlight every specific the AI supplied that the evidence did not support — label each one 'ASSUMPTION'.
7. Merge the two into a final statement your team can defend to the Head of Retail Operations.
8. Post the final statement to the shared wall at https://alfredang.github.io/collabnote/
9. Nominate one speaker to read it out in 60 seconds and name the one assumption you are least comfortable with.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
You are a business analyst for a Singapore fashion retailer.

Refine the vague statement below into ONE clear, measurable problem statement.

Vague statement: "Customers are unhappy and sales are dropping."

Evidence:
- App page load rose from 2.1s to 4.8s (benchmark <2.0s)
- Checkout completion fell 68% -> 51% (benchmark 70%)
- Cart abandonment rose 61% -> 74%
- CSAT fell 84% -> 70%
- Online sales fell S$2.8m -> S$1.9m per month; in-store flat

Your problem statement MUST contain, each labelled:
- Context (who, where, which process)
- Metric (the single primary measure)
- Baseline (where it is now, with the number)
- Target (where it must be, with the number)
- Timeframe (by when)
- Constraints (budget, headcount, compliance, brand)

Then list any assumption you had to make, and state what additional evidence would let you remove that assumption. Do not propose solutions yet.
```

## Discussion Questions

1. Which metric in the table is the SYMPTOM the executive noticed, and which metric is closest to the actual performance deficiency? Justify with the numbers.
2. The evidence shows in-store sales are flat while online sales fell 32%. What does that single contrast rule out as a cause, and why does that matter before you spend a dollar?
3. Write the problem statement with all six elements. Which element was hardest to fill, and what does the gap tell you about your organisation's data?
4. Compare your team's statement with the GenAI-generated one. What did the AI assume that is NOT supported by the evidence? (Every team will find at least one.)
5. Whose sign-off do you need on this problem statement before work starts, and what would you show them to get it?

## Self-Check — Is Your Output Finished?

Your statement is complete when a colleague who was NOT in the room can read it and correctly state (a) which metric is being fixed, (b) the number it is at today, (c) the number it must reach, (d) by when, and (e) what you are not allowed to change — without asking you a question. If any of the five is missing, the statement is not finished.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
