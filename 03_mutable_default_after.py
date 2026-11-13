"""
Demo 03, after: None as the default, built inside.

Each call without an extras list now builds its own, so the first
two displays show a single extra each. An explicit list still
works. The is None comparison is deliberate: None is one object,
so identity is the right question. Never write a list, dictionary,
or set as a default value. Compare with
03_mutable_default_before.py.
"""


def add_extra(extra, extras=None):
    """Add an extra to a drink order, starting fresh by default."""
    if extras is None:
        extras = []
    extras.append(extra)
    return extras


def main():
    """Drive the demo."""
    print(add_extra("Oat milk"))
    print(add_extra("Vanilla"))
    print(add_extra("Cinnamon", ["Decaf"]))


if __name__ == "__main__":
    main()
