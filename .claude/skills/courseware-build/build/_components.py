"""
Course-specific visual components for Generative AI for Problem Solving.

These extend the shared house component set (tile_grid, process_map, compare_table,
chart_slide, cards3, big_statement...) with the diagrams this course actually teaches:
fishbone, 5-Whys ladder, Pareto, causal loops, Impact-Ease matrix, prompt cards,
case-study briefings, discussion questions and debrief panels.

All are native PowerPoint vector shapes — editable, resolution-independent, on-brand.
This file is exec'd after _engine_head.py, so all helpers/palette are in scope.
"""


# ---------------------------------------------------------------- prompt card
def prompt_slide(title, prompt_text, kicker=None, accent=VIOLET, note=None,
                 tool_hint="Paste into ChatGPT · Copilot · Gemini · Claude"):
    """THE PROMPT, verbatim and readable — the single most-used slide in this course.
    Renders as a dark 'editor' panel so it reads as something to be copied."""
    s = head(slide(), title, kicker, kcolor=accent)
    rect(s, Inches(0.85), Inches(1.9), Inches(11.63), Inches(0.42), LIGHT)
    rect(s, Inches(0.85), Inches(1.9), Inches(0.09), Inches(0.42), accent)
    txt(s, Inches(1.12), Inches(1.9), Inches(11.2), Inches(0.42),
        [[("PROMPT  ·  ", 11, accent, True), (tool_hint, 11, GREY, False)]],
        anchor=MSO_ANCHOR.MIDDLE)

    bottom = Inches(6.72) if not note else Inches(5.92)
    py = Inches(2.46)
    rect(s, Inches(0.85), py, Inches(11.63), bottom - py, RGBColor(0x0B, 0x12, 0x20))

    lines = [l for l in prompt_text.split("\n")]
    avail_h = bottom - py - Inches(0.3)
    # count VISUAL rows: a long line wraps, so char count drives height as much as
    # line count. ~86 chars fit per row at 12.5pt in this 11.1in panel.
    # Size from MEASURED geometry, not a lookup table. Consolas advance width is
    # ~0.55em; usable panel width is 11.1in less padding. Row pitch is ~1.30x the
    # point size. Renderers (LibreOffice/PowerPoint) differ slightly, so a 12%
    # safety margin is applied to the row budget.
    panel_w_in = 11.1 - 0.30
    panel_h_pt = (avail_h / 914400.0) * 72.0

    def fits(sz):
        char_w_in = (sz * 0.55) / 72.0
        cpr = max(20, int(panel_w_in / char_w_in))
        rows = sum(max(1, -(-len(l) // cpr)) if l.strip() else 1 for l in lines)
        return rows * (sz * 1.30) <= panel_h_pt * 0.88

    size = 6.0
    for cand in (12.5, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6.0):
        if fits(cand):
            size = cand; break

    tb = s.shapes.add_textbox(Inches(1.12), py + Inches(0.16), Inches(11.1), avail_h)
    tf = tb.text_frame; tf.word_wrap = True
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(1.5)
        st = ln.strip()
        col = RGBColor(0xD4, 0xD4, 0xD4)
        bold = False
        if st.startswith("-") or st.startswith("*"):
            col = RGBColor(0x9C, 0xDC, 0xFE)
        if st.endswith(":") and len(st) < 60:
            col = RGBColor(0x4E, 0xC9, 0xB0); bold = True
        if st.startswith("<<") or st.startswith("["):
            col = RGBColor(0xF5, 0x9E, 0x0B); bold = True
        if st and st[0].isdigit() and st[1:2] in (".", ")"):
            col = RGBColor(0x4E, 0xC9, 0xB0); bold = True
        r = p.add_run(); r.text = ln if ln else " "
        r.font.size = Pt(size); r.font.name = "Consolas"
        r.font.color.rgb = col; r.font.bold = bold
    if note:
        rect(s, Inches(0.85), Inches(6.06), Inches(11.63), Inches(0.78), LIGHT)
        rect(s, Inches(0.85), Inches(6.06), Inches(0.09), Inches(0.78), AMBER)
        txt(s, Inches(1.15), Inches(6.06), Inches(11.1), Inches(0.78),
            [[("WATCH FOR  ", 10.5, AMBER, True), (note, 11.5, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s


# ---------------------------------------------------------------- case study
def case_slide(title, case_title, scenario, kicker=None, accent=AMBER, tag="CASE STUDY"):
    """The scenario briefing — a magazine-style case card. Scenario text is the hero."""
    s = head(slide(), title, kicker, kcolor=accent)
    rect(s, Inches(0.85), Inches(1.88), Inches(1.85), Inches(0.44), accent)
    txt(s, Inches(0.85), Inches(1.88), Inches(1.85), Inches(0.44),
        [[(tag, 12, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(2.88), Inches(1.88), Inches(9.6), Inches(0.44),
        [[(case_title, 15, INK, True)]], anchor=MSO_ANCHOR.MIDDLE)

    body = " ".join(scenario.split()) if "\n\n" not in scenario else scenario
    paras = [p.strip() for p in scenario.split("\n\n") if p.strip()]
    rect(s, Inches(0.85), Inches(2.5), Inches(11.63), Inches(4.3), LIGHT)
    rect(s, Inches(0.85), Inches(2.5), Inches(0.1), Inches(4.3), accent)

    total = sum(len(p) for p in paras)
    size = 14.5
    if total > 620: size = 13
    if total > 820: size = 11.5
    if total > 1020: size = 10.5
    if total > 1250: size = 9.5

    tb = s.shapes.add_textbox(Inches(1.2), Inches(2.66), Inches(11.0), Inches(4.0))
    tf = tb.text_frame; tf.word_wrap = True
    for i, p_ in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(7)
        r = p.add_run(); r.text = " ".join(p_.split())
        r.font.size = Pt(size); r.font.name = "Arial"; r.font.color.rgb = INK
    footer(s); return s


def evidence_table(title, caption, rows, kicker=None, accent=BLUE):
    """The case's evidence table — data learners actually work from."""
    hdr, body = rows[0], rows[1:]
    return compare_table(title, hdr, body, kicker=kicker, accent=accent, note=caption)


def questions_slide(title, questions, kicker=None, accent=BLUE, header="DISCUSSION QUESTIONS"):
    """Numbered discussion questions — the breakout's actual agenda."""
    s = head(slide(), title, kicker, kcolor=accent)
    rect(s, Inches(0.85), Inches(1.88), Inches(11.63), Inches(0.4), LIGHT)
    rect(s, Inches(0.85), Inches(1.88), Inches(0.09), Inches(0.4), accent)
    txt(s, Inches(1.14), Inches(1.88), Inches(11.2), Inches(0.4),
        [[(header, 11, accent, True)]], anchor=MSO_ANCHOR.MIDDLE)

    y0 = Inches(2.44); n = len(questions); gap = Inches(0.13)
    avail = Inches(6.84) - y0
    rh = int(min(Inches(1.24), (avail - gap * (n - 1)) / max(n, 1)))
    total = sum(len(q) for q in questions)
    size = 12.5 if total < 620 else (11.5 if total < 800 else 10.5)
    for i, q in enumerate(questions):
        y = int(y0 + (rh + gap) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, Inches(0.85), y, Inches(11.63), rh, LIGHT)
        rect(s, Inches(0.85), y, Inches(0.09), rh, col)
        bd = Inches(0.46)
        oval(s, Inches(1.1), int(y + rh / 2 - bd / 2), bd, bd, col)
        txt(s, Inches(1.1), int(y + rh / 2 - bd / 2), bd, bd,
            [[("Q%d" % (i + 1), 12, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, Inches(1.76), y, Inches(10.5), rh, [[(q, size, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s


def debrief_slide(title, points, kicker=None, accent=TEAL, header="TRAINER DEBRIEF"):
    """The debrief — what the trainer draws out. points: list of (label, body)."""
    s = head(slide(), title, kicker, kcolor=accent)
    rect(s, Inches(0.85), Inches(1.88), Inches(11.63), Inches(0.4), LIGHT)
    rect(s, Inches(0.85), Inches(1.88), Inches(0.09), Inches(0.4), accent)
    txt(s, Inches(1.14), Inches(1.88), Inches(11.2), Inches(0.4),
        [[(header, 11, accent, True)]], anchor=MSO_ANCHOR.MIDDLE)

    y0 = Inches(2.44); n = len(points); gap = Inches(0.14)
    avail = Inches(6.84) - y0
    rh = int(min(Inches(1.5), (avail - gap * (n - 1)) / max(n, 1)))
    total = sum(len(b) for _, b in points)
    size = 12 if total < 560 else (11 if total < 760 else 10)
    for i, (lbl, body) in enumerate(points):
        y = int(y0 + (rh + gap) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, Inches(0.85), y, Inches(11.63), rh, LIGHT)
        rect(s, Inches(0.85), y, Inches(0.09), rh, col)
        txt(s, Inches(1.2), int(y + Inches(0.11)), Inches(11.0), Inches(0.32),
            [[(lbl.upper(), 10.5, col, True)]])
        txt(s, Inches(1.2), int(y + Inches(0.45)), Inches(11.0), int(rh - Inches(0.56)),
            [[(body, size, INK, False)]])
    footer(s); return s


# ---------------------------------------------------------------- 5 Whys ladder
def whys_ladder(title, pairs, root, kicker=None, accent=BLUE):
    """A descending 5-Whys staircase ending in a root-cause band.
    pairs: list of (why_question, answer)."""
    s = head(slide(), title, kicker, kcolor=accent)
    n = len(pairs)
    y0 = Inches(1.9); rh = Inches(0.72); gap = Inches(0.1)
    indent = Inches(0.42)
    for i, (q, a) in enumerate(pairs):
        y = int(y0 + (rh + gap) * i)
        x = int(Inches(0.85) + indent * i)
        w = int(Inches(11.63) - indent * i)
        col = PALETTE[i % len(PALETTE)]
        rect(s, x, y, w, rh, LIGHT); rect(s, x, y, Inches(0.09), rh, col)
        bd = Inches(0.42)
        oval(s, x + Inches(0.2), int(y + rh / 2 - bd / 2), bd, bd, col)
        txt(s, x + Inches(0.2), int(y + rh / 2 - bd / 2), bd, bd,
            [[(str(i + 1), 13, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x + Inches(0.78), int(y + Inches(0.05)), w - Inches(1.0), Inches(0.32),
            [[(_ellipsis(q, 96), 11, col, True)]])
        txt(s, x + Inches(0.78), int(y + Inches(0.36)), w - Inches(1.0), Inches(0.34),
            [[(_ellipsis(a, 108), 10.5, INK, False)]])
        if i < n - 1:
            cx = int(x + Inches(0.41))
            connector(s, cx, int(y + rh), cx, int(y + rh + gap), col, width=Pt(1.6))
    ry = int(y0 + (rh + gap) * n + Inches(0.06))
    rect(s, Inches(0.85), ry, Inches(11.63), Inches(0.86), RGBColor(0xE8, 0xF7, 0xEE))
    rect(s, Inches(0.85), ry, Inches(0.11), Inches(0.86), RGBColor(0x12, 0x7A, 0x3E))
    txt(s, Inches(1.2), int(ry + Inches(0.09)), Inches(11.0), Inches(0.3),
        [[("ROOT CAUSE IDENTIFIED", 10.5, RGBColor(0x12, 0x7A, 0x3E), True)]])
    txt(s, Inches(1.2), int(ry + Inches(0.4)), Inches(11.0), Inches(0.42),
        [[(root, 12, INK, True)]])
    footer(s); return s


# ---------------------------------------------------------------- fishbone
def fishbone(title, problem, bones, kicker=None, accent=BLUE):
    """A real Ishikawa diagram: spine, angled bones, cause twigs, problem head.
    bones: list of (bone_name, [causes]) — up to 6."""
    s = head(slide(), title, kicker, kcolor=accent)
    SPINE_Y = Inches(4.44)
    X0 = Inches(1.0)
    HEAD_X = Inches(10.75)
    # spine
    connector(s, X0, SPINE_Y, HEAD_X, SPINE_Y, INK, width=Pt(2.6))
    # problem head
    hb = roundrect(s, HEAD_X, int(SPINE_Y - Inches(0.85)), Inches(2.42), Inches(1.7),
                   RGBColor(0xB9, 0x1C, 0x1C))
    label_in(hb, _ellipsis(problem, 96), 9.5, WHITE)

    top = [b for i, b in enumerate(bones) if i % 2 == 0]
    bot = [b for i, b in enumerate(bones) if i % 2 == 1]
    span = HEAD_X - X0 - Inches(0.6)

    def draw(group, up):
        if not group: return
        step = int(span / (len(group) + 0.35))
        for j, (name, causes) in enumerate(group):
            col = PALETTE[(j * 2 + (0 if up else 1)) % len(PALETTE)]
            bx = int(X0 + Inches(0.55) + step * (j + 0.42))
            dy = Inches(1.16)
            tipx = int(bx - Inches(0.5))
            tipy = int(SPINE_Y - dy) if up else int(SPINE_Y + dy)
            connector(s, bx, int(SPINE_Y), tipx, tipy, col, width=Pt(2.0), arrow=False)
            # bone label sits at the tip; causes stack BETWEEN the label and the spine
            lbl_y = int(tipy - Inches(0.4)) if up else int(tipy + Inches(0.02))
            lb = rect(s, int(tipx - Inches(0.9)), lbl_y, Inches(1.8), Inches(0.36), col)
            label_in(lb, name.upper(), 9, WHITE)
            for k, c in enumerate(causes[:3]):
                yy = (int(lbl_y - Inches(0.3) * (k + 1) - Inches(0.02)) if up
                      else int(lbl_y + Inches(0.38) + Inches(0.3) * k))
                txt(s, int(tipx - Inches(1.05)), yy, Inches(2.5), Inches(0.28),
                    [[("• " + _ellipsis(c, 32), 8.5, GREY, False)]])
    draw(top, True)
    draw(bot, False)
    footer(s); return s


# ---------------------------------------------------------------- causal loop
def causal_loop(title, loops, kicker=None, accent=VIOLET, note=None):
    """Reinforcing/balancing loop cards, each showing the variable chain with +/- signs.
    loops: list of (code, name, kind 'R'|'B', [chain items], effect)."""
    s = head(slide(), title, kicker, kcolor=accent)
    n = len(loops)
    cols = 2 if n > 2 else n
    rows = (n + cols - 1) // cols
    X0 = Inches(0.85); Y0 = Inches(1.95)
    TOTW = Inches(11.63); AREAH = Inches(4.85)
    gx = Inches(0.3); gy = Inches(0.26)
    cw = int((TOTW - gx * (cols - 1)) / cols)
    ch = int((AREAH - gy * (rows - 1)) / rows)
    for i, (code, name, kind, chain, effect) in enumerate(loops):
        r = i // cols; c = i % cols
        x = int(X0 + (cw + gx) * c); y = int(Y0 + (ch + gy) * r)
        col = RGBColor(0xB9, 0x1C, 0x1C) if kind == "R" else RGBColor(0x0E, 0x7A, 0x5E)
        rect(s, x, y, cw, ch, LIGHT); rect(s, x, y, cw, Inches(0.1), col)
        bd = Inches(0.56)
        oval(s, x + Inches(0.26), int(y + Inches(0.26)), bd, bd, col)
        txt(s, x + Inches(0.26), int(y + Inches(0.26)), bd, bd,
            [[(kind, 20, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x + Inches(0.98), int(y + Inches(0.26)), cw - Inches(1.2), Inches(0.3),
            [[("%s  ·  %s" % (code, "REINFORCING" if kind == "R" else "BALANCING"), 9.5, col, True)]])
        txt(s, x + Inches(0.98), int(y + Inches(0.55)), cw - Inches(1.2), Inches(0.34),
            [[(_ellipsis(name, 46), 12.5, INK, True)]])
        cy = int(y + Inches(1.02))
        # the chain must fit BETWEEN the header and the effect band — size the type
        # to the row count so the last link is never hidden behind the band.
        chain_h = int(ch - Inches(1.02) - Inches(0.5))
        csize = 9.5
        if len(chain) >= 5: csize = 8.5
        if len(chain) >= 6: csize = 7.8
        tb = s.shapes.add_textbox(x + Inches(0.3), cy, cw - Inches(0.6), chain_h)
        tf = tb.text_frame; tf.word_wrap = True
        for k, item in enumerate(chain):
            p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
            p.space_after = Pt(0.5)
            r1 = p.add_run(); r1.text = ("↳ " if k else "") + item
            r1.font.size = Pt(csize); r1.font.name = "Arial"; r1.font.color.rgb = INK
        ey = int(y + ch - Inches(0.42))
        rect(s, x + Inches(0.2), ey, cw - Inches(0.4), Inches(0.32), col)
        txt(s, x + Inches(0.2), ey, cw - Inches(0.4), Inches(0.32),
            [[(_ellipsis(effect, 62), 9, WHITE, True)]],
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if note:
        pass
    footer(s); return s


# ---------------------------------------------------------------- 2x2 matrix
def matrix_2x2(title, xlabel, ylabel, quadrants, kicker=None, accent=BLUE, note=None):
    """A real 2x2 prioritisation matrix with labelled axes.
    quadrants: dict with keys 'tl','tr','bl','br' -> (name, colour, [items])."""
    s = head(slide(), title, kicker, kcolor=accent)
    MX, MY = Inches(2.05), Inches(2.0)
    MW, MH = Inches(9.4), Inches(3.92)
    qw, qh = int(MW / 2), int(MH / 2)
    order = [("tl", 0, 0), ("tr", 1, 0), ("bl", 0, 1), ("br", 1, 1)]
    for key, cx, cy in order:
        if key not in quadrants: continue
        name, col, items = quadrants[key]
        x = int(MX + qw * cx); y = int(MY + qh * cy)
        rect(s, x, y, qw, qh, LIGHT, line=LINE)
        rect(s, x, y, qw, Inches(0.09), col)
        txt(s, x + Inches(0.24), int(y + Inches(0.2)), qw - Inches(0.45), Inches(0.34),
            [[(name.upper(), 13, col, True)]])
        tb = s.shapes.add_textbox(x + Inches(0.24), int(y + Inches(0.62)),
                                  qw - Inches(0.45), int(qh - Inches(0.78)))
        tf = tb.text_frame; tf.word_wrap = True
        for k, it in enumerate(items[:4]):
            p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
            p.space_after = Pt(3)
            r = p.add_run(); r.text = "• " + it
            r.font.size = Pt(10); r.font.name = "Arial"; r.font.color.rgb = INK
    # axes
    connector(s, MX, int(MY + MH), int(MX + MW), int(MY + MH), INK, width=Pt(2.0))
    connector(s, MX, int(MY + MH), MX, MY, INK, width=Pt(2.0))
    txt(s, MX, int(MY + MH + Inches(0.12)), MW, Inches(0.36),
        [[(xlabel.upper(), 11.5, INK, True)]], align=PP_ALIGN.CENTER)
    tbv = txt(s, Inches(0.35), int(MY + MH / 2 - Inches(0.9)), Inches(1.5), Inches(1.8),
              [[(ylabel.upper(), 11.5, INK, True)]], align=PP_ALIGN.CENTER,
              anchor=MSO_ANCHOR.MIDDLE)
    try:
        tbv.text_frame._txBody.find(qn('a:bodyPr')).set('vert', 'vert270')
    except Exception:
        pass
    if note:
        ny = int(MY + MH + Inches(0.5))
        rect(s, Inches(0.85), ny, Inches(11.63), Inches(0.44), LIGHT)
        rect(s, Inches(0.85), ny, Inches(0.09), Inches(0.44), accent)
        txt(s, Inches(1.15), ny, Inches(11.1), Inches(0.44),
            [[(note, 10.5, GREY, False)]], anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s


# ---------------------------------------------------------------- edtool card
def edtool_slide(title, name, url, purpose, how, kicker=None, accent=TEAL):
    """An ed-tool introduction — the browser-style card with the live URL."""
    s = head(slide(), title, kicker, kcolor=accent)
    rect(s, Inches(0.85), Inches(1.95), Inches(11.63), Inches(1.5), LIGHT)
    rect(s, Inches(0.85), Inches(1.95), Inches(0.11), Inches(1.5), accent)
    txt(s, Inches(1.2), Inches(2.1), Inches(11.0), Inches(0.44),
        [[(name, 22, INK, True)]])
    # browser chrome
    rect(s, Inches(1.2), Inches(2.66), Inches(10.9), Inches(0.62), WHITE, line=LINE)
    for k, c in enumerate([RGBColor(0xEF, 0x44, 0x44), RGBColor(0xF5, 0x9E, 0x0B), RGBColor(0x22, 0xC5, 0x5E)]):
        oval(s, int(Inches(1.38) + Inches(0.22) * k), Inches(2.87), Inches(0.14), Inches(0.14), c)
    txt(s, Inches(2.2), Inches(2.66), Inches(9.6), Inches(0.62),
        [[(url, 13.5, BLUE, True)]], anchor=MSO_ANCHOR.MIDDLE)
    tiles = [(BLUE, "WHAT IT DOES", purpose), (VIOLET, "HOW YOU'LL USE IT", how)]
    tw = Inches(5.67); xs = [Inches(0.85), Inches(6.81)]
    for (col, lbl, body), x in zip(tiles, xs):
        rect(s, x, Inches(3.68), tw, Inches(2.6), LIGHT)
        rect(s, x, Inches(3.68), tw, Inches(0.1), col)
        txt(s, x + Inches(0.26), Inches(3.88), tw - Inches(0.5), Inches(0.34),
            [[(lbl, 11, col, True)]])
        txt(s, x + Inches(0.26), Inches(4.26), tw - Inches(0.5), Inches(1.9),
            [[(body, 13, INK, False)]])
    footer(s); return s


# ---------------------------------------------------------------- activity brief
def activity_brief(tag, title, case_title, desc, grouping, duration, edtool, kicker,
                   objective=None, accent=TEAL):
    """Activity briefing card tuned for discussion activities (not code labs)."""
    s = head(slide(), title, kicker, kcolor=accent)
    rect(s, Inches(0.85), Inches(1.88), Inches(1.6), Inches(0.44), accent)
    txt(s, Inches(0.85), Inches(1.88), Inches(1.6), Inches(0.44),
        [[(tag, 14, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if objective:
        txt(s, Inches(2.62), Inches(1.88), Inches(9.8), Inches(0.44),
            [[(_ellipsis(objective, 120), 11, GREY, False)]], anchor=MSO_ANCHOR.MIDDLE)
    rect(s, Inches(0.85), Inches(2.5), Inches(11.63), Inches(1.42), LIGHT)
    rect(s, Inches(0.85), Inches(2.5), Inches(0.1), Inches(1.42), accent)
    txt(s, Inches(1.18), Inches(2.64), Inches(11.1), Inches(0.36),
        [[(case_title, 15.5, INK, True)]])
    txt(s, Inches(1.18), Inches(3.04), Inches(11.1), Inches(0.8),
        [[(_ellipsis(desc, 250), 12.5, GREY, False)]])
    tiles = [(BLUE, "TEAM", grouping), (TEAL, "TIME", duration),
             (VIOLET, "TOOL", edtool)]
    tw = Inches(3.71); xs = [Inches(0.85), Inches(4.81), Inches(8.77)]
    for (col, lbl, body), x in zip(tiles, xs):
        rect(s, x, Inches(4.14), tw, Inches(1.62), LIGHT)
        rect(s, x, Inches(4.14), tw, Inches(0.1), col)
        txt(s, x + Inches(0.24), Inches(4.3), tw - Inches(0.45), Inches(0.32),
            [[(lbl, 11, col, True)]])
        bsz = 12.5 if len(body) < 46 else (10.5 if len(body) < 74 else 9.5)
        txt(s, x + Inches(0.24), Inches(4.66), tw - Inches(0.45), Inches(1.0),
            [[(body, bsz, INK, False)]])
    footer(s); return s
