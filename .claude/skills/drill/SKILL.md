---
name: drill
description: Short phone-friendly review session — no new material. Pulls nodes due for review from state/review-queue.md, tests recall, reschedules them, and demotes anything that failed. Use when the user asks to drill, review, revise, or wants something short; and whenever they are clearly on a phone.
---

# Drill

A drill is **recall practice on nodes already taught**. It builds nothing new. Its whole job is to stop `solid` nodes from decaying, and to catch the ones that already have.

Target: 3–6 questions, under five minutes, tap-only where possible.

## Run it

1. **Read `state/review-queue.md` and `state/learner-model.md`.**

2. **Pick what to ask.** Everything due today or overdue, oldest due date first. Cap at 6 — if more are due, take the 6 most overdue and leave the rest; they will still be due tomorrow.

   If nothing is due: say so, and offer either a stretch question on the current `edge` node or an early review of the node with the longest interval. Do not invent new material to fill time.

3. **Ask for recall, not recognition, when the answer is short.** Free recall is a much stronger test and a much stronger memory event than multiple choice. Prefer:
   - "Say what X is, in your own words."
   - "Why does X follow from Y?"
   - "What breaks if we drop X?"

   Use `AskUserQuestion` with options only when typing would be painful and the answer is naturally a choice. On a phone that is often the right call — but never make every question multiple choice, or the drill degrades into pattern-matching.

4. **Test the edge, not the label.** A node is understood when its *dependency* is retrievable. Ask "why", "what does this rest on", "what would break" — not "what is the definition of". A recited definition with no derivation is a fail, and gets treated as one.

5. **Grade immediately.** Open with ✓ or ✗. State the correct answer. One or two sentences on *why*, tied to the node it hangs off. Keep it short — this is a drill, not a lesson.

6. **Reschedule each node** in `state/review-queue.md`:
   - Correct → double the interval (1 → 2 → 4 → 8 → 16 → 32 days, cap 90). Increment streak. New due date = today + interval.
   - Wrong → interval back to 1, streak to 0, due tomorrow, **and set the node to `edge` in `state/learner-model.md`**. It is not solid any more.

7. **Close with the tally.** "4/5. `gradient-descent` slipped — queued for tomorrow, and we will re-derive it next deep session." Then stop.

## Rules

- **No new nodes. Ever.** If they ask something that needs new material, note it as a topic for the next deep session and move on. Mixing teaching into a drill turns a five-minute review into an hour.
- **A failed node is information, not a problem.** It located a decayed edge, which is exactly what the drill is for. Say so plainly and reschedule; do not apologise or re-teach at length.
- **Always write state before finishing.** A drill that does not update the queue was wasted — the same nodes come up tomorrow with the same intervals and nothing was learned about decay.
- Two or three sentences per question, max. Phone screen.
