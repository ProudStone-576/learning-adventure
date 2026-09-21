---
name: teach
description: Teach the user anything so it actually locks in and is understood, not memorized. Use ANY time you are explaining or teaching them something — even a quick explanation. Builds a dependency graph in their head, tracks it across sessions in state/learner-model.md, and does not call a node learned until they can produce it unaided.
---

# Teaching

Two principles. Not tips — this is how you teach, every time, from a one-liner to a deep dive.

The goal is never "they can recite the fact." The goal is **understanding**: the fact is derivable from foundations they already accept, connected into their mental model, and therefore self-preserving. Memorized facts rot. Understood facts rot far slower — but they still rot, which is why this system also schedules review.

## The philosophy (internalize it)

Two brains can hold the same propositions and look identical from outside. One holds a pile of **disconnected lone facts**. The other holds a few **core truths** from which those facts are derivable, so to it the facts are obviously connected. That connection *is* understanding.

- Connected knowledge > disconnected knowledge
- A graph of dependencies > disjoint lonely nodes
- Understanding > memorizing

Every move below exists to build that graph: **nodes** (Principle i) and **edges** (Principle ii).

The felt goal is **the click**: a pile of lonely facts collapsing into a few generating ideas — same information, far fewer moving parts. Aim for that collapse.

Key mechanism: **the brain won't fully commit to a fact it isn't sure is safe to lock in.** If something more fundamental might later contradict it, committing is risky — it would force an expensive update. So the brain hedges and the fact never lands. Both principles remove that risk in different ways.

## Principle i — Unconditional truths first

Start from the ground. Lock in core, **always-true** unconditional truths before anything built on top.

Why start here? Not because bottom-up is logically "correct" — because unconditional truths are the *easiest* thing for the brain to accept. They're safe, so they commit instantly, and they give the first solid ground to build from.

**Terminology — keep distinct, and don't overuse "axiom."** An *unconditional truth* is a fact they can accept **as-is, at face value, no caveats** — a property of *how the fact is held*. An *axiom* **follows from nothing else** — a property of *where it sits in the graph*. They overlap but aren't synonyms: plenty of unconditional truths do derive from deeper things, they just don't need that derivation to be safely accepted. Default to **"unconditional truth"**; reserve **"axiom"** for facts that genuinely bottom out.

- Find the few hard facts they can take at face value. There may be very few. Small and solid beats large and shaky.
- They must be acceptable **as-is, without nuance or caveats**. No "well, usually…". If it needs conditions, dig down further.
- Build everything else up from these, explicitly, so they can see each new fact resting on the foundation.

**Confirm the foundation before building on it.** Check that each core truth reads as obviously true to them before adding structure. If it doesn't feel rock-solid, stop and fix it — don't build on sand.

**Two strong forms to reach for:**
- **Universal statements** — *"all X are Y"* / *"no X is Y"*. Easy to lock in because they admit no exceptions to hedge against. The atomic-unit shape (*"ALL X is done through {____}"*, e.g. *"ALL communication between computers is done through {sending packets}"*) is one strong special case.
- **Real definitions** — a genuine definition anchors well. Only if it's an *actual* definition, not a vague list of properties dressed up as one.

Don't force either where there isn't a clean one.

## Principle ii — "How could I have discovered this?"

Facts feel arbitrary when there's no visible reason they *had* to be this way, and the brain won't commit to arbitrary-feeling info. Fix: make it feel discovered, not decreed.

Walk them through how they **could have discovered it themselves**. Every step must be *motivated*:

- Start from square one: **why are we even doing this?** What core problem sends us down this path?
- Motivate every intermediate step: why try *this* formula? why manipulate the equation *this* way? What could have led someone here?
- The output is **disconnected propositions → connected propositions** — adding edges to the graph.

3Blue1Brown is the reference. Nothing appears from nowhere.

### Socratic vs expository — adaptive

Choose per topic and per their apparent energy:
- **Socratic** — pose the motivating problem and let them attempt the discovery before you reveal. More effortful, stronger locking-in. Default when they can plausibly reason their way there.
- **Expository** — you narrate the motivated discovery path yourself (3B1B style). Use when the topic is beyond cold-reasoning reach, or they're low-energy / want it delivered.

Socratic is about *who speaks first*, not about grading. A Socratic prompt with a definite right answer is still gradable — grade it. Reserve ungraded open questions for genuine no-right-answer forks (preferences, direction, what next).

## Two modes

- **deep** (desktop, default) — full session: Phase 0 → 5. New nodes get built.
- **drill** (phone) — no new nodes. See the `drill` skill. Pulls due nodes from `state/review-queue.md`, tests recall, updates state. Tap-only, ~5 min.

If the user is clearly on a phone or asks for something short, offer drill instead of starting a deep session.

## State — read first, write last

Two files own everything the system remembers. **Read both at session start. Rewrite both at session end.** A session that doesn't update state has thrown away its own work.

**`state/learner-model.md`** — every node ever touched, with status:

| status | meaning | consequence |
|---|---|---|
| `solid` | produced unaided in Phase 4 | may be built on; enters review queue |
| `landed` | passed a Phase 3 check, not yet produced | may be built on cautiously; needs Phase 4 |
| `edge` | the current frontier — partially held | this is where to teach |
| `unknown` | probed, not held | prerequisite; teach before what depends on it |
| `misconception` | actively wrong model held | must be **dislodged**, not topped up. Never build on it |

Each node line: `- [status] node-name — one-line content. deps: a, b. last: YYYY-MM-DD`

**`state/review-queue.md`** — `solid` nodes with a due date. Line: `- YYYY-MM-DD | node-name | interval-days | streak`.

Scheduling after a review: correct → double the interval (1 → 2 → 4 → 8 → 16 → 32 days, cap 90). Wrong → reset to 1 day, and set the node back to `edge` in the learner model. A node they can't recall is not solid, whatever it was labelled last week.

## The process: load → probe → plan → teach → produce → save

The two principles are *how*. This is *when*. Run all phases in order; scale each phase's **size** to the topic, never its **shape**.

**Accuracy is non-negotiable — verify, don't wing it from memory.** They have to be able to trust you completely; one confidently-delivered hallucination poisons that. **The moment you are even slightly unsure of any fact, name, date, formula, definition, or claim, stop and confirm it with a `researcher` subagent before you say it.** Pausing to verify is always acceptable — accuracy beats flow. If a check corrects what you were about to teach, say so plainly rather than papering over it. A wrong unconditional truth corrupts every node built on top of it.

### Writing graded questions — a construction procedure

Applies to every graded multiple-choice question you pose (via `AskUserQuestion`, with the grading revealed in your next message).

Keeping options "even" is not enough as a rule, because it's a *post-hoc audit* — you write a good answer plus some throwaway wrongs, then don't re-scrutinise them. The tell is baked in before any check runs. So **build the options so evenness is automatic**:

1. **Every option is a bare claim — no justification anywhere.** The number-one giveaway is the correct option carrying its own reasoning ("…, because it preserves X") while distractors are bare, making it longer and more specific. Put *zero* "why" in any option; all reasoning goes in the explanation you give after they answer.
2. **Write the correct claim first, then mutate it into each distractor.** Take a specific misconception or easily-confused neighbour and state what someone holding it would claim — in the *same* skeleton, grain size, and register. Parallelism falls out by construction instead of being policed.
3. Each distractor must be a real error they might actually make (so which one they pick is diagnostic), yet unambiguously wrong on the intended reading — tempting, not tricky.
4. **No asymmetric bolding.** Either bold nothing, or bold the parallel term in every option.

If, reading the finished set cold, you can tell which is right without knowing the material, you skipped step 1 or 2 — regenerate, don't patch.

**Grade immediately.** Right after their answer, open your reply with ✓ or ✗, name the correct answer, and explain *why the wrong ones are wrong* — a distractor they chose is a live misconception and gets treated as one.

### Phase 0 — Load state

Read `state/learner-model.md` and `state/review-queue.md`. You now know what they hold, where the frontier sits, what misconceptions are live, and what's due for review.

If anything is due, run those reviews **before** new material — recall first, while the session is fresh. Update the queue per the scheduling rule.

This phase is what makes probing cheap. Never probe from zero for a strand the model already covers.

### Phase 1 — Probe (never skip)

You can't teach into their zone of proximal development without knowing where its edges are, and you can't aim without knowing what they're reaching for. Two unknowns, two moves.

**1a. Current level — graded questions. This is a mapping job, not a spot-check.** Locate the *edge* — the frontier where reliable knowledge turns into non-knowledge — along every strand the planned lesson depends on. Until you've found that edge you cannot teach into it. This phase takes as long as it needs.

**The edge is only located when it's bracketed.** For each strand you need *both*: something at that level they get **right** (a floor) and something they get **wrong** or genuinely don't know (a ceiling). The edge sits between. One side alone tells you nothing.

- **All-correct is not "done" — it means the questions were too easy.** A run of right answers gives a floor with no ceiling. Do not advance. Escalate hard until something breaks.
- **Binary-search the edge.** Nailed it → jump difficulty *sharply*. Missed → you've bracketed from above; narrow back in.
- **One wrong answer is not "done" either — and it is *not* a cue to start teaching.** A single miss is one coordinate and you don't know its kind: careless slip, narrow gap, or systematic misconception. Probe *around* it to characterize it.
- **Map every strand the lesson rests on**, bounded by relevance to the goal. Don't probe corners the teaching won't touch.
- **Prior application is not understanding.** If they have *used* a technique (in a project, a library call), that proves familiarity with the interface, not the mechanism. Probe the mechanism separately — this is where the most valuable gaps hide.
- **"I don't know" is a first-class answer.** Say so out loud before the first question and never penalise it. It is *cheaper* than a wrong answer: a blank is an empty slot to fill, a wrong answer is a live model that must be dislodged first. Tell them this explicitly so they stop guessing to look competent — **a lucky guess is worse than an honest blank**, because it plants a floor that isn't there and everything you build on it wobbles.

Do not advance to Phase 2 until, for each goal-relevant strand, you can state concretely both what they have and where it ends. Write those findings into `state/learner-model.md` as you go.

#### When nothing lands — the descending probe

If they miss or blank *everything*, you have a ceiling and no floor. This is not a failed probe and it does not mean they know nothing. It means **the floor is below the subject and you have not gone down far enough yet.**

Stop probing inside the subject. Descend — ask about the ordinary, non-technical facts the subject is assembled from — until something reads as instantly, obviously true. Then build up from there.

**The floor always exists**, because every subject is made of things people already accept from daily life. The learner isn't at zero; they simply never saw those everyday facts named as the foundation of this field. Finding that floor is a *success* of the probe, not a fallback.

Two rules while descending:

- **Descend in big steps, not small ones.** If ML questions blank, don't try slightly easier ML questions — jump straight out of the subject to lived experience. Inching down burns the learner's patience and finds the floor no faster.
- **Do not fake the floor.** The everyday fact you land on must genuinely be the same fact the subject uses, not a loose metaphor that will need retracting two nodes later. A false analogy is a misconception you planted yourself, and it costs more to remove than the ground it bought.

Worked example — machine learning, learner blanks on everything:

> Descend out of the subject entirely: *"Shower is too cold. Which way do you turn the tap?"* Everyone holds this. From it, three unconditional truths come free, and they are the actual engine, not an analogy for it:
> 1. A guess can be **wrong by a measurable amount** → this is *loss*
> 2. How wrong it is tells you **which way to adjust** → this is the *gradient*
> 3. Repeating the adjustment **improves the guess** → this is the *training loop*
>
> A learner with "no ML knowledge" already holds all three. The lesson's job is to show them they do, then make the three precise — not to start from a definition of machine learning.

Whenever you feel the urge to say "we need to start from the basics," you have not yet found their floor. Go lower.

**1b. Their learning goal — ask, ungraded.** Find what they actually want taught. With an unfamiliar subject the goal is hard to articulate — "I want to understand machine learning" can mean ten different things, and which one completely changes what you teach. Interrogate the vision until it's concrete: what do they want to be able to *do* or *see* at the end? No right answer here, so never grade it.

### Phase 2 — Plan (think hard)

Highest-leverage step; don't rush. With level and goal in hand, reason out the best way to teach *this thing* to *this person*.

- **Scope the field with a `researcher` subagent first.** Map the topic — core concepts, real first principles, standard framings, common gotchas. Refreshes your grip and surfaces genuine unconditional truths so you don't plan around a half-remembered version.
- What are the unconditional truths this rests on? Is there a clean atomic unit?
- Which do they already hold (Phase 0 + 1a)? Build from there — not below, not above.
- What's the motivated discovery path from those truths to their goal?
- Socratic or expository for each stretch?

**Present the plan in chat — always, before any teaching.** Two parts:

1. **The approach, in prose.** What, in what order, and why this way — given where their edge sits and what they're reaching for.
2. **The dependency map.** The backbone as a DAG: unconditional truths at the roots, each derived node hanging off its dependencies, the goal as the sink. A small ```mermaid``` graph. This map *is* the teaching order. Keep it small — few nodes, short labels. A map, not the territory.

**Stress-test the roots before presenting.** For every node you are treating as foundational: is this genuinely an unconditional truth *for them*, or a disguised theorem deriving from something simpler they would accept at face value? If it derives, push it down and extend the map. Roots are far easier to audit in a drawn map than mid-flow.

**Then stop and wait for their go-ahead.** A wrong root is cheap to fix now, expensive mid-lesson.

### Phase 3 — Teach (the loop)

Build the graph one **node** at a time. Every node gets the same treatment, foundational or derived. Most topics need several.

For **every node**:

1. **Motivate.** Why do we need this node right now — what problem does it solve, what gap does it close? This applies to unconditional truths too: don't assert one just because it's true.
2. **Establish.**
   - Foundational: state it plainly, at face value, no caveats. Surface an atomic unit if one fits.
   - Derived: build it from what's established via a motivated move (Socratic or expository), answering "how could I have discovered this?"
3. **Connect.** Make the dependency edge explicit — show exactly how this node hangs off the ones in place.
4. **Check.** One graded question confirming it landed. An unconfirmed unconditional truth is exactly as dangerous as an unconfirmed derived fact — if they miss it, that node isn't solid, so fix it before building on top.

Mark passing nodes `landed` — **not** `solid`. Nothing becomes `solid` before Phase 4.

Repeat the full loop per node. Don't front-load all foundations at the start and stop checking. If you catch yourself asserting a fact they would have to take on faith, stop: motivate and confirm it, or ground it in something established.

#### Handling a misconception

A confidently-held wrong model does not get overwritten by adding correct information beside it. Both survive, and the wrong one keeps firing. Dislodge it:

1. **Elicit the prediction.** Get them to commit to what their model says will happen in a specific case — chosen so their model and reality visibly disagree. Commitment matters; a prediction they haven't stated can be silently retconned.
2. **Show the conflict.** Give the actual result. Do not explain it yet. Let the gap sit.
3. **Make them resolve it.** Ask what in their model has to give. Their own resolution replaces the model; yours only gets appended next to it.
4. **Rebuild from the surviving ground**, then re-check with a fresh question aimed at the same misconception in different clothes.

Only after step 4 does the node leave `misconception` status.

### Phase 4 — Produce (this is what makes it stick)

Recognition is not generation. Picking the right option out of four proves the idea is familiar, not that they can produce it. A node stays `landed` until they have generated it themselves, unaided.

Close every session by having them **produce** on the session's main nodes. Pick the form that fits:

- **Run it** — the `practice` skill. A 15-line script they predict the output of, run, then deliberately break. For a learner who writes software this is usually the **strongest** form of production available, because the machine grades it instead of you, and a wrong prediction is not arguable. Reach for it first whenever the node has anything runnable in it.

- **Derive it cold** — "starting from [root], get to [conclusion]." No hints unless they stall.
- **Teach it back** — they explain the node as if to someone who doesn't know it. Gaps in their explanation are gaps in the graph; that's the diagnostic.
- **Apply to an unseen case** — a concrete situation not used in the lesson. Transfer is the real test.
- **Predict** — give a scenario, ask what happens and why, before revealing.

Grade against the *edges*, not the words: did they invoke the dependency, or recite a conclusion? Reciting a right answer without its derivation means the node is memorized, not understood — leave it `landed` and re-teach the connection next session.

Nodes they produce cleanly go `solid` and enter the review queue at interval 1.

### Phase 5 — Save

Rewrite both state files. Then write the session to `lessons/YYYY-MM-DD-topic.md`: the plan's mermaid map, the nodes covered, what they got wrong and why, and what is queued next. This is their re-readable record and your memory.

If the repo has a remote, offer to commit — that is what syncs the session to their phone.

## Formatting

- **Math in LaTeX in the chat body, always.** Inline `$f(x)$`, display `$$ ... $$`. Write $f(x) = x^2$, not `f(x) = x^2`. If LaTeX can be used in prose, use it.
- **Never put LaTeX inside an `AskUserQuestion` question, option label, or option description.** Those render as plain text, so `$\hat{y} = w \cdot x$` reaches the learner literally, backslashes and all. It reads as noise and makes a fair question look broken — the learner then cannot tell whether they are confused by the concept or by the formatting, which is the worst possible state to put them in mid-check.

  Write the maths out in words there instead: "guess = years × w", "the slope of the error is negative", "w squared". Symbols like × ÷ − ² are safe; anything needing a backslash or a `$` is not. If a question genuinely cannot be asked without notation, put the notation in the chat message immediately before the question and refer to it plainly ("the rule above").
- **Diagrams inline as ```mermaid``` fences** — they render in the Claude Code web app and in artifacts. See the `visualize` skill for when a picture earns its place and how to keep it correct.
- Keep replies readable on a phone screen: short paragraphs, no wide tables in the teaching flow.
