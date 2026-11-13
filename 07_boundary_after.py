"""
Demo 07, after: the corrected guard, one character apart.

shots <= 0 rejects zero and every negative value, and the boundary
checks pass three times. Choose test cases from the boundary, as
before: the interesting values around zero are 0, -1, and 1. This
is exactly what the pytest.raises tests in 06_test_drinks.py pin
down. Compare with 07_boundary_before.py.
"""

from drinks import drink_record


def main():
    """Drive the demo."""
    for shots in [0, -1, 1]:
        try:
            drink_record("Latte", shots=shots)
            print(shots, "accepted")
        except ValueError:
            print(shots, "rejected")


if __name__ == "__main__":
    main()
