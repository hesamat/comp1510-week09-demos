"""
Demo 11, after: the loop states the same job.

Both for clauses run in the order you would write them in a nested
loop, and the loop says so directly. Keep the loop when each item
needs an action instead of a value (printing, writing to a file),
more than one statement, an early exit, or a debug print, and for
nested iteration. Compare with
11_loop_says_it_better_before.py.
"""

TABLES = [
    ["Codenames", "Catan"],
    ["Azul", "Splendor"],
]


def main():
    """Drive the demo."""
    played = []
    for table in TABLES:
        for game in table:
            played.append(game)
    print(played)


if __name__ == "__main__":
    main()
