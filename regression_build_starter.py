"""The regression build starter: show_record with no guard yet.

Copy this file under your own name. The docstring carries the
parameters and the exception; complete the contract with the
precondition and postcondition, then add the guard it promises and
two rejection tests (zero and a string). Run:

    python -m pytest your_copy.py -v

Three tests pass against a correct guard. Change the guard's
comparison and run again: the rejection test you wrote is what
catches the break. The demonstration ran on drinks.py and
06_test_drinks.py; this build runs on a fresh interface, so the
pattern has to transfer, not copy.
"""

import pytest


def show_record(title, episodes=8, minutes=45):
    """Return one show record.

    :param episodes: a positive whole number of episodes
    :raises ValueError: if episodes is not a positive whole number
    """
    return {"title": title, "episodes": episodes, "minutes": minutes}


def test_builds_the_promised_record():
    # The ordinary case the interface promises, at the smallest pass.
    assert show_record("Meridian", episodes=1) == {
        "title": "Meridian", "episodes": 1, "minutes": 45,
    }


# Add the precondition and postcondition entries to the docstring.
# Add the guard here: type check first, then the boundary.
# Add two rejection tests: zero episodes, then a string.
