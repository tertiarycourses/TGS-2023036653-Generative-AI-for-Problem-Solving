<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 4 — Pareto Analysis to Target the Vital Few

**Topic 1** · A1, A3 · K2 — Prioritise causes by contribution and identify key implications.

| Field | Detail |
|---|---|
| Case study | Nexa Logistics — 2,000 failed deliveries a month |
| Duration | 40 minutes |
| Grouping | Teams of 3-5 |
| Tools | Pareto Chart ed-tool, ChatGPT / Copilot / Gemini |
| Ed-tool | [Pareto Chart Tool](https://alfredang.github.io/paretochart/) |

---

## The Scenario

Nexa Logistics runs last-mile delivery for e-commerce clients across Singapore. Of 40,000 monthly deliveries, 2,000 fail on first attempt — a 5% failure rate against a contractual SLA of 2%. Every failed delivery costs S$8.50 to re-attempt: S$17,000 a month, and two clients have invoked SLA penalty clauses.

The Operations Director has a list of eleven failure reasons and a budget that will fund roughly two initiatives this quarter. His instinct is to start with 'Address incorrect' because it generates the angriest client emails.

Your team must decide where the two initiatives should go — using the data, not the noise.

## The Evidence

*Nexa Logistics — first-attempt delivery failures by reason, last month*

| Failure reason | Count | Cost impact (S$) |
|---|---|---|
| Recipient not at home (no delivery window given) | 742 | 6307 |
| Driver could not access condo / office lobby | 486 | 4131 |
| Address incomplete or incorrect | 231 | 1964 |
| Parcel not loaded (sorting error) | 188 | 1598 |
| Recipient refused (wrong item expected) | 121 | 1029 |
| Vehicle breakdown / route disruption | 94 | 799 |
| Weather-related suspension | 61 | 519 |
| Recipient contact number invalid | 38 | 323 |
| Parcel damaged in transit | 24 | 204 |
| Restricted delivery hours at destination | 20 | 170 |
| Other / unclassified | 15 | 128 |

## Step-by-Step

1. Read the Nexa Logistics scenario and the failure reason table.
2. Open the Pareto ed-tool at https://alfredang.github.io/paretochart/
3. Enter each failure reason and its count. The tool sorts descending and computes the cumulative line.
4. Read off the cumulative percentage and mark where the line crosses 80%.
5. Count how many reasons sit to the left of that line — these are your vital few.
6. Calculate by hand: a 60% reduction on the top two gives what new failure rate? Compare against the 2% SLA.
7. Run the GenAI Pareto prompt from the slide and check the AI's arithmetic against your own. Note any error.
8. Restate the top two reasons so that Nexa — not the customer — owns the fix.
9. Decide where the two funded initiatives should go and prepare a one-minute case for the Operations Director.
10. Present, including the arithmetic showing whether the SLA is reachable.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as an operations analyst. Perform a Pareto (80/20) analysis on the delivery failure data below for a Singapore last-mile logistics company.

Total deliveries: 40,000/month. Failures: 2,000 (5%). SLA target: 2%. Re-attempt cost: S$8.50 each.

Data (reason, count):
Recipient not at home 742; Lobby access denied 486; Address incorrect 231; Parcel not loaded 188; Recipient refused 121; Vehicle breakdown 94; Weather 61; Invalid contact 38; Damaged 24; Restricted hours 20; Other 15.

Produce:
1. A table with count, percentage, and CUMULATIVE percentage, sorted descending
2. The cut-off line — which reasons make up the vital few (roughly 80%)
3. The monthly S$ recovery if the top 2 reasons were reduced by 60%
4. Whether hitting the 2% SLA is achievable by fixing the vital few alone — show the arithmetic
5. One caution about what this Pareto analysis does NOT tell me
```

## Discussion Questions

1. Build the Pareto chart. How many of the eleven reasons account for roughly 80% of failures? What does that ratio mean for how the Operations Director should spend his budget?
2. The Director wants to start with 'Address incorrect' because it generates the angriest emails. What does the data say, and how would you make that argument to him without dismissing his concern?
3. Calculate: if the top two reasons drop by 60%, what is the new failure rate? Does that meet the 2% SLA? Show your arithmetic.
4. The top two reasons — 'not at home' and 'lobby access' — look like customer problems. Reframe each as something Nexa controls. What changes about who owns the fix?
5. Pareto ranks by FREQUENCY. Name a situation in your own workplace where the most frequent problem is not the most important one. What would you rank by instead?

## Self-Check — Is Your Output Finished?

Your analysis is sound when: the cumulative column reaches 100%; you can name the vital few and the exact cumulative percentage at your cut-off; you have shown the arithmetic on whether the 2% SLA is reachable (it is not, on the top two alone); and you can state in one sentence what Pareto does NOT tell you. Verify the AI's percentages against the tool's — if they disagree, the tool is right and you have just learned something about trusting AI arithmetic.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
