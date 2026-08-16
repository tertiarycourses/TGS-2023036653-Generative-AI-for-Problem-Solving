# WSQ — Generative AI for Problem Solving

[![WSQ](https://img.shields.io/badge/WSQ-TGS--2023036653-1F6FEB)](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-problem-solving.html)
[![TSC](https://img.shields.io/badge/TSC-RET--ACE--4006--1.1-10B981)](https://www.skillsfuture.gov.sg/skills-framework)
[![Duration](https://img.shields.io/badge/Duration-2%20days%20·%2016%20hours-7C3AED)](#lesson-plan)
[![Version](https://img.shields.io/badge/Version-v21.0-F59E0B)](#version)

Courseware for the SkillsFuture-funded WSQ course **Generative AI for Problem Solving**,
delivered by **Tertiary Infotech Academy Pte Ltd** (UEN 201200696W).

> **The premise:** most organisations are very good at generating solutions and very poor at
> defining problems. This course teaches a complete, repeatable method — frame, diagnose,
> generate, converge, implement, prove — with generative AI as a divergence engine and a
> challenger, never as an oracle.

---

## Course at a Glance

| | |
|---|---|
| **Course code** | TGS-2023036653 |
| **TSC alignment** | Problem Identification (RET-ACE-4006-1.1) |
| **Duration** | 2 days · 16 hours (8 instructional hours per day) |
| **Level** | Beginner — no prior problem-solving or AI training required |
| **Assessment** | Written Assessment (SAQ) + Case Study, both open book |
| **Delivery** | Physical classroom, synchronous Zoom, or corporate on-site |
| **Funding validity** | 18 Aug 2023 – 17 Aug 2027 |

### Learning Outcomes

1. **LO1** — Identify performance deficiencies and root causes impacting organisational aspects
2. **LO2** — Deduce key implications, develop corrective plans, and shortlist viable solutions
3. **LO3** — Determine preferred solutions and evaluate the effectiveness of implemented plans

---

## Repository Contents

```
courseware/
├── courseware/                     the four learner-facing artifacts
│   ├── Generative AI for Problem Solving-v21.0.pptx    160-slide trainer deck
│   ├── Generative AI for Problem Solving-v21.0.pdf     learner slides
│   ├── LP-Generative AI for Problem Solving.docx/.pdf  Lesson Plan
│   └── LG-Generative AI for Problem Solving.docx/.pdf  Learner Guide (59 pp)
├── activities/                     10 case-study activities, one folder each
│   ├── activity-01-…/              README · scenario · prompt · debrief.pdf · worksheet
│   └── Activity-Debrief-Pack-….pdf combined trainer pack
├── LG-Generative AI for Problem Solving.md             Markdown mirror of the LG
└── .claude/skills/courseware-build/build/              the single-source generators
```

> **Note** — `assessment/` is **confidential** and is deliberately **not** in this repository.
> The papers live in the course's Google Drive folder and on the LMS.

---

## The Method

The course follows a single arc, and every activity advances it:

| Stage | What happens | Tools taught |
|---|---|---|
| **Frame** | Turn a vague complaint into a measurable problem statement | Six-element statement, IDEAL cycle |
| **Diagnose** | Find the true root cause, not the loudest symptom | 5 Whys · Fishbone · Pareto · System Loops |
| **Generate** | Expand the option set before judging any of it | Brainstorming · SCAMPER · analogy |
| **Converge** | Choose defensibly, not by seniority | Impact-Ease matrix · weighted decision matrix |
| **Deliver** | Survive contact with real people | Corrective action plan · stakeholder strategy |
| **Prove** | Establish whether it actually worked | Leading/lagging indicators · attribution |

---

## The Activities

Ten real-life Singapore workplace case studies. Each folder carries the scenario, an evidence
table, detailed steps, the GenAI prompt, discussion questions, a trainer debrief (PDF) and a
printable worksheet.

| # | Activity | Case study | Ed-tool |
|---|---|---|---|
| 1 | Rewriting a vague problem into a measurable statement | ShopFront SG | [CollabNote](https://alfredang.github.io/collabnote/) |
| 2 | 5 Whys root cause analysis | Meridian Health | [5 Whys](https://alfredang.github.io/5whys/) |
| 3 | Fishbone diagram for breadth of causes | Horizon Bank | [Fishbone](https://alfredang.github.io/fishbone/) |
| 4 | Pareto analysis to target the vital few | Nexa Logistics | [Pareto](https://alfredang.github.io/paretochart/) |
| 5 | System loops — why the problem keeps coming back | Horizon Bank revisited | [System Loop](https://alfredang.github.io/systemloop/) |
| 6 | Divergent ideation with GenAI + SCAMPER | Meridian Health | [Pinboard](https://alfredang.github.io/pinboard/) |
| 7 | Converging — Impact-Ease and weighted decision matrix | Meridian Health | Pinboard |
| 8 | Building the corrective action plan | Meridian Health | Pinboard |
| 9 | Implementation planning and stakeholder resistance | ShopFront SG | Pinboard |
| 10 | Measuring effectiveness — did it actually work? | ShopFront SG | Pareto |

The cases deliberately **recur**: Horizon Bank's fishbone in Activity 3 becomes its system-loop
post-mortem in Activity 5; Meridian Health's root cause in Activity 2 drives the solutions in
6–8; ShopFront SG's problem statement in Activity 1 is what makes evaluation possible in
Activity 10. The course closes its own loop.

---

## Ed-Tools

Browser-based tools used live in class — no install, no login.

| Tool | Purpose |
|---|---|
| [5 Whys](https://alfredang.github.io/5whys/) | Why-laddering from symptom to root cause |
| [Fishbone](https://alfredang.github.io/fishbone/) | Ishikawa cause categorisation across six dimensions |
| [Pareto Chart](https://alfredang.github.io/paretochart/) | 80/20 ranking to find the vital few |
| [System Loop](https://alfredang.github.io/systemloop/) | Causal loop mapping of reinforcing and balancing feedback |
| [CollabNote](https://alfredang.github.io/collabnote/) | Shared wall for team problem statements |
| [Pinboard](https://alfredang.github.io/pinboard/) | Digital post-it wall for ideation and reflection |

---

## Building the Courseware

All artifacts are generated from a **single source** — `course_data.py` plus
`data_domain1..3.py` — so the deck, Lesson Plan, Learner Guide and activities can never drift
apart.

```bash
bash .claude/skills/courseware-build/build/build_courseware.sh
```

This generates the PPT, LP and LG, builds the ten activity folders and their debrief PDFs,
renders every PDF, and injects page-numbered tables of contents.

To rebuild a single artifact:

```bash
python3 .claude/skills/courseware-build/build/build_slides.py         # deck
python3 .claude/skills/courseware-build/build/build_lesson_plan.py    # LP
python3 .claude/skills/courseware-build/build/build_learner_guide.py  # LG + .md
python3 .claude/skills/courseware-build/build/build_activities.py     # activity folders
```

**Requirements:** Python 3 with `python-pptx`, `python-docx`, `pypdf`, `PyMuPDF`; LibreOffice
(`soffice`) on the PATH for PDF rendering.

---

## Content Sources

The courseware is built on the legacy master deck plus current practitioner and academic
sources:

- [Skills for Success — Problem Solving](https://alis.alberta.ca/inspire-and-motivate/the-9-skills-for-success/skills-for-success-problem-solving/) (Government of Canada) — the six sub-skills
- [IMD — Problem-solving skills](https://www.imd.org/blog/strategy/problem-solving-skills/) — cognitive fixedness, consensus fatigue
- [MIT CCMIT — Problem Solving](https://ccmit.mit.edu/problem-solving/) — the IDEAL heuristic
- [Coursera — Problem-Solving Skills](https://www.coursera.org/articles/problem-solving-skills)
- [Wikipedia — Problem solving](https://en.wikipedia.org/wiki/Problem_solving) — barriers, well/ill-defined problems
- [6sigma.us](https://www.6sigma.us/six-sigma-in-focus/problem-solving-techniques/) and [The Knowledge Academy](https://www.theknowledgeacademy.com/blog/problem-solving-techniques/) — RCA, Pareto, decision matrices, SCAMPER
- [LSE Business Review](https://blogs.lse.ac.uk/businessreview/2024/05/24/how-to-enhance-generative-ais-problem-solving-capabilities-and-boost-workplace-productivity/) — RAG, agent tooling, GenAI limits
- [Your Everyday AI ep.675](https://www.youreverydayai.com/ep-675-creative-frameworks-for-problem-solving-with-generative-ai/) — Generic Parts Technique, SCAMPER with GenAI
- [arXiv 2412.13281](https://arxiv.org/html/2412.13281v2) — generative optimisation

---

## Version

**v21.0** · 17 August 2026 · Dr. Alfred Ang

Major revision: retitled to the published course title, rebuilt around ten real-life case-study
activities with full scenarios, evidence, debriefs and worksheets; added the four
problem-solving ed-tools, a reusable ten-prompt GenAI library, expanded theory chapters and a
31-term glossary.

---

## Links

- [Course page](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-problem-solving.html)
- [MySkillsFuture listing](https://courses.myskillsfuture.gov.sg/courses/TGS-2023036653)
- [LMS / TMS](https://lms-tms.tertiaryinfotech.com)

---

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
