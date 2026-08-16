"""
Topic 2 activities — Developing Corrective Plans and Evaluating Potential Solutions.
"""

DOMAIN2 = [
    dict(
        num=6, topic=2,
        title="Activity 6 — Divergent Ideation with GenAI (Breadth Before Judgement)",
        objective="A5 · K4 — Generate a wide solution set using appropriate problem-solving techniques.",
        edtool=dict(name="Pinboard", url="https://alfredang.github.io/pinboard/"),
        services="ChatGPT / Copilot / Gemini, Pinboard",
        duration="45 minutes",
        grouping="Teams of 3-5",
        case_title="Meridian Health — solving the retention root cause",
        scenario=(
            "Your 5 Whys in Activity 2 established the root cause at Meridian Health: a workforce "
            "retention and onboarding failure that leaves 40% of the 07:00 roster staffed by untrained "
            "relief phlebotomists at 14 minutes per draw instead of 6.\n\n"
            "The Clinical Director has accepted the analysis and killed the S$1.2m seventh-centre "
            "proposal. She now wants options — and she has been explicit: \"Don't bring me three "
            "sensible ideas. Bring me twenty, including the ones that sound ridiculous, and then tell "
            "me which four are real.\"\n\n"
            "Budget guidance: up to S$250,000 over 12 months. Constraint: MOH clinical protocols on "
            "phlebotomy competency cannot be relaxed under any circumstances."
        ),
        data=dict(
            name="meridian-constraints",
            caption="Meridian Health — solution constraints and context",
            rows=[
                ["Constraint", "Detail"],
                ["Budget", "Up to S$250,000 over 12 months"],
                ["Clinical", "MOH phlebotomy competency standards are non-negotiable"],
                ["Contract", "07:00-09:30 fasting draw window is contractual with corporate clients"],
                ["Courier", "Lab courier at 09:45 is fixed by the external lab partner"],
                ["Workforce", "Permanent phlebotomist turnover 44%/yr; relief pool is agency-supplied"],
                ["Training", "Current onboarding is 2 days shadowing, no structured sign-off"],
                ["Market", "Phlebotomist salaries are within 5% of the market median"],
                ["Shift", "Early shift (06:30 start) attracts no differential pay"],
            ],
        ),
        prompt=(
            "Act as an innovation consultant running a divergent ideation session. Do NOT evaluate or "
            "filter yet.\n\n"
            "Root cause to solve: A Singapore health-screening operator has 44% annual turnover among "
            "permanent phlebotomists. Vacancies are backfilled by agency relief staff who take 14 min "
            "per blood draw versus 6 min for trained staff. 40% of the 07:00 roster is relief staff, "
            "causing 31% of morning appointments to overrun and 23% of samples to miss the fixed 09:45 "
            "lab courier.\n\n"
            "Constraints: S$250k over 12 months; MOH phlebotomy competency standards cannot be relaxed; "
            "the 07:00-09:30 fasting window and the 09:45 courier are both fixed.\n\n"
            "Generate 20 distinct solutions grouped under:\n"
            "- People & Retention\n"
            "- Training & Onboarding\n"
            "- Process & Scheduling\n"
            "- Technology & Automation\n"
            "- Customer/Client Experience\n\n"
            "Rules:\n"
            "- Include at least 4 ideas that would normally be dismissed as unrealistic\n"
            "- Include at least 2 ideas borrowed from a COMPLETELY different industry (say which)\n"
            "- One line each, phrased as an action\n"
            "- Do NOT rank, cost or evaluate them\n\n"
            "Then, separately: apply SCAMPER (Substitute, Combine, Adapt, Modify, Put to another use, "
            "Eliminate, Reverse) to the single assumption that 'every draw must be done by a "
            "phlebotomist at the centre between 07:00 and 09:30' and give one idea per SCAMPER letter."
        ),
        questions=[
            "Your team generated ideas manually first, then with GenAI. Compare the two lists — how many did the AI produce that your team would never have said out loud, and why not?",
            "The AI was asked for two ideas borrowed from another industry. Which cross-industry idea is most transferable to Meridian, and what would have to be true for it to work?",
            "Apply SCAMPER's 'Reverse' and 'Eliminate' to the fixed 07:00-09:30 window. Which supposedly fixed constraint turns out to be an assumption rather than a real constraint?",
            "Identify one idea on your list that is genuinely ruled out by the MOH clinical constraint. How do you tell a hard constraint from a habit?",
            "Cognitive fixedness is the tendency to reach for the familiar solution. Find one idea on your list that only appeared because you deliberately broke fixedness — what triggered it?",
        ],
        debrief=(
            "EXPECTED RANGE — a strong list spans all five groups and includes at least these shapes:\n"
            "  PEOPLE & RETENTION — early-shift differential pay; career ladder to senior phlebotomist; "
            "convert best relief staff to permanent; retention bonus at 12 and 24 months; exit-interview "
            "programme to find the real reason people leave.\n"
            "  TRAINING & ONBOARDING — structured 10-day onboarding with competency sign-off; simulation "
            "arm practice before live draws; buddy system pairing relief with permanent staff; a "
            "micro-credential the agency pool can earn before their first shift.\n"
            "  PROCESS & SCHEDULING — stagger appointment slots so relief staff take simpler draws; "
            "roster all 5 permanent staff at 07:00 and taper later; pre-screen difficult-draw patients "
            "to trained staff; negotiate a second courier pickup.\n"
            "  TECHNOLOGY — vein-finder devices to cut the 18% repeat rate; digital pre-registration; "
            "automated fasting-compliance reminders the night before; queue app.\n"
            "  CLIENT EXPERIENCE — corporate on-site draws at the client's office; extend the window by "
            "agreement; tiered booking so the largest client gets trained staff.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. DIVERGENCE MUST PRECEDE JUDGEMENT. Teams that evaluate while generating typically stop "
            "at 6-8 ideas, all conventional. The instruction to include 'ridiculous' ideas exists because "
            "the ridiculous ones are where fixedness breaks — and the merely unusual ones next to them "
            "are often viable. Count your team's manual list against the AI list; the gap IS the lesson.\n"
            "2. GENAI IS A DIVERGENCE ENGINE. This is its strongest contribution to problem solving: "
            "breadth at near-zero cost, free of the political self-censorship that stops a junior "
            "employee proposing 'pay the early shift more' in front of a Finance Director. The AI has no "
            "career risk. Note that it also has no judgement — which is Activity 7's job.\n"
            "3. THE SCAMPER REVEAL: the biggest unlock is that the 07:00-09:30 window is fixed only "
            "because draws happen AT THE CENTRE. 'Reverse' (bring the draw to the client's office) and "
            "'Eliminate' (remove the centre visit for corporate clients entirely) both dissolve the "
            "constraint rather than working within it. Meanwhile the MOH competency standard is a genuine "
            "hard constraint — it is a regulation, not a habit. Teaching learners to separate REGULATION "
            "from HABIT is the durable skill here.\n"
            "4. CROSS-INDUSTRY TRANSFER: mobile phlebotomy mirrors mobile blood-donation drives; the "
            "buddy/competency-card model comes from aviation and F&B; surge differential pay comes from "
            "ride-hailing. Analogy is a recognised problem-solving strategy, and GenAI is unusually good "
            "at it because it has read across every domain.\n"
            "5. Do NOT let teams rank yet. Ranking is Activity 7. Holding the line between divergence and "
            "convergence is itself the discipline being taught."
        ),
        steps=[
            ("Restate the Meridian root cause from Activity 2 in one sentence so the whole team is solving the same thing.", ""),
            ("MANUAL ROUND FIRST — set a 7-minute timer. Each person writes ideas silently on post-its. No discussion, no evaluation, no 'that won't work'.", ""),
            ("Post all ideas to the wall at https://alfredang.github.io/pinboard/ and count them.", ""),
            ("Now run the GenAI divergent ideation prompt from the slide.", ""),
            ("Add every AI idea your team did not already have to the board, in a different colour.", ""),
            ("Count the two groups. Discuss: which AI ideas would nobody in your team have proposed in a real meeting, and what stopped them?", ""),
            ("Run the SCAMPER section of the prompt against the '07:00-09:30 at the centre' assumption.", ""),
            ("For each SCAMPER letter, add the resulting idea to the board.", ""),
            ("Go through the board and mark each idea HARD CONSTRAINT (genuinely ruled out by MOH or contract) or HABIT (only feels fixed).", ""),
            ("Do NOT rank or cost anything yet — carry the full board forward to Activity 7.", ""),
        ],
        test=(
            "Your divergence is sufficient when: you have at least 20 distinct ideas spanning all five "
            "groups; at least 4 would raise an eyebrow in a management meeting; at least 2 are borrowed "
            "from another industry and you can name it; you have one idea per SCAMPER letter; and you have "
            "correctly separated at least one HARD CONSTRAINT from at least one HABIT. If every idea on "
            "your board is comfortable, you have not diverged — you have listed."
        ),
    ),

    dict(
        num=7, topic=2,
        title="Activity 7 — Converging: Impact-Ease Matrix and Weighted Decision Matrix",
        objective="A5 · K4, K6 — Shortlist and evaluate the most viable ideas using decision-making techniques.",
        edtool=dict(name="Pinboard", url="https://alfredang.github.io/pinboard/"),
        services="ChatGPT / Copilot / Gemini, Pinboard",
        duration="50 minutes",
        grouping="Teams of 3-5",
        case_title="Meridian Health — choosing four from twenty",
        scenario=(
            "You now hold twenty-plus candidate solutions from Activity 6. The Clinical Director will "
            "fund approximately four, inside S$250,000 over 12 months.\n\n"
            "Two members of your team are already advocating loudly for their favourite ideas and the "
            "discussion is circling. This is exactly the moment where teams either make an evidence-based "
            "decision or default to whoever is most senior or most persistent.\n\n"
            "Your job is to convert the board into a defensible shortlist using two complementary tools: "
            "a fast Impact-Ease screen, then a weighted decision matrix on the survivors."
        ),
        data=dict(
            name="meridian-decision-criteria",
            caption="Meridian Health — agreed decision criteria and weightings",
            rows=[
                ["Criterion", "Weight", "Scoring guidance (1-5)"],
                ["Impact on root cause (retention/training)", "35%", "5 = directly fixes the root cause"],
                ["Speed to measurable effect", "20%", "5 = effect visible within 8 weeks"],
                ["Cost within S$250k envelope", "20%", "5 = under S$25k"],
                ["Clinical/regulatory risk", "15%", "5 = no MOH implication at all"],
                ["Staff and client acceptance", "10%", "5 = actively welcomed by both"],
            ],
        ),
        prompt=(
            "Act as a decision analyst. I will give you a list of candidate solutions. Do NOT add new "
            "ideas.\n\n"
            "STEP 1 — Classify every solution on an Impact vs Ease matrix as exactly one of:\n"
            "- Quick Win (high impact, easy)\n"
            "- Big Bet (high impact, hard)\n"
            "- Fill-In (low impact, easy)\n"
            "- Thankless Task (low impact, hard)\n"
            "Give a one-line reason for each placement.\n\n"
            "STEP 2 — Take only the Quick Wins and Big Bets and score them in a weighted decision matrix:\n"
            "- Impact on root cause (weight 35%)\n"
            "- Speed to measurable effect (20%)\n"
            "- Cost within a S$250k envelope (20%)\n"
            "- Clinical/regulatory risk (15%)\n"
            "- Staff and client acceptance (10%)\n"
            "Score each 1-5, show the weighted total, and rank them.\n\n"
            "STEP 3 — Recommend the best FOUR as a portfolio, and explicitly state:\n"
            "- why this combination is stronger than the top four individual scores\n"
            "- which two solutions overlap or make each other redundant\n"
            "- what the portfolio still leaves unaddressed\n\n"
            "Solutions: [paste your team's list here]"
        ),
        questions=[
            "Place all your ideas on the Impact-Ease matrix. Which quadrant is most crowded, and what does a crowded Fill-In quadrant tell you about how your team was thinking?",
            "Run the weighted matrix. Did the top-scoring solution match your team's gut favourite from Activity 6? If not, what did the weighting expose?",
            "Change the weight on 'Speed to measurable effect' from 20% to 40% and re-rank. Does the winner change? What does that sensitivity tell you about how robust your recommendation is?",
            "The AI recommended a portfolio of four. Explain why the best four INDIVIDUAL scores are not automatically the best four TOGETHER.",
            "Consensus fatigue is when a team accepts a weak option just to end the discussion. Where in this activity was your team most at risk of it, and what stopped you?",
        ],
        debrief=(
            "EXPECTED SHAPE OF A STRONG ANSWER:\n"
            "  QUICK WINS — roster all 5 permanent phlebotomists at 07:00 and taper later (near-zero cost, "
            "immediate effect); early-shift differential pay; pre-visit fasting-compliance reminders; "
            "route difficult draws to trained staff.\n"
            "  BIG BETS — structured 10-day onboarding with competency sign-off; convert top relief staff "
            "to permanent; corporate on-site draws.\n"
            "  FILL-INS — better signage, updated leaflets, minor booking-form changes.\n"
            "  THANKLESS — a new centre; a full HR system replacement.\n\n"
            "A defensible portfolio of four usually pairs an immediate stabiliser with a root-cause fix, "
            "e.g.: (1) re-roster the 07:00 shift — buys relief NOW at almost no cost; (2) early-shift "
            "differential — attacks why people leave the early shift; (3) structured onboarding with "
            "competency sign-off — attacks the 14-min relief draw time and the 18% repeat rate; "
            "(4) convert top relief staff to permanent — converts the agency pool into retained capacity.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. TWO TOOLS, TWO JOBS. Impact-Ease is a fast screen that clears the board of Fill-Ins and "
            "Thankless Tasks in minutes. The weighted matrix is the rigorous instrument you use on the "
            "survivors and, crucially, the one you can DEFEND to a board. Using the heavy tool on all "
            "twenty wastes the session; using only the light tool leaves you unable to justify the call.\n"
            "2. THE WEIGHTS ARE THE REAL DECISION. Most teams argue about scores when the disagreement is "
            "actually about weights. Surfacing weights first — before any scoring — converts a political "
            "argument into an explicit, recorded choice. This is the single most useful facilitation move "
            "in the activity.\n"
            "3. SENSITIVITY TESTING: if doubling the speed weight flips the winner, your recommendation is "
            "fragile and you must say so. If the same solution wins under several weightings, you have a "
            "robust recommendation. Boards trust the second kind. Teach learners to run the test BEFORE "
            "they present, not after they are challenged.\n"
            "4. PORTFOLIO, NOT LEADERBOARD: the top four scores may all attack the same cause and leave "
            "another exposed, or two may be redundant (on-site corporate draws largely removes the need "
            "for the 07:00 re-roster for those clients). A portfolio balances quick stabilisation against "
            "durable root-cause repair. This is where human judgement outperforms the AI's ranking, and "
            "learners should see that clearly.\n"
            "5. AI LIMITATION TO NAME OUT LOUD: the AI will confidently invent cost figures and timelines "
            "it has no basis for. Its ranking is only as good as the criteria you set. It is a fast, "
            "tireless, unbiased-by-politics scorer — not a decision maker. The Clinical Director will ask "
            "YOU why, not the model."
        ),
        steps=[
            ("Bring the full idea board from Activity 6. Remove any duplicates by merging them.", ""),
            ("Draw the Impact-Ease matrix on a flip chart with four labelled quadrants.", ""),
            ("Place every idea in a quadrant as a team. Where you disagree, place it on the line and move on — do not stall.", ""),
            ("Discard the Thankless Tasks. Set the Fill-Ins aside as 'do if free capacity'.", ""),
            ("BEFORE scoring anything, agree the five criteria weights as a team. Write them down. This prevents arguing about scores when you actually disagree about weights.", ""),
            ("Build the weighted decision matrix for the surviving Quick Wins and Big Bets. Score each criterion 1-5.", ""),
            ("Compute the weighted totals and rank.", ""),
            ("Run the GenAI convergence prompt from the slide with your actual list pasted in.", ""),
            ("Compare the AI ranking to yours. Investigate every place they disagree by more than two positions.", ""),
            ("SENSITIVITY TEST: change the speed weight from 20% to 40% and re-rank. Record whether the winner changes.", ""),
            ("Select your final FOUR as a PORTFOLIO — check they do not all attack the same cause, and check for redundancy.", ""),
            ("Prepare a two-minute recommendation to the Clinical Director: the four, the total cost, the criteria, and the one thing you are still leaving unaddressed.", ""),
        ],
        test=(
            "Your shortlist is defensible when: every surviving idea sits in a named quadrant; the "
            "weighted matrix shows criteria, weights, scores and totals; you have run at least one "
            "sensitivity test and can state whether the winner held; your four are a portfolio rather than "
            "the top four scores; the total cost fits inside S$250k; and you can name one thing the "
            "portfolio does NOT fix. If you cannot explain to the Clinical Director why idea #5 lost, the "
            "matrix has not done its job."
        ),
    ),

    dict(
        num=8, topic=2,
        title="Activity 8 — Building the Corrective Action Plan",
        objective="A4 · K9 — Develop corrective action plans for shortfalls identified.",
        edtool=dict(name="Pinboard", url="https://alfredang.github.io/pinboard/"),
        services="ChatGPT / Copilot / Gemini, Pinboard",
        duration="45 minutes",
        grouping="Teams of 3-5",
        case_title="Meridian Health — from chosen solutions to an auditable plan",
        scenario=(
            "The Clinical Director has approved your four solutions. She now asks the question that "
            "separates a good analysis from a delivered result:\n\n"
            "\"Who is doing what, by when, with what money, and how will I know it worked?\"\n\n"
            "She also adds a warning from experience: \"The last improvement project we ran had a "
            "beautiful slide deck and no owner. Six months later nothing had changed and everyone "
            "assumed someone else was doing it.\"\n\n"
            "Your team must convert four approved solutions into a corrective action plan that would "
            "survive an internal audit — and that a colleague could execute without you in the room."
        ),
        data=dict(
            name="cap-components",
            caption="Corrective Action Plan — mandatory components (K9)",
            rows=[
                ["Component", "Why it exists", "Failure if missing"],
                ["Root cause addressed", "Ties the action to the diagnosis", "Solution drifts to a symptom"],
                ["Corrective action", "The specific thing being done", "Vague intent, no execution"],
                ["Owner (named person)", "Single point of accountability", "Everyone assumes someone else"],
                ["Timeline / milestone", "Makes progress checkable", "Slips indefinitely, unnoticed"],
                ["Resources required", "Budget, people, tools committed", "Stalls at first resource conflict"],
                ["Success measure + baseline", "Defines what 'worked' means", "Cannot evaluate; endless debate"],
                ["Risk and mitigation", "Anticipates what breaks it", "Surprised by predictable failure"],
                ["Review checkpoint", "Forces a decision to continue/stop", "Runs on past the point of failure"],
            ],
        ),
        prompt=(
            "You are an execution-focused planning assistant. Convert each approved solution into a "
            "corrective action plan row. Be concrete and brief — no theory.\n\n"
            "For EACH solution, produce exactly these fields:\n"
            "- Root cause addressed (link back to the diagnosis)\n"
            "- Corrective action (one specific sentence)\n"
            "- Owner (a job title, not a department)\n"
            "- Timeline (start, key milestone, completion)\n"
            "- Resources (budget in S$, people, tools)\n"
            "- Success measure (metric + baseline + target)\n"
            "- Key risk + mitigation\n"
            "- Review checkpoint (date and the decision to be made at it)\n\n"
            "Then flag, in a separate section:\n"
            "1. Any two actions that depend on each other and must be sequenced\n"
            "2. Any owner who appears on more than two actions (overload risk)\n"
            "3. Any success measure that cannot actually be measured with data the organisation already has\n\n"
            "Approved solutions: [paste your four here]\n"
            "Root cause: 44% phlebotomist turnover leaving 40% of the 07:00 roster untrained, causing "
            "14-min draws vs 6-min, 31% appointment overruns and 23% of samples missing the 09:45 courier.\n"
            "Budget: S$250,000 over 12 months."
        ),
        questions=[
            "Complete all eight components for each of your four actions. Which component did your team find hardest to fill honestly, and what does that reveal?",
            "Every owner must be a named role, not a department. Why does 'Operations' fail as an owner where 'Centre Operations Manager' succeeds?",
            "Check your success measures against the baseline in your original problem statement. Can each one actually be measured with data Meridian already collects? Which cannot?",
            "The AI flagged dependencies between actions. Which two of your actions must be sequenced, and what breaks if you run them in parallel?",
            "Identify the biggest risk across your whole plan. Is your mitigation a real action with an owner, or a hope?",
        ],
        debrief=(
            "WORKED EXAMPLE — one complete row to standard:\n"
            "  Root cause addressed: Untrained relief staff on the 07:00 roster (14-min vs 6-min draws).\n"
            "  Corrective action: Implement a structured 10-day phlebotomy onboarding with formal "
            "competency sign-off before any unsupervised draw.\n"
            "  Owner: Clinical Training Lead.\n"
            "  Timeline: Design by week 3; pilot at two centres weeks 4-8; full rollout by week 14.\n"
            "  Resources: S$65,000 (trainer time, simulation arms, backfill cover); 0.4 FTE for 14 weeks.\n"
            "  Success measure: Mean relief-staff draw time from 14 min (baseline) to under 8 min by "
            "week 16; first-attempt success from 82% to 92%.\n"
            "  Key risk: Backfill cover unavailable during pilot, so centres refuse to release staff. "
            "Mitigation: Clinical Director pre-commits agency budget for pilot weeks; escalation path named.\n"
            "  Review checkpoint: Week 8 — decision to roll out, extend the pilot, or stop.\n\n"
            "KEY TEACHING POINTS:\n"
            "1. THE OWNER IS THE PLAN'S SPINE. 'Operations' cannot be phoned, cannot be held to a date "
            "and cannot be asked why it slipped. A named role can. The Clinical Director's warning in the "
            "scenario is the most common real-world failure of improvement projects, and it is entirely "
            "preventable with one discipline: one named owner per action, no exceptions, no co-owners.\n"
            "2. THE MEASURE MUST TIE TO THE BASELINE FROM TOPIC 1. This is where the course closes its "
            "own loop: the problem statement's baseline in Activity 1 is what makes evaluation possible "
            "in Topic 3. A team that skipped the baseline now literally cannot write this field — let "
            "them discover that themselves; it lands harder than being told.\n"
            "3. MEASURABILITY CHECK: 'improved staff morale' is not measurable with data Meridian holds. "
            "'Voluntary resignations per quarter' and 'early-shift roster fill rate' are. Force the "
            "substitution now, not at review time.\n"
            "4. SEQUENCING: converting relief staff to permanent DEPENDS on the onboarding programme "
            "existing — convert first and you have permanent staff trained to the old inadequate standard, "
            "locking in the defect. Dependencies are where good plans quietly fail.\n"
            "5. OWNER OVERLOAD: if the Centre Operations Manager owns three of four actions, the plan is "
            "a single point of failure regardless of how good each row looks. GenAI is genuinely useful "
            "at spotting this pattern mechanically — a good example of AI catching what a team misses "
            "because they are too close to it.\n"
            "6. THE REVIEW CHECKPOINT MUST CARRY A DECISION. 'Review progress' is theatre. 'Decide to "
            "roll out, extend or stop' is governance."
        ),
        steps=[
            ("List your four approved solutions from Activity 7 across the top of a flip chart.", ""),
            ("Draw the eight CAP components down the side as rows.", ""),
            ("Fill in 'Root cause addressed' for all four FIRST. If any solution cannot be traced to your diagnosed root cause, challenge whether it belongs in the plan.", ""),
            ("Assign a NAMED ROLE as owner for each action. Reject any department name. One owner per action — no co-owners.", ""),
            ("Add timelines with a start, a milestone and a completion date. Use week numbers, not 'Q3'.", ""),
            ("Cost each action and check the four together fit inside S$250,000.", ""),
            ("Write each success measure as metric + baseline + target. Cross-check the baseline against your Activity 1 problem statement.", ""),
            ("Test each measure: can Meridian measure this with data it already collects? If not, either change the measure or add 'establish measurement' as a task.", ""),
            ("Add the key risk and a mitigation that is itself an action with an owner — not a hope.", ""),
            ("Set a review checkpoint for each action and state the DECISION to be made at it.", ""),
            ("Run the GenAI corrective action plan prompt from the slide.", ""),
            ("Act on the AI's three flags: sequence the dependent actions, rebalance any overloaded owner, and fix any unmeasurable success measure.", ""),
            ("Post the completed plan to https://alfredang.github.io/pinboard/ and present one row in full to the room.", ""),
        ],
        test=(
            "Your CAP is audit-ready when: all eight components are complete for all four actions; every "
            "owner is a named role and no role owns more than two actions; every success measure has a "
            "metric, a baseline number and a target number; every measure is obtainable from data the "
            "organisation already has (or has an explicit task to start collecting it); dependencies are "
            "sequenced; every mitigation is an action with an owner; and every checkpoint names a decision. "
            "The real test: hand the plan to another team and ask them to execute row one without asking "
            "you a single question."
        ),
    ),
]
