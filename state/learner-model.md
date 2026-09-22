# Learner model

Every node ever touched, with status. Read at session start, rewritten at session end.

Line format: `- [status] node-name — one-line content. deps: a, b. last: YYYY-MM-DD`

Statuses: `solid` (produced unaided) · `landed` (passed a check, not yet produced) · `edge` (current frontier) · `unknown` (probed, not held) · `misconception` (wrong model held — dislodge, never build on)

## Learner profile

- Current subject: **machine learning**. Roadmap: stages 0–6, agreed 2026-09-07.
- Goal: all four of — build/train models, understand LLMs internally, read papers, understand his own shipped ML code. All share the same roots, so build roots then branch.
- Builds real software: Next.js web apps, native Android in Kotlin/Compose, data/analysis repos. Comfortable with code, APIs, shipping.
- **Has applied ML-adjacent techniques without holding the mechanism** — isolation forest, z-score, entropy scoring (Aethon); trend modelling (WNA ozone). Confirmed as interface familiarity, not understanding.
- **Wants plain simple English, not compressed/terse style.** Asked for this explicitly 2026-09-07. Honour it — short sentences, no jargon without unpacking.
- **Wants vocabulary introduced very slowly, a few terms per session, each defined in plain words before use.** Asked 2026-09-21, to build a tech dictionary he actually owns. Running glossary lives in `state/glossary.md` — append new terms there every session and reuse them deliberately so they repeat.
- **Hedges on answers he has already reasoned out correctly.** 2026-09-21: produced the right trace mid-sentence ("backup is pointing at the same list"), then talked himself back out of it and wrote "not sure". On being asked to commit, he committed correctly. Repeated 2026-09-21 on the `wipe`/`empty` check — answered `b` confidently, then "not sure about a, does it add a space or something", despite having just read the rule that settles it. **He hedges specifically when the answer requires applying a rule rather than recalling a fact.** Point him back at the rule; do not restate it for him. **Always make him commit to one answer before revealing anything** — the machine grading him is what fixes this, not reassurance. Confidence, not knowledge, was the failing half.
- Interrupts to ask meta-questions about the method. This is good; answer fully, it is how he builds trust in the process. But do not let the session become entirely meta — return to teaching.
- Front-loaded multiple-choice probing did not work for him: he paused three consecutive probe rounds. **Probe inside the lesson instead of before it.** One check per node, embedded.

## Nodes

### Stage 0 — the chain
- [solid] proxy-signal — when the direct measurement is unavailable, substitute an observable that moves with it. **Produced unaided**: given "you cannot feel the water", he invented "turn until the mirror fogs" with no prompting. deps: chain-of-support. last: 2026-09-07
- [landed] chain-of-support — measure error → get direction → repeat; each rests on the one before, cutting the top kills all of it. **Failed recall 2026-09-21** (13 days overdue): broken-gauge factory case, answered "yes he can still improve, with many tries" — the `more-data-fixes-everything` misconception in fresh clothes. Took two conflict rounds to re-derive; named the missing error signal himself, but kept attaching "yes" to it (confused *passing through* the target with *arriving at* it). Resolved once told that stopping requires knowing you are there. Still `landed`, not solid. deps: —. last: 2026-09-21
- [landed] weak-proxy-cost — a proxy that loses magnitude and direction thins the chain rather than breaking it; you can still learn, slowly, and you cannot detect overshoot. deps: proxy-signal. last: 2026-09-07
- [edge] why-gradients-exist — direction is discoverable by trial at one test per number, which is impossible at millions of parameters; the gradient gives direction for all numbers at once. Taught expository, **not yet checked**. Check it before building Stage 1 on it. deps: chain-of-support. last: 2026-09-07

### Stage 1 — make it numeric
- [landed] model-is-function-with-parameters — a model is a function; the numbers inside it are parameters; "training" means searching for parameter values that lower the error. 175B parameters = 175B taps, same idea as one w. deps: chain-of-support. last: 2026-09-08
- [landed] capacity-vs-parameter-values — two independent failures: the shape cannot express the pattern (fix by changing the rule) vs the tap is set badly (fix by adjusting/more data). Derived the intercept b himself-adjacent: watched "guess = years × w" forced through the origin and saw why a second parameter is needed. deps: model-is-function-with-parameters. last: 2026-09-08

### Track 1 — systems (added 2026-09-21)
Goal he stated: build an LLM router framework unaided, read code he didn't write, clean vibe code, get hired. Root node is predict-before-run; full map in `lessons/2026-09-21-predict-before-run.md`.

- [landed] name-vs-object — `b = a` makes a second name for the same list, so changing it through `b` changes `a`; `b = list(a)` makes a real copy, so it does not. Numbers are not shared this way. Produced unaided twice at top level — **then failed transfer into functions the same session**, so it was marked `solid` too early and has been downgraded. Top-level fluency is not the same node as understanding why. Re-test in a deep session, not a drill. deps: —. last: 2026-09-21
- [solid] len-vs-index — length is a count and starts at one; index is a position label and starts at zero. A 3-item list has length 3 and last index 2. Arrived via `scores[total - 1]` unaided. deps: —. last: 2026-09-21
- [landed] mutate-vs-rebind — `.append()` / `.clear()` reach through the name and change the shared thing, so everyone pointing at it sees the change; `=` never touches the thing, it points the name somewhere else. A function gets its own **private names**, so moving one changes nothing outside, but changing a shared object is visible everywhere. Reached it via `n = n + 1` vs `items.append(99)`. Still `landed` — he applied it correctly on the fresh-clothes check (`wipe` vs `empty`) but only after being pointed back at the rule. deps: name-vs-object, functions. last: 2026-09-21
- [landed] functions — a named block of code, run on demand with arguments. Taught only as far as the router needs: `def`, argument, call. **`return` not yet introduced.** deps: —. last: 2026-09-21
- [landed] predict-before-run — execution is mechanical, so output is derivable by tracking values line by line; the discipline is refusing to add anything the code did not say. **Not solid — the habit is unproven.** His failure mode showed twice in one session: he read `print(a, x)` as printing a *length* that appears nowhere in the code, and read improvement into a factory with no measuring instrument. Same move both times — filling a gap with something plausible instead of checking the page. Named for him as bookkeeping, not intelligence. **Surfaced a third time later the same session**: told `count` printed 5 not 6, he invented "print(count) just pulled the variable rather than calling the function" — an explanation with nothing on the page behind it. Killed by applying his own rule to the line he got right, which predicted the wrong output. Needs several more reps on unseen code. deps: name-vs-object, len-vs-index. last: 2026-09-21

### Live misconception
- [misconception] more-data-fixes-everything — believes a bad model is a data-quantity problem. **Confirmed systematic, not a slip: hit twice in different clothes.** First on "best possible w found, guesses still bad" (answered "too little data"), then again after a full explanation, on the flattening-salary case (answered "yes, enough data finds w and b"). Note that plain telling already failed once — only the predict → conflict → resolve procedure will move it. Mid-dislodge as of 2026-09-08, see the PAUSED section below. **2026-09-21: surfaced a third time**, unprompted, in a non-ML case (broken factory gauge → "he will have to get many tries"). He abandoned it within that case once shown 500 rods no closer after a week. That is real progress but it is one case, not the general model — **do not clear this until he is re-checked in fresh clothes.** deps: capacity-vs-parameter-values. last: 2026-09-08
- [misconception] iforest-mechanism — believes isolation forest flags a point because it is **far from the mean**. It has no mean, no distance, no loss. Almost certainly z-score and iForest collapsing into one "far from normal" idea, since his Aethon project ran both side by side. **Scheduled for dislodge in Stage 3** via predict → conflict → resolve, using the two-cluster case (point at 50 between clusters at 0 and 100 has a z-score near zero yet is the most isolated point present). Do not pre-empt it; the conflict is the teaching. deps: —. last: 2026-09-07

### Not yet probed
- [unknown] derivative-as-slope — whether $\frac{dL}{dw}$ is usable, not just recognisable. Probe was drafted and never answered. **Gate for Stage 1** — gradient descent cannot be derived without it, only asserted.
- [unknown] overfitting — whether it is held as "memorised the training set" or the vaguer "model is bad".
- [unknown] parameters-vs-hyperparameters — never probed.

## PAUSED MID-DISLODGE — resume word: "Stonewall"

Session paused 2026-09-08 partway through dislodging `more-data-fixes-everything`. **Do not restart the topic from the beginning when he says Stonewall** — pick up at the exact step below, or the conflict loses its force.

Where we stopped — step 1 of predict → conflict → resolve:

- Setup given: true salaries are 0 yr → 40,000, 10 yr → 90,000, 30 yr → 97,000 (flattening). Fitted straight line is **guess = 40,000 + 5,000 × years**.
- He was asked to compute the prediction at 30 years. Correct arithmetic: **190,000**. He did not answer.
- **Next move on resume:** get him to commit to that number (190,000), then reveal the truth is 97,000 — a miss of 93,000, nearly double. Do not explain the gap. Ask him what has to give: the line was *exactly right* at 0 and 10 years and still catastrophically wrong at 30, so "not enough data" has nowhere left to stand. Let him state the resolution himself.
- Then rebuild: capacity is fixed before training; data searches inside the ceiling, it does not raise it. Re-check with a third set of clothes.

## Resume words

- **"begon"** — resume Track 1 where 2026-09-21 left off: re-test `name-vs-object` and `mutate-vs-rebind` cold, then `return`, then what an LLM call really is.
- **"Stonewall"** — resume the paused Track 2 dislodge, mid-step. See the PAUSED section.

## Next session

**Track 1 is now the primary lane** (his call, 2026-09-21 — he wants hireable capability and a router framework he built himself). Track 2 (ML) continues at low burn via `drill`, not as a project.

Track 1 order from here: more `predict-before-run` reps on code he has not seen → what an LLM call really is (tokens, context window, cost, latency) → types as design (one provider interface, two implementations) → routing as a decision function → eval harness → failure handling.

Rule he set and I agreed to: **AI may explain anything, but may not produce the artifact.** Do not write his files for him on this track.

Still open from Track 2: `why-gradients-exist` was taught expository and never checked. `derivative-as-slope` remains the ungated prerequisite. Resume word for the paused dislodge is still "Stonewall".
