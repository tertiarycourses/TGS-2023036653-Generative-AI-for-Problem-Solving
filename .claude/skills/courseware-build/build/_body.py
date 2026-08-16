"""
Deck body — WSQ Generative AI for Problem Solving.
Exec'd after _engine_head.py and _components.py, so every helper is in scope.
"""

TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}


def admin_assessment_block(tag="ASSESSMENT"):
    """Assessment -> Assessment Flow -> Digital Attendance (TRAQOM). Used at front AND end."""
    tile_grid("Final Assessment", [
        ("Written Assessment (WA)", "Short-answer questions covering problem identification, root cause analysis, solution selection and evaluation."),
        ("Case Study (CS)", "An integrated workplace scenario — you diagnose, decide and justify, exactly as in the activities."),
        ("Open book", "Slides, Learner Guide and approved materials only. No internet search, no AI tools during assessment."),
        ("Competent / Not Yet Competent", "Both instruments must be assessed Competent. A re-assessment path is available."),
    ], kicker=tag, cols=2, accent=BLUE)

    s = head(slide(), "Assessment Flow", tag, kcolor=BLUE)
    stages = [("TRAQOM Survey", "Complete on the LMS"),
              ("Digital Attendance", "Assessment QR scan"),
              ("Written Assessment", "SAQ · 1 hour"),
              ("Case Study", "Scenario · 1 hour"),
              ("Submit on LMS", "Upload your answers"),
              ("Summary Record", "Sign the ASR")]
    n = len(stages); X0 = Inches(0.85); TOTW = Inches(11.63)
    gap = Inches(0.16); cw = int((TOTW - gap * (n - 1)) / n)
    y = Inches(2.6); ch = Inches(1.9)
    for i, (lbl, det) in enumerate(stages):
        x = int(X0 + (cw + gap) * i)
        col = PALETTE[i % len(PALETTE)]
        cv = chevron(s, x, y, cw, ch, col)
        # Shrink the chevron's notch so the flat body is wide enough for a label.
        try: cv.adjustments[0] = 0.28
        except Exception: pass
        # Label sits in the flat body, biased right of the incoming notch.
        lsz = 11.5 if n <= 5 else 10
        txt(s, int(x + Inches(0.40)), int(y + ch / 2 - Inches(0.36)),
            int(cw - Inches(0.62)), Inches(0.72),
            [[(lbl, lsz, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x, int(y + ch + Inches(0.18)), cw, Inches(0.5),
            [[(det, 10.5, GREY, False)]], align=PP_ALIGN.CENTER)
    rect(s, Inches(0.85), Inches(5.35), Inches(11.63), Inches(1.15), LIGHT)
    rect(s, Inches(0.85), Inches(5.35), Inches(0.11), Inches(1.15), TEAL)
    txt(s, Inches(1.15), Inches(5.5), Inches(11.1), Inches(0.32),
        [[("RE-ASSESSMENT", 11, TEAL, True)]])
    txt(s, Inches(1.15), Inches(5.84), Inches(11.1), Inches(0.6),
        [[("A learner assessed Not Yet Competent is counselled on the gap and offered a re-assessment. "
           "An appeal may be lodged with the training administrator within 7 working days.", 12, INK, False)]])
    footer(s)

    tile_grid("Digital Attendance & TRAQOM Survey", [
        ("AM · PM · Assessment", "Digital attendance is taken three times a day. It is mandatory for every WSQ-funded course."),
        ("Scan the SSG QR code", "The trainer displays the QR code from the SSG portal. Scan it with your phone camera and submit."),
        ("75% minimum attendance", "Below 75% you are not eligible for assessment or for course fee funding."),
        ("TRAQOM survey", "Complete the mandatory post-course survey and collect your certificate at " + C.LMS),
    ], kicker="MANDATORY ADMIN", cols=2, accent=VIOLET)


# ============================================================ COVER
cover()

# ============================================================ ADMIN (FRONT)
section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

tile_grid("Digital Attendance (Mandatory)", [
    ("Three times a day", "Take the AM, PM and Assessment digital attendance — mandatory for every WSQ-funded course."),
    ("Trainer shows the QR", "The trainer or administrator displays the digital attendance QR code from the SSG portal."),
    ("Scan and submit", "Scan the QR code with your mobile phone camera and submit your attendance."),
    ("75% minimum", "A minimum of 75% attendance is required to be eligible for assessment and for funding."),
], kicker="ADMIN", cols=2, accent=VIOLET)

big_statement("Let's know each other.",
              "Your name · your role · one workplace problem that keeps coming back no matter how many times you fix it.",
              "ICE BREAKER", color=TEAL)

# --- two trainer profiles (house rule) ---
trainer_slide("GENERAL TRAINER TEMPLATE", "Trainer Name",
              "WSQ Accredited Adult Educator  ·  Tertiary Infotech Academy",
              [("QUALIFICATIONS", ""), ("INDUSTRY EXPERIENCE", ""),
               ("SPECIALISATION", ""), ("CONTACT", "")],
              "TN", accent=GREY)

trainer_slide("YOUR TRAINER TODAY", "Dr. Alfred Ang",
              "Principal Trainer & Courseware Developer  ·  Tertiary Infotech Academy",
              [("QUALIFICATIONS", "PhD (NUS) · MEng (NTU) · MBA · ACTA · DACE"),
               ("INDUSTRY EXPERIENCE", "25+ years in engineering, data science, AI and process improvement"),
               ("SPECIALISATION", "Generative AI, problem solving, Six Sigma / SPC, design thinking"),
               ("CONTACT", C.EMAIL + "  ·  " + C.TEL)],
              "AA", accent=BLUE)

tile_grid("Ground Rules", [
    ("Phones on silent", "Set your mobile phone to silent mode. Step out quietly for calls."),
    ("Participate actively", "No question is stupid. The best problem solvers ask the most obvious questions."),
    ("Respect every view", "Disagree with the idea, never the person. Diversity of view is how blind spots get found."),
    ("Breaks", "Exit and re-enter quietly during the session for toilet or phone breaks."),
], kicker="HOUSEKEEPING", cols=2, accent=AMBER)

# --- download course material (visual, not a bare link) ---
s = head(slide(), "Download Your Course Material", "BEFORE WE START", kcolor=BLUE)
rect(s, Inches(0.85), Inches(1.95), Inches(11.63), Inches(0.72), LIGHT)
rect(s, Inches(0.85), Inches(1.95), Inches(0.11), Inches(0.72), BLUE)
txt(s, Inches(1.15), Inches(1.95), Inches(11.1), Inches(0.72),
    [[("All slides, the Learner Guide and the activity briefs are on the LMS portal.", 14, INK, False)]],
    anchor=MSO_ANCHOR.MIDDLE)
# browser mock
rect(s, Inches(0.85), Inches(2.95), Inches(6.6), Inches(3.5), WHITE, line=LINE)
rect(s, Inches(0.85), Inches(2.95), Inches(6.6), Inches(0.52), RGBColor(0xF1, 0xF5, 0xF9))
for k, c in enumerate([RGBColor(0xEF, 0x44, 0x44), RGBColor(0xF5, 0x9E, 0x0B), RGBColor(0x22, 0xC5, 0x5E)]):
    oval(s, int(Inches(1.05) + Inches(0.22) * k), Inches(3.12), Inches(0.15), Inches(0.15), c)
rect(s, Inches(1.85), Inches(3.06), Inches(5.4), Inches(0.32), WHITE, line=LINE)
txt(s, Inches(1.98), Inches(3.06), Inches(5.2), Inches(0.32),
    [[("lms-tms.tertiaryinfotech.com", 10.5, BLUE, True)]], anchor=MSO_ANCHOR.MIDDLE)
rect(s, Inches(1.1), Inches(3.72), Inches(6.1), Inches(0.55), RGBColor(0xEF, 0xF6, 0xFF))
txt(s, Inches(1.3), Inches(3.72), Inches(5.8), Inches(0.55),
    [[("📁  " + C.SHORT_TITLE, 11.5, INK, True)]], anchor=MSO_ANCHOR.MIDDLE)
for k, (nm, col) in enumerate([("Trainer Slides (PPT)", BLUE), ("Learner Slides (PDF)", TEAL),
                                ("Learner Guide (PDF)", VIOLET), ("Activities Folder", AMBER)]):
    yy = int(Inches(4.42) + Inches(0.47) * k)
    rect(s, Inches(1.3), yy, Inches(5.7), Inches(0.38), LIGHT)
    rect(s, Inches(1.3), yy, Inches(0.07), Inches(0.38), col)
    txt(s, Inches(1.52), yy, Inches(5.4), Inches(0.38), [[(nm, 10.5, INK, False)]],
        anchor=MSO_ANCHOR.MIDDLE)
steps = [("Log in to " + C.LMS, BLUE), ("Open My Courses and select this course", TEAL),
         ("Click the Courseware tab", VIOLET), ("Download the slides, Learner Guide and activities", AMBER)]
for k, (t_, col) in enumerate(steps):
    yy = int(Inches(3.0) + Inches(0.86) * k)
    rect(s, Inches(7.75), yy, Inches(4.73), Inches(0.72), LIGHT)
    rect(s, Inches(7.75), yy, Inches(0.09), Inches(0.72), col)
    bd = Inches(0.42)
    oval(s, Inches(7.95), int(yy + Inches(0.15)), bd, bd, col)
    txt(s, Inches(7.95), int(yy + Inches(0.15)), bd, bd, [[(str(k + 1), 13, WHITE, True)]],
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(8.52), yy, Inches(3.8), Inches(0.72), [[(t_, 11.5, INK, False)]],
        anchor=MSO_ANCHOR.MIDDLE)
footer(s)

# --- skills framework ---
tile_grid("Skills Framework Alignment", [
    ("TSC Title", C.TSC_TITLE),
    ("TSC Code", C.TSC_CODE),
    ("Proficiency Level", "Level 4 — analyse causes, evaluate options and decide"),
    ("Course Code", C.COURSE_CODE),
], kicker="WSQ · SKILLS FRAMEWORK", cols=2, accent=BLUE)

content("TSC Abilities Covered", C.TSC_ABILITIES, kicker="SKILLS FRAMEWORK", size=14)
content("TSC Knowledge Covered", C.TSC_KNOWLEDGE, kicker="SKILLS FRAMEWORK", size=14)

tile_grid("Prerequisites", [
    ("Level", "Beginner — no prior problem-solving or AI training required."),
    ("Education", "Minimum 3 GCE 'O' Level passes including English, or WPL Level 5."),
    ("Experience", "At least 1 year of working experience."),
    ("Equipment", "A laptop with a browser. Spare units available on request."),
], kicker="BEFORE YOU START", cols=2, accent=TEAL)

content("Learning Outcomes", C.LEARNING_OUTCOMES, kicker="BY THE END OF THIS COURSE", size=17)

for t in C.TOPICS:
    tile_grid("Topic %d: %s" % (t["num"], t["title"]),
              [(c.split(" — ")[0] if " — " in c else _ellipsis(c, 58), c) if False else c
               for c in t["concepts"]],
              kicker="COURSE OUTLINE  ·  " + t["weighting"], cols=1, size=13, accent=PALETTE[(t["num"] - 1) % 4])

# --- lesson plan ---
for d in (1, 2):
    acts = [a for a in ACTIVITIES if (a["topic"] == 1 if d == 1 else a["topic"] in (2, 3))]
    rows = []
    if d == 1:
        rows = [["9.30am", "Digital Attendance (AM) · Introductions · Learning Outcomes"],
                ["10.00am", "Topic 1: Problem framing and measurable problem statements"],
                ["11.00am", "Activity 1 — Problem Statement (ShopFront SG)"],
                ["12.30pm", "Lunch Break (1 hour)"],
                ["1.30pm", "Digital Attendance (PM) · Root cause analysis toolkit"],
                ["2.00pm", "Activity 2 — 5 Whys (Meridian Health)"],
                ["3.00pm", "Activity 3 — Fishbone (Horizon Bank)"],
                ["4.15pm", "Activity 4 — Pareto (Nexa Logistics)"],
                ["5.15pm", "Activity 5 — System Loops (Horizon Bank revisited)"],
                ["6.30pm", "End of Day 1"]]
    else:
        rows = [["9.30am", "Digital Attendance (AM) · Recap of Day 1"],
                ["10.00am", "Topic 2: Divergent ideation and GenAI as a divergence engine"],
                ["10.45am", "Activity 6 — Divergent Ideation + SCAMPER (Meridian Health)"],
                ["11.45am", "Activity 7 — Impact-Ease and weighted decision matrix"],
                ["12.30pm", "Lunch Break (1 hour)"],
                ["1.30pm", "Digital Attendance (PM) · Activity 8 — Corrective Action Plan"],
                ["2.30pm", "Topic 3: Implementation, change management and evaluation"],
                ["3.00pm", "Activity 9 — Implementation & stakeholder resistance (ShopFront SG)"],
                ["4.00pm", "Activity 10 — Measuring effectiveness at 90 days"],
                ["4.45pm", "Revision · Course feedback · TRAQOM survey"],
                ["5.15pm", "Digital Attendance (Assessment) · Final Assessment (WA + Case Study)"],
                ["6.30pm", "End of Course"]]
    compare_table("Lesson Plan — Day %d" % d, ["Time", "Session"], rows,
                  kicker="SCHEDULE  ·  8 INSTRUCTIONAL HOURS", accent=PALETTE[(d - 1) % 4],
                  note=C.DAY_THEMES[d])

# --- briefing BEFORE assessment (house rule) ---
tile_grid("Briefing for Assessment", [
    ("Clear your table", "Place phones and all other materials under the table or on the floor."),
    ("No photos or recording", "Assessment scripts must not be photographed, copied or recorded."),
    ("No discussion", "The assessment is individual work. No discussion once the paper is handed out."),
    ("Use black or blue pen", "For hard-copy scripts. No liquid paper or correction tape."),
    ("Time is called", "Scripts are collected when time is up. Late submissions are not accepted."),
    ("Open book means", "Slides, Learner Guide and approved materials only — no internet, no AI tools."),
], kicker="READ BEFORE THE ASSESSMENT", cols=2, accent=AMBER)

admin_assessment_block(tag="ASSESSMENT")

tile_grid("Criteria for Course Fee Funding", [
    ("Attendance", "Minimum 75% attendance based on the SSG Digital Attendance record."),
    ("Assessment", "Complete both instruments and be assessed 'Competent'."),
    ("Certificate", "Certificate of Achievement from Tertiary Infotech Academy Pte Ltd."),
    ("SSG Statement", "OpenCert / Statement of Achievement issued by SkillsFuture Singapore."),
], kicker="FUNDING", cols=2, accent=TEAL)

# ============================================================ TOPIC 1
T = C.TOPICS[0]
section("TOPIC 1", T["title"], "01", T["subtitle"])

big_statement("A problem well stated is a problem half solved.",
              "Charles Kettering. Most organisations skip straight to solutions — and pay for it twice.",
              "WHY FRAMING COMES FIRST", color=BLUE)

tile_grid("What Problem Solving Actually Is", [
    ("Issue identification", "Is the problem familiar or novel, simple or complex? Different answers demand different tools."),
    ("Information gathering", "Collect the facts. Find out how similar problems were solved before."),
    ("Analysis", "Break the problem into parts and establish cause and effect."),
    ("Action generation", "Develop several possible solutions across short and long horizons."),
    ("Implementation", "Select and execute the most promising approach — and stay flexible."),
    ("Evaluation", "Assess whether it worked, and extract the lesson for next time."),
], kicker="SKILLS FOR SUCCESS  ·  6 SUB-SKILLS", cols=2, size=13, accent=BLUE)

process_map("The IDEAL Problem-Solving Cycle",
            [("Identify", "the real problem"), ("Define", "the context"),
             ("Explore", "possible strategies"), ("Act", "on the best option"),
             ("Look back", "and learn")],
            kicker="BRANSFORD & STEIN  ·  MIT CCMIT", color=BLUE,
            synthesis=("THE DISCIPLINE",
                       "Most teams start at 'Act'. The cost of skipping Identify and Define is paid later, "
                       "with interest — you fix the wrong thing, then fix it again."))

compare_table("Symptom vs Problem vs Root Cause",
              ["", "Symptom", "Problem", "Root Cause"],
              [["What it is", "What people notice", "The measurable deficiency", "The system condition producing it"],
               ["Example", "'Customers are unhappy'", "Checkout completion fell 68%→51%", "No capacity planning from analytics"],
               ["Fixing it", "Feels responsive", "Improves the number", "Stops recurrence"],
               ["If you stop here", "Problem returns next quarter", "Returns in another form", "It is actually solved"]],
              kicker="THE DISTINCTION THAT SAVES BUDGETS", accent=BLUE,
              note="Treating a symptom always feels faster. It is the most expensive habit in problem solving.")

compare_table("Well-Defined vs Ill-Defined Problems",
              ["", "Well-defined", "Ill-defined"],
              [["Goal", "Clear and specific", "Vague or contested"],
               ["Path", "Known method exists", "No standard method"],
               ["Example", "Reduce load time to under 2s", "Improve the customer experience"],
               ["Right approach", "Apply the known technique", "Frame it first, then decompose"],
               ["GenAI's role", "Execute and check", "Explore, reframe, generate options"]],
              kicker="DIFFERENT PROBLEMS, DIFFERENT TOOLS", accent=TEAL,
              note="Most workplace problems arrive ill-defined. Framing IS the work.")

tile_grid("Six Elements of a Workplace Problem Statement", [
    ("Context", "Who, where, and which process is affected."),
    ("Metric", "The single primary measure you will move."),
    ("Baseline", "Where that metric is today — with the number."),
    ("Target", "Where it must be — with the number."),
    ("Timeframe", "By when. Without this, nothing is ever late."),
    ("Constraints", "Budget, headcount, compliance, brand — what you may not change."),
], kicker="THE TEMPLATE YOU WILL USE ALL COURSE", cols=3, size=13, accent=VIOLET)

two_col("Good or Bad Problem Definition?",
        ["\"Our customers are not happy with our services.\"",
         "No metric. No baseline. No target. No timeframe.",
         "Every department will interpret it differently.",
         "Unmeasurable — you can never prove it was solved."],
        ["\"Checkout completion on our app fell from 68% to 51% over 12 months against a 70% benchmark. "
         "We aim to restore it to 68% within 90 days without added headcount.\"",
         "Metric, baseline, target, timeframe and constraint all present.",
         "Actionable by a specific team.",
         "Evaluable at day 90 against a real number."],
        kicker="COMPARE", lhead="✗  BAD", rhead="✓  GOOD")

tile_grid("Barriers That Quietly Wreck Problem Solving", [
    ("Functional fixedness", "Seeing a thing only for its usual purpose — the reason obvious re-uses stay invisible."),
    ("Mental set", "Re-using the solution that worked last time, on a problem that has changed."),
    ("Confirmation bias", "Collecting evidence that supports the cause you already suspect."),
    ("Unnecessary constraints", "Self-imposed limits nobody actually stated. Most 'fixed' constraints are habits."),
    ("Irrelevant information", "Rich data that distracts from the few numbers that matter."),
    ("Consensus fatigue", "Accepting a weak option just to end the meeting."),
], kicker="COGNITIVE TRAPS  ·  KNOW THEM TO BEAT THEM", cols=2, size=13, accent=AMBER)

# --- GenAI in problem solving ---
big_statement("GenAI does not solve your problem.",
              "It expands what you consider, and accelerates how fast you get there. The judgement stays yours.",
              "SETTING EXPECTATIONS", color=VIOLET)

compare_table("What GenAI Is Good At — and Not",
              ["Dimension", "GenAI is strong", "GenAI is weak"],
              [["Breadth of options", "Generates 20 ideas in seconds, free of politics", "Cannot tell which are real"],
               ["Framing help", "Restates vague problems into structured form", "Invents specifics not in your evidence"],
               ["Analogy", "Borrows patterns across every industry", "May transfer an inapplicable pattern"],
               ["Arithmetic", "Improving, but still errs", "Verify every number it produces"],
               ["Context", "Applies general best practice", "Does not know your people, history or politics"],
               ["Accountability", "Tireless, unbiased by hierarchy", "Cannot be held responsible for the decision"]],
              kicker="LSE BUSINESS REVIEW  ·  AI LITERACY", accent=VIOLET,
              note="Use it as a divergence engine and a challenger — never as an oracle.")

process_map("How GenAI Fits the Problem-Solving Cycle",
            [("Frame", "Sharpen the statement"), ("Diagnose", "Generate cause hypotheses"),
             ("Ideate", "Expand the option set"), ("Decide", "Score against your criteria"),
             ("Evaluate", "Structure the evidence")],
            kicker="WHERE IT ADDS VALUE", color=VIOLET,
            synthesis=("THE HUMAN'S JOB",
                       "Supply the evidence, challenge the assumptions, own the decision. "
                       "The AI proposes; you dispose."))

tile_grid("Prompting Habits That Actually Work", [
    ("Give it a role", "'Act as a root cause analysis expert' sets the reasoning frame."),
    ("Supply the evidence", "Paste your real numbers. Without them the AI invents plausible ones."),
    ("Demand structure", "Name the fields you want back — Context, Metric, Baseline, Target."),
    ("Ask it to flag assumptions", "'Mark anything you assumed that my evidence did not support.'"),
    ("Make it challenge you", "'Ask me for evidence rather than accepting my answer.'"),
    ("Iterate, don't accept", "The first output is a draft. The third is usually useful."),
], kicker="PROMPT ENGINEERING FOR PROBLEM SOLVING", cols=2, size=13, accent=TEAL)

prompt_slide("The Problem Statement Prompt",
             "You are a business analyst for an e-commerce company.\n\n"
             "Refine this vague problem into a clear, measurable problem statement:\n"
             "<<State your problem here>>\n\n"
             "Include, each clearly labelled:\n"
             "- Context (who, where, which process)\n"
             "- Metric (the single primary measure)\n"
             "- Baseline (where it is now, with the number)\n"
             "- Target (where it must be, with the number)\n"
             "- Timeframe (by when)\n"
             "- Constraints (budget, headcount, compliance)\n\n"
             "Then list every assumption you had to make, and state what\n"
             "evidence would let me remove that assumption.\n\n"
             "Do not propose solutions yet.",
             kicker="TOPIC 1  ·  PROMPT 1", accent=VIOLET,
             note="The AI will supply specifics your evidence never contained. Mark each one as an assumption.")

# ---- Activity 1
A = ACTIVITIES[0]
activity_brief("ACTIVITY 1", A["title"], A["case_title"],
               "Rewrite an executive's vague complaint into a measurable problem statement your team can defend.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 1  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 1  ·  CASE STUDY")
evidence_table("The Evidence", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 1  ·  DATA")
prompt_slide("Activity 1 — The Prompt", A["prompt"], kicker="ACTIVITY 1  ·  RUN THIS", accent=VIOLET)
questions_slide("Activity 1 — Discussion Questions", A["questions"], kicker="ACTIVITY 1  ·  BREAKOUT")
debrief_slide("Activity 1 — Debrief", [
    ("The deficiency", "In-store flat while online fell 32% localises the problem to the digital funnel — "
                       "which invalidates the S$180k discount campaign before a dollar more is spent."),
    ("Symptom vs problem", "CSAT is a lagging perception measure. Checkout completion is the operational "
                           "deficiency you can act on."),
    ("The AI's assumptions", "Every team finds the AI inventing peak-hour windows, gateway names or segments "
                             "the evidence never supplied. Mark them. This is the core AI-literacy habit."),
    ("What is still unknown", "WHY load time rose is root cause — that is Activity 2. Resist 'we need more servers'."),
], kicker="ACTIVITY 1  ·  WHAT WE LEARNED")

# --- root cause toolkit ---
big_statement("Four tools. Four different jobs.",
              "Depth · Breadth · Priority · Dynamics. Mature problem solvers use them together, not instead of each other.",
              "THE ROOT CAUSE TOOLKIT", color=BLUE)

compare_table("Choosing Your Root Cause Tool",
              ["Tool", "What it gives you", "Use it when", "Limitation"],
              [["5 Whys", "Depth on one causal chain", "The problem is focused", "Only follows one branch"],
               ["Fishbone", "Breadth across all dimensions", "Causes are many and unclear", "Shallow on each"],
               ["Pareto", "Priority by contribution", "You have counted data", "Ranks frequency, not severity"],
               ["System Loops", "Feedback dynamics over time", "Fixes keep rebounding", "Needs time-series insight"]],
              kicker="K2  ·  ANALYTICAL TOOLS", accent=BLUE,
              note="Pareto tells you WHERE to look. 5 Whys tells you WHY. They chain together.")

# ---- Activity 2 (5 Whys)
A = ACTIVITIES[1]
edtool_slide("Ed-Tool: 5 Whys", "5 Whys Analysis Tool", A["edtool"]["url"],
             "Drives a symptom down to a systemic root cause by asking 'why' five times, "
             "recording each level so the chain stays visible and auditable.",
             "Enter the problem statement, then add one why and answer per level. "
             "Stay on ONE causal branch — depth is the point.",
             kicker="TOPIC 1  ·  TOOL", accent=TEAL)

whys_ladder("5 Whys — Worked Example",
            [("Why do morning appointments overrun?", "Blood draws take longer than the slot allows."),
             ("Why do draws take longer?", "40% of morning staff are relief at 14 min vs 6 min; 18% need a repeat."),
             ("Why so many relief staff?", "Only 3 of 5 permanent phlebotomists are rostered at 07:00."),
             ("Why under-rostered at 07:00?", "Turnover is 44%/yr; vacancies are backfilled by untrained agency staff."),
             ("Why is turnover 44%?", "The early shift is unattractive and there is no structured onboarding or career path.")],
            "A workforce retention and onboarding failure — surfacing as a capacity problem.",
            kicker="MERIDIAN HEALTH  ·  DEPTH ON ONE BRANCH", accent=BLUE)

big_statement("\"We're short-staffed\" was wrong in the way that matters.",
              "They are not short of headcount. They are short of TRAINED headcount at 07:00. That distinction is worth S$1.2m.",
              "WHY ROOT CAUSE PAYS", color=AMBER)

prompt_slide("The 5 Whys Prompt", A["prompt"], kicker="TOPIC 1  ·  PROMPT 2", accent=VIOLET,
             note="Instructing the AI to demand evidence at each level turns it into a facilitator, not an echo.")

activity_brief("ACTIVITY 2", A["title"], A["case_title"],
               "Drive a staffing complaint down five levels to the systemic cause — and test a S$1.2m proposal against it.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 1  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 2  ·  CASE STUDY")
evidence_table("The Evidence", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 2  ·  DATA")
questions_slide("Activity 2 — Discussion Questions", A["questions"], kicker="ACTIVITY 2  ·  BREAKOUT")
debrief_slide("Activity 2 — Debrief", [
    ("The chain", "Overrun → relief staff at 14 min → only 3 of 5 permanent rostered → 44% turnover → "
                  "unattractive early shift with no onboarding or career path."),
    ("The S$1.2m test", "A seventh centre staffed by the same untrained relief pool reproduces the same "
                        "overrun. You buy the problem twice."),
    ("Facilitation discipline", "One why at a time; every level must survive 'what evidence supports this?'. "
                                "The AI modelling that challenge is the K5 outcome."),
    ("The branch point", "At Why 2 a team could have followed the 12% fasting non-compliance instead. "
                         "That is a legitimate second cause — and exactly why we use Fishbone next."),
], kicker="ACTIVITY 2  ·  WHAT WE LEARNED")

# ---- Activity 3 (Fishbone)
A = ACTIVITIES[2]
tile_grid("The Fishbone (Ishikawa) Diagram", [
    ("Who invented it", "Dr Kaoru Ishikawa, Japanese quality control expert — to stop teams treating symptoms."),
    ("What it does", "Categorises every potential cause of one problem so nothing is missed."),
    ("The head", "The problem statement — measurable, with the number."),
    ("The bones", "People · Process · Technology · Material/Information · Environment · Measurement."),
    ("The twigs", "Specific candidate causes on each bone, phrased as causes, not complaints."),
    ("The payoff", "Shows you which dimension your intervention is actually targeting."),
], kicker="BREADTH ACROSS ALL DIMENSIONS", cols=2, size=13, accent=BLUE)

fishbone("Fishbone — Horizon Bank Jurong East",
         "60 complaints/month (network avg 14); 58-min peak wait vs a 15-min standard",
         [("People", ["44% tellers under 6 months", "Two resignations this quarter", "Thin coaching"]),
          ("Process", ["Single queue, no triage", "Complex cases block counters 27 min", "Rostering misses peak"]),
          ("Technology", ["KYC needs triple data entry", "Screen response 2s → 8s", "Systems not integrated"]),
          ("Material", ["App checklist ≠ branch signage", "34% arrive without documents", "Forms confusing"]),
          ("Environment", ["18 seats for a 58-min wait", "Standing customers agitated", "No queue visibility"]),
          ("Measurement", ["KPI is transactions/hour only", "No experience measure", "No branch→HO feedback"])],
         kicker="SIX BONES  ·  EVIDENCE-LOADED", accent=BLUE)

big_statement("Head Office trained the People bone.",
              "It carries the fewest evidenced causes. That is precisely why complaints did not move — they intervened on the wrong bone.",
              "THE EXPENSIVE LESSON", color=AMBER)

edtool_slide("Ed-Tool: Fishbone", "Fishbone Diagram Tool", A["edtool"]["url"],
             "Builds an Ishikawa diagram across six cause categories, so a team can see "
             "at a glance which dimension carries the weight of evidence.",
             "Enter the problem as the head, then add causes bone by bone. "
             "Mark each [EVIDENCED] or [HYPOTHESIS].",
             kicker="TOPIC 1  ·  TOOL", accent=TEAL)

prompt_slide("The Fishbone Prompt", A["prompt"], kicker="TOPIC 1  ·  PROMPT 3", accent=VIOLET,
             note="Forcing [EVIDENCED] vs [HYPOTHESIS] labels stops the AI's confident guesses becoming your facts.")

activity_brief("ACTIVITY 3", A["title"], A["case_title"],
               "Map every contributing cause across six dimensions — and discover why the training refresher failed.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 1  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 3  ·  CASE STUDY")
evidence_table("The Evidence", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 3  ·  DATA")
questions_slide("Activity 3 — Discussion Questions", A["questions"], kicker="ACTIVITY 3  ·  BREAKOUT")
debrief_slide("Activity 3 — Debrief", [
    ("Where the evidence sits", "Process, Technology and Measurement carry the weight. People carries the "
                                "least — and People is exactly what Head Office trained."),
    ("Cross-bone causation", "The transactions/hour KPI drives tellers to rush complex cases back into the "
                             "queue, lengthening waits. Bones are not independent."),
    ("Fishbone vs 5 Whys", "One deep chain vs six shallow ones. Depth without breadth fixes one cause and "
                           "the problem persists; breadth without depth fixes symptoms everywhere."),
    ("GenAI's role", "Excellent at populating bones fast; poor at knowing which are real. Count how many "
                     "came back [HYPOTHESIS] — those are your verification list."),
], kicker="ACTIVITY 3  ·  WHAT WE LEARNED")

# ---- Activity 4 (Pareto)
A = ACTIVITIES[3]
tile_grid("Pareto Analysis — the 80/20 Rule", [
    ("The principle", "Roughly 80% of the effect comes from roughly 20% of the causes."),
    ("What it does", "Breaks a big problem into ranked pieces so effort lands where it counts."),
    ("The vital few", "The small set of categories carrying most of the volume."),
    ("The trivial many", "The long tail — real, but not where your first dollar goes."),
    ("Ranking dimension", "Count, cost, risk or customer harm. Choosing this IS the analysis."),
    ("The limitation", "It ranks frequency. Frequency is not severity."),
], kicker="PRIORITY  ·  WHERE TO LOOK FIRST", cols=2, size=13, accent=BLUE)

chart_slide("Pareto — Nexa Logistics Delivery Failures",
            ["Not at home", "Lobby access", "Address wrong", "Not loaded", "Refused",
             "Breakdown", "Weather", "Bad contact", "Damaged", "Restricted", "Other"],
            [("Failures", [742, 486, 231, 188, 121, 94, 61, 38, 24, 20, 15])],
            kicker="80/20 IN PRACTICE", accent=BLUE, kind="column",
            insight="Four of eleven reasons carry 82% of failures; the top two alone carry 61%. "
                    "'Address incorrect' — the one generating the angriest emails — is only 11.6%. "
                    "Loud is not the same as large.")

big_statement("A 60% cut on the top two still misses the SLA.",
              "1,228 × 0.6 = 737 removed, leaving 1,263 of 40,000 = 3.2%. The 2% SLA needs the top four. Always do the arithmetic.",
              "SHOW YOUR WORKING", color=AMBER)

edtool_slide("Ed-Tool: Pareto Chart", "Pareto Chart Tool", A["edtool"]["url"],
             "Sorts categories by count, computes the cumulative percentage line, and shows "
             "exactly where the 80% cut-off falls.",
             "Enter each failure reason and its count. Read the cumulative line to find your vital few.",
             kicker="TOPIC 1  ·  TOOL", accent=TEAL)

prompt_slide("The Pareto Prompt", A["prompt"], kicker="TOPIC 1  ·  PROMPT 4", accent=VIOLET,
             note="Always verify the AI's percentages against the tool. Arithmetic is where it still slips.")

activity_brief("ACTIVITY 4", A["title"], A["case_title"],
               "Rank eleven failure reasons, find the vital few, and decide where two funded initiatives go.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 1  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 4  ·  CASE STUDY")
evidence_table("The Evidence", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 4  ·  DATA")
questions_slide("Activity 4 — Discussion Questions", A["questions"], kicker="ACTIVITY 4  ·  BREAKOUT")
debrief_slide("Activity 4 — Debrief", [
    ("The vital few", "Four of eleven reasons = 82%. Top two = 61%. 'Address incorrect' is third at 11.6%."),
    ("Loud vs large", "The Director responds to escalation volume, which tracks client temperament, not "
                      "failure frequency. Pareto is how you have that conversation with evidence."),
    ("Reframe ownership", "'Not at home' is a customer problem only if you never offered a delivery window. "
                          "Restating moves 61% of the problem into Nexa's control."),
    ("What Pareto cannot do", "It ranks frequency, never severity — and it tells you WHERE, never WHY. "
                              "The 742 failures still need a 5 Whys."),
], kicker="ACTIVITY 4  ·  WHAT WE LEARNED")

# ---- Activity 5 (System loops)
A = ACTIVITIES[4]
tile_grid("Systems Thinking — Why Fixes Rebound", [
    ("A system, not a queue", "Organisations are webs of feedback loops, not linear cause-and-effect chains."),
    ("Reinforcing loop (R)", "Compounds over time — makes things better and better, or worse and worse."),
    ("Balancing loop (B)", "Pushes toward a target and stabilises — this is what most 'fixes' pull."),
    ("Delay", "R-loops act slowly. That delay is why a bad decision can look right in month one."),
    ("Dormant loops", "A balancing loop that exists but is not running is as dangerous as an active R-loop."),
    ("Leverage", "Breaking one link in an R-loop beats adding effort to a B-loop forever."),
], kicker="DYNAMICS  ·  WHY THE PROBLEM CAME BACK", cols=2, size=13, accent=VIOLET)

causal_loop("Horizon Bank — The Four Loops",
            [("B1", "Capacity control — what he intended", "B",
              ["Wait time ↑", "Management pressure ↑", "Counters staffed ↑", "Service capacity ↑", "Wait time ↓"],
              "Real — and it produced the month-1 win"),
             ("R1", "Redeployment backfire", "R",
              ["Counters staffed ↑", "Back-office staff ↓", "Backlog ↑", "Rework returns to counter ↑",
               "Handling time ↑ (9→13 min)", "Wait time ↑"],
              "Compounds — overwhelms B1 by month 4"),
             ("R2", "Burnout spiral", "R",
              ["Workload ↑", "Overtime ↑ (88→196h)", "Resignations ↑", "Inexperience ↑ (44%→58%)",
               "Errors ↑ (6%→14%)", "Rework ↑", "Workload ↑"],
              "Compounds — feeds R1"),
             ("B2", "Digital migration — DORMANT", "B",
              ["Wait time ↑", "Willingness to try digital ↑", "Digital adoption ↑",
               "Branch volume ↓", "Wait time ↓"],
              "Never engaged — adoption flat at ~20%")],
            kicker="TWO REINFORCING · TWO BALANCING", accent=VIOLET)

big_statement("A quick win measured too early is indistinguishable from a mistake.",
              "B1 acts in days. R1 and R2 act over months. The month-1 result validated a decision that was making things worse.",
              "THE DELAY TRAP", color=AMBER)

compare_table("Leverage vs Effort",
              ["", "Effort", "Leverage"],
              [["Example", "Add more counters", "Triage complex cases away from the counter"],
               ["Cost", "Must be sustained forever", "Changes the structure once"],
               ["Effect on R1", "Feeds it", "Breaks a link in it"],
               ["Sustainability", "Decays the moment you stop", "Holds without continuous push"],
               ["Test", "'Are we pushing harder?'", "'Have we changed what produces the behaviour?'"]],
              kicker="WHERE TO INTERVENE", accent=TEAL,
              note="If your answer is 'hire more people', you have described effort, not leverage.")

edtool_slide("Ed-Tool: System Loop", "System Loop Tool", A["edtool"]["url"],
             "Maps variables and causal links into closed feedback loops, marking each "
             "reinforcing (R) or balancing (B) so loop dynamics become visible.",
             "Add variables as nodes, link them with (+)/(−), and close the loop. "
             "Count negative links: even = reinforcing, odd = balancing.",
             kicker="TOPIC 1  ·  TOOL", accent=TEAL)

prompt_slide("The Systems Thinking Prompt", A["prompt"], kicker="TOPIC 1  ·  PROMPT 5", accent=VIOLET,
             note="Ask explicitly for the DELAY and the dormant loop — the AI rarely volunteers either.")

activity_brief("ACTIVITY 5", A["title"], A["case_title"],
               "Map the loops that turned a successful fix into a worse outcome, and find the real leverage points.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 1  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 5  ·  CASE STUDY")
evidence_table("The Evidence", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 5  ·  DATA")
questions_slide("Activity 5 — Discussion Questions", A["questions"], kicker="ACTIVITY 5  ·  BREAKOUT")
debrief_slide("Activity 5 — Debrief", [
    ("What actually happened", "He pulled B1 and unknowingly powered R1 and R2. R-loops compound, so they "
                               "eventually overwhelm a one-off capacity increase."),
    ("The delay is the trap", "B1 acts in days; R1 and R2 act over months. That is why month 1 lied."),
    ("The dormant loop", "B2 (digital migration) was available all along and nobody activated it. Ask "
                         "'which balancing loop is NOT running?'"),
    ("Topic 1 complete", "5 Whys gave depth, Fishbone breadth, Pareto priority, Loops dynamics. "
                         "You now have the full diagnostic set before touching solutions."),
], kicker="ACTIVITY 5  ·  WHAT WE LEARNED")

brk("Lunch Break", "1 hour")
brk("End of Day 1", "See you at 9.30am tomorrow", color=TEAL)

big_statement("Day 1 in one line.",
              "You cannot solve what you have not defined, and you cannot fix what you have not diagnosed.",
              "RECAP", color=BLUE)

# ============================================================ TOPIC 2
T = C.TOPICS[1]
section("TOPIC 2", T["title"], "02", T["subtitle"])

big_statement("Generate and judge at the same time, and you will kill your best ideas.",
              "Divergence and convergence are different cognitive modes. Run them in sequence, never in parallel.",
              "THE CENTRAL DISCIPLINE OF TOPIC 2", color=BLUE)

process_map("Divergence Then Convergence",
            [("Diverge", "Generate widely"), ("Cluster", "Group by theme"),
             ("Screen", "Impact vs Ease"), ("Score", "Weighted matrix"),
             ("Commit", "Portfolio of four")],
            kicker="THE SOLUTION FUNNEL", color=BLUE,
            synthesis=("WHY THE ORDER MATTERS",
                       "Teams that evaluate while generating stop at 6-8 conventional ideas. "
                       "The uncomfortable ideas are where fixedness breaks."))

tile_grid("Techniques for Generating Solutions", [
    ("Brainstorming", "All ideas welcome, judgement suspended. Quantity first, quality later."),
    ("SCAMPER", "Substitute · Combine · Adapt · Modify · Put to another use · Eliminate · Reverse."),
    ("Generic Parts Technique", "Strip a problem to abstract functions — solutions appear in unexpected places."),
    ("Analogy / cross-industry", "Borrow a working pattern from a completely different sector."),
    ("Reverse brainstorming", "Ask how to make it WORSE, then invert every answer."),
    ("Nominal group technique", "Silent individual generation first, then group discussion — beats groupthink."),
    ("Six Thinking Hats", "Examine the problem from facts, feelings, risks, benefits, creativity and process."),
    ("Mind mapping", "Radiate ideas from the central problem to surface relationships."),
], kicker="K4  ·  DIVERGENT TOOLKIT", cols=2, size=12.5, accent=TEAL)

tile_grid("SCAMPER — Seven Moves on a Fixed Assumption", [
    ("Substitute", "What can be swapped out? Different person, material, place or rule."),
    ("Combine", "What can be merged? Two steps, two roles, two services."),
    ("Adapt", "What works elsewhere that we can borrow?"),
    ("Modify", "What if we magnify, shrink, or change the shape of it?"),
    ("Put to another use", "What else could this resource or step do?"),
    ("Eliminate", "What if we simply removed it? Often the biggest unlock."),
    ("Reverse", "What if we ran it backwards, or swapped who does what?"),
], kicker="BREAKING COGNITIVE FIXEDNESS", cols=2, size=13, accent=VIOLET)

big_statement("The 07:00 window is fixed only because draws happen at the centre.",
              "Reverse and Eliminate dissolve the constraint instead of working inside it. Most 'fixed' constraints are habits.",
              "SCAMPER IN ACTION", color=AMBER)

compare_table("Regulation vs Habit — Telling Hard Constraints Apart",
              ["", "Hard constraint", "Habit"],
              [["Meridian example", "MOH phlebotomy competency standard", "07:00-09:30 draws at the centre"],
               ["Source", "Law, regulation, contract, physics", "Precedent, convenience, 'we've always'"],
               ["Test", "Who enforces it, and what is the penalty?", "Who would actually object, and why?"],
               ["If you break it", "Legal or clinical consequence", "Someone has to change a routine"],
               ["What to do", "Design within it", "Challenge it explicitly"]],
              kicker="THE DISTINCTION THAT UNLOCKS OPTIONS", accent=AMBER,
              note="Teams routinely treat habits as regulations. Ask 'who enforces this?' every single time.")

prompt_slide("The Divergent Ideation Prompt",
             "Act as an innovation consultant running a divergent ideation session.\n"
             "Do NOT evaluate or filter yet.\n\n"
             "Root cause to solve:\n"
             "<<State your diagnosed root cause>>\n\n"
             "Constraints:\n"
             "<<Budget, regulatory, contractual>>\n\n"
             "Generate 20 distinct solutions grouped under:\n"
             "- People & Retention      - Training & Onboarding\n"
             "- Process & Scheduling    - Technology & Automation\n"
             "- Customer/Client Experience\n\n"
             "Rules:\n"
             "- Include at least 4 ideas normally dismissed as unrealistic\n"
             "- Include at least 2 borrowed from a DIFFERENT industry (say which)\n"
             "- One line each, phrased as an action\n"
             "- Do NOT rank, cost or evaluate\n\n"
             "Then apply SCAMPER to this assumption:\n"
             "<<State the assumption everyone treats as fixed>>\n"
             "Give one idea per SCAMPER letter.",
             kicker="TOPIC 2  ·  PROMPT 6", accent=VIOLET,
             note="'Do not evaluate yet' is the most important line. Without it the AI self-censors to safe ideas.")

# ---- Activity 6
A = ACTIVITIES[5]
activity_brief("ACTIVITY 6", A["title"], A["case_title"],
               "Generate 20+ solutions to the diagnosed root cause, then break a fixed assumption with SCAMPER.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 2  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 6  ·  CASE STUDY")
evidence_table("The Constraints", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 6  ·  CONTEXT")
prompt_slide("Activity 6 — The Prompt", A["prompt"], kicker="ACTIVITY 6  ·  RUN THIS", accent=VIOLET)
questions_slide("Activity 6 — Discussion Questions", A["questions"], kicker="ACTIVITY 6  ·  BREAKOUT")
debrief_slide("Activity 6 — Debrief", [
    ("Count the gap", "Teams that evaluate while generating stop at 6-8 ideas. The gap between your manual "
                      "list and the AI list IS the lesson."),
    ("Why GenAI diverges better", "It has no career risk. It will propose 'pay the early shift more' in "
                                  "front of a Finance Director without hesitation."),
    ("The SCAMPER unlock", "Reverse and Eliminate dissolve the 07:00 window entirely — bring the draw to "
                           "the client. The MOH standard, by contrast, is a genuine hard constraint."),
    ("Hold the line", "Do not rank yet. Holding divergence separate from convergence is itself the skill."),
], kicker="ACTIVITY 6  ·  WHAT WE LEARNED")

# ---- Activity 7
A = ACTIVITIES[6]
matrix_2x2("Impact vs Ease — the Fast Screen", "Ease of implementation", "Impact",
           {"tl": ("Big Bets", VIOLET, ["High impact, hard to do", "Structured onboarding programme",
                                        "Convert relief staff to permanent", "Do these — but plan properly"]),
            "tr": ("Quick Wins", TEAL, ["High impact, easy to do", "Re-roster all 5 at 07:00",
                                        "Early-shift differential pay", "Do these FIRST"]),
            "bl": ("Thankless Tasks", GREY, ["Low impact, hard to do", "New seventh centre",
                                             "Full HR system replacement", "Do not start these"]),
            "br": ("Fill-Ins", AMBER, ["Low impact, easy to do", "Updated signage and leaflets",
                                       "Minor booking-form tweaks", "Do if you have spare capacity"])},
           kicker="SCREEN 20 IDEAS IN 10 MINUTES", accent=BLUE,
           note="Quick Wins build momentum and credibility. Big Bets deliver the durable fix. You need both.")

compare_table("Weighted Decision Matrix — the Rigorous Instrument",
              ["Criterion", "Weight", "What a 5 looks like"],
              [["Impact on root cause", "35%", "Directly fixes the diagnosed root cause"],
               ["Speed to measurable effect", "20%", "Effect visible within 8 weeks"],
               ["Cost within envelope", "20%", "Under S$25k"],
               ["Clinical / regulatory risk", "15%", "No MOH implication at all"],
               ["Staff and client acceptance", "10%", "Actively welcomed by both"]],
              kicker="K6  ·  DECISION MODELS", accent=BLUE,
              note="Agree the WEIGHTS before any scoring. Most 'score arguments' are really weight disagreements.")

big_statement("If doubling one weight flips your winner, your recommendation is fragile.",
              "Run the sensitivity test before you present, not after you are challenged. Boards trust robust answers.",
              "SENSITIVITY TESTING", color=AMBER)

compare_table("Two Tools, Two Jobs",
              ["", "Impact-Ease matrix", "Weighted decision matrix"],
              [["Speed", "Minutes", "30-45 minutes"],
               ["Use on", "All 20 ideas", "The surviving 6-8"],
               ["Output", "Four quadrants", "A ranked, scored list"],
               ["Defensibility", "Directional", "Auditable — you can show a board"],
               ["Risk if used alone", "Cannot justify the call", "Wastes the session on weak ideas"]],
              kicker="USE THEM IN SEQUENCE", accent=TEAL,
              note="Screen with the light tool; decide with the heavy one.")

prompt_slide("The Convergence Prompt", A["prompt"], kicker="TOPIC 2  ·  PROMPT 7", accent=VIOLET,
             note="The AI invents cost figures with total confidence. Its ranking is only as good as your criteria.")

activity_brief("ACTIVITY 7", A["title"], A["case_title"],
               "Screen twenty ideas down to four fundable solutions — and defend the ranking with evidence.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 2  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 7  ·  CASE STUDY")
evidence_table("The Decision Criteria", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 7  ·  CRITERIA")
questions_slide("Activity 7 — Discussion Questions", A["questions"], kicker="ACTIVITY 7  ·  BREAKOUT")
debrief_slide("Activity 7 — Debrief", [
    ("The weights are the decision", "Surfacing weights BEFORE scoring converts a political argument into "
                                     "an explicit, recorded choice."),
    ("Portfolio, not leaderboard", "The top four scores may all attack the same cause, or be redundant. "
                                   "Balance quick stabilisation against durable repair."),
    ("Sensitivity", "If the winner holds under several weightings, you have a robust recommendation. "
                    "If it flips, say so."),
    ("The AI's limit", "It is a fast, tireless scorer with no politics — and no accountability. "
                       "The Clinical Director will ask YOU why, not the model."),
], kicker="ACTIVITY 7  ·  WHAT WE LEARNED")

# ---- Activity 8
A = ACTIVITIES[7]
tile_grid("The Corrective Action Plan — Eight Components", [
    ("Root cause addressed", "Ties the action to the diagnosis. Without it, solutions drift to symptoms."),
    ("Corrective action", "The specific thing being done — one sentence, unambiguous."),
    ("Owner (named role)", "Single point of accountability. A department cannot be phoned."),
    ("Timeline / milestone", "Start, milestone, completion — in weeks, not quarters."),
    ("Resources required", "Budget, people, tools — committed, not hoped for."),
    ("Success measure", "Metric + baseline + target. This is what makes evaluation possible."),
    ("Risk and mitigation", "What breaks it, and the action (with an owner) that prevents that."),
    ("Review checkpoint", "A date AND the decision to be made: continue, extend or stop."),
], kicker="K9  ·  WHY EACH COMPONENT EXISTS", cols=2, size=12.5, accent=BLUE)

big_statement("'Operations' cannot be phoned, held to a date, or asked why it slipped.",
              "One named owner per action. No co-owners. This single discipline prevents the most common cause of project death.",
              "THE OWNER IS THE SPINE", color=AMBER)

compare_table("Measures That Work vs Measures That Don't",
              ["", "Unmeasurable", "Measurable with existing data"],
              [["Morale", "'Improved staff morale'", "Voluntary resignations per quarter"],
               ["Capability", "'Better trained staff'", "Mean relief-staff draw time: 14 → under 8 min"],
               ["Quality", "'Fewer mistakes'", "First-attempt success rate: 82% → 92%"],
               ["Coverage", "'Properly staffed mornings'", "07:00 roster fill rate by permanent staff"]],
              kicker="A7  ·  MAKING EVALUATION POSSIBLE", accent=TEAL,
              note="If the organisation cannot measure it today, either change the measure or add a task to start collecting it.")

prompt_slide("The Corrective Action Plan Prompt", A["prompt"], kicker="TOPIC 2  ·  PROMPT 8", accent=VIOLET,
             note="Asking the AI to flag dependencies and overloaded owners catches what a close-in team misses.")

activity_brief("ACTIVITY 8", A["title"], A["case_title"],
               "Convert four approved solutions into an auditable plan another team could execute without you.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 2  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 8  ·  CASE STUDY")
evidence_table("The Components", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 8  ·  TEMPLATE")
questions_slide("Activity 8 — Discussion Questions", A["questions"], kicker="ACTIVITY 8  ·  BREAKOUT")
debrief_slide("Activity 8 — Debrief", [
    ("The baseline pays off", "Teams that skipped the baseline in Activity 1 literally cannot write the "
                              "success measure now. The course has closed its own loop."),
    ("Sequencing", "Converting relief staff to permanent DEPENDS on the onboarding programme existing — "
                   "otherwise you lock in the defect."),
    ("Owner overload", "If one role owns three of four actions, the plan is a single point of failure "
                       "however good each row looks."),
    ("Checkpoints carry decisions", "'Review progress' is theatre. 'Decide to roll out, extend or stop' "
                                    "is governance."),
], kicker="ACTIVITY 8  ·  WHAT WE LEARNED")

brk("Lunch Break", "1 hour")

# ============================================================ TOPIC 3
T = C.TOPICS[2]
section("TOPIC 3", T["title"], "03", T["subtitle"])

big_statement("The CRM worked perfectly. That was not the problem.",
              "Solutions fail on adoption far more often than on design. Implementation is mostly about people.",
              "K8  ·  WHAT ACTUALLY DETERMINES SUCCESS", color=BLUE)

process_map("From Decision to Proven Result",
            [("Sequence", "What before what"), ("Assign", "Named owners"),
             ("Engage", "Stakeholders & resistance"), ("Execute", "With checkpoints"),
             ("Evaluate", "Against the baseline")],
            kicker="THE IMPLEMENTATION ARC", color=BLUE,
            synthesis=("THE CLOSING LOOP",
                       "Evaluation compares against the baseline captured in your problem statement. "
                       "Topic 3 only works because Topic 1 was done properly."))

tile_grid("Factors Affecting Implementation Effectiveness", [
    ("Sponsorship", "A senior owner who can re-prioritise competing work — not just endorse it."),
    ("Sequencing", "Dependencies respected. A recovery campaign before a speed fix burns the customer twice."),
    ("Capacity", "Teams already at capacity will not absorb new work by goodwill."),
    ("Stakeholder buy-in", "Resistance is a design input, not a surprise to be managed later."),
    ("Communication", "Regular, specific, and continuing past launch — not a single kick-off email."),
    ("Measurement", "Defined at day 0, with the window and the control agreed before you start."),
], kicker="K8  ·  WHAT MAKES OR BREAKS A ROLLOUT", cols=2, size=13, accent=TEAL)

tile_grid("Change Management Actions That Work", [
    ("Leadership alignment", "Communicate the business goal and tie measurable KPIs to outcomes."),
    ("Quick wins first", "Deliver an early visible improvement to build momentum and credibility."),
    ("Involve early", "Bring affected teams into solution design before rollout, not after."),
    ("Co-design with resisters", "An imposed standard is complied with on paper. A co-designed one sticks."),
    ("Incentives & accountability", "Link the change to performance metrics people are actually measured on."),
    ("Train and support", "SOPs, quick guides and a real helpdesk — adoption dies without support."),
], kicker="SECURING ADOPTION", cols=2, size=13, accent=VIOLET)

compare_table("Reading Stakeholder Resistance",
              ["Stakeholder type", "What they actually object to", "The move that works"],
              [["At-capacity team", "Workload, not the idea", "Real relief — re-prioritise or fund capacity"],
               ["Face at risk", "Being shown to have been wrong", "Reframe; give them ownership of a win"],
               ["External party", "Cost and scrutiny", "Co-design, then tie to commercial consequence"],
               ["Job-security fear", "A rational threat", "Commit only to what you can guarantee"],
               ["The indifferent", "Nothing — and that is the danger", "Give them a stake before you need them"]],
              kicker="RESISTANCE IS INFORMATION", accent=AMBER,
              note="The messenger matters as much as the message. Assign one to every conversation.")

big_statement("Indifference kills more rollouts than opposition.",
              "Nobody escalates an absence of enthusiasm — so it is never fixed until the launch fails.",
              "THE QUIET RISK", color=AMBER)

prompt_slide("The Implementation & Change Prompt", A["prompt"] if False else
             "Act as a change management and implementation planning advisor.\n\n"
             "Approved solutions:\n"
             "<<List your solutions>>\n\n"
             "PART A — Implementation plan. For each solution give ONLY:\n"
             "- Action (what will be done)\n"
             "- Method/tool (how)\n"
             "- Owner and timeline (who, by when)\n"
             "- Sequencing note (what must happen before it)\n\n"
             "PART B — Stakeholder strategy. For EACH stakeholder give:\n"
             "- Their specific objection in THEIR words, not yours\n"
             "- What they need to hear or receive to move\n"
             "- One concrete action to secure cooperation\n"
             "- Who should deliver that message, and why\n\n"
             "PART C — Name the ONE stakeholder most likely to sink this\n"
             "rollout and explain what makes them dangerous. Then give a\n"
             "90-day communication plan: what, to whom, how often, by whom.\n\n"
             "Be blunt about political realities. Do not assume goodwill.",
             kicker="TOPIC 3  ·  PROMPT 9", accent=VIOLET,
             note="The AI has no stake in your office politics — it will name the face-saving problem you would not write down.")

# ---- Activity 9
A = ACTIVITIES[8]
activity_brief("ACTIVITY 9", A["title"], A["case_title"],
               "Build the rollout plan AND the stakeholder strategy that makes it survive contact with people.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 3  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 9  ·  CASE STUDY")
evidence_table("The Stakeholders", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 9  ·  MAP")
questions_slide("Activity 9 — Discussion Questions", A["questions"], kicker="ACTIVITY 9  ·  BREAKOUT")
debrief_slide("Activity 9 — Debrief", [
    ("Sequencing is not optional", "Cart recovery must follow the speed fix. Driving traffic back to a "
                                   "4.8-second app burns the customer twice."),
    ("The face problem", "Marketing's objection is reputational, not logical. Reframe rather than "
                         "relitigate — and let the COO deliver it, peer to peer."),
    ("Co-design beats imposition", "An imposed supplier checklist is complied with on paper for two months. "
                                   "Watch what happens to it in Activity 10."),
    ("Resistance is data", "IT's objection revealed a capacity conflict the plan had not costed. "
                           "That improves the plan."),
], kicker="ACTIVITY 9  ·  WHAT WE LEARNED")

# ---- Activity 10
A = ACTIVITIES[9]
compare_table("Leading vs Lagging Indicators",
              ["", "Leading", "Lagging"],
              [["Responds in", "Days to weeks", "Months to quarters"],
               ["ShopFront example", "App load, checkout completion, adoption", "CSAT, repeat purchase, brand trust"],
               ["Tells you", "Whether the change is taking hold", "Whether the outcome actually improved"],
               ["Risk of using alone", "Early signal, may not persist", "Too late to steer"],
               ["Planning implication", "Steer with these", "Set realistic horizons for these"]],
              kicker="K7  ·  YOU NEED BOTH", accent=BLUE,
              note="Expecting CSAT to move in 90 days was a planning error, not an execution failure.")

chart_slide("ShopFront SG — 90 Days Against Baseline",
            ["App load (s)", "Checkout %", "Abandon %", "CSAT %", "Returns %"],
            [("Baseline", [4.8, 51, 74, 70, 12]),
             ("Target", [2.0, 68, 60, 85, 5]),
             ("Day 90 actual", [1.7, 63, 64, 72, 13])],
            kicker="DID IT WORK?", accent=BLUE, kind="column",
            insight="App load beat target. Checkout and abandonment improved but fell short. CSAT barely "
                    "moved — it is a lagging indicator. Returns got WORSE, which needs explaining before "
                    "anyone concludes the solution failed.")

tile_grid("Evaluating Honestly — the Four Questions", [
    ("Did the metric move?", "Against the BASELINE and the TARGET — both, with numbers."),
    ("Can you attribute it?", "Or is it confounded by season, market or another change? Say which."),
    ("Solution or implementation?", "A solution not adopted has not been tested. Those need opposite responses."),
    ("What would change your mind?", "Naming this is what makes your recommendation credible to a CFO."),
], kicker="A7  ·  THE EVALUATION DISCIPLINE", cols=2, size=13, accent=TEAL)

big_statement("The return rate got worse — and the solution did not fail.",
              "Only 4 of 12 suppliers adopted the checklist, while higher volume brought in first-time buyers who return more. That is a mix shift, not a quality collapse.",
              "DECOMPOSE BEFORE YOU CONCLUDE", color=AMBER)

compare_table("Solution Failure vs Implementation Failure",
              ["", "Solution failure", "Implementation failure"],
              [["What happened", "It was done, and it did not work", "It was never really done"],
               ["ShopFront example", "Cart recovery at 3.1% vs 8% target", "Supplier QC — 4 of 12 adopted"],
               ["Evidence to check", "Open rates, click rates, benchmarks", "Adoption and compliance rates"],
               ["Right response", "Change or drop the solution", "Fix the rollout and change management"],
               ["Traceable back to", "Weak diagnosis or wrong target", "Stakeholder resistance you predicted"]],
              kicker="THE DISTINCTION THAT DECIDES THE NEXT S$200K", accent=VIOLET,
              note="Abandoning a solution that was never adopted throws away a fix that might have worked.")

prompt_slide("The Evaluation Prompt", A["prompt"], kicker="TOPIC 3  ·  PROMPT 10", accent=VIOLET,
             note="Without an explicit instruction to flag what cannot be determined, the AI will quietly overclaim attribution.")

activity_brief("ACTIVITY 10", A["title"], A["case_title"],
               "Judge an ambiguous 90-day result honestly and make the funding call to the CFO.",
               A["grouping"], A["duration"], A["edtool"]["name"] + " · " + A["edtool"]["url"],
               kicker="TOPIC 3  ·  HANDS-ON", objective=A["objective"])
case_slide("The Situation", A["case_title"], A["scenario"], kicker="ACTIVITY 10  ·  CASE STUDY")
evidence_table("The Results", A["data"]["caption"], A["data"]["rows"], kicker="ACTIVITY 10  ·  DATA")
questions_slide("Activity 10 — Discussion Questions", A["questions"], kicker="ACTIVITY 10  ·  BREAKOUT")
debrief_slide("Activity 10 — Debrief", [
    ("Attribution is the skill", "App load is cleanly attributable. Online sales are confounded by the GSS "
                                 "and cannot be claimed either way. Say so — that honesty is what makes the "
                                 "rest credible."),
    ("The returns puzzle", "Mix shift, not quality collapse. Segment by supplier and by customer type to "
                           "confirm before concluding anything."),
    ("The connection that matters", "Supplier QC missed because suppliers resisted — exactly as predicted "
                                    "in Activity 9. Your stakeholder analysis foretold your missed metric."),
    ("The verdict", "Continue with adjustment: rebase the cart-recovery target, fix supplier adoption as a "
                    "change-management problem, and give CSAT a longer horizon."),
], kicker="ACTIVITY 10  ·  WHAT WE LEARNED")

tile_grid("Sustaining the Gain", [
    ("PDCA / DMAIC-Control", "Plan-Do-Check-Act. Without a control phase, improvements decay back."),
    ("Standardise", "Write the new way into the SOP, the induction and the checklist."),
    ("Monitor", "Keep the leading indicator on a dashboard someone actually looks at."),
    ("Assign ownership", "A named role owns the sustained metric after the project team disbands."),
    ("Review cadence", "A standing checkpoint with a decision, not a status update."),
    ("Capture the lesson", "'Look back and learn' — the L in IDEAL, and the step most often skipped."),
], kicker="K7  ·  MAKING IT STICK", cols=2, size=13, accent=TEAL)

# ============================================================ CLOSING
section("WRAP UP", "Summary, Q&A and Assessment", "")

process_map("The Complete Method You Now Have",
            [("Frame", "Six-element statement"), ("Diagnose", "5 Whys · Fishbone · Pareto · Loops"),
             ("Generate", "Diverge widely, SCAMPER"), ("Decide", "Impact-Ease then weighted matrix"),
             ("Deliver", "CAP · stakeholders · evaluation")],
            kicker="TWO DAYS IN ONE DIAGRAM", color=BLUE,
            synthesis=("THE ONE THING TO REMEMBER",
                       "GenAI expands what you consider and accelerates how you get there. "
                       "The evidence, the judgement and the accountability remain yours."))

tile_grid("Your Problem-Solving Toolkit", [
    ("5 Whys", "https://alfredang.github.io/5whys/"),
    ("Fishbone", "https://alfredang.github.io/fishbone/"),
    ("Pareto Chart", "https://alfredang.github.io/paretochart/"),
    ("System Loop", "https://alfredang.github.io/systemloop/"),
    ("CollabNote", "https://alfredang.github.io/collabnote/"),
    ("Pinboard", "https://alfredang.github.io/pinboard/"),
], kicker="KEEP USING THESE AT WORK", cols=2, size=13, accent=TEAL)

tile_grid("Ten Prompts You Can Reuse Tomorrow", [
    ("1 · Problem statement", "Refine a vague complaint into six labelled elements."),
    ("2 · 5 Whys facilitator", "One why at a time, demanding evidence at each level."),
    ("3 · Fishbone populator", "Six bones, each cause marked [EVIDENCED] or [HYPOTHESIS]."),
    ("4 · Pareto analyst", "Cumulative percentages and the vital-few cut-off."),
    ("5 · Systems mapper", "R and B loops, the delay, and the leverage points."),
    ("6 · Divergent ideation", "20 ideas plus SCAMPER on a fixed assumption."),
    ("7 · Decision analyst", "Impact-Ease screen then a weighted matrix."),
    ("8 · CAP builder", "Eight components, with dependency and overload flags."),
    ("9 · Change advisor", "Objections in their words, plus the right messenger."),
    ("10 · Evaluator", "Verdicts, attribution, and what cannot be determined."),
], kicker="THE PROMPT LIBRARY IN YOUR LEARNER GUIDE", cols=2, size=12, accent=VIOLET)

big_statement("Summary & Q&A",
              "What is the one problem you will go back and re-frame on Monday?",
              "BEFORE WE ASSESS", color=BLUE)

tile_grid("Certificate & TRAQOM Survey (Mandatory)", [
    ("Complete the survey", "The TRAQOM course quality survey is mandatory for WSQ-funded courses."),
    ("Where", C.LMS),
    ("Certificate", "Your Certificate of Achievement is released after the survey and a Competent result."),
    ("SSG record", "Your Statement of Achievement appears in your SkillsFuture / MySkillsFuture record."),
], kicker="BEFORE YOU LEAVE", cols=2, accent=VIOLET)

# --- closing admin block (house rule: Assessment -> Flow -> TRAQOM -> Thank You) ---
tile_grid("Briefing for Assessment", [
    ("Clear your table", "Phones and materials under the table or on the floor."),
    ("No photos or recording", "Assessment scripts must not be photographed or copied."),
    ("No discussion", "Individual work only once the paper is handed out."),
    ("Black or blue pen", "No liquid paper or correction tape on hard-copy scripts."),
    ("Time is called", "Scripts are collected when time is up."),
    ("Open book means", "Slides, Learner Guide and approved materials — no internet, no AI tools."),
], kicker="READ BEFORE THE ASSESSMENT", cols=2, accent=AMBER)

admin_assessment_block(tag="FINAL ASSESSMENT")

tile_grid("Recommended Next Courses",
          [(c.replace("WSQ - ", ""), "WSQ funded  ·  tertiarycourses.com.sg")
           for c in C.RECOMMENDED_COURSES],
          kicker="CONTINUE YOUR LEARNING", cols=1, size=13, accent=TEAL)

tile_grid("Support", [
    ("Email", C.EMAIL),
    ("Telephone", C.TEL),
    ("Website", C.WEBSITE),
    ("After the course", "Free post-course consultation on subject-matter queries by email."),
], kicker="WE'RE HERE TO HELP", cols=2, accent=BLUE)

s = slide(); rect(s, 0, 0, SW, SH, WHITE)
rect(s, 0, 0, SW, Inches(0.22), BLUE); rect(s, 0, Inches(7.28), SW, Inches(0.22), TEAL)
txt(s, 0, Inches(2.6), SW, Inches(1.3), [[("Thank You!", 54, INK, True)]], align=PP_ALIGN.CENTER)
rect(s, Inches(5.4), Inches(4.05), Inches(2.53), Inches(0.1), TEAL)
txt(s, 0, Inches(4.4), SW, Inches(0.6), [[(C.TITLE, 18, GREY, False)]], align=PP_ALIGN.CENTER)
txt(s, 0, Inches(5.0), SW, Inches(0.5), [[(C.COURSE_CODE + "  ·  " + C.WEBSITE, 14, BLUE, True)]],
    align=PP_ALIGN.CENTER)
txt(s, 0, Inches(6.4), SW, Inches(0.4),
    [[("© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.", 10, GREY, False)]],
    align=PP_ALIGN.CENTER)
PAGE["n"] += 1

# ---------------- motion: one pass at the end ----------------
for i, sl in enumerate(prs.slides):
    shp = len(sl.shapes)
    _transition(sl, "fade", "med")

OUT = os.path.join(REPO, "courseware", "%s-%s.pptx" % (C.SHORT_TITLE, C.VERSION))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print("saved:", OUT)
print("slides:", len(prs.slides))
