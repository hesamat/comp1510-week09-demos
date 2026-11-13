"""
Demo 03, before: the mutable default trap.

The default list was created once, when def ran. Every call that
leaves extras out gets the same list, and the parameter inside the
function is one more name for it, so Vanilla finds Oat milk already
there. Prediction: write both displayed lists before running.
"""


def add_extra(extra, extras=[]):
    """Add an extra to a drink order."""
    extras.append(extra)
    return extras


def main():
    """Drive the demo."""
    print(add_extra("Oat milk"))
    print(add_extra("Vanilla"))


if __name__ == "__main__":
    main()
