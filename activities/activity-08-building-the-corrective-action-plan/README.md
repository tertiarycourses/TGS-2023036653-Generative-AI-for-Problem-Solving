<!-- WSQ - Generative AI for Problem Solving (TGS-2023036653) · Tertiary Infotech Academy Pte Ltd · v21.0 -->

# Activity 8 — Building the Corrective Action Plan

**Topic 2** · A4 · K9 — Develop corrective action plans for shortfalls identified.

| Field | Detail |
|---|---|
| Case study | Meridian Health — from chosen solutions to an auditable plan |
| Duration | 45 minutes |
| Grouping | Teams of 3-5 |
| Tools | ChatGPT / Copilot / Gemini, Pinboard |
| Ed-tool | [Pinboard](https://alfredang.github.io/pinboard/) |

---

## The Scenario

The Clinical Director has approved your four solutions. She now asks the question that separates a good analysis from a delivered result:

"Who is doing what, by when, with what money, and how will I know it worked?"

She also adds a warning from experience: "The last improvement project we ran had a beautiful slide deck and no owner. Six months later nothing had changed and everyone assumed someone else was doing it."

Your team must convert four approved solutions into a corrective action plan that would survive an internal audit — and that a colleague could execute without you in the room.

## The Evidence

*Corrective Action Plan — mandatory components (K9)*

| Component | Why it exists | Failure if missing |
|---|---|---|
| Root cause addressed | Ties the action to the diagnosis | Solution drifts to a symptom |
| Corrective action | The specific thing being done | Vague intent, no execution |
| Owner (named person) | Single point of accountability | Everyone assumes someone else |
| Timeline / milestone | Makes progress checkable | Slips indefinitely, unnoticed |
| Resources required | Budget, people, tools committed | Stalls at first resource conflict |
| Success measure + baseline | Defines what 'worked' means | Cannot evaluate; endless debate |
| Risk and mitigation | Anticipates what breaks it | Surprised by predictable failure |
| Review checkpoint | Forces a decision to continue/stop | Runs on past the point of failure |

## Step-by-Step

1. List your four approved solutions from Activity 7 across the top of a flip chart.
2. Draw the eight CAP components down the side as rows.
3. Fill in 'Root cause addressed' for all four FIRST. If any solution cannot be traced to your diagnosed root cause, challenge whether it belongs in the plan.
4. Assign a NAMED ROLE as owner for each action. Reject any department name. One owner per action — no co-owners.
5. Add timelines with a start, a milestone and a completion date. Use week numbers, not 'Q3'.
6. Cost each action and check the four together fit inside S$250,000.
7. Write each success measure as metric + baseline + target. Cross-check the baseline against your Activity 1 problem statement.
8. Test each measure: can Meridian measure this with data it already collects? If not, either change the measure or add 'establish measurement' as a task.
9. Add the key risk and a mitigation that is itself an action with an owner — not a hope.
10. Set a review checkpoint for each action and state the DECISION to be made at it.
11. Run the GenAI corrective action plan prompt from the slide.
12. Act on the AI's three flags: sequence the dependent actions, rebalance any overloaded owner, and fix any unmeasurable success measure.
13. Post the completed plan to https://alfredang.github.io/pinboard/ and present one row in full to the room.

## The GenAI Prompt

Copy this into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details.

```text
You are an execution-focused planning assistant. Convert each approved solution into a corrective action plan row. Be concrete and brief — no theory.

For EACH solution, produce exactly these fields:
- Root cause addressed (link back to the diagnosis)
- Corrective action (one specific sentence)
- Owner (a job title, not a department)
- Timeline (start, key milestone, completion)
- Resources (budget in S$, people, tools)
- Success measure (metric + baseline + target)
- Key risk + mitigation
- Review checkpoint (date and the decision to be made at it)

Then flag, in a separate section:
1. Any two actions that depend on each other and must be sequenced
2. Any owner who appears on more than two actions (overload risk)
3. Any success measure that cannot actually be measured with data the organisation already has

Approved solutions: [paste your four here]
Root cause: 44% phlebotomist turnover leaving 40% of the 07:00 roster untrained, causing 14-min draws vs 6-min, 31% appointment overruns and 23% of samples missing the 09:45 courier.
Budget: S$250,000 over 12 months.
```

## Discussion Questions

1. Complete all eight components for each of your four actions. Which component did your team find hardest to fill honestly, and what does that reveal?
2. Every owner must be a named role, not a department. Why does 'Operations' fail as an owner where 'Centre Operations Manager' succeeds?
3. Check your success measures against the baseline in your original problem statement. Can each one actually be measured with data Meridian already collects? Which cannot?
4. The AI flagged dependencies between actions. Which two of your actions must be sequenced, and what breaks if you run them in parallel?
5. Identify the biggest risk across your whole plan. Is your mitigation a real action with an owner, or a hope?

## Self-Check — Is Your Output Finished?

Your CAP is audit-ready when: all eight components are complete for all four actions; every owner is a named role and no role owns more than two actions; every success measure has a metric, a baseline number and a target number; every measure is obtainable from data the organisation already has (or has an explicit task to start collecting it); dependencies are sequenced; every mitigation is an action with an owner; and every checkpoint names a decision. The real test: hand the plan to another team and ask them to execute row one without asking you a single question.

---

*See [debrief.md](debrief.md) for the trainer debrief and expected answers.*
