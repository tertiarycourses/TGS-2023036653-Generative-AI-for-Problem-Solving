"""
Topic 1 activities — Identifying Performance Gaps and Root Causes with Generative AI.

Each activity is a REAL-LIFE Singapore workplace case study carrying:
  scenario   — the situation, with hard numbers
  data       — the evidence table the team works from
  questions  — discussion questions for the breakout
  debrief    — what the trainer draws out, including the expected answer
  prompt     — the GenAI prompt learners actually run
"""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Activity 1 — Rewriting a Vague Problem into a Measurable Problem Statement",
        objective="A1 · K1 — Identify the type of performance deficiency and express it as a measurable problem statement.",
        edtool=dict(name="CollabNote", url="https://alfredang.github.io/collabnote/"),
        services="ChatGPT / Copilot / Gemini, CollabNote",
        duration="45 minutes",
        grouping="Teams of 3",
        case_title="ShopFront SG — 'Customers are unhappy and sales are dropping'",
        scenario=(
            "ShopFront SG is a 42-outlet fashion retailer with an e-commerce site and a mobile app. "
            "At the Monday management meeting the Head of Retail Operations opens with one line: "
            "\"Customers are unhappy and sales are dropping — fix it.\" No metric, no baseline, no scope. "
            "Three departments leave the room with three different interpretations. Marketing books a "
            "S$180,000 discount campaign. IT starts an app redesign. Customer Service hires two temps. "
            "Ninety days later the complaint rate is unchanged and the budget is gone.\n\n"
            "You are the business analyst asked to restate the problem BEFORE any more money is committed. "
            "The dashboard extract below is all the evidence you have."
        ),
        data=dict(
            name="shopfront-baseline",
            caption="ShopFront SG — 90-day performance extract",
            rows=[
                ["Metric", "12 months ago", "Current", "Industry benchmark"],
                ["Average app page load", "2.1 s", "4.8 s", "under 2.0 s"],
                ["Checkout completion rate", "68%", "51%", "70%"],
                ["Cart abandonment", "61%", "74%", "60%"],
                ["CSAT (post-purchase)", "84%", "70%", "85%"],
                ["Repeat purchase (90-day)", "38%", "29%", "40%"],
                ["Complaint tickets / week", "120", "410", "-"],
                ["In-store sales", "S$4.2m/mo", "S$4.1m/mo", "-"],
                ["Online sales", "S$2.8m/mo", "S$1.9m/mo", "-"],
            ],
        ),
        prompt=(
            "You are a business analyst for a Singapore fashion retailer.\n\n"
            "Refine the vague statement below into ONE clear, measurable problem statement.\n\n"
            "Vague statement: \"Customers are unhappy and sales are dropping.\"\n\n"
            "Evidence:\n"
            "- App page load rose from 2.1s to 4.8s (benchmark <2.0s)\n"
            "- Checkout completion fell 68% -> 51% (benchmark 70%)\n"
            "- Cart abandonment rose 61% -> 74%\n"
            "- CSAT fell 84% -> 70%\n"
            "- Online sales fell S$2.8m -> S$1.9m per month; in-store flat\n\n"
            "Your problem statement MUST contain, each labelled:\n"
            "- Context (who, where, which process)\n"
            "- Metric (the single primary measure)\n"
            "- Baseline (where it is now, with the number)\n"
            "- Target (where it must be, with the number)\n"
            "- Timeframe (by when)\n"
            "- Constraints (budget, headcount, compliance, brand)\n\n"
            "Then list any assumption you had to make, and state what additional evidence "
            "would let you remove that assumption. Do not propose solutions yet."
        ),
        questions=[
            "Which metric in the table is the SYMPTOM the executive noticed, and which metric is closest to the actual performance deficiency? Justify with the numbers.",
            "The evidence shows in-store sales are flat while online sales fell 32%. What does that single contrast rule out as a cause, and why does that matter before you spend a dollar?",
            "Write the problem statement with all six elements. Which element was hardest to fill, and what does the gap tell you about your organisation's data?",
            "Compare your team's statement with the GenAI-generated one. What did the AI assume that is NOT supported by the evidence? (Every team will find at least one.)",
            "Whose sign-off do you need on this problem statement before work starts, and what would you show them to get it?",
        ],
        debrief=(
            "EXPECTED DIRECTION — the deficiency is a DIGITAL CHANNEL conversion failure, not a "
            "general 'unhappy customer' problem. In-store being flat while online fell 32% localises the "
            "problem to the digital funnel and rules out brand, product and pricing as the primary cause — "
            "which immediately invalidates Marketing's S$180k discount campaign.\n\n"
            "A defensible statement reads roughly: 'Checkout completion on the ShopFront SG app and web "
            "store has fallen from 68% to 51% (benchmark 70%) over 12 months, alongside app load times "
            "rising from 2.1s to 4.8s, contributing to a S$0.9m per month decline in online sales. We aim "
            "to restore checkout completion to at least 68% and app load to under 2.0s within 90 days, "
            "without additional headcount and without changes requiring PDPA re-consent.'\n\n"
            "KEY TEACHING POINTS:\n"
            "1. The executive named a symptom ('unhappy'). CSAT is a lagging perception measure; checkout "
            "completion is the operational deficiency you can actually act on.\n"
            "2. Six elements are non-negotiable. A statement missing a Baseline cannot be evaluated later — "
            "this is exactly what Topic 3 comes back to.\n"
            "3. GenAI reliably invents plausible specifics (a peak-hour window, a payment gateway name, a "
            "customer segment) that the evidence never supplied. Learners must mark these as assumptions. "
            "This is the single most important AI-literacy habit in the course.\n"
            "4. Note what has NOT been established yet: WHY load time rose. That is root cause, and it is "
            "Activity 2. Resist the team that jumps to 'we need more servers'."
        ),
        steps=[
            ("Read the ShopFront SG scenario and the 90-day evidence table as a team.", ""),
            ("Individually and in silence, underline the one metric you believe is the real performance deficiency. Do not discuss yet — this prevents anchoring on the loudest voice.", ""),
            ("Compare choices around the table. Where you disagree, argue from the numbers only.", ""),
            ("Draft the problem statement on paper with all six elements labelled: Context, Metric, Baseline, Target, Timeframe, Constraints.", ""),
            ("Open your GenAI tool and run the Problem Statement prompt supplied on the slide.", ""),
            ("Compare the AI output against your draft. Highlight every specific the AI supplied that the evidence did not support — label each one 'ASSUMPTION'.", ""),
            ("Merge the two into a final statement your team can defend to the Head of Retail Operations.", ""),
            ("Post the final statement to the shared wall at https://alfredang.github.io/collabnote/", ""),
            ("Nominate one speaker to read it out in 60 seconds and name the one assumption you are least comfortable with.", ""),
        ],
        test=(
            "Your statement is complete when a colleague who was NOT in the room can read it and correctly "
            "state (a) which metric is being fixed, (b) the number it is at today, (c) the number it must "
            "reach, (d) by when, and (e) what you are not allowed to change — without asking you a question. "
            "If any of the five is missing, the statement is not finished."
        ),
    ),

    dict(
        num=2, topic=1,
        title="Activity 2 — 5 Whys Root Cause Analysis",
        objective="A2 · K2, K5 — Identify root causes with team members using structured group facilitation.",
        edtool=dict(name="5 Whys Tool", url="https://alfredang.github.io/5whys/"),
        services="5 Whys ed-tool, ChatGPT / Copilot / Gemini",
        duration="45 minutes",
        grouping="Teams of 3-5",
        case_title="Meridian Health Screening — the 07:00 blood-test backlog",
        scenario=(
            "Meridian Health operates six health-screening centres in Singapore. Corporate clients book "
            "annual screening packages; the fasting blood draw must happen between 07:00 and 09:30.\n\n"
            "Over the last four months, 31% of morning appointments overrun by more than 40 minutes. "
            "Corporate clients have escalated twice. One major client (1,400 employees, S$310,000 annual "
            "contract) has given notice of review. The Operations Manager's proposal is to open a seventh "
            "centre at a capital cost of S$1.2m.\n\n"
            "The Clinical Director is unconvinced. She has asked your team to establish the ROOT CAUSE "
            "before the board approves any capital expenditure. The nurses tell you the same thing every "
            "morning: \"We're just short-staffed.\" The data below says something more interesting."
        ),
        data=dict(
            name="meridian-morning-ops",
            caption="Meridian Health — morning screening operations, 4-month sample",
            rows=[
                ["Observation", "Value"],
                ["Booked slots 07:00-09:30", "48 per centre"],
                ["Phlebotomists rostered 07:00", "3 of 5"],
                ["Phlebotomists rostered 08:30", "5 of 5"],
                ["Mean draw time, trained staff", "6 min"],
                ["Mean draw time, relief staff", "14 min"],
                ["Relief staff share of morning roster", "40%"],
                ["Repeat draws (failed first attempt)", "18%"],
                ["Clients arriving without fasting compliance", "12%"],
                ["Lab courier pickup (fixed)", "09:45"],
                ["Samples missing the 09:45 courier", "23%"],
                ["Permanent staff turnover, 12 months", "44%"],
            ],
        ),
        prompt=(
            "Act as a root cause analysis expert facilitating a clinical operations team.\n\n"
            "Problem: 31% of morning health-screening appointments at Meridian Health overrun by "
            "more than 40 minutes, and 23% of blood samples miss the fixed 09:45 lab courier.\n\n"
            "Evidence: only 3 of 5 phlebotomists are rostered at 07:00 (all 5 by 08:30); relief staff "
            "take 14 min per draw vs 6 min for trained staff; relief staff are 40% of the morning roster; "
            "18% of draws need a repeat attempt; permanent staff turnover is 44% a year.\n\n"
            "Apply the 5 Whys technique. Ask ONE why at a time and wait for my answer before asking the "
            "next. Go five levels deep.\n\n"
            "At each level, state what EVIDENCE would confirm or refute that level — do not accept my "
            "answer at face value. If my answer is an opinion rather than a fact, say so and ask me for "
            "the data that would support it.\n\n"
            "After level 5, summarise: the root cause, the evidence supporting it, and which levels "
            "remain unverified assumptions."
        ),
        questions=[
            "Run the 5 Whys to five levels. At which level did you stop describing WHAT happens and start explaining WHY the system produces it?",
            "The nurses say 'we're short-staffed'. The data shows all 5 phlebotomists are rostered by 08:30. What is the real constraint — headcount, or something else?",
            "Trace the causal chain to 44% annual turnover. If turnover is the root cause, what does that say about the S$1.2m seventh centre proposal?",
            "Where could this 5 Whys chain have gone wrong? Identify one point where a different, equally plausible 'why' would have led you somewhere completely different.",
            "The GenAI facilitator challenged at least one of your answers as opinion rather than fact. Which one, and were you able to supply the evidence?",
        ],
        debrief=(
            "EXPECTED CHAIN (teams may reach this by slightly different routes — accept any chain that is "
            "evidence-supported and reaches a systemic cause):\n"
            "  Why 1: Appointments overrun -> draws take longer than the slot allows.\n"
            "  Why 2: Draws take longer -> 40% of morning staff are relief staff at 14 min vs 6 min, and "
            "18% of draws need a repeat.\n"
            "  Why 3: So many relief staff -> only 3 of 5 permanent phlebotomists are rostered at 07:00.\n"
            "  Why 4: Under-rostered at 07:00 -> permanent staff turnover is 44%/yr; vacancies are "
            "backfilled with relief staff who are not trained to the centre's protocol.\n"
            "  Why 5: Turnover is 44% -> the early shift is unattractive and there is no structured "
            "onboarding or retention path for phlebotomists.\n\n"
            "ROOT CAUSE: a workforce retention and onboarding failure, surfacing as a capacity problem.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. The S$1.2m seventh centre solves the SYMPTOM. A new centre staffed by the same 40% "
            "untrained relief pool reproduces the same overrun — you buy the problem twice.\n"
            "2. 'We're short-staffed' was the team's stated cause and it was WRONG in the way that "
            "matters: they are not short of headcount, they are short of TRAINED headcount at 07:00. "
            "This distinction is worth S$1.2m.\n"
            "3. Facilitation discipline: one why at a time, and every level must survive 'what evidence "
            "supports this?'. The GenAI acting as challenger models the facilitator behaviour learners "
            "should copy — this is the K5 group facilitation outcome.\n"
            "4. Note the branch point: at Why 2 a team could have followed the 12% fasting non-compliance "
            "instead and landed on 'client communication'. That is a legitimate SECOND cause. 5 Whys "
            "gives depth on one branch — which is exactly why Activity 3 uses Fishbone for breadth."
        ),
        steps=[
            ("Read the Meridian Health scenario and study the operations table.", ""),
            ("Appoint a facilitator (asks the whys and keeps the team on one branch) and a scribe.", ""),
            ("Open the 5 Whys ed-tool at https://alfredang.github.io/5whys/", ""),
            ("Enter the problem statement in the tool's problem field, using numbers from the table.", ""),
            ("Ask Why #1. The facilitator's job: reject any answer that is an opinion, and ask 'what evidence supports that?'", ""),
            ("Continue to five levels, entering each why and answer in the tool. Stay on ONE causal branch.", ""),
            ("Mark the level where the answer stopped being a description of events and became a system explanation.", ""),
            ("Run the same problem through the GenAI 5 Whys prompt from the slide, answering as the clinical team would.", ""),
            ("Compare the two chains. Where they diverge, decide which branch the EVIDENCE supports and record why.", ""),
            ("Write your root cause statement in one sentence, and note which levels remain unverified.", ""),
            ("Present to the room in 90 seconds: the chain, the root cause, and your verdict on the S$1.2m proposal.", ""),
        ],
        test=(
            "Your root cause is sound when you can answer YES to all three: (1) If this cause were removed, "
            "would the 31% overrun stop recurring — not just improve this month? (2) Is every level in the "
            "chain supported by a number in the evidence table, or explicitly flagged as an assumption? "
            "(3) Does the root cause point at a SYSTEM (policy, process, incentive) rather than at a person? "
            "If your chain ends at 'the relief staff are slow', you have found a symptom and blamed a human — "
            "go two levels deeper."
        ),
    ),

    dict(
        num=3, topic=1,
        title="Activity 3 — Fishbone (Ishikawa) Diagram for Breadth of Causes",
        objective="A2 · K2, K5 — Categorise potential causes across all contributing dimensions.",
        edtool=dict(name="Fishbone Tool", url="https://alfredang.github.io/fishbone/"),
        services="Fishbone ed-tool, ChatGPT / Copilot / Gemini",
        duration="45 minutes",
        grouping="Teams of 3-5",
        case_title="Horizon Bank — branch service complaints at Jurong East",
        scenario=(
            "Horizon Bank's Jurong East branch has moved from best to worst in the retail network on "
            "customer experience in eleven months. Complaints run at 60 per month against a network "
            "average of 14. Average counter wait time is 58 minutes at peak; the service standard is 15.\n\n"
            "Head Office ran a 'Service Excellence' refresher for all branch staff four months ago. "
            "Complaints did not move. The Branch Manager is now under performance review and morale is "
            "visibly poor — two tellers have resigned this quarter.\n\n"
            "The Regional Director suspects the training was aimed at the wrong cause. Your team has been "
            "asked to map ALL contributing causes across every dimension before another intervention is "
            "funded. 5 Whys gave depth on one branch; this problem is too broad for one branch."
        ),
        data=dict(
            name="horizon-branch-observations",
            caption="Horizon Bank Jurong East — observation log and system data",
            rows=[
                ["Dimension", "Observation"],
                ["Queue", "Single queue for all transaction types; no triage between simple and complex"],
                ["Peak", "11:30-14:00 accounts for 61% of daily footfall (lunch crowd from nearby offices)"],
                ["Counters", "6 counters exist; mean 3.2 staffed at peak"],
                ["Systems", "New KYC platform launched 11 months ago; teller must key client data into 3 systems"],
                ["Systems", "Mean core-banking screen response 8s, was 2s before the KYC platform"],
                ["Staff", "44% of tellers have under 6 months tenure"],
                ["Staff", "Teller KPI is transactions-per-hour; no customer-experience measure"],
                ["Customer", "34% of customers arrive without required documents"],
                ["Customer", "Branch signage and the app's document checklist do not match"],
                ["Process", "Complex cases (loans, disputes) occupy a counter for a mean of 27 minutes"],
                ["Management", "No structured feedback route from branch to Head Office product owners"],
                ["Environment", "Only 18 seats in the waiting area; standing customers visibly agitated"],
            ],
        ),
        prompt=(
            "Act as a quality improvement facilitator running an Ishikawa (fishbone) analysis with a "
            "bank branch team.\n\n"
            "Problem (the fish head): Customer complaints at the Horizon Bank Jurong East branch have "
            "risen to 60 per month (network average 14), with peak counter wait time at 58 minutes "
            "against a 15-minute standard.\n\n"
            "Generate candidate causes under these six bones: People, Process, Technology, "
            "Material/Information, Environment, Measurement.\n\n"
            "Rules:\n"
            "- Give 4-6 candidate causes per bone, each phrased as a CAUSE not a complaint\n"
            "- Mark each cause [EVIDENCED] or [HYPOTHESIS] based only on what I give you below\n"
            "- Do NOT propose solutions\n"
            "- Finish by naming the 3 causes you would investigate first and say why\n\n"
            "Evidence available: single queue with no triage; 61% of footfall between 11:30-14:00; "
            "3.2 of 6 counters staffed at peak; new KYC platform requires triple data entry; screen "
            "response degraded 2s to 8s; 44% of tellers under 6 months tenure; teller KPI is "
            "transactions-per-hour only; 34% of customers arrive without documents; app checklist and "
            "branch signage disagree; complex cases take 27 minutes at the counter; no branch-to-HO "
            "feedback route; 18 seats in the waiting area."
        ),
        questions=[
            "Populate all six bones. Which bone filled up fastest, and which was hardest? What does an empty bone usually mean — no causes, or no visibility?",
            "Head Office's answer was a Service Excellence training refresher. Which bone does that intervention target, and what share of your evidenced causes sit on that bone?",
            "Find a cause on your diagram that CREATES another cause on a different bone. (Hint: look at the KPI and the queue.) What does that tell you about treating bones as independent?",
            "Which three causes would you investigate first? Defend the ranking on evidence strength and likely contribution — not on ease of fixing.",
            "The teller KPI is transactions-per-hour. Predict the behaviour that KPI produces at a counter when a confused elderly customer needs 20 minutes. Which bone does that belong on?",
        ],
        debrief=(
            "EXPECTED DISTRIBUTION — a well-built diagram is heavily loaded on Process, Technology and "
            "Measurement, and only lightly on People:\n"
            "  PEOPLE — 44% of tellers under 6 months; two resignations; low morale; thin coaching.\n"
            "  PROCESS — single queue, no triage; complex cases (27 min) block counters; rostering does "
            "not match the 11:30-14:00 peak (3.2 of 6 counters staffed).\n"
            "  TECHNOLOGY — KYC platform forces triple data entry; screen response degraded 2s to 8s.\n"
            "  MATERIAL/INFORMATION — app checklist contradicts branch signage; 34% arrive without documents.\n"
            "  ENVIRONMENT — 18 seats for a 58-minute wait; standing customers escalate faster.\n"
            "  MEASUREMENT — transactions-per-hour KPI with no experience measure; no branch-to-HO feedback loop.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. THE HEADLINE: Head Office trained the PEOPLE bone, which carries the fewest evidenced "
            "causes. That is precisely why complaints did not move and S$ was wasted. Learners should "
            "leave able to say: 'we intervened on the wrong bone.'\n"
            "2. CROSS-BONE CAUSATION: the transactions-per-hour KPI (Measurement) drives tellers to rush "
            "or avoid complex cases (Process), which pushes complex customers back into the queue "
            "(Process), which lengthens the wait (Environment), which raises complaint volume. Bones are "
            "NOT independent — this observation is the bridge into System Loops in Activity 5.\n"
            "3. FISHBONE vs 5 WHYS: 5 Whys gave one deep chain; Fishbone gives six shallow ones. Depth "
            "without breadth means you fix one cause and the problem persists; breadth without depth "
            "means you fix symptoms everywhere. Mature practice uses both — and the deliberate contrast "
            "between Activity 2 and Activity 3 is the point of running them back to back.\n"
            "4. GenAI is excellent at populating bones fast (breadth at near-zero cost) and poor at "
            "knowing which are real. Note how many causes it returned as [HYPOTHESIS] — those are the "
            "ones your team must go and verify. The AI generates; the human evidences."
        ),
        steps=[
            ("Read the Horizon Bank scenario and the observation log.", ""),
            ("Open the Fishbone ed-tool at https://alfredang.github.io/fishbone/", ""),
            ("Enter the problem statement as the fish head, with the 60-complaints and 58-minute numbers.", ""),
            ("Label the six bones: People, Process, Technology, Material/Information, Environment, Measurement.", ""),
            ("Work bone by bone as a team. For each observation in the log, decide which bone it belongs on and phrase it as a CAUSE, not a complaint.", ""),
            ("Mark every cause [EVIDENCED] if a number in the log supports it, or [HYPOTHESIS] if it is your team's inference.", ""),
            ("Run the GenAI Fishbone prompt from the slide and add any bone entries your team missed.", ""),
            ("Draw an arrow between any two causes on DIFFERENT bones where one drives the other. Note how many arrows you find.", ""),
            ("Count the evidenced causes per bone. Identify which bone Head Office's training actually targeted.", ""),
            ("Circle the three causes you would investigate first and write one line of justification for each.", ""),
            ("Screenshot or export the diagram and present your top three plus your verdict on the training decision.", ""),
        ],
        test=(
            "Your fishbone is complete when: every bone has at least three entries; every entry is marked "
            "[EVIDENCED] or [HYPOTHESIS]; every entry is phrased as a cause ('single queue with no triage') "
            "rather than a complaint ('the queue is terrible') or a solution ('add more counters'); and you "
            "have found at least one cross-bone arrow. If any bone is empty, you have a visibility gap, not "
            "an absence of causes — say so explicitly."
        ),
    ),

    dict(
        num=4, topic=1,
        title="Activity 4 — Pareto Analysis to Target the Vital Few",
        objective="A1, A3 · K2 — Prioritise causes by contribution and identify key implications.",
        edtool=dict(name="Pareto Chart Tool", url="https://alfredang.github.io/paretochart/"),
        services="Pareto Chart ed-tool, ChatGPT / Copilot / Gemini",
        duration="40 minutes",
        grouping="Teams of 3-5",
        case_title="Nexa Logistics — 2,000 failed deliveries a month",
        scenario=(
            "Nexa Logistics runs last-mile delivery for e-commerce clients across Singapore. Of 40,000 "
            "monthly deliveries, 2,000 fail on first attempt — a 5% failure rate against a contractual "
            "SLA of 2%. Every failed delivery costs S$8.50 to re-attempt: S$17,000 a month, and two "
            "clients have invoked SLA penalty clauses.\n\n"
            "The Operations Director has a list of eleven failure reasons and a budget that will fund "
            "roughly two initiatives this quarter. His instinct is to start with 'Address incorrect' "
            "because it generates the angriest client emails.\n\n"
            "Your team must decide where the two initiatives should go — using the data, not the noise."
        ),
        data=dict(
            name="nexa-failure-reasons",
            caption="Nexa Logistics — first-attempt delivery failures by reason, last month",
            rows=[
                ["Failure reason", "Count", "Cost impact (S$)"],
                ["Recipient not at home (no delivery window given)", "742", "6307"],
                ["Driver could not access condo / office lobby", "486", "4131"],
                ["Address incomplete or incorrect", "231", "1964"],
                ["Parcel not loaded (sorting error)", "188", "1598"],
                ["Recipient refused (wrong item expected)", "121", "1029"],
                ["Vehicle breakdown / route disruption", "94", "799"],
                ["Weather-related suspension", "61", "519"],
                ["Recipient contact number invalid", "38", "323"],
                ["Parcel damaged in transit", "24", "204"],
                ["Restricted delivery hours at destination", "20", "170"],
                ["Other / unclassified", "15", "128"],
            ],
        ),
        prompt=(
            "Act as an operations analyst. Perform a Pareto (80/20) analysis on the delivery failure "
            "data below for a Singapore last-mile logistics company.\n\n"
            "Total deliveries: 40,000/month. Failures: 2,000 (5%). SLA target: 2%. "
            "Re-attempt cost: S$8.50 each.\n\n"
            "Data (reason, count):\n"
            "Recipient not at home 742; Lobby access denied 486; Address incorrect 231; Parcel not "
            "loaded 188; Recipient refused 121; Vehicle breakdown 94; Weather 61; Invalid contact 38; "
            "Damaged 24; Restricted hours 20; Other 15.\n\n"
            "Produce:\n"
            "1. A table with count, percentage, and CUMULATIVE percentage, sorted descending\n"
            "2. The cut-off line — which reasons make up the vital few (roughly 80%)\n"
            "3. The monthly S$ recovery if the top 2 reasons were reduced by 60%\n"
            "4. Whether hitting the 2% SLA is achievable by fixing the vital few alone — show the arithmetic\n"
            "5. One caution about what this Pareto analysis does NOT tell me"
        ),
        questions=[
            "Build the Pareto chart. How many of the eleven reasons account for roughly 80% of failures? What does that ratio mean for how the Operations Director should spend his budget?",
            "The Director wants to start with 'Address incorrect' because it generates the angriest emails. What does the data say, and how would you make that argument to him without dismissing his concern?",
            "Calculate: if the top two reasons drop by 60%, what is the new failure rate? Does that meet the 2% SLA? Show your arithmetic.",
            "The top two reasons — 'not at home' and 'lobby access' — look like customer problems. Reframe each as something Nexa controls. What changes about who owns the fix?",
            "Pareto ranks by FREQUENCY. Name a situation in your own workplace where the most frequent problem is not the most important one. What would you rank by instead?",
        ],
        debrief=(
            "EXPECTED ANALYSIS:\n"
            "  Not at home 742 (37.1%, cum 37.1%)\n"
            "  Lobby access 486 (24.3%, cum 61.4%)\n"
            "  Address incorrect 231 (11.6%, cum 73.0%)\n"
            "  Parcel not loaded 188 (9.4%, cum 82.4%)  <- the 80% line falls here\n"
            "  The remaining 7 reasons together account for under 18%.\n\n"
            "So FOUR of eleven reasons carry 82% of the failures — and the top TWO alone carry 61%.\n\n"
            "ARITHMETIC: a 60% reduction on the top two removes 0.6 x 1,228 = 737 failures, leaving 1,263 "
            "of 40,000 = 3.2%. That is a large win but it does NOT reach the 2% SLA (which needs failures "
            "under 800). Reaching SLA requires the top two AND a meaningful dent in reasons 3 and 4. "
            "Learners who claim the SLA is met have not done the arithmetic — make them show it.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. 'Address incorrect' is only 11.6% — third place. It is loud, not large. The Director is "
            "responding to escalation volume, which correlates with client temperament, not failure "
            "frequency. The Pareto chart is how you have that conversation with evidence rather than "
            "opinion. This is the transferable political skill in this activity.\n"
            "2. REFRAMING OWNERSHIP is the deeper lesson: 'recipient not at home' is only a customer "
            "problem if you never offered a delivery window. 'Lobby access denied' is only a customer "
            "problem if you never negotiated building access protocols. Both become Nexa-controllable "
            "the moment you restate them — and 61% of the problem changes owner.\n"
            "3. LIMITATION: Pareto ranks by frequency, and frequency is not severity. A single "
            "safety-critical or regulatory failure can outrank 700 inconveniences. Always ask what the "
            "right ranking dimension is — count, cost, risk or customer harm. Here, cost tracks count "
            "closely (uniform S$8.50), which is why the two rankings agree; that is not always true.\n"
            "4. Pareto tells you WHERE to look, never WHY. The 742 'not at home' failures still need a "
            "5 Whys. The tools chain: Pareto for priority, then 5 Whys for cause."
        ),
        steps=[
            ("Read the Nexa Logistics scenario and the failure reason table.", ""),
            ("Open the Pareto ed-tool at https://alfredang.github.io/paretochart/", ""),
            ("Enter each failure reason and its count. The tool sorts descending and computes the cumulative line.", ""),
            ("Read off the cumulative percentage and mark where the line crosses 80%.", ""),
            ("Count how many reasons sit to the left of that line — these are your vital few.", ""),
            ("Calculate by hand: a 60% reduction on the top two gives what new failure rate? Compare against the 2% SLA.", ""),
            ("Run the GenAI Pareto prompt from the slide and check the AI's arithmetic against your own. Note any error.", ""),
            ("Restate the top two reasons so that Nexa — not the customer — owns the fix.", ""),
            ("Decide where the two funded initiatives should go and prepare a one-minute case for the Operations Director.", ""),
            ("Present, including the arithmetic showing whether the SLA is reachable.", ""),
        ],
        test=(
            "Your analysis is sound when: the cumulative column reaches 100%; you can name the vital few "
            "and the exact cumulative percentage at your cut-off; you have shown the arithmetic on whether "
            "the 2% SLA is reachable (it is not, on the top two alone); and you can state in one sentence "
            "what Pareto does NOT tell you. Verify the AI's percentages against the tool's — if they "
            "disagree, the tool is right and you have just learned something about trusting AI arithmetic."
        ),
    ),

    dict(
        num=5, topic=1,
        title="Activity 5 — System Loops: Why the Problem Keeps Coming Back",
        objective="A3 · K2 — Deduce linkages and patterns to identify key implications on organisational systems.",
        edtool=dict(name="System Loop Tool", url="https://alfredang.github.io/systemloop/"),
        services="System Loop ed-tool, ChatGPT / Copilot / Gemini",
        duration="50 minutes",
        grouping="Teams of 3-5",
        case_title="Horizon Bank revisited — the fix that made it worse",
        scenario=(
            "Return to Horizon Bank Jurong East. Acting on the fishbone, the Regional Director did the "
            "obvious thing: he ordered two additional counters staffed at peak, redeploying staff from "
            "the back office.\n\n"
            "Month 1: average wait fell from 58 to 34 minutes. Everyone celebrated.\n"
            "Month 4: average wait is back to 61 minutes — WORSE than before. Complaints are at 68 per "
            "month. Three more tellers have resigned. Back-office processing is now two days behind, "
            "which has started generating a new complaint category of its own.\n\n"
            "The Regional Director is baffled: \"We added capacity and the problem came back bigger. "
            "What am I missing?\"\n\n"
            "What he is missing is that a branch is not a queue — it is a system of feedback loops. "
            "Your team must map them."
        ),
        data=dict(
            name="horizon-loop-variables",
            caption="Horizon Bank — system variables and observed 4-month movements",
            rows=[
                ["Variable", "Month 1", "Month 4", "Direction"],
                ["Counters staffed at peak", "3.2", "5.1", "up"],
                ["Average wait time (min)", "58 -> 34", "61", "down then up"],
                ["Back-office processing backlog (days)", "0.5", "2.0", "up"],
                ["Teller errors requiring rework", "6%", "14%", "up"],
                ["Rework returning to the counter", "low", "high", "up"],
                ["Teller overtime hours / month", "88", "196", "up"],
                ["Staff resignations (quarter)", "2", "3", "up"],
                ["Share of counter staff under 6 months", "44%", "58%", "up"],
                ["Mean transaction handling time (min)", "9", "13", "up"],
                ["Customer complaints / month", "60", "68", "up"],
                ["Digital channel adoption", "21%", "20%", "flat"],
            ],
        ),
        prompt=(
            "Act as a systems thinking facilitator. Help me map the causal feedback loops in this case.\n\n"
            "Situation: A bank branch added 2 counters at peak by redeploying back-office staff. Wait "
            "time fell from 58 to 34 minutes in month 1, then rose to 61 minutes by month 4 — worse than "
            "the starting point.\n\n"
            "Observed changes over 4 months: back-office backlog 0.5 -> 2.0 days; teller errors 6% -> 14%; "
            "rework returning to the counter rose; overtime 88 -> 196 hrs/month; resignations rose; share "
            "of tellers under 6 months 44% -> 58%; mean handling time 9 -> 13 min; digital adoption flat "
            "at ~20%.\n\n"
            "Produce:\n"
            "1. At least 2 REINFORCING (R) loops and 2 BALANCING (B) loops. For each, list the variables "
            "in causal order with (+) or (-) on each link, and name the loop\n"
            "2. Explain specifically WHY the month-1 improvement reversed — which loop overwhelmed which\n"
            "3. Identify the delay in the system and explain why the delay made the wrong decision look right\n"
            "4. Name 2 leverage points that would break the reinforcing loops, and say what makes them "
            "leverage rather than just more effort"
        ),
        questions=[
            "Map at least two reinforcing (R) and two balancing (B) loops. Which loop did the Regional Director believe he was pulling, and which loop did he actually trigger?",
            "Month 1 showed real improvement. Explain the DELAY: why did the harmful loop take three months to overwhelm the helpful one, and what does that mean for how we evaluate quick wins?",
            "Follow the back-office redeployment all the way round. Trace how a decision about counters ended up increasing teller resignations.",
            "Digital adoption stayed flat at 20% throughout. Which loop is NOT running that should be, and why is a dormant balancing loop as dangerous as an active reinforcing one?",
            "Name two leverage points. What makes a leverage point different from simply doing more of the same thing harder?",
        ],
        debrief=(
            "EXPECTED LOOPS:\n\n"
            "B1 — CAPACITY CONTROL (balancing, what the Director intended): wait time up (+) -> management "
            "pressure (+) -> counters staffed (+) -> service capacity (+) -> wait time DOWN (-). This is "
            "the loop that produced the month-1 win. It is real, but it is not the only loop running.\n\n"
            "R1 — REDEPLOYMENT BACKFIRE (reinforcing, the loop he triggered without seeing it): counters "
            "staffed (+) -> back-office staff removed (+) -> processing backlog (+) -> errors and "
            "unresolved cases (+) -> rework returns to the counter (+) -> counter workload (+) -> handling "
            "time (+) -> WAIT TIME (+) -> more pressure to staff counters (+). Handling time rising from "
            "9 to 13 minutes is the fingerprint of this loop.\n\n"
            "R2 — BURNOUT SPIRAL (reinforcing): workload (+) -> overtime (+) -> stress and burnout (+) -> "
            "resignations (+) -> share of inexperienced tellers (+) -> error rate (+) -> rework (+) -> "
            "workload (+). Tellers under 6 months rising 44% -> 58% while errors doubled 6% -> 14% is the "
            "fingerprint here.\n\n"
            "B2 — DIGITAL MIGRATION (balancing, DORMANT): wait time (+) -> willingness to try digital (+) "
            "-> digital adoption (+) -> branch transaction volume (-) -> wait time (-). Adoption stayed "
            "flat at ~20%, so this loop never engaged. Nothing was done to activate it.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. THE CENTRAL INSIGHT: he pulled B1 and unknowingly powered R1 and R2. Because R-loops "
            "compound, they eventually overwhelm a one-off capacity increase. Adding capacity to a system "
            "with an active reinforcing loop buys a temporary win and a bigger relapse.\n"
            "2. DELAY IS THE TRAP: B1 acts in days (staff a counter, wait drops). R1 and R2 act over "
            "months (backlog builds, errors accumulate, people quit). The delay is precisely why the "
            "month-1 result validated a decision that was making things worse. Every learner should leave "
            "able to say: 'a quick win measured too early is indistinguishable from a mistake.' This is "
            "the direct bridge into Topic 3's leading vs lagging indicators.\n"
            "3. DORMANT LOOPS: B2 was available the whole time and nobody activated it. Shifting simple "
            "transactions to digital reduces the load that feeds R1. Asking 'which balancing loop is not "
            "running?' is often more productive than adding effort to loops that are.\n"
            "4. LEVERAGE vs EFFORT: more counters = effort (you must sustain it forever, and it feeds R1). "
            "Leverage = breaking a link in a reinforcing loop: triage complex cases away from the counter; "
            "eliminate the triple data entry so error rate falls; protect back-office capacity so rework "
            "never returns to the counter; activate B2 with in-branch digital ambassadors. Leverage "
            "changes the structure; effort fights the structure.\n"
            "5. This is why Topic 1 ends here. 5 Whys gave depth, Fishbone gave breadth, Pareto gave "
            "priority — and System Loops explains why well-intentioned fixes rebound. Learners now have "
            "the full diagnostic set before touching solutions in Topic 2."
        ),
        steps=[
            ("Read the revisited Horizon Bank scenario and the 4-month variable movements.", ""),
            ("Open the System Loop ed-tool at https://alfredang.github.io/systemloop/", ""),
            ("List the key variables from the table as nodes: counters staffed, wait time, backlog, errors, rework, overtime, resignations, inexperience, handling time, digital adoption.", ""),
            ("Draw the loop the Director INTENDED: pressure -> counters -> capacity -> wait time down. Label it B1 and confirm it closes as balancing.", ""),
            ("Now trace the redeployment: where did the back-office staff come from, and what happened downstream? Close that loop and label it R1.", ""),
            ("Trace the workload consequences on people: overtime, resignations, inexperience, errors. Close it and label it R2.", ""),
            ("Mark (+) or (-) on every link. Verify each loop: an even number of (-) links makes it reinforcing; an odd number makes it balancing.", ""),
            ("Identify where the DELAY sits — which loop acts in days and which acts in months.", ""),
            ("Ask which balancing loop is available but not running. Add B2 (digital adoption) and mark it dormant.", ""),
            ("Run the GenAI system-thinking prompt from the slide and compare its loops against yours.", ""),
            ("Circle two leverage points where breaking ONE link would collapse a reinforcing loop.", ""),
            ("Present: the four loops, why month 1 lied to you, and your two leverage points.", ""),
        ],
        test=(
            "Your loop map is valid when: every loop CLOSES (the last variable feeds back to the first); "
            "every link carries a (+) or (-); each loop is correctly typed as R or B by counting negative "
            "links; you can explain the month-1-to-month-4 reversal by naming which loop overwhelmed which; "
            "and your leverage points break a LINK in a reinforcing loop rather than adding more effort to "
            "a balancing one. If your answer is 'hire more people', you have described effort, not leverage."
        ),
    ),
]
