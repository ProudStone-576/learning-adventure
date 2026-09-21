---
name: practice
description: The hands-on lane. Turns a node that was just taught into a tiny runnable script the learner predicts the output of, runs, and then deliberately breaks. Use straight after a node lands in a teach session, or when the learner asks to code something, build something, or says the theory feels abstract.
---

# Practice

Theory gives you the mechanism. Practice gives you the mechanism **surviving contact with a machine that does not care what you believe.**

This lane is not "now do a project." Projects are mostly scaffolding, and scaffolding teaches nothing. Practice here is **one node, one tiny script, one prediction, one deliberate break.** Ten to twenty minutes.

## The one rule: predict before running

The learner states what the output will be **before** the script runs. Every time, without exception.

This is the same engine as the misconception procedure on the theory side — predict, meet the conflict, resolve it — except the computer delivers the conflict instead of you. That is better: it is faster, it is not arguable, and the learner cannot suspect the teacher of steering.

A script that is run without a prediction first teaches almost nothing. The output just looks reasonable and slides past. **Never let them run first and interpret afterwards.**

## The four moves

**1. Generate the data. Never download it.**

The learner writes a formula, then makes data from it plus noise. This is not a shortcut — it is strictly better for learning:

- **You know the true answer**, so "did it work" is checkable in one line: did the fitted numbers come back near the ones you put in?
- **Zero cleaning time.** Real datasets burn 80% of the session on missing values and encodings, none of which is the thing being learned.
- **You can dial one thing at a time** — more noise, fewer rows, a bend in the curve — and watch exactly what changes.

Real data comes later, once the mechanism is solid. It teaches data handling, which is a different subject.

**2. Write it from scratch before touching a library.**

Implement the mechanism in plain numpy first — the loop, the error, the update. Then, and only then, show the one-line library version and let them see it is the same thing.

Done in that order, `LinearRegression().fit(X, y)` becomes shorthand for something they built. Done in the other order, it stays magic forever, and they end up with interface familiarity instead of understanding — which is exactly the failure mode this whole system exists to prevent.

**3. Run it, having predicted the output.**

Numbers on screen. If the prediction matched, the node is real. If it did not, you have found something better than a correct answer.

**4. Break it on purpose.**

This is the highest-value ten minutes in the whole lane, and almost no course does it. Pick the parameter that will fail loudly, ask them to predict the failure, then run it:

- learning rate to 10 → the loss explodes instead of shrinking
- learning rate to 0.0000001 → nothing happens for a thousand steps
- train and test on the same rows → error looks perfect and means nothing
- 3 rows of data, 10 parameters → fits perfectly, predicts garbage
- feed it a pattern the shape cannot express → error plateaus high no matter the data

Every real debugging session they ever have is one of these. Meeting each one deliberately, in a script small enough to see all of at once, is how a broken model later becomes recognisable in thirty seconds instead of two days.

## Writing the script

- **15–40 lines.** If it is longer, it contains scaffolding that is not the lesson. Cut it.
- **One idea per script.** Numbered by node: `code/01-shape-vs-data.py`.
- **No classes, no argparse, no config files.** Top to bottom, readable in one screen.
- **Print, do not plot** — unless the point is genuinely visual. A printed number can be predicted in advance; a chart usually cannot.
- **Seed the randomness** (`np.random.seed(0)`) so a rerun gives the same numbers and a prediction stays checkable.
- **Comment the *why*, never the *what*.** `# squared so big misses hurt more` is worth a line. `# loop over rows` is noise.

## Who types it

Default: **the teacher writes the script, the learner runs and modifies it.** Typing it out is transcription, and transcription is not learning.

The exception is the from-scratch implementation of the mechanism itself — the update loop, the error calculation. That part the learner writes, because writing it is where the mechanism gets tested. Everything around it (data generation, printing) is scaffolding and the teacher supplies it.

## Where this sits in a teach session

It attaches to Phase 4. A node reaches `solid` when the learner has produced it — and running a script they predicted correctly, then predicting its failure correctly, **is** production. It is often a stronger form than explaining it back, because the machine grades it instead of the teacher.

For a learner who builds software, prefer the code form of Phase 4. For a maths-flavoured node with nothing to run, keep the verbal form.

Log the script path in the node's line in `state/learner-model.md`, so a later session can say "run 03 again" instead of rebuilding it.
