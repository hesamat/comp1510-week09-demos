"""
Demo 01: arguments by position and by name.

ounces and shots are both numbers, so a positional call that swaps
them is legal, runs happily, and quietly builds the wrong record.
Keyword arguments state which number is which, at the place where a
mistake would otherwise hide. Two rules keep calls unambiguous:
positional arguments come before keyword arguments, and each
parameter gets a value once. Prediction: write all three records
before running.
"""


def drink_record(name, ounces, shots):
    """Build one drink record."""
    return {"name": name, "ounces": ounces, "shots": shots}


def main():
    """Drive the demo."""
    print(drink_record("Latte", 12, 2))
    print(drink_record("Latte", 2, 12))
    print(drink_record(name="Latte", shots=12, ounces=2))
    # drink_record("Latte", name="Mocha")



if __name__ == "__main__":
    main()
