<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 3 — Fishbone (Ishikawa) Diagram for Breadth of Causes

**Topic 1** · A2 · K2, K5 — Categorise potential causes across all contributing dimensions.

| Field | Detail |
|---|---|
| Case study | Horizon Bank — branch service complaints at Jurong East |
| Duration | 45 minutes |
| Grouping | Teams of 3-5 |
| Tools | Fishbone ed-tool, ChatGPT / Copilot / Gemini |
| Ed-tool | [Fishbone Tool](https://alfredang.github.io/fishbone/) |

---

## The Scenario

Horizon Bank's Jurong East branch has moved from best to worst in the retail network on customer experience in eleven months. Complaints run at 60 per month against a network average of 14. Average counter wait time is 58 minutes at peak; the service standard is 15.

Head Office ran a 'Service Excellence' refresher for all branch staff four months ago. Complaints did not move. The Branch Manager is now under performance review and morale is visibly poor — two tellers have resigned this quarter.

The Regional Director suspects the training was aimed at the wrong cause. Your team has been asked to map ALL contributing causes across every dimension before another intervention is funded. 5 Whys gave depth on one branch; this problem is too broad for one branch.

## The Evidence

*Horizon Bank Jurong East — observation log and system data*

| Dimension | Observation |
|---|---|
| Queue | Single queue for all transaction types; no triage between simple and complex |
| Peak | 11:30-14:00 accounts for 61% of daily footfall (lunch crowd from nearby offices) |
| Counters | 6 counters exist; mean 3.2 staffed at peak |
| Systems | New KYC platform launched 11 months ago; teller must key client data into 3 systems |
| Systems | Mean core-banking screen response 8s, was 2s before the KYC platform |
| Staff | 44% of tellers have under 6 months tenure |
| Staff | Teller KPI is transactions-per-hour; no customer-experience measure |
| Customer | 34% of customers arrive without required documents |
| Customer | Branch signage and the app's document checklist do not match |
| Process | Complex cases (loans, disputes) occupy a counter for a mean of 27 minutes |
| Management | No structured feedback route from branch to Head Office product owners |
| Environment | Only 18 seats in the waiting area; standing customers visibly agitated |

## Step-by-Step

1. Read the Horizon Bank scenario and the observation log.
2. Open the Fishbone ed-tool at https://alfredang.github.io/fishbone/
3. Enter the problem statement as the fish head, with the 60-complaints and 58-minute numbers.
4. Label the six bones: People, Process, Technology, Material/Information, Environment, Measurement.
5. Work bone by bone as a team. For each observation in the log, decide which bone it belongs on and phrase it as a CAUSE, not a complaint.
6. Mark every cause [EVIDENCED] if a number in the log supports it, or [HYPOTHESIS] if it is your team's inference.
7. Run the GenAI Fishbone prompt from the slide and add any bone entries your team missed.
8. Draw an arrow between any two causes on DIFFERENT bones where one drives the other. Note how many arrows you find.
9. Count the evidenced causes per bone. Identify which bone Head Office's training actually targeted.
10. Circle the three causes you would investigate first and write one line of justification for each.
11. Screenshot or export the diagram and present your top three plus your verdict on the training decision.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as a quality improvement facilitator running an Ishikawa (fishbone) analysis with a bank branch team.

Problem (the fish head): Customer complaints at the Horizon Bank Jurong East branch have risen to 60 per month (network average 14), with peak counter wait time at 58 minutes against a 15-minute standard.

Generate candidate causes under these six bones: People, Process, Technology, Material/Information, Environment, Measurement.

Rules:
- Give 4-6 candidate causes per bone, each phrased as a CAUSE not a complaint
- Mark each cause [EVIDENCED] or [HYPOTHESIS] based only on what I give you below
- Do NOT propose solutions
- Finish by naming the 3 causes you would investigate first and say why

Evidence available: single queue with no triage; 61% of footfall between 11:30-14:00; 3.2 of 6 counters staffed at peak; new KYC platform requires triple data entry; screen response degraded 2s to 8s; 44% of tellers under 6 months tenure; teller KPI is transactions-per-hour only; 34% of customers arrive without documents; app checklist and branch signage disagree; complex cases take 27 minutes at the counter; no branch-to-HO feedback route; 18 seats in the waiting area.
```

## Discussion Questions

1. Populate all six bones. Which bone filled up fastest, and which was hardest? What does an empty bone usually mean — no causes, or no visibility?
2. Head Office's answer was a Service Excellence training refresher. Which bone does that intervention target, and what share of your evidenced causes sit on that bone?
3. Find a cause on your diagram that CREATES another cause on a different bone. (Hint: look at the KPI and the queue.) What does that tell you about treating bones as independent?
4. Which three causes would you investigate first? Defend the ranking on evidence strength and likely contribution — not on ease of fixing.
5. The teller KPI is transactions-per-hour. Predict the behaviour that KPI produces at a counter when a confused elderly customer needs 20 minutes. Which bone does that belong on?

## Self-Check — Is Your Output Finished?

Your fishbone is complete when: every bone has at least three entries; every entry is marked [EVIDENCED] or [HYPOTHESIS]; every entry is phrased as a cause ('single queue with no triage') rather than a complaint ('the queue is terrible') or a solution ('add more counters'); and you have found at least one cross-bone arrow. If any bone is empty, you have a visibility gap, not an absence of causes — say so explicitly.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
