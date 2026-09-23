# Glossary

Every technical word introduced, in plain language, with the date and the node it belongs to.

Rules: a few new words per session, never more. Define before use. Reuse old words on purpose so they repeat.

| Word | Plain meaning | Node | Added |
|---|---|---|---|
| value | A piece of information the program is holding. The number 10 is a value. The text "hello" is a value. | predict-before-run | 2026-09-21 |
| variable | A name that points at a value, so you can refer to it later. In `x = 10`, the variable is `x`. | predict-before-run | 2026-09-21 |
| list | Several values kept in order, written inside square brackets. `[1, 2]` is a list holding two values. | predict-before-run | 2026-09-21 |
| append | Add one new item onto the end of an existing list. | predict-before-run | 2026-09-21 |
| output | What the program shows you when it finishes a `print`. | predict-before-run | 2026-09-21 |
| index | The position number of one item in a list. The first item sits at index 0. | len-vs-index | 2026-09-21 |
| len | Written `len(a)`. Gives back how many items the list holds. A plain count, starts at one. | len-vs-index | 2026-09-21 |
| list(a) | Builds a brand new list holding the same values. A real copy, not a second name for the same thing. | name-vs-object | 2026-09-21 |
| function | A named block of code you can run whenever you want, as many times as you want. | functions | 2026-09-21 |
| def | How you start writing a function. `def add_item(items):` means "here begins a function named add_item". | functions | 2026-09-21 |
| argument | The value you hand a function when you run it. | functions | 2026-09-21 |
| call | Running the function. `add_item(original)` is a call. | functions | 2026-09-21 |
| .clear() | Empties a list in place. The same list stays, its contents go. | mutate-vs-rebind | 2026-09-21 |
| local variable | A variable that exists only inside one function. Created when it starts, thrown away when it ends. | local-scope | 2026-09-22 |
| scope | Where a name is visible. The `x` inside a function and the `x` outside are different variables that happen to be spelled the same. | local-scope | 2026-09-22 |
| return | Hands a value back to whoever called the function. The front door. Also ends the function immediately. | return | 2026-09-22 |
| None | Python's word for "nothing here". What you get back from a function that returns nothing. | return | 2026-09-22 |
| caller | The line of code that ran the function. In `answer = add(2, 3)`, that line is the caller. | return | 2026-09-22 |
| side effect | When a function changes something outside itself instead of handing a value back. | return | 2026-09-22 |
