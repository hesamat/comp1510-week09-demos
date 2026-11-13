"""One café order interface for the week 9 testing demos.

drink_record carries its precondition in the docstring and enforces
it with a guard clause: shots must be a positive whole number. The
guard checks the type before the comparison, so a string reaches the
ValueError rather than a TypeError. The tests in 06_test_drinks.py
check both directions, the records the function accepts and the
calls it rejects.
"""


def drink_record(name: str, ounces: int = 12, shots: int = 1) -> dict:
    """Return one drink record.

    :param name: the drink's name
    :param ounces: the size in fluid ounces
    :param shots: a positive whole number of espresso shots
    :return: a dictionary record for one drink
    :raises ValueError: if shots is not a positive whole number
    """
    if not isinstance(shots, int) or shots <= 0:
        raise ValueError(
            f"Shots must be a positive whole number, not {shots}."
        )
    return {"name": name, "ounces": ounces, "shots": shots}
