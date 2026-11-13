"""
Demo 11, before: the comprehension that should have been a loop.

Two for clauses exist, and this one reads backwards: by the time
you have parsed it, the loop already says it. A comprehension
builds a collection; it cannot break early, print one item at a
time, or run more than one statement per record. The rule of thumb
needs no defence: if the comprehension takes longer to read than
the loop, keep the loop.
"""

TABLES = [
    ["Codenames", "Catan"],
    ["Azul", "Splendor"],
]


def main():
    """Drive the demo."""
    played = [game for table in TABLES for game in table]
    print(played)


if __name__ == "__main__":
    main()
