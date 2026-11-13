"""
Demo 06: pytest.raises turns "this call should explode" into a check.

Four tests: the ordinary case the interface promises, then
rejections of zero, a negative, and a string. Each rejection test's
match argument checks that the message names the bad value. Remove
the guard from drinks.py and all three rejection tests fail, because
the calls quietly succeed. Change the message so it no longer names
the value and they fail for the other reason. The ordinary test
still passes in both cases: that is the guard's insurance policy,
and Activity 4's mutation matrix makes the difference visible.

Run from this folder with:  python -m pytest 06_test_drinks.py -v
"""

import pytest

from drinks import drink_record


def test_builds_the_promised_record():
    # Ordinary case: the default is one shot, the smallest passing value.
    assert drink_record("Latte") == {
        "name": "Latte", "ounces": 12, "shots": 1,
    }


def test_rejects_zero_shots():
    # Boundary: zero violates the positive-whole-number rule.
    with pytest.raises(ValueError, match="not 0"):
        drink_record("Latte", shots=0)


def test_rejects_negative_shots():
    # Boundary below the rule, and the message must name the bad value.
    with pytest.raises(ValueError, match="not -3"):
        drink_record("Latte", shots=-3)


def test_rejects_text_shots():
    # The type check runs before the comparison, so this is a ValueError.
    with pytest.raises(ValueError, match="not two"):
        drink_record("Latte", shots="two")
