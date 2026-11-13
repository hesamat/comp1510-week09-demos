"""
Demo 05: the guard clause rejects before the work begins.

The precondition sits in the docstring, and the if-and-raise pair
at the top enforces it before any work that assumes the condition.
The type check comes first, so a string reaches the guard's
ValueError rather than a TypeError in the comparison. Run the loop
to see the record for a valid count and the report for zero, a
negative, and a string. This file is the subject of the tests in
06_test_drinks.py.
"""

from drinks import drink_record


def main():
    """Drive the demo."""
    for shots in [2, 0, -3, "two"]:
        try:
            print(drink_record("Latte", shots=shots))
        except ValueError as error:
            print("Rejected:", error)


if __name__ == "__main__":
    main()
