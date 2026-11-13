"""
Demo 02: a default value makes a parameter optional.

drink_record fills any omitted parameter from the default evaluated
once, when def runs. A parameter with a default may never precede
one without, because Python could not tell where the required ones
end. help() shows the signature and which parameters are optional:
that is how a caller discovers what may be left out.
"""


def drink_record(name, ounces=12, shots=1):
    """Build one drink record."""
    return {"name": name, "ounces": ounces, "shots": shots}


def main():
    """Drive the demo."""
    print(drink_record("Latte"))
    print(drink_record("Americano", 16))
    print(drink_record("Mocha", shots=3))
    help(drink_record)


if __name__ == "__main__":
    main()
