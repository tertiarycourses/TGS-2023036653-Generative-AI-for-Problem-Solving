#!/usr/bin/env python3
"""Generate the per-activity folders.

activities/
  README.md                         index of all ten activities
  activity-01-<slug>/
    README.md                       full brief (scenario, evidence, steps, prompt, questions)
    scenario.md                     the case scenario + evidence, for handing to learners
    prompt.txt                      the GenAI prompt, ready to copy
    debrief.md                      trainer debrief (also rendered to debrief.pdf)
    worksheet.md                    printable team worksheet
"""
import os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACT = DOMAIN1 + DOMAIN2 + DOMAIN3


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "activities")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
ROOT = os.path.join(REPO, "activities")
os.makedirs(ROOT, exist_ok=True)


def slug(t):
    t = t.split("— ", 1)[-1].lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return re.sub(r"-+", "-", t)[:48]


def md_table(rows):
    hdr, body = rows[0], rows[1:]
    out = ["| " + " | ".join(str(c) for c in hdr) + " |",
           "|" + "|".join(["---"] * len(hdr)) + "|"]
    for r in body:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)


HDR = ("<!-- %s (%s) · %s · %s -->\n" % (C.TITLE, C.COURSE_CODE, C.ORG, C.VERSION))

index = ["# Activities — %s" % C.TITLE, "",
         "**WSQ Course Code:** %s  |  **Version %s · %s**" % (C.COURSE_CODE, C.VERSION, C.VERSION_DATE), "",
         "Ten real-life workplace case-study activities. Each has its own folder containing the "
         "scenario, the evidence, the step-by-step, the GenAI prompt, the discussion questions, "
         "the trainer debrief and a printable team worksheet.", "",
         "| # | Activity | Topic | Case study | Duration | Team | Ed-tool |",
         "|---|---|---|---|---|---|---|"]

for a in ACT:
    d = os.path.join(ROOT, "activity-%02d-%s" % (a["num"], slug(a["title"])))
    os.makedirs(d, exist_ok=True)
    short = a["title"].split("— ", 1)[-1]
    index.append("| %d | [%s](%s/README.md) | %d | %s | %s | %s | [%s](%s) |"
                 % (a["num"], short, os.path.basename(d), a["topic"],
                    a["case_title"].split(" — ")[0], a["duration"], a["grouping"],
                    a["edtool"]["name"], a["edtool"]["url"]))

    steps_md = "\n".join("%d. %s" % (i, s[0]) for i, s in enumerate(a["steps"], 1))
    q_md = "\n".join("%d. %s" % (i, q) for i, q in enumerate(a["questions"], 1))
    scen_md = "\n\n".join(x.strip() for x in a["scenario"].split("\n\n") if x.strip())
    deb_md = "\n\n".join(x.strip() for x in a["debrief"].split("\n\n") if x.strip())

    # ---------- README.md (the full brief) ----------
    readme = [HDR, "# %s" % a["title"], "",
              "**Topic %d** · %s" % (a["topic"], a["objective"]), "",
              "| Field | Detail |", "|---|---|",
              "| Case study | %s |" % a["case_title"],
              "| Duration | %s |" % a["duration"],
              "| Grouping | %s |" % a["grouping"],
              "| Tools | %s |" % a["services"],
              "| Ed-tool | [%s](%s) |" % (a["edtool"]["name"], a["edtool"]["url"]),
              "", "---", "", "## The Scenario", "", scen_md, "",
              "## The Evidence", "", "*%s*" % a["data"]["caption"], "",
              md_table(a["data"]["rows"]), "",
              "## Step-by-Step", "", steps_md, "",
              "## The GenAI Prompt", "",
              "Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. "
              "Replace anything in `<<double angle brackets>>` with your own details.", "",
              "```text", a["prompt"], "```", "",
              "## Discussion Questions", "", q_md, "",
              "## Self-Check — Is Your Output Finished?", "", a["test"], "",
              "---", "",
              "*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*", ""]
    open(os.path.join(d, "README.md"), "w").write("\n".join(readme))

    # ---------- scenario.md (learner handout) ----------
    scen = [HDR, "# %s" % a["case_title"], "",
            "**Activity %d** · %s · %s" % (a["num"], a["duration"], a["grouping"]), "",
            "## The Situation", "", scen_md, "",
            "## The Evidence", "", "*%s*" % a["data"]["caption"], "",
            md_table(a["data"]["rows"]), "",
            "## Your Discussion Questions", "", q_md, "",
            "## You Are Finished When", "", a["test"], ""]
    open(os.path.join(d, "scenario.md"), "w").write("\n".join(scen))

    # ---------- prompt.txt ----------
    open(os.path.join(d, "prompt.txt"), "w").write(
        "# Activity %d — %s\n# %s\n# Paste into ChatGPT / Copilot / Gemini / Claude\n\n%s\n"
        % (a["num"], short, C.TITLE, a["prompt"]))

    # ---------- debrief.md (trainer) ----------
    deb = [HDR, "# Trainer Debrief — Activity %d" % a["num"], "",
           "## %s" % a["title"], "",
           "**Case study:** %s  \n**Objective:** %s" % (a["case_title"], a["objective"]), "",
           "---", "", deb_md, "", "---", "",
           "## Discussion Questions (for reference)", "", q_md, "",
           "## Success Criteria", "", a["test"], ""]
    open(os.path.join(d, "debrief.md"), "w").write("\n".join(deb))

    # ---------- worksheet.md (printable) ----------
    ws = [HDR, "# Team Worksheet — Activity %d" % a["num"], "",
          "## %s" % short, "",
          "**Team members:** ______________________________________________  \n"
          "**Date:** ____________________", "",
          "---", "",
          "### 1. Our understanding of the problem", "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "### 2. Our working (use the ed-tool: %s)" % a["edtool"]["url"], "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "### 3. What the GenAI produced that our evidence did NOT support", "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "### 4. Our conclusion", "",
          "_______________________________________________________________________", "",
          "_______________________________________________________________________", "",
          "### 5. Discussion question notes", ""]
    for i, q in enumerate(a["questions"], 1):
        ws += ["**Q%d.** %s" % (i, q), "",
               "_______________________________________________________________________", "",
               "_______________________________________________________________________", ""]
    open(os.path.join(d, "worksheet.md"), "w").write("\n".join(ws))

index += ["", "## Ed-Tools Used", "",
          "| Tool | URL | Purpose |", "|---|---|---|"]
for e in C.EDTOOLS:
    index.append("| %s | %s | %s |" % (e["name"], e["url"], e["use"]))
index += ["", "---", "",
          "© 2026 %s. All rights reserved." % C.ORG, ""]
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(index))
print("Saved", ROOT, "—", len(ACT), "activity folders")
