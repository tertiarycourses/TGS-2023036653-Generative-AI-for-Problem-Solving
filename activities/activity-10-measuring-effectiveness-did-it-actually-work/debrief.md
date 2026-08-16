<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Trainer Debrief — Activity 10

## Activity 10 — Measuring Effectiveness: Did It Actually Work?

**Case study:** ShopFront SG — 90 days later, and the numbers are ambiguous  
**Objective:** A7 · K7 — Evaluate the effectiveness of implemented solutions and implementation plans.

---

EXPECTED EVALUATION:

ATTRIBUTION IS THE CENTRAL SKILL. App load 4.8s -> 1.7s is cleanly attributable to the CDN and caching — technical, direct, no plausible alternative cause. Checkout completion is PARTIALLY attributable to guest checkout (44% adoption is strong supporting evidence). Online sales, however, are CONFOUNDED by the Great Singapore Sale and cannot be cleanly attributed either way. A team that credits the full S$0.6m to the programme is overclaiming; a team that dismisses it as seasonal is underclaiming. The honest answer is: not determinable with this design, and here is what would have made it determinable.

THE RETURN RATE PUZZLE — the most instructive result on the board. Most likely explanation: only 4 of 12 suppliers adopted the QC checklist, so the intervention barely happened. Simultaneously, higher conversion and GSS volume brought in more first-time and discount-driven buyers, who return at a higher rate than loyal customers. So the return rate rose because of a MIX SHIFT, not because quality fell. Confirming evidence: segment return rate by supplier (adopters vs non-adopters) and by customer type (new vs repeat, full-price vs discounted). This is the moment learners see that a metric moving the wrong way does not automatically mean the solution failed — you must decompose before you conclude.

LEADING vs LAGGING: app load, checkout completion and guest checkout adoption are LEADING — they respond within days. CSAT, repeat purchase and brand perception are LAGGING — they reflect accumulated experience across multiple purchase cycles and typically lag two to three cycles, i.e. 6-9 months for a fashion retailer. Expecting CSAT to move in 90 days was a planning error, not an execution failure. The target itself was wrong.

CART RECOVERY at 3.1% vs 8%: distinguish the three diagnoses. Wrong solution (cart recovery does not work for this audience); wrong implementation (poor timing, weak copy, no incentive, emails hitting spam); wrong target (8% was benchmarked from a different sector). The way to tell: check open and click rates. High open + low conversion = offer/landing problem. Low open = deliverability or timing problem. Industry benchmarks for fashion cart-recovery sit around 3-5%, which strongly suggests the TARGET was unrealistic. Teams that immediately conclude 'the solution failed' have skipped the diagnosis — and that is exactly the behaviour the whole course exists to correct.

RECOMMENDATION TO THE CFO — the defensible answer is CONTINUE WITH ADJUSTMENT: the technical solutions delivered and are attributable; supplier QC did not actually get implemented (4 of 12) so it has not been tested and should not be abandoned on non-adoption; cart recovery needs its target rebased and its execution diagnosed; CSAT needs a longer horizon. Redirect effort to supplier adoption — which is a CHANGE MANAGEMENT failure, traceable straight back to Activity 9's prediction that suppliers would resist. That connection is the strongest single moment in the course: the resistance they predicted is the resistance that actually materialised, and it is the reason a metric missed.

KEY TEACHING POINTS:
1. 'IT'S WORKING' IS NOT AN EVALUATION. Metric-by-metric verdicts against baseline and target, with explicit attribution and explicit uncertainty, is.
2. EVALUATION IS ONLY POSSIBLE BECAUSE ACTIVITY 1 CAPTURED A BASELINE. Say this out loud — the course has now closed its loop, and learners should feel why the six-element problem statement mattered 16 hours ago.
3. DISTINGUISH SOLUTION FAILURE FROM IMPLEMENTATION FAILURE. Supplier QC did not fail; it was not adopted. Those demand completely different responses — one means change the solution, the other means fix the rollout.
4. CONFOUNDING IS ALWAYS PRESENT IN REAL WORKPLACES. You will rarely get a clean experiment. Good practice: define the measurement window at day 0, hold a control (e.g. staged rollout by region), and segment the data. Say what you cannot determine — that honesty is what makes the rest of your evaluation credible to a CFO.
5. GenAI will produce a confident, well-structured evaluation that quietly overclaims attribution unless you explicitly instruct it to flag what cannot be determined. Note that the prompt on the slide does exactly that — and compare it against what the AI returns without that instruction. That contrast is the AI-literacy takeaway of the entire course.

---

## Discussion Questions (for reference)

1. Give a verdict on each metric. Overall — did this programme succeed? Defend a single-sentence answer to the COO.
2. The product return rate got WORSE (12% to 13%) despite the QC initiative. Give the most likely explanation, and say what evidence would confirm or refute it.
3. App load smashed its target but CSAT barely moved. Explain this using leading versus lagging indicators. How long would you expect CSAT to lag?
4. The Great Singapore Sale sits inside the measurement window. How would you isolate the programme effect from the seasonal effect? What would you have done differently at day 0 to make this answerable?
5. Cart recovery converts at 3.1% against an 8% target. Is the solution wrong, or the implementation, or the target? How would you tell the difference — and what does each answer imply?
6. Make the call to the CFO: release the next S$200,000, adjust, or stop. Justify it with the evidence, and name what would change your mind.

## Success Criteria

Your evaluation is credible when: every metric has a verdict against its baseline AND target; attribution is stated explicitly and confounded results are named as confounded rather than claimed; you can explain the worsening return rate without concluding the solution failed; you distinguish solution failure from implementation failure for supplier QC; your CFO recommendation names what would change your mind; and you can trace at least one missed metric back to a stakeholder resistance you predicted in Activity 9. If your evaluation credits the programme with everything that improved and blames the season for everything that did not, you have written advocacy, not evaluation.
