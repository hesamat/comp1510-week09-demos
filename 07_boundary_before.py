"""
Demo 07, before: the boundary catches a <= versus < mix-up.

This copy of the café interface has the bug: the guard tests
shots < 0, so zero slips through and the record is built with a
zero-shot espresso. The checks below are the boundary tests from
the reading: around zero, 0 and -1 must be rejected and 1 is the
smallest value that passes. Watch which line reports, and read the
evidence before editing.
"""


def drink_record(name, ounces=12, shots=1):
    """Return one drink record.

    :param shots: a positive whole number of espresso shots
    """
    if shots < 0:  # the bug: zero is not negative, so it passes
        raise ValueError(f"Shots must be positive, not {shots}.")
    return {"name": name, "ounces": ounces, "shots": shots}


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
