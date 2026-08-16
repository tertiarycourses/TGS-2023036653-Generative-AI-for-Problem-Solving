#!/usr/bin/env python3
"""Derive slide anchors from the BUILT deck and write slide_map.py.

The Lesson Plan cites slide numbers. Hand-maintained numbers drift the moment a
slide is added or removed, which sends a trainer to the wrong slide at every
transition. This script reads the actual .pptx and emits the real numbers, so
build_lesson_plan.py can never be wrong. It runs as part of the orchestrator,
after the deck is built and before the LP.
"""
import os, re, sys, glob
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C


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
decks = sorted(glob.glob(os.path.join(REPO, "courseware", "*.pptx")), key=os.path.getmtime)
if not decks:
    raise SystemExit("no deck found — build the slides first")
prs = Presentation(decks[-1])


def text(s):
    return " ".join(" ".join(sh.text_frame.text.split()) for sh in s.shapes
                    if sh.has_text_frame and sh.text_frame.text.strip())


T = [text(s) for s in prs.slides]          # T[i] is slide i+1
N = len(T)


def first(pred, lo=1, hi=None):
    hi = hi or N
    for i in range(lo, hi + 1):
        if pred(T[i - 1]):
            return i
    return None


def all_hits(pred):
    return [i for i in range(1, N + 1) if pred(T[i - 1])]


# ---- activity blocks: the ACTIVITY n briefing slide through its debrief slide ----
acts = {}
brief = {}
for i, t in enumerate(T, 1):
    m = re.search(r"\bACTIVITY (\d+)\b", t)
    if m and "HANDS-ON" in t:
        brief.setdefault(int(m.group(1)), i)
for n, s in brief.items():
    # the block ends at THIS activity's debrief slide (kicker "ACTIVITY n · WHAT WE LEARNED")
    tag = "ACTIVITY %d · WHAT WE LEARNED" % n
    e = first(lambda x, tag=tag: tag in x.replace("  ", " "), lo=s)
    if e is None:
        # fall back: end just before the next activity's briefing
        nxt = min((v for k, v in brief.items() if v > s), default=N)
        e = nxt - 1
    acts[n] = (s, e)

# ---- section dividers: a divider carries the big topic number and no kicker body ----
def divider(num, title_frag):
    return first(lambda t: t.startswith("TOPIC %d" % num) or
                 ("TOPIC %d" % num in t[:40] and title_frag.lower() in t.lower()))


topics = {}
for tp in C.TOPICS:
    n = tp["num"]
    frag = tp["title"].split()[0]
    # the divider slide shows "TOPIC n" as its kicker AND the topic title AND the big numeral
    hit = first(lambda t, n=n, tp=tp: ("TOPIC %d" % n) in t and tp["title"] in t
                and tp["subtitle"][:24] in t)
    topics[n] = hit or divider(n, frag)

ANCHORS = dict(
    total=N,
    activities=acts,
    topics=topics,
    admin_start=1,
    ice_breaker=first(lambda t: "Let's know each other" in t),
    trainer_template=first(lambda t: "GENERAL TRAINER TEMPLATE" in t),
    trainer_named=first(lambda t: C.TRAINER in t and "YOUR TRAINER" in t),
    ground_rules=first(lambda t: "Ground Rules" in t),
    download=first(lambda t: "Download Your Course Material" in t),
    skills_framework=first(lambda t: "Skills Framework Alignment" in t),
    outcomes=first(lambda t: "Learning Outcomes" in t and "BY THE END" in t),
    lesson_plan=all_hits(lambda t: "Lesson Plan — Day" in t),
    briefing=all_hits(lambda t: "Briefing for Assessment" in t),
    assessment=all_hits(lambda t: "Final Assessment" in t and "Written Assessment (WA)" in t),
    flow=all_hits(lambda t: "Assessment Flow" in t),
    attendance=all_hits(lambda t: "Digital Attendance" in t and "TRAQOM" in t),
    lunch=all_hits(lambda t: "Lunch Break" in t),
    end_day1=first(lambda t: "End of Day 1" in t),
    recap_day1=first(lambda t: "Day 1 in one line" in t),
    toolkit=first(lambda t: "Four tools. Four different jobs." in t
                  or "Choosing Your Root Cause Tool" in t),
    convergence=first(lambda t: "Divergence Then Convergence" in t),
    implementation=first(lambda t: "From Decision to Proven Result" in t),
    summary=first(lambda t: "The Complete Method" in t),
    traqom_cert=first(lambda t: "Certificate & TRAQOM" in t),
    thanks=first(lambda t: "Thank You" in t),
)

OUT = os.path.join(HERE, "slide_map.py")
with open(OUT, "w") as f:
    f.write('"""AUTO-GENERATED from the built deck by derive_slide_map.py.\n'
            'DO NOT HAND-EDIT — regenerated on every build so the Lesson Plan\n'
            'slide references can never drift from the deck."""\n\n')
    f.write("ANCHORS = %r\n" % (ANCHORS,))

print("slide_map.py written from:", os.path.basename(decks[-1]))
print("  slides:", N)
print("  activities:", {k: acts[k] for k in sorted(acts)})
print("  topics:", topics)
print("  briefing:", ANCHORS["briefing"], " assessment:", ANCHORS["assessment"],
      " flow:", ANCHORS["flow"], " attendance:", ANCHORS["attendance"])
missing = [k for k, v in ANCHORS.items() if v is None]
if missing:
    raise SystemExit("ANCHOR NOT FOUND: %s — the deck changed; fix the matcher." % missing)
