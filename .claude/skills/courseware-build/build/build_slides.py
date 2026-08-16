#!/usr/bin/env python3
"""Generate the WSQ Generative AI for Problem Solving slide deck.

Single source: course_data.py + data_domain1..3.py.
Engine = shared house helpers (_engine_head.py) + course components (_components.py)
       + the deck narrative (_body.py).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ns = {"__name__": "__slides__", "__file__": os.path.join(HERE, "build_slides.py")}

for part in ("_engine_head.py", "_components.py", "_body.py"):
    with open(os.path.join(HERE, part)) as fh:
        exec(compile(fh.read(), part, "exec"), ns)
