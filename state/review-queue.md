# Review queue

`solid` nodes with a due date. Read at session start; rewritten after every drill or deep session.

Line format: `- YYYY-MM-DD | node-name | interval-days | streak`

Scheduling: correct → double the interval (1 → 2 → 4 → 8 → 16 → 32, cap 90 days). Wrong → interval back to 1, streak to 0, due tomorrow, and the node drops to `edge` in the learner model.

## Due

- 2026-09-22 | proxy-signal | 1 | 0
- 2026-09-22 | chain-of-support | 1 | 0
- 2026-09-22 | name-vs-object | 1 | 0
- 2026-09-22 | len-vs-index | 1 | 0
