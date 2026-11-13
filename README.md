# COMP 1510 Week 9 Demos

The lecture examples for function interfaces and comprehensions:
chapters 25 and 26, one example family per chapter (a café order
for interfaces, a board-game shelf for comprehensions). Every
numbered demo is a before/after pair or a single prediction file,
and each runs top to bottom. `drinks.py` is the shared module the
testing demos import. `games.json` is the data file the in-class
exercises read; the numbered comprehension demos carry their own
three-game table inline.

## Interfaces, guards, and testing (chapter 25)

- `01_call_forms.py`: positional and keyword arguments; the swapped
  numbers that run happily, the duplicate-value `TypeError`, and
  the positional-after-keyword `SyntaxError`.
- `02_defaults.py`: a default makes a parameter optional;
  `help()` shows the signature.
- `03_mutable_default_before.py` / `03_mutable_default_after.py`:
  the shared-list trap, then the `None` repair, whose third call
  supplies an explicit list.
- `04_annotations_before.py` / `04_annotations_after.py`: the
  undocumented signature, then annotations as documentation that
  converts and checks nothing.
- `05_guard_clause.py`: the precondition in the docstring, the
  guard clause at the top, and the caller deciding what rejection
  means. The guard checks `isinstance` before the comparison, so a
  string reaches the `ValueError` rather than a `TypeError`; the
  loop runs 2, 0, -3, and "two".
- `regression_build_starter.py`: a streaming-show `show_record`
  with no guard yet, the contract partly written, and the ordinary
  test supplied at the smallest passing value (1). Complete the
  contract, add the guard and two rejection tests (zero and a
  string), run pytest green, then break the guard's comparison and
  watch your own zero test fail. Copy the file first, then run
  `python -m pytest your_copy.py -v`.
- `06_test_drinks.py`: `pytest.raises` turns "this call should
  explode" into a check. Four tests: the ordinary case, then
  rejections of zero, a negative, and a string; each `match=`
  checks that the message names the bad value. A good exercise:
  delete the guard from `drinks.py`, change its message, or change
  `<=` to `<`, and predict each test before rerunning. Run with
  `python -m pytest 06_test_drinks.py -v`.
- `07_boundary_before.py` / `07_boundary_after.py`: the `<=` versus
  `<` mix-up caught by the boundary values 0, -1, and 1.

## Comprehensions (chapter 26)

- `games.json`: the week's shared JSON data, used by the in-class
  exercises (the JSON round-trip review and the `quick_titles`
  collection). No numbered demo opens it; read it from this folder
  with `open("games.json", encoding="utf-8")`.
- `08_loop_to_expression_before.py` /
  `08_loop_to_expression_after.py`: the accumulator loop folded
  into the list, including a computed expression.
- `09_filter_before.py` / `09_filter_after.py`: the `if` clause
  that filters, compound conditions, and the `quick(game)`
  predicate. On the book's three games every quick game also has
  more than five players, so the compound-condition print matches
  the first; a larger table is where the compound condition
  separates two records.
- `10_dict_set_comprehensions.py`: dictionary and set forms, and
  the repeated title that separates list, set, and dict.
- `11_loop_says_it_better_before.py` /
  `11_loop_says_it_better_after.py`: the two-`for` comprehension
  that should have been a nested loop.
- `12_conditional_expression_before.py` /
  `12_conditional_expression_after.py`: `a if condition else b`
  choosing each item's value while keeping every record, beside the
  filter that drops records.
