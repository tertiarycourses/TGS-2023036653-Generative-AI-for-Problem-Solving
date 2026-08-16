<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 7 — Converging: Impact-Ease Matrix and Weighted Decision Matrix

**Topic 2** · A5 · K4, K6 — Shortlist and evaluate the most viable ideas using decision-making techniques.

| Field | Detail |
|---|---|
| Case study | Meridian Health — choosing four from twenty |
| Duration | 50 minutes |
| Grouping | Teams of 3-5 |
| Tools | ChatGPT / Copilot / Gemini, Pinboard |
| Ed-tool | [Pinboard](https://alfredang.github.io/pinboard/) |

---

## The Scenario

You now hold twenty-plus candidate solutions from Activity 6. The Clinical Director will fund approximately four, inside S$250,000 over 12 months.

Two members of your team are already advocating loudly for their favourite ideas and the discussion is circling. This is exactly the moment where teams either make an evidence-based decision or default to whoever is most senior or most persistent.

Your job is to convert the board into a defensible shortlist using two complementary tools: a fast Impact-Ease screen, then a weighted decision matrix on the survivors.

## The Evidence

*Meridian Health — agreed decision criteria and weightings*

| Criterion | Weight | Scoring guidance (1-5) |
|---|---|---|
| Impact on root cause (retention/training) | 35% | 5 = directly fixes the root cause |
| Speed to measurable effect | 20% | 5 = effect visible within 8 weeks |
| Cost within S$250k envelope | 20% | 5 = under S$25k |
| Clinical/regulatory risk | 15% | 5 = no MOH implication at all |
| Staff and client acceptance | 10% | 5 = actively welcomed by both |

## Step-by-Step

1. Bring the full idea board from Activity 6. Remove any duplicates by merging them.
2. Draw the Impact-Ease matrix on a flip chart with four labelled quadrants.
3. Place every idea in a quadrant as a team. Where you disagree, place it on the line and move on — do not stall.
4. Discard the Thankless Tasks. Set the Fill-Ins aside as 'do if free capacity'.
5. BEFORE scoring anything, agree the five criteria weights as a team. Write them down. This prevents arguing about scores when you actually disagree about weights.
6. Build the weighted decision matrix for the surviving Quick Wins and Big Bets. Score each criterion 1-5.
7. Compute the weighted totals and rank.
8. Run the GenAI convergence prompt from the slide with your actual list pasted in.
9. Compare the AI ranking to yours. Investigate every place they disagree by more than two positions.
10. SENSITIVITY TEST: change the speed weight from 20% to 40% and re-rank. Record whether the winner changes.
11. Select your final FOUR as a PORTFOLIO — check they do not all attack the same cause, and check for redundancy.
12. Prepare a two-minute recommendation to the Clinical Director: the four, the total cost, the criteria, and the one thing you are still leaving unaddressed.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
Act as a decision analyst. I will give you a list of candidate solutions. Do NOT add new ideas.

STEP 1 — Classify every solution on an Impact vs Ease matrix as exactly one of:
- Quick Win (high impact, easy)
- Big Bet (high impact, hard)
- Fill-In (low impact, easy)
- Thankless Task (low impact, hard)
Give a one-line reason for each placement.

STEP 2 — Take only the Quick Wins and Big Bets and score them in a weighted decision matrix:
- Impact on root cause (weight 35%)
- Speed to measurable effect (20%)
- Cost within a S$250k envelope (20%)
- Clinical/regulatory risk (15%)
- Staff and client acceptance (10%)
Score each 1-5, show the weighted total, and rank them.

STEP 3 — Recommend the best FOUR as a portfolio, and explicitly state:
- why this combination is stronger than the top four individual scores
- which two solutions overlap or make each other redundant
- what the portfolio still leaves unaddressed

Solutions: [paste your team's list here]
```

## Discussion Questions

1. Place all your ideas on the Impact-Ease matrix. Which quadrant is most crowded, and what does a crowded Fill-In quadrant tell you about how your team was thinking?
2. Run the weighted matrix. Did the top-scoring solution match your team's gut favourite from Activity 6? If not, what did the weighting expose?
3. Change the weight on 'Speed to measurable effect' from 20% to 40% and re-rank. Does the winner change? What does that sensitivity tell you about how robust your recommendation is?
4. The AI recommended a portfolio of four. Explain why the best four INDIVIDUAL scores are not automatically the best four TOGETHER.
5. Consensus fatigue is when a team accepts a weak option just to end the discussion. Where in this activity was your team most at risk of it, and what stopped you?

## Self-Check — Is Your Output Finished?

Your shortlist is defensible when: every surviving idea sits in a named quadrant; the weighted matrix shows criteria, weights, scores and totals; you have run at least one sensitivity test and can state whether the winner held; your four are a portfolio rather than the top four scores; the total cost fits inside S$250k; and you can name one thing the portfolio does NOT fix. If you cannot explain to the Clinical Director why idea #5 lost, the matrix has not done its job.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
