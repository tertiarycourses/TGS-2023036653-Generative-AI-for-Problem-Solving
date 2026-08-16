<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 5 — System Loops: Why the Problem Keeps Coming Back

**Topic 1** · A3 · K2 — Deduce linkages and patterns to identify key implications on organisational systems.

| Field | Detail |
|---|---|
| Case study | Horizon Bank revisited — the fix that made it worse |
| Duration | 50 minutes |
| Grouping | Teams of 3-5 |
| Tools | System Loop ed-tool, ChatGPT / Copilot / Gemini |
| Ed-tool | [System Loop Tool](https://alfredang.github.io/systemloop/) |

---

## The Scenario

Return to Horizon Bank Jurong East. Acting on the fishbone, the Regional Director did the obvious thing: he ordered two additional counters staffed at peak, redeploying staff from the back office.

Month 1: average wait fell from 58 to 34 minutes. Everyone celebrated.
Month 4: average wait is back to 61 minutes — WORSE than before. Complaints are at 68 per month. Three more tellers have resigned. Back-office processing is now two days behind, which has started generating a new complaint category of its own.

The Regional Director is baffled: "We added capacity and the problem came back bigger. What am I missing?"

What he is missing is that a branch is not a queue — it is a system of feedback loops. Your team must map them.

## The Evidence

*Horizon Bank — system variables and observed 4-month movements*

| Variable | Month 1 | Month 4 | Direction |
|---|---|---|---|
| Counters staffed at peak | 3.2 | 5.1 | up |
| Average wait time (min) | 58 -> 34 | 61 | down then up |
| Back-office processing backlog (days) | 0.5 | 2.0 | up |
| Teller errors requiring rework | 6% | 14% | up |
| Rework returning to the counter | low | high | up |
| Teller overtime hours / month | 88 | 196 | up |
| Staff resignations (quarter) | 2 | 3 | up |
| Share of counter staff under 6 months | 44% | 58% | up |
| Mean transaction handling time (min) | 9 | 13 | up |
| Customer complaints / month | 60 | 68 | up |
| Digital channel adoption | 21% | 20% | flat |

## Step-by-Step

1. Read the revisited Horizon Bank scenario and the 4-month variable movements.
2. Open the System Loop ed-tool at https://alfredang.github.io/systemloop/
3. List the key variables from the table as nodes: counters staffed, wait time, backlog, errors, rework, overtime, resignations, inexperience, handling time, digital adoption.
4. Draw the loop the Director INTENDED: pressure -> counters -> capacity -> wait time down. Label it B1 and confirm it closes as balancing.
5. Now trace the redeployment: where did the back-office staff come from, and what happened downstream? Close that loop and label it R1.
6. Trace the workload consequences on people: overtime, resignations, inexperience, errors. Close it and label it R2.
7. Mark (+) or (-) on every link. Verify each loop: an even number of (-) links makes it reinforcing; an odd number makes it balancing.
8. Identify where the DELAY sits — which loop acts in days and which acts in months.
9. Ask which balancing loop is available but not running. Add B2 (digital adoption) and mark it dormant.
10. Run the GenAI system-thinking prompt from the slide and compare its loops against yours.
11. Circle two leverage points where breaking ONE link would collapse a reinforcing loop.
12. Present: the four loops, why month 1 lied to you, and your two leverage points.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as a systems thinking facilitator. Help me map the causal feedback loops in this case.

Situation: A bank branch added 2 counters at peak by redeploying back-office staff. Wait time fell from 58 to 34 minutes in month 1, then rose to 61 minutes by month 4 — worse than the starting point.

Observed changes over 4 months: back-office backlog 0.5 -> 2.0 days; teller errors 6% -> 14%; rework returning to the counter rose; overtime 88 -> 196 hrs/month; resignations rose; share of tellers under 6 months 44% -> 58%; mean handling time 9 -> 13 min; digital adoption flat at ~20%.

Produce:
1. At least 2 REINFORCING (R) loops and 2 BALANCING (B) loops. For each, list the variables in causal order with (+) or (-) on each link, and name the loop
2. Explain specifically WHY the month-1 improvement reversed — which loop overwhelmed which
3. Identify the delay in the system and explain why the delay made the wrong decision look right
4. Name 2 leverage points that would break the reinforcing loops, and say what makes them leverage rather than just more effort
```

## Discussion Questions

1. Map at least two reinforcing (R) and two balancing (B) loops. Which loop did the Regional Director believe he was pulling, and which loop did he actually trigger?
2. Month 1 showed real improvement. Explain the DELAY: why did the harmful loop take three months to overwhelm the helpful one, and what does that mean for how we evaluate quick wins?
3. Follow the back-office redeployment all the way round. Trace how a decision about counters ended up increasing teller resignations.
4. Digital adoption stayed flat at 20% throughout. Which loop is NOT running that should be, and why is a dormant balancing loop as dangerous as an active reinforcing one?
5. Name two leverage points. What makes a leverage point different from simply doing more of the same thing harder?

## Self-Check — Is Your Output Finished?

Your loop map is valid when: every loop CLOSES (the last variable feeds back to the first); every link carries a (+) or (-); each loop is correctly typed as R or B by counting negative links; you can explain the month-1-to-month-4 reversal by naming which loop overwhelmed which; and your leverage points break a LINK in a reinforcing loop rather than adding more effort to a balancing one. If your answer is 'hire more people', you have described effort, not leverage.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
