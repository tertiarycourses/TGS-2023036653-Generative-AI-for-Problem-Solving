<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 9 — Implementation Planning and Stakeholder Resistance

**Topic 3** · A6 · K3, K8 — Draw up implementation plans and address factors affecting effectiveness.

| Field | Detail |
|---|---|
| Case study | ShopFront SG — the rollout that has to survive contact with people |
| Duration | 50 minutes |
| Grouping | Teams of 3-5 |
| Tools | ChatGPT / Copilot / Gemini, Pinboard |
| Ed-tool | [Pinboard](https://alfredang.github.io/pinboard/) |

---

## The Scenario

Return to ShopFront SG from Activity 1. The diagnosis is complete and the solution set is approved: a one-page guest checkout, a CDN and caching layer to bring app load under 2 seconds, a supplier QC checklist to cut the return rate, and cart-recovery notifications.

The Chief Operating Officer has seen improvement projects die before. She says:

"The plan is fine. Now tell me who is going to fight it, why, and what you are going to do about it. Last year we bought a S$400,000 CRM that nobody used. It worked perfectly. That was not the problem."

Your team must build the implementation plan AND the stakeholder strategy that makes it stick. Assume nothing about goodwill.

## The Evidence

*ShopFront SG — stakeholder map and known positions*

| Stakeholder | Interest | Likely position |
|---|---|---|
| IT Development team | Already at capacity on a POS migration | Resist — sees added workload |
| Head of Marketing | Sponsored the S$180k discount campaign | Resist — solution implies her spend was wrong |
| Store Operations | In-store sales flat, feels unaffected | Indifferent — 'not my problem' |
| Suppliers (12 vendors) | Face new QC standards and possible delisting | Resist — cost and scrutiny |
| Customer Service | Handling 410 tickets/week, overloaded | Support — expects relief |
| Finance | Approved budget, wants ROI evidence | Conditional — needs measurement |
| COO (sponsor) | Accountable for the turnaround | Champion |
| Frontline retail staff | Fear digital shift reduces store headcount | Anxious — job security |

## Step-by-Step

1. Review the four approved ShopFront SG solutions and the stakeholder map.
2. Build the implementation plan: for each solution write Action, Method/Tool, Owner, Timeline.
3. Draw the four solutions on a timeline and mark dependencies with arrows. Identify what must not run in parallel.
4. For each of the eight stakeholders, write their objection IN THEIR OWN WORDS — first person, as they would actually say it in a meeting.
5. For each, decide what they need to hear or receive to move from their current position.
6. Assign a MESSENGER to each stakeholder and justify why that person rather than you.
7. Run the GenAI change management prompt from the slide.
8. Compare the AI's stakeholder analysis to yours. Note any objection it named more bluntly than your team was willing to write down — and ask why you softened it.
9. Rank all stakeholders by their power to block the rollout. Debate the top one as a team.
10. Build the 90-day communication plan: what, to whom, how often, by whom.
11. Post your stakeholder strategy to https://alfredang.github.io/pinboard/ and present your most dangerous stakeholder plus your mitigation.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as a change management and implementation planning advisor for a Singapore fashion retailer.

Approved solutions: (1) one-page guest checkout; (2) CDN + caching to bring app load from 4.8s to under 2.0s; (3) supplier QC checklist to cut the 12% return rate; (4) automated cart-recovery notifications.

PART A — Implementation plan. For each solution give ONLY:
- Action (what will be done)
- Method/tool (how)
- Owner and timeline (who, by when)
- Sequencing note (what must happen before it)

PART B — Stakeholder strategy. Stakeholders and positions:
IT Development (at capacity, resists workload); Head of Marketing (sponsored a S$180k campaign the diagnosis implies was misdirected — resists); Store Operations (indifferent); 12 suppliers (face new QC standards — resist); Customer Service (supportive, overloaded); Finance (conditional on ROI evidence); COO (champion); frontline retail staff (fear job loss).

For EACH stakeholder give:
- Their specific objection in THEIR words, not yours
- What they need to hear or receive to move
- One concrete action to secure their cooperation
- Who is best placed to deliver that message and why

PART C — Name the single stakeholder most likely to sink this rollout, and explain what makes them dangerous. Then give a 90-day communication plan: what is communicated, to whom, how often, by whom.

Be blunt about political realities. Do not assume goodwill.
```

## Discussion Questions

1. Build the implementation plan for all four solutions. Which two MUST be sequenced rather than run in parallel, and what breaks if you ignore that?
2. The Head of Marketing resists because the diagnosis implies her S$180k campaign was misdirected. This is a face problem, not a logic problem. How do you secure her cooperation without requiring her to admit error?
3. Frontline retail staff fear the digital push costs them jobs. Is that fear irrational? What would you actually commit to — and what happens to your credibility if you promise something you cannot guarantee?
4. Twelve suppliers face new QC standards. What is the difference between imposing the checklist and getting them to adopt it, and which one survives after month three?
5. Identify the single stakeholder most likely to sink this rollout. Note: it may not be the loudest one. Justify your choice.

## Self-Check — Is Your Output Finished?

Your implementation plan is realistic when: every solution has an action, method, owner and timeline; dependencies are sequenced (cart recovery AFTER load time is fixed); every stakeholder has an objection written in their own voice, a specific move, and a named messenger; you have identified the highest-risk blocker with justification; and your communication plan runs the full 90 days rather than stopping at launch. If your plan assumes everyone cooperates because the analysis is correct, you have written a wish, not a plan.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
