# Review queue

`solid` nodes with a due date. Read at session start; rewritten after every drill or deep session.

Line format: `- YYYY-MM-DD | node-name | interval-days | streak`

Scheduling: correct → double the interval (1 → 2 → 4 → 8 → 16 → 32, cap 90 days). Wrong → interval back to 1, streak to 0, due tomorrow, and the node drops to `edge` in the learner model.

## Due

- 2026-09-24 | proxy-signal | 1 | 0
- 2026-09-24 | len-vs-index | 1 | 0
- 2026-09-24 | name-vs-object | 1 | 1
- 2026-09-24 | mutate-vs-rebind | 1 | 1
- 2026-09-25 | chain-of-support | 2 | 1

## Not queued — still `edge`

`return` was missed twice and its final check was never answered. Re-pose that check cold at the start of the next deep session, before any new material.
