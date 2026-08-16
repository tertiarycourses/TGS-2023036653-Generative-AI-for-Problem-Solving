<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 10 — Measuring Effectiveness: Did It Actually Work?

**Topic 3** · A7 · K7 — Evaluate the effectiveness of implemented solutions and implementation plans.

| Field | Detail |
|---|---|
| Case study | ShopFront SG — 90 days later, and the numbers are ambiguous |
| Duration | 45 minutes |
| Grouping | Teams of 3-5 |
| Tools | ChatGPT / Copilot / Gemini, Pareto Chart ed-tool |
| Ed-tool | [Pareto Chart Tool](https://alfredang.github.io/paretochart/) |

---

## The Scenario

Ninety days have passed. The COO has the results and she is not sure what to make of them. Some numbers moved well. Some did not move at all. One moved in the wrong direction. And the quarter included the Great Singapore Sale, which everyone is now using to explain whichever result suits their argument.

The Head of Marketing says the improvement is obviously seasonal. The IT lead says the improvement is obviously the CDN. Finance wants to know whether to release the next S$200,000 tranche.

Your team must evaluate honestly: what worked, what did not, what you cannot yet tell, and what you recommend next. "It's working" is not an acceptable answer.

## The Evidence

*ShopFront SG — 90-day results against baseline*

| Metric | Baseline | Target | Day 90 actual | Verdict |
|---|---|---|---|---|
| App page load | 4.8 s | under 2.0 s | 1.7 s | Target met |
| Checkout completion | 51% | 68% | 63% | Improved, short |
| Cart abandonment | 74% | 60% | 64% | Improved, short |
| Online sales / month | S$1.9m | S$2.8m | S$2.5m | Improved, short |
| CSAT | 70% | 85% | 72% | Barely moved |
| Complaint tickets / week | 410 | 150 | 295 | Improved, short |
| Product return rate | 12% | 5% | 13% | WORSE |
| Repeat purchase (90-day) | 29% | 40% | 31% | Barely moved |
| Guest checkout adoption | n/a | n/a | 44% of orders | New data |
| Supplier QC checklist adoption | 0 | 12 of 12 | 4 of 12 | Behind |
| Cart recovery emails sent | n/a | n/a | 18,400 | Live |
| Cart recovery conversion | n/a | 8% | 3.1% | Underperforming |

## Step-by-Step

1. Review the 90-day results table against the original problem statement baselines from Activity 1.
2. Assign a verdict to every metric: Met / Partially met / Not met / Deteriorated.
3. For each improved metric, ask: what CAUSED this? Mark each as Attributable, Partially attributable, or Confounded.
4. Investigate the return rate deterioration. Note that only 4 of 12 suppliers adopted the checklist — what does that tell you about whether the solution was ever actually tested?
5. Separate all metrics into LEADING and LAGGING. Check whether any target was set on an unrealistic horizon.
6. Identify how the Great Singapore Sale confounds the sales figures. Decide what analysis would isolate the programme effect.
7. Diagnose the cart recovery underperformance: wrong solution, wrong implementation, or wrong target? State what data would settle it.
8. Run the GenAI evaluation prompt from the slide.
9. Check the AI's attribution claims critically. Mark anywhere it claimed credit the evidence cannot support.
10. Trace the supplier QC shortfall back to your Activity 9 stakeholder analysis. Did you predict this resistance? What would you have done differently?
11. Write your recommendation to the CFO in three sentences: the verdict, the decision on the S$200k, and what would change your mind.
12. List the three things you would measure differently if you started again.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as a performance evaluation analyst. Assess whether this improvement programme worked. Be rigorous and do not flatter the results.

Results after 90 days (metric: baseline -> target -> actual):
App load 4.8s -> <2.0s -> 1.7s
Checkout completion 51% -> 68% -> 63%
Cart abandonment 74% -> 60% -> 64%
Online sales S$1.9m -> S$2.8m -> S$2.5m
CSAT 70% -> 85% -> 72%
Complaints/week 410 -> 150 -> 295
Product return rate 12% -> 5% -> 13% (WORSE)
Repeat purchase 29% -> 40% -> 31%
Supplier QC checklist adopted by 4 of 12 suppliers
Cart recovery conversion 3.1% against an 8% target

Context: the 90-day window included the Great Singapore Sale.

Produce:
1. A verdict per metric: Met / Partially met / Not met / Deteriorated
2. Which solutions can be credited with which movements — and where you CANNOT establish attribution, say so explicitly and explain why
3. Why the product return rate got WORSE despite the QC initiative — give the most likely explanation and state what evidence would confirm it
4. Separate LEADING from LAGGING indicators here, and explain why CSAT and repeat purchase barely moved even though operational metrics improved
5. How the Great Singapore Sale confounds this evaluation, and what analysis would isolate the programme effect from the seasonal effect
6. A clear recommendation to the CFO on releasing the next S$200k tranche: continue, adjust, or stop — with reasoning
7. The three things you would measure differently next time
```

## Discussion Questions

1. Give a verdict on each metric. Overall — did this programme succeed? Defend a single-sentence answer to the COO.
2. The product return rate got WORSE (12% to 13%) despite the QC initiative. Give the most likely explanation, and say what evidence would confirm or refute it.
3. App load smashed its target but CSAT barely moved. Explain this using leading versus lagging indicators. How long would you expect CSAT to lag?
4. The Great Singapore Sale sits inside the measurement window. How would you isolate the programme effect from the seasonal effect? What would you have done differently at day 0 to make this answerable?
5. Cart recovery converts at 3.1% against an 8% target. Is the solution wrong, or the implementation, or the target? How would you tell the difference — and what does each answer imply?
6. Make the call to the CFO: release the next S$200,000, adjust, or stop. Justify it with the evidence, and name what would change your mind.

## Self-Check — Is Your Output Finished?

Your evaluation is credible when: every metric has a verdict against its baseline AND target; attribution is stated explicitly and confounded results are named as confounded rather than claimed; you can explain the worsening return rate without concluding the solution failed; you distinguish solution failure from implementation failure for supplier QC; your CFO recommendation names what would change your mind; and you can trace at least one missed metric back to a stakeholder resistance you predicted in Activity 9. If your evaluation credits the programme with everything that improved and blames the season for everything that did not, you have written advocacy, not evaluation.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
