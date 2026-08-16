<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 2 — 5 Whys Root Cause Analysis

**Topic 1** · A2 · K2, K5 — Identify root causes with team members using structured group facilitation.

| Field | Detail |
|---|---|
| Case study | Meridian Health Screening — the 07:00 blood-test backlog |
| Duration | 45 minutes |
| Grouping | Teams of 3-5 |
| Tools | 5 Whys ed-tool, ChatGPT / Copilot / Gemini |
| Ed-tool | [5 Whys Tool](https://alfredang.github.io/5whys/) |

---

## The Scenario

Meridian Health operates six health-screening centres in Singapore. Corporate clients book annual screening packages; the fasting blood draw must happen between 07:00 and 09:30.

Over the last four months, 31% of morning appointments overrun by more than 40 minutes. Corporate clients have escalated twice. One major client (1,400 employees, S$310,000 annual contract) has given notice of review. The Operations Manager's proposal is to open a seventh centre at a capital cost of S$1.2m.

The Clinical Director is unconvinced. She has asked your team to establish the ROOT CAUSE before the board approves any capital expenditure. The nurses tell you the same thing every morning: "We're just short-staffed." The data below says something more interesting.

## The Evidence

*Meridian Health — morning screening operations, 4-month sample*

| Observation | Value |
|---|---|
| Booked slots 07:00-09:30 | 48 per centre |
| Phlebotomists rostered 07:00 | 3 of 5 |
| Phlebotomists rostered 08:30 | 5 of 5 |
| Mean draw time, trained staff | 6 min |
| Mean draw time, relief staff | 14 min |
| Relief staff share of morning roster | 40% |
| Repeat draws (failed first attempt) | 18% |
| Clients arriving without fasting compliance | 12% |
| Lab courier pickup (fixed) | 09:45 |
| Samples missing the 09:45 courier | 23% |
| Permanent staff turnover, 12 months | 44% |

## Step-by-Step

1. Read the Meridian Health scenario and study the operations table.
2. Appoint a facilitator (asks the whys and keeps the team on one branch) and a scribe.
3. Open the 5 Whys ed-tool at https://alfredang.github.io/5whys/
4. Enter the problem statement in the tool's problem field, using numbers from the table.
5. Ask Why #1. The facilitator's job: reject any answer that is an opinion, and ask 'what evidence supports that?'
6. Continue to five levels, entering each why and answer in the tool. Stay on ONE causal branch.
7. Mark the level where the answer stopped being a description of events and became a system explanation.
8. Run the same problem through the GenAI 5 Whys prompt from the slide, answering as the clinical team would.
9. Compare the two chains. Where they diverge, decide which branch the EVIDENCE supports and record why.
10. Write your root cause statement in one sentence, and note which levels remain unverified.
11. Present to the room in 90 seconds: the chain, the root cause, and your verdict on the S$1.2m proposal.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as a root cause analysis expert facilitating a clinical operations team.

Problem: 31% of morning health-screening appointments at Meridian Health overrun by more than 40 minutes, and 23% of blood samples miss the fixed 09:45 lab courier.

Evidence: only 3 of 5 phlebotomists are rostered at 07:00 (all 5 by 08:30); relief staff take 14 min per draw vs 6 min for trained staff; relief staff are 40% of the morning roster; 18% of draws need a repeat attempt; permanent staff turnover is 44% a year.

Apply the 5 Whys technique. Ask ONE why at a time and wait for my answer before asking the next. Go five levels deep.

At each level, state what EVIDENCE would confirm or refute that level — do not accept my answer at face value. If my answer is an opinion rather than a fact, say so and ask me for the data that would support it.

After level 5, summarise: the root cause, the evidence supporting it, and which levels remain unverified assumptions.
```

## Discussion Questions

1. Run the 5 Whys to five levels. At which level did you stop describing WHAT happens and start explaining WHY the system produces it?
2. The nurses say 'we're short-staffed'. The data shows all 5 phlebotomists are rostered by 08:30. What is the real constraint — headcount, or something else?
3. Trace the causal chain to 44% annual turnover. If turnover is the root cause, what does that say about the S$1.2m seventh centre proposal?
4. Where could this 5 Whys chain have gone wrong? Identify one point where a different, equally plausible 'why' would have led you somewhere completely different.
5. The GenAI facilitator challenged at least one of your answers as opinion rather than fact. Which one, and were you able to supply the evidence?

## Self-Check — Is Your Output Finished?

Your root cause is sound when you can answer YES to all three: (1) If this cause were removed, would the 31% overrun stop recurring — not just improve this month? (2) Is every level in the chain supported by a number in the evidence table, or explicitly flagged as an assumption? (3) Does the root cause point at a SYSTEM (policy, process, incentive) rather than at a person? If your chain ends at 'the relief staff are slow', you have found a symptom and blamed a human — go two levels deeper.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
