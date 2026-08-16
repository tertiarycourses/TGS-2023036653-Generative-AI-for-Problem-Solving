"""
Topic 3 activities — Selecting, Implementing and Measuring Solution Effectiveness.
"""

DOMAIN3 = [
    dict(
        num=9, topic=3,
        title="Activity 9 — Implementation Planning and Stakeholder Resistance",
        objective="A6 · K3, K8 — Draw up implementation plans and address factors affecting effectiveness.",
        edtool=dict(name="Pinboard", url="https://alfredang.github.io/pinboard/"),
        services="ChatGPT / Copilot / Gemini, Pinboard",
        duration="50 minutes",
        grouping="Teams of 3-5",
        case_title="ShopFront SG — the rollout that has to survive contact with people",
        scenario=(
            "Return to ShopFront SG from Activity 1. The diagnosis is complete and the solution set is "
            "approved: a one-page guest checkout, a CDN and caching layer to bring app load under 2 "
            "seconds, a supplier QC checklist to cut the return rate, and cart-recovery notifications.\n\n"
            "The Chief Operating Officer has seen improvement projects die before. She says:\n\n"
            "\"The plan is fine. Now tell me who is going to fight it, why, and what you are going to do "
            "about it. Last year we bought a S$400,000 CRM that nobody used. It worked perfectly. That "
            "was not the problem.\"\n\n"
            "Your team must build the implementation plan AND the stakeholder strategy that makes it "
            "stick. Assume nothing about goodwill."
        ),
        data=dict(
            name="shopfront-stakeholders",
            caption="ShopFront SG — stakeholder map and known positions",
            rows=[
                ["Stakeholder", "Interest", "Likely position"],
                ["IT Development team", "Already at capacity on a POS migration", "Resist — sees added workload"],
                ["Head of Marketing", "Sponsored the S$180k discount campaign", "Resist — solution implies her spend was wrong"],
                ["Store Operations", "In-store sales flat, feels unaffected", "Indifferent — 'not my problem'"],
                ["Suppliers (12 vendors)", "Face new QC standards and possible delisting", "Resist — cost and scrutiny"],
                ["Customer Service", "Handling 410 tickets/week, overloaded", "Support — expects relief"],
                ["Finance", "Approved budget, wants ROI evidence", "Conditional — needs measurement"],
                ["COO (sponsor)", "Accountable for the turnaround", "Champion"],
                ["Frontline retail staff", "Fear digital shift reduces store headcount", "Anxious — job security"],
            ],
        ),
        prompt=(
            "Act as a change management and implementation planning advisor for a Singapore fashion "
            "retailer.\n\n"
            "Approved solutions: (1) one-page guest checkout; (2) CDN + caching to bring app load from "
            "4.8s to under 2.0s; (3) supplier QC checklist to cut the 12% return rate; (4) automated "
            "cart-recovery notifications.\n\n"
            "PART A — Implementation plan. For each solution give ONLY:\n"
            "- Action (what will be done)\n"
            "- Method/tool (how)\n"
            "- Owner and timeline (who, by when)\n"
            "- Sequencing note (what must happen before it)\n\n"
            "PART B — Stakeholder strategy. Stakeholders and positions:\n"
            "IT Development (at capacity, resists workload); Head of Marketing (sponsored a S$180k "
            "campaign the diagnosis implies was misdirected — resists); Store Operations (indifferent); "
            "12 suppliers (face new QC standards — resist); Customer Service (supportive, overloaded); "
            "Finance (conditional on ROI evidence); COO (champion); frontline retail staff (fear job loss).\n\n"
            "For EACH stakeholder give:\n"
            "- Their specific objection in THEIR words, not yours\n"
            "- What they need to hear or receive to move\n"
            "- One concrete action to secure their cooperation\n"
            "- Who is best placed to deliver that message and why\n\n"
            "PART C — Name the single stakeholder most likely to sink this rollout, and explain what "
            "makes them dangerous. Then give a 90-day communication plan: what is communicated, to whom, "
            "how often, by whom.\n\n"
            "Be blunt about political realities. Do not assume goodwill."
        ),
        questions=[
            "Build the implementation plan for all four solutions. Which two MUST be sequenced rather than run in parallel, and what breaks if you ignore that?",
            "The Head of Marketing resists because the diagnosis implies her S$180k campaign was misdirected. This is a face problem, not a logic problem. How do you secure her cooperation without requiring her to admit error?",
            "Frontline retail staff fear the digital push costs them jobs. Is that fear irrational? What would you actually commit to — and what happens to your credibility if you promise something you cannot guarantee?",
            "Twelve suppliers face new QC standards. What is the difference between imposing the checklist and getting them to adopt it, and which one survives after month three?",
            "Identify the single stakeholder most likely to sink this rollout. Note: it may not be the loudest one. Justify your choice.",
        ],
        debrief=(
            "EXPECTED IMPLEMENTATION SEQUENCING:\n"
            "  Guest checkout (weeks 1-4, quick win — builds momentum and credibility with Finance).\n"
            "  CDN/caching (weeks 2-10, big bet — MUST precede or accompany cart-recovery notifications; "
            "driving traffic back to a 4.8-second app converts a recovery campaign into a second bad "
            "experience and burns the customer twice).\n"
            "  Supplier QC (weeks 3-16, longest lead time — external parties, contractual change).\n"
            "  Cart recovery (weeks 10-14, AFTER load time is fixed).\n\n"
            "STAKEHOLDER STRATEGY — the key moves:\n"
            "  MARKETING is the classic trap. The objection is not logical, it is reputational. The move "
            "is to reframe rather than relitigate: the campaign proved demand exists; conversion is where "
            "it leaks. Give her ownership of the cart-recovery workstream so she wins visibly from the "
            "fix. Delivered by the COO, peer to peer — never by the analyst who produced the diagnosis.\n"
            "  IT DEVELOPMENT resists capacity, not the idea. The move is real relief, not "
            "encouragement: re-sequence the POS migration, or fund contract capacity. Delivered by the "
            "COO because only the sponsor can re-prioritise.\n"
            "  SUPPLIERS respond to incentives, not instructions. Co-design the checklist with the three "
            "best-performing vendors, then tie compliance to order volume. An imposed checklist is "
            "complied with on paper for two months; a co-designed one with commercial consequence sticks.\n"
            "  FRONTLINE STAFF have a rational fear and deserve an honest answer. Commit to what you can "
            "actually control — no headcount reduction tied to this programme, and involvement in "
            "click-and-collect roles. Never promise what you cannot guarantee; one broken promise here "
            "costs you every subsequent change programme.\n"
            "  STORE OPERATIONS indifference is the quiet risk — click-and-collect needs them and they "
            "have no reason to care yet. Give them a stake before you need them.\n\n"
            "MOST DANGEROUS STAKEHOLDER — accept a well-argued case for either, but push teams past the "
            "obvious: IT Development can hard-block delivery (nothing ships without them), while Marketing "
            "can soft-block through political attrition, which is harder to see and harder to escalate. "
            "Many teams name the loudest resister; the more sophisticated answer notes that INDIFFERENCE "
            "(Store Operations) often kills rollouts more quietly than opposition, because nobody escalates "
            "an absence of enthusiasm.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. THE COO'S LINE IS THE WHOLE LESSON: the CRM 'worked perfectly. That was not the problem.' "
            "Solutions fail on ADOPTION far more often than on design. K8 — factors affecting the "
            "effectiveness of an implementation plan — is mostly about people, not technology.\n"
            "2. MESSENGER MATTERS AS MUCH AS MESSAGE. The same words land differently from the COO, a "
            "peer, or the analyst. Teams consistently under-think this; make them assign a messenger to "
            "every message and justify it.\n"
            "3. RESISTANCE IS INFORMATION. IT's objection reveals a genuine capacity conflict your plan "
            "had not costed. Suppliers' objection reveals the checklist needs commercial teeth. Treating "
            "resistance as data improves the plan; treating it as obstruction guarantees failure.\n"
            "4. GenAI is unusually good here because it has no stake in the office politics — it will "
            "state plainly that Marketing's objection is about face, which a junior analyst may not dare "
            "write down. It is weak on the specific human relationships and history, which only the team "
            "knows. Divide the labour accordingly."
        ),
        steps=[
            ("Review the four approved ShopFront SG solutions and the stakeholder map.", ""),
            ("Build the implementation plan: for each solution write Action, Method/Tool, Owner, Timeline.", ""),
            ("Draw the four solutions on a timeline and mark dependencies with arrows. Identify what must not run in parallel.", ""),
            ("For each of the eight stakeholders, write their objection IN THEIR OWN WORDS — first person, as they would actually say it in a meeting.", ""),
            ("For each, decide what they need to hear or receive to move from their current position.", ""),
            ("Assign a MESSENGER to each stakeholder and justify why that person rather than you.", ""),
            ("Run the GenAI change management prompt from the slide.", ""),
            ("Compare the AI's stakeholder analysis to yours. Note any objection it named more bluntly than your team was willing to write down — and ask why you softened it.", ""),
            ("Rank all stakeholders by their power to block the rollout. Debate the top one as a team.", ""),
            ("Build the 90-day communication plan: what, to whom, how often, by whom.", ""),
            ("Post your stakeholder strategy to https://alfredang.github.io/pinboard/ and present your most dangerous stakeholder plus your mitigation.", ""),
        ],
        test=(
            "Your implementation plan is realistic when: every solution has an action, method, owner and "
            "timeline; dependencies are sequenced (cart recovery AFTER load time is fixed); every "
            "stakeholder has an objection written in their own voice, a specific move, and a named "
            "messenger; you have identified the highest-risk blocker with justification; and your "
            "communication plan runs the full 90 days rather than stopping at launch. If your plan assumes "
            "everyone cooperates because the analysis is correct, you have written a wish, not a plan."
        ),
    ),

    dict(
        num=10, topic=3,
        title="Activity 10 — Measuring Effectiveness: Did It Actually Work?",
        objective="A7 · K7 — Evaluate the effectiveness of implemented solutions and implementation plans.",
        edtool=dict(name="Pareto Chart Tool", url="https://alfredang.github.io/paretochart/"),
        services="ChatGPT / Copilot / Gemini, Pareto Chart ed-tool",
        duration="45 minutes",
        grouping="Teams of 3-5",
        case_title="ShopFront SG — 90 days later, and the numbers are ambiguous",
        scenario=(
            "Ninety days have passed. The COO has the results and she is not sure what to make of them. "
            "Some numbers moved well. Some did not move at all. One moved in the wrong direction. And "
            "the quarter included the Great Singapore Sale, which everyone is now using to explain "
            "whichever result suits their argument.\n\n"
            "The Head of Marketing says the improvement is obviously seasonal. The IT lead says the "
            "improvement is obviously the CDN. Finance wants to know whether to release the next "
            "S$200,000 tranche.\n\n"
            "Your team must evaluate honestly: what worked, what did not, what you cannot yet tell, and "
            "what you recommend next. \"It's working\" is not an acceptable answer."
        ),
        data=dict(
            name="shopfront-90day-results",
            caption="ShopFront SG — 90-day results against baseline",
            rows=[
                ["Metric", "Baseline", "Target", "Day 90 actual", "Verdict"],
                ["App page load", "4.8 s", "under 2.0 s", "1.7 s", "Target met"],
                ["Checkout completion", "51%", "68%", "63%", "Improved, short"],
                ["Cart abandonment", "74%", "60%", "64%", "Improved, short"],
                ["Online sales / month", "S$1.9m", "S$2.8m", "S$2.5m", "Improved, short"],
                ["CSAT", "70%", "85%", "72%", "Barely moved"],
                ["Complaint tickets / week", "410", "150", "295", "Improved, short"],
                ["Product return rate", "12%", "5%", "13%", "WORSE"],
                ["Repeat purchase (90-day)", "29%", "40%", "31%", "Barely moved"],
                ["Guest checkout adoption", "n/a", "n/a", "44% of orders", "New data"],
                ["Supplier QC checklist adoption", "0", "12 of 12", "4 of 12", "Behind"],
                ["Cart recovery emails sent", "n/a", "n/a", "18,400", "Live"],
                ["Cart recovery conversion", "n/a", "8%", "3.1%", "Underperforming"],
            ],
        ),
        prompt=(
            "Act as a performance evaluation analyst. Assess whether this improvement programme worked. "
            "Be rigorous and do not flatter the results.\n\n"
            "Results after 90 days (metric: baseline -> target -> actual):\n"
            "App load 4.8s -> <2.0s -> 1.7s\n"
            "Checkout completion 51% -> 68% -> 63%\n"
            "Cart abandonment 74% -> 60% -> 64%\n"
            "Online sales S$1.9m -> S$2.8m -> S$2.5m\n"
            "CSAT 70% -> 85% -> 72%\n"
            "Complaints/week 410 -> 150 -> 295\n"
            "Product return rate 12% -> 5% -> 13% (WORSE)\n"
            "Repeat purchase 29% -> 40% -> 31%\n"
            "Supplier QC checklist adopted by 4 of 12 suppliers\n"
            "Cart recovery conversion 3.1% against an 8% target\n\n"
            "Context: the 90-day window included the Great Singapore Sale.\n\n"
            "Produce:\n"
            "1. A verdict per metric: Met / Partially met / Not met / Deteriorated\n"
            "2. Which solutions can be credited with which movements — and where you CANNOT establish "
            "attribution, say so explicitly and explain why\n"
            "3. Why the product return rate got WORSE despite the QC initiative — give the most likely "
            "explanation and state what evidence would confirm it\n"
            "4. Separate LEADING from LAGGING indicators here, and explain why CSAT and repeat purchase "
            "barely moved even though operational metrics improved\n"
            "5. How the Great Singapore Sale confounds this evaluation, and what analysis would isolate "
            "the programme effect from the seasonal effect\n"
            "6. A clear recommendation to the CFO on releasing the next S$200k tranche: continue, "
            "adjust, or stop — with reasoning\n"
            "7. The three things you would measure differently next time"
        ),
        questions=[
            "Give a verdict on each metric. Overall — did this programme succeed? Defend a single-sentence answer to the COO.",
            "The product return rate got WORSE (12% to 13%) despite the QC initiative. Give the most likely explanation, and say what evidence would confirm or refute it.",
            "App load smashed its target but CSAT barely moved. Explain this using leading versus lagging indicators. How long would you expect CSAT to lag?",
            "The Great Singapore Sale sits inside the measurement window. How would you isolate the programme effect from the seasonal effect? What would you have done differently at day 0 to make this answerable?",
            "Cart recovery converts at 3.1% against an 8% target. Is the solution wrong, or the implementation, or the target? How would you tell the difference — and what does each answer imply?",
            "Make the call to the CFO: release the next S$200,000, adjust, or stop. Justify it with the evidence, and name what would change your mind.",
        ],
        debrief=(
            "EXPECTED EVALUATION:\n\n"
            "ATTRIBUTION IS THE CENTRAL SKILL. App load 4.8s -> 1.7s is cleanly attributable to the CDN "
            "and caching — technical, direct, no plausible alternative cause. Checkout completion is "
            "PARTIALLY attributable to guest checkout (44% adoption is strong supporting evidence). "
            "Online sales, however, are CONFOUNDED by the Great Singapore Sale and cannot be cleanly "
            "attributed either way. A team that credits the full S$0.6m to the programme is overclaiming; "
            "a team that dismisses it as seasonal is underclaiming. The honest answer is: not "
            "determinable with this design, and here is what would have made it determinable.\n\n"
            "THE RETURN RATE PUZZLE — the most instructive result on the board. Most likely explanation: "
            "only 4 of 12 suppliers adopted the QC checklist, so the intervention barely happened. "
            "Simultaneously, higher conversion and GSS volume brought in more first-time and "
            "discount-driven buyers, who return at a higher rate than loyal customers. So the return rate "
            "rose because of a MIX SHIFT, not because quality fell. Confirming evidence: segment return "
            "rate by supplier (adopters vs non-adopters) and by customer type (new vs repeat, full-price "
            "vs discounted). This is the moment learners see that a metric moving the wrong way does not "
            "automatically mean the solution failed — you must decompose before you conclude.\n\n"
            "LEADING vs LAGGING: app load, checkout completion and guest checkout adoption are LEADING — "
            "they respond within days. CSAT, repeat purchase and brand perception are LAGGING — they "
            "reflect accumulated experience across multiple purchase cycles and typically lag two to "
            "three cycles, i.e. 6-9 months for a fashion retailer. Expecting CSAT to move in 90 days was "
            "a planning error, not an execution failure. The target itself was wrong.\n\n"
            "CART RECOVERY at 3.1% vs 8%: distinguish the three diagnoses. Wrong solution (cart recovery "
            "does not work for this audience); wrong implementation (poor timing, weak copy, no "
            "incentive, emails hitting spam); wrong target (8% was benchmarked from a different sector). "
            "The way to tell: check open and click rates. High open + low conversion = offer/landing "
            "problem. Low open = deliverability or timing problem. Industry benchmarks for fashion "
            "cart-recovery sit around 3-5%, which strongly suggests the TARGET was unrealistic. Teams "
            "that immediately conclude 'the solution failed' have skipped the diagnosis — and that is "
            "exactly the behaviour the whole course exists to correct.\n\n"
            "RECOMMENDATION TO THE CFO — the defensible answer is CONTINUE WITH ADJUSTMENT: the "
            "technical solutions delivered and are attributable; supplier QC did not actually get "
            "implemented (4 of 12) so it has not been tested and should not be abandoned on non-adoption; "
            "cart recovery needs its target rebased and its execution diagnosed; CSAT needs a longer "
            "horizon. Redirect effort to supplier adoption — which is a CHANGE MANAGEMENT failure, "
            "traceable straight back to Activity 9's prediction that suppliers would resist. That "
            "connection is the strongest single moment in the course: the resistance they predicted is "
            "the resistance that actually materialised, and it is the reason a metric missed.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. 'IT'S WORKING' IS NOT AN EVALUATION. Metric-by-metric verdicts against baseline and "
            "target, with explicit attribution and explicit uncertainty, is.\n"
            "2. EVALUATION IS ONLY POSSIBLE BECAUSE ACTIVITY 1 CAPTURED A BASELINE. Say this out loud — "
            "the course has now closed its loop, and learners should feel why the six-element problem "
            "statement mattered 16 hours ago.\n"
            "3. DISTINGUISH SOLUTION FAILURE FROM IMPLEMENTATION FAILURE. Supplier QC did not fail; it "
            "was not adopted. Those demand completely different responses — one means change the "
            "solution, the other means fix the rollout.\n"
            "4. CONFOUNDING IS ALWAYS PRESENT IN REAL WORKPLACES. You will rarely get a clean experiment. "
            "Good practice: define the measurement window at day 0, hold a control (e.g. staged rollout "
            "by region), and segment the data. Say what you cannot determine — that honesty is what makes "
            "the rest of your evaluation credible to a CFO.\n"
            "5. GenAI will produce a confident, well-structured evaluation that quietly overclaims "
            "attribution unless you explicitly instruct it to flag what cannot be determined. Note that "
            "the prompt on the slide does exactly that — and compare it against what the AI returns "
            "without that instruction. That contrast is the AI-literacy takeaway of the entire course."
        ),
        steps=[
            ("Review the 90-day results table against the original problem statement baselines from Activity 1.", ""),
            ("Assign a verdict to every metric: Met / Partially met / Not met / Deteriorated.", ""),
            ("For each improved metric, ask: what CAUSED this? Mark each as Attributable, Partially attributable, or Confounded.", ""),
            ("Investigate the return rate deterioration. Note that only 4 of 12 suppliers adopted the checklist — what does that tell you about whether the solution was ever actually tested?", ""),
            ("Separate all metrics into LEADING and LAGGING. Check whether any target was set on an unrealistic horizon.", ""),
            ("Identify how the Great Singapore Sale confounds the sales figures. Decide what analysis would isolate the programme effect.", ""),
            ("Diagnose the cart recovery underperformance: wrong solution, wrong implementation, or wrong target? State what data would settle it.", ""),
            ("Run the GenAI evaluation prompt from the slide.", ""),
            ("Check the AI's attribution claims critically. Mark anywhere it claimed credit the evidence cannot support.", ""),
            ("Trace the supplier QC shortfall back to your Activity 9 stakeholder analysis. Did you predict this resistance? What would you have done differently?", ""),
            ("Write your recommendation to the CFO in three sentences: the verdict, the decision on the S$200k, and what would change your mind.", ""),
            ("List the three things you would measure differently if you started again.", ""),
        ],
        test=(
            "Your evaluation is credible when: every metric has a verdict against its baseline AND target; "
            "attribution is stated explicitly and confounded results are named as confounded rather than "
            "claimed; you can explain the worsening return rate without concluding the solution failed; "
            "you distinguish solution failure from implementation failure for supplier QC; your CFO "
            "recommendation names what would change your mind; and you can trace at least one missed "
            "metric back to a stakeholder resistance you predicted in Activity 9. If your evaluation "
            "credits the programme with everything that improved and blames the season for everything "
            "that did not, you have written advocacy, not evaluation."
        ),
    ),
]
