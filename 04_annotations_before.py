"""
Demo 04, before: the signature keeps its promises undocumented.

A caller cannot see the code behind a function, so nothing in this
signature says that ounces should be a number, that shots should be
a positive whole number, or what comes back. The record still gets
built; the interface just refuses to tell anyone what it depends
on.
"""


def drink_record(name, ounces=12, shots=1):
    """Build one drink record."""
    return {"name": name, "ounces": ounces, "shots": shots}


def main():
    """Drive the demo."""
    print(drink_record("Latte", 12, 2))
    print(drink_record("Latte", "sixteen", 2))


if __name__ == "__main__":
    main()
