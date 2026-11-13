"""
Demo 04, after: annotations document the interface.

name: str says the caller should pass a string; -> dict says the
function returns a dictionary; list[dict] says every element of the
records is a dictionary. The surprise is what they do not do: the
interpreter ignores them at run time, so "sixteen" still lands in
the record and nothing converts it. They are documentation, so when
a value's type genuinely matters, the function has to check it
itself. Compare with 04_annotations_before.py.
"""


def drink_record(name: str, ounces: int = 12, shots: int = 1) -> dict:
    """Build one drink record."""
    return {"name": name, "ounces": ounces, "shots": shots}


def drink_names(records: list[dict]) -> list[str]:
    """Collect the name from each record."""
    result = []
    for record in records:
        result.append(record["name"])
    return result


def main():
    """Drive the demo."""
    print(drink_record("Latte", 12, 2))
    print(drink_record("Latte", "sixteen", 2))  # no check, no conversion
    print(drink_names([drink_record("Latte"), drink_record("Americano", 16)]))


if __name__ == "__main__":
    main()
