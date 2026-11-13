"""
Demo 12, after: a if condition else b, inside the comprehension.

The conditional expression sits before the for clause and chooses
each item's value while keeping every record. That is the
difference from the filter: the filter's if comes after the for
clause and drops records. The last line uses both, dropping Catan
by players and labelling the rest. Compare with
12_conditional_expression_before.py.
"""

GAMES = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "Catan", "players": 4, "minutes": 90},
]


def main():
    """Drive the demo."""
    labels = ["quick" if game["minutes"] <= 30 else "long"
              for game in GAMES]
    print(labels)

    filtered = ["quick" if game["minutes"] <= 30 else "long"
                for game in GAMES if game["players"] <= 6]
    print(filtered)


if __name__ == "__main__":
    main()
