# 2026-09-21 — predict-before-run

First session of Track 1 (systems). Also the first overdue review run.

## Why this node

He asked to be made capable of four things: designing an LLM router framework, reverse-engineering a model from a paper without AI, getting hired, and cleaning up vibe code. They are not four. They share one root — being able to say what code or a system will do *before* running it. Everything else is built on that.

```mermaid
graph TD
    A["predict-before-run<br/>read code, state the output"] --> B["what an LLM call really is"]
    A --> C["types as design"]
    B --> D["cost / latency / quality as numbers"]
    C --> E["router = a decision function"]
    D --> E
    E --> F["eval harness"]
    F --> G["failure handling"]
    G --> H["the framework, built by him"]
    A --> I["read code he didn't write<br/>= clean vibe code, pass interviews"]
    style A fill:#2d3748,color:#fff
    style H fill:#2d3748,color:#fff
```

## What happened

**Review — `chain-of-support`, 13 days overdue: failed.**
Factory case: the gauge that measures rod length breaks, dial still works. Can the worker still improve? He said yes — "he will have to get many tries", learning by feel and timing. That is `more-data-fixes-everything` surfacing a third time, now outside ML entirely.

Took two conflict rounds. The first scenario I built was flawed — I bolted the dial to remove drift, which also removed his ability to adjust at all, so "he can't dial" became a fair reading. My error; rebuilt it with a freely-turning dial and no measuring instrument anywhere.

He then named the right thing himself — "no way to tell if it was the right length" — but kept attaching **yes** to it. The residual gap was definitional: he treated *passing through* the target as *arriving at* it. Closed by pointing out that arriving requires stopping, and stopping requires knowing you are there.

`proxy-signal` review was spoiled before it ran — I quoted the mirror-fogs answer at him earlier in the conversation. Re-queued untested.

**New — the code trace.**

```python
a = [1, 2]
b = a
b.append(3)
x = 10
y = x
y += 1
print(a, x)
```

He answered `2, 10`. Two stacked errors, and two real wins underneath them.

Wins, and they are the hard half: he tracked that appending through `b` changed `a` (shared object), *and* that `y += 1` left `x` alone (numbers not shared). He held both asymmetric cases at once and said why.

Errors, both surface: he read `print(a, x)` as printing a **length** — a word that appears nowhere in that code — and he computed that length as 3 items → 2, merging *count* with *index*.

The two wrong answers shared one move: a gap appeared and he filled it with something plausible instead of checking what was written. Named for him explicitly as a habit, not an intelligence problem, with the fix being bookkeeping — track the values, add nothing unwritten.

**Production.** Predicted `[70, 80, 90, 100] / 4 / 100` — correct, but only after being pushed to commit; he had reasoned it right mid-sentence then written "not sure". Then the deliberately-broken variant with `list(scores)`: `[70, 80, 90] / 3 / 90`, correct, committed with no hedge. Both run and confirmed.

## Standing observation

His reasoning was right and his confidence was wrong. That is two separate skills and today only one of them was failing. Make him commit before revealing, always — machine grading is what fixes this, not reassurance.

## Vocabulary added (8)

value, variable, list, append, output, index, len, `list(a)` — all in `state/glossary.md`. He asked for vocabulary very slowly, a few per session, defined before use.

## Queued next

More `predict-before-run` reps on unseen code, then: what an LLM call really is → types as design → routing as a decision function → eval harness → failure handling.

Rule agreed: AI may explain anything, but may not produce the artifact.

---

# Same session, part two — functions

Motivated by the router directly: *given this task, which model gets it?* is one question asked a thousand times with different inputs. That is what a function is for. Everything in Track 1 will be functions calling each other.

## What happened

Same asymmetry as part one, moved into functions:

```python
def add_item(items):
    items.append(99)

def add_number(n):
    n = n + 1
```

He predicted `[1, 2, 99]` and `6`. The real output was `[1, 2, 99]` and **5**.

**This is the important finding of the session.** He had produced `name-vs-object` unaided twice an hour earlier, cleanly, including a deliberately-broken variant. It did not survive being moved into a function. So top-level fluency was not the same thing as holding the idea — I marked it `solid` too early and have downgraded it to `landed`.

When shown the conflict he reached for an invented explanation: *"we just printed count rather than calling the function; print(count) pulled the variable."* Nothing on the page supports that. It was killed cheaply by applying his own rule to the line he got right — by that rule `print(original)` should also have shown `[1, 2]`, and it didn't. His rule could not tell the two cases apart, so it wasn't the rule.

That is the third instance in one session of the same move: gap appears, gets filled with something plausible, page never checked. Named for him each time, in the act.

## The node that came out of it

- `.append()` / `.clear()` **reach through the name** and change the thing itself. Everyone pointing at that thing sees it.
- `=` **never touches the thing.** It points the name somewhere else.
- A function gets its **own private names**. Moving a private name changes nothing outside. Changing a shared object is visible to everyone holding it.

He got there himself on the key observation — *"there was no duplication of the list"* — but merged two events into one, saying `items` no longer pointed at the same list. The contents changed; the pointing did not. Sharpened with a memory diagram.

## Check, fresh clothes

```python
def wipe(items):  items = []
def empty(items): items.clear()
```

`[1, 2]` and `[]`. Both correct — but he answered `b` confidently and hedged on `a` until pointed back at the rule he had just read. Pattern confirmed: **he hedges when the answer needs a rule applied, not when it needs a fact recalled.** His final wording — "there was no operation" — was corrected: the operation was real, it just landed on the name.

## Vocabulary added (5 more, 13 total)

function, `def`, argument, call, `.clear()`. `return` deliberately not introduced yet.

## Next session

Re-test `name-vs-object` and `mutate-vs-rebind` cold, in a deep session — not a drill, since neither is solid. Then `return`, then what an LLM call really is.
