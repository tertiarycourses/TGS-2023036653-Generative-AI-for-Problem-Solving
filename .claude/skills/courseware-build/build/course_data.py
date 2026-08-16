"""
SINGLE SOURCE OF TRUTH — WSQ Generative AI for Problem Solving (TGS-2023036653).

Every artifact (PPT, LP, LG, LG.md, activities index) is generated from this file
plus data_domain1.py … data_domain3.py, so they stay 100% aligned.

TSC: Problem Identification — RET-ACE-4006-1.1
Content is beefed up from the legacy v20 master deck PLUS the research corpus:
  - Skills for Success (Government of Canada / alis.alberta.ca) — 6 sub-skills
  - IMD — 8 problem-solving competencies, cognitive fixedness, consensus fatigue
  - MIT CCMIT — IDEAL heuristic (Bransford & Stein)
  - Coursera — 7 workplace problem-solving skills
  - Wikipedia — well/ill-defined problems, barriers, problem-solving cycle
  - 6sigma.us + Knowledge Academy — DMAIC, RCA, Pareto, decision matrices, SCAMPER
  - LSE Business Review — RAG, agent tooling, GenAI limits
  - Your Everyday AI ep.675 — Generic Parts Technique, SCAMPER with GenAI
  - arXiv 2412.13281 — generative optimization (GenAI explores, optimisation evaluates)
  - INFORMS Organization Science 2023.18430 — algorithmic vs human problem formulation
"""

# ------------------------------------------------------------------ metadata
TITLE        = "WSQ - Generative AI for Problem Solving"
SHORT_TITLE  = "Generative AI for Problem Solving"
COURSE_CODE  = "TGS-2023036653"
TSC_TITLE    = "Problem Identification"
TSC_CODE     = "RET-ACE-4006-1.1"
VERSION      = "v21.0"
VERSION_DATE = "17 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
DURATION_HRS = 16

WEBSITE = "www.tertiarycourses.com.sg"
EMAIL   = "enquiry@tertiaryinfotech.com"
TEL     = "+65 6100 0613"
LMS     = "https://lms-tms.tertiaryinfotech.com"

# ------------------------------------------------------------------ ed-tools
# Companion problem-solving ed-tools used live in the activities.
EDTOOLS = [
    dict(name="5 Whys",        url="https://alfredang.github.io/5whys/",
         use="Iterative why-laddering to drive from symptom to root cause."),
    dict(name="Fishbone",      url="https://alfredang.github.io/fishbone/",
         use="Ishikawa cause categorisation across People, Process, Technology, Material, Environment, Measurement."),
    dict(name="Pareto Chart",  url="https://alfredang.github.io/paretochart/",
         use="80/20 ranking of defect/complaint categories to target the vital few."),
    dict(name="System Loop",   url="https://alfredang.github.io/systemloop/",
         use="Causal loop mapping of reinforcing (R) and balancing (B) feedback loops."),
    dict(name="CollabNote",    url="https://alfredang.github.io/collabnote/",
         use="Shared note wall for posting team problem statements."),
    dict(name="Pinboard",      url="https://alfredang.github.io/pinboard/",
         use="Digital post-it wall for solution brainstorming and reflection."),
]

GENAI_TOOLS = "ChatGPT, Microsoft Copilot, Google Gemini, Claude"

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Identify performance deficiencies and root causes impacting organisational aspects",
    "LO2: Deduce key implications, develop corrective plans, and shortlist viable solutions",
    "LO3: Determine preferred solutions and evaluate the effectiveness of implemented plans",
]

# TSC abilities (from the Skills Framework) — carried onto the Skills Framework slides
TSC_ABILITIES = [
    "A1: Identify the types of performance deficiency and examine the causes and their impact on organisation-related aspects",
    "A2: Identify the root causes of the problems with team members using appropriate group facilitation techniques",
    "A3: Deduce relevant linkages and patterns to identify key implications on organisational systems and processes",
    "A4: Develop corrective action plans for any shortfalls identified in implemented solutions",
    "A5: Shortlist and evaluate the most viable ideas using appropriate problem-solving and decision-making techniques and tools",
    "A6: Determine a preferred solution using appropriate methods and draw up implementation plans",
    "A7: Evaluate the effectiveness of the implemented solution and implementation plans",
]

TSC_KNOWLEDGE = [
    "K1: Criteria for identifying performance deficiency or cause of failure in organisational systems and processes",
    "K2: Types of analytical tools and techniques in terms of problem identification",
    "K3: Application of problem solving tools and techniques",
    "K4: Techniques used during problem solving and decision making processes",
    "K5: Group facilitation techniques for root cause identification",
    "K6: Types of decision making models for arriving at the preferred solution and their features",
    "K7: Techniques to evaluate the effectiveness of implemented solution and implementation plan",
    "K8: Factors affecting the effectiveness of an implementation plan",
    "K9: Rationale for the different components in a corrective action plan",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Identifying Performance Gaps and Root Causes with Generative AI",
         subtitle="Problem framing · Problem statements · 5 Whys · Fishbone · Pareto · System loops",
         weighting="K1, K2, K5 · A1, A2",
         concepts=[
            "A problem well stated is a problem half solved — poor problem definitions burn budget on the wrong fix.",
            "Distinguish the symptom, the problem and the root cause; only root causes stop recurrence.",
            "Well-defined vs ill-defined problems demand different tooling and different levels of framing effort.",
            "A workplace problem statement carries Context, Metric, Baseline, Target, Timeframe and Constraints.",
            "Root-cause toolkit: 5 Whys (depth), Fishbone (breadth), Pareto (priority), System Loops (dynamics).",
            "GenAI accelerates framing and hypothesis generation, but the human owns evidence and judgement.",
         ]),
    dict(num=2, code="02",
         title="Developing Corrective Plans and Evaluating Potential Solutions",
         subtitle="Divergent ideation · SCAMPER · Impact–Ease matrix · Decision matrix · Corrective action plans",
         weighting="K4, K6, K9 · A3, A4, A5",
         concepts=[
            "Separate divergence from convergence — generating and judging at the same time kills good ideas.",
            "GenAI is a divergence engine: it produces breadth and unfamiliar analogies at near-zero cost.",
            "Convergence needs explicit criteria — Impact vs Ease for speed, weighted decision matrix for rigour.",
            "A corrective action plan states the root cause addressed, action, owner, timeline, resource and measure.",
            "Cognitive fixedness and consensus fatigue are the two biases that quietly narrow the solution set.",
            "Generative optimisation: GenAI explores the option space, structured criteria evaluate against constraints.",
         ]),
    dict(num=3, code="03",
         title="Selecting, Implementing and Measuring Solution Effectiveness",
         subtitle="Implementation planning · Stakeholders & resistance · Change management · KPIs · PDCA",
         weighting="K3, K7, K8 · A6, A7",
         concepts=[
            "A preferred solution is a decision you can defend — criteria, evidence, trade-offs and risks made explicit.",
            "An implementation plan converts a chosen solution into action, owner, timeline, resource and checkpoint.",
            "Most solutions fail on adoption, not on design — stakeholder resistance is a design input, not a surprise.",
            "Leading indicators warn you early; lagging indicators confirm the outcome. You need both.",
            "Evaluate against the baseline in the problem statement — this closes the loop back to Topic 1.",
            "PDCA / DMAIC-Control sustains the gain; without a control plan improvements decay.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Frame the problem and find the true root cause — with GenAI as your analyst",
    2: "Generate, choose, implement and prove the solution — with GenAI as your consultant",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), open book.",
    practical="Case Study (CS) — an integrated workplace problem-solving scenario, open book.",
    note="A minimum of 75% attendance based on the SSG Digital Attendance record, and a "
         "'Competent' result in both instruments, are required for certification and funding.",
    openbook="Open book covers the slides, Learner Guide and approved materials only.",
)

# ------------------------------------------------------------------ recommended
RECOMMENDED_COURSES = [
    "WSQ - Project Management with Generative AI (GenAI)",
    "WSQ - Design Thinking Course for Businesses",
    "WSQ - Effective Project Management for Small Projects",
    "WSQ - Project Management Professional (PMP) 35 PDU Training",
    "WSQ - Mastering Notion for Content, Project, and Database Management",
]
