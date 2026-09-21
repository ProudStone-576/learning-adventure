---
name: visualize
description: Add a correct, minimal diagram to a lesson — dependency graph, system/flow, sequence, state machine, tree, comparison, or a spatial/geometric picture. Use when an idea is genuinely clearer as a picture than as prose. Renders inline via mermaid fences (or hand-written SVG for geometry).
---

# Visualize

A picture earns its place only when it shows something words cannot — shape, structure, direction, relationship, geometry. This skill produces ONE such picture and keeps it **correct**.

## When to visualize (and when not to)

This teaching system builds a **dependency graph in the learner's head** — unconditional truths at the roots, derived facts hanging off them. A visual is powerful exactly when it makes that structure, or a geometry, visible. Reach for one when:

- The idea is a **structure or relationship**: dependencies, a system with parts and arrows, a flow, a sequence of exchanges, a state machine, a tree, a comparison, a containment.
- The idea is **spatial or geometric**: coordinate geometry, a number line, vectors, a function's shape, a loss surface, a decision boundary, a physical arrangement.

Do NOT visualize when prose or a single equation already carries it. A decorative diagram that restates the sentence next to it adds noise and a chance to be wrong. **When in doubt, don't — a missing visual is cheaper than a false one.**

## Pick the form

- **```mermaid``` fence** — structural and relational: dependency graphs, flowcharts, sequence, state, ER, class, mindmap, timeline. This is the default and it maps directly onto the dependency-graph pedagogy. Renders natively in the Claude Code web app and in artifacts.
- **Inline SVG** — spatial and geometric things mermaid cannot lay out: exact coordinates, geometry figures, number lines, vectors, plots, decision boundaries. Hand-write it; keep the coordinate arithmetic simple enough to check by eye.
- **A published Artifact** — only when the picture needs to be interactive or the learner wants it on their phone as a standalone page. Otherwise inline is better: it sits in the lesson where the explanation is.

## One idea, fewest elements

The most common failure is **cramming**. Every extra label makes the picture harder to read AND more likely to be wrong. Before drawing, prune: for each element ask *"if I delete this, is the idea still clear?"* If yes, delete it.

- **Ceiling of ~7 nodes.** Four nodes that each pull weight beat twelve fighting for space. If you are about to exceed seven, you are drawing two diagrams, or one diagram and some prose.
- **Short labels.** A node holds a term or short phrase, never a sentence. Long labels wreck mermaid layout.
- **No title inside the diagram.** The sentence introducing it is the title.
- `graph TD` with foundations at the top flowing down to conclusions is often the natural shape here — it is literally the dependency graph being taught.

## Correctness

You are asserting something when you draw an arrow. Before posting:

- Is every arrow pointing the right way? Does A really depend on B, or is it the reverse?
- Is every label accurate and unambiguous?
- Would the learner read the *intended* idea off this picture alone, with no prose?
- If unsure whether an edge is true, **omit it**. An incomplete diagram is fine; a false one corrupts a node.

Mermaid syntax errors render as an error block, not a picture. Keep syntax plain — avoid exotic features, and quote labels containing punctuation: `A["log-loss, per sample"]`.

## Embed it

Put the fence directly in the teaching reply, introduced by one sentence. Then let it carry the idea — do not narrate every element back in prose. The diagram and the paragraph restating it are redundant; keep the diagram.

Every diagram that appears in a lesson also goes into that lesson's `lessons/YYYY-MM-DD-topic.md` file, so it survives the session and renders on their phone.
