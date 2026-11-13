"""
Demo 09, after: the if clause filters, and a predicate reads as the
sentence it replaces.

The comprehension keeps the test and the result and drops the
scaffolding. When the condition grows, give it a name: quick(game)
turns the line into a phrase, the title, for each game, if the game
is quick. Compare with 09_filter_before.py.
"""

GAMES = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "Catan", "players": 4, "minutes": 90},
]


def quick(game):
    """Report whether a game finishes inside half an hour."""
    return game["minutes"] <= 30


def main():
    """Drive the demo."""
    print([game["title"] for game in GAMES if game["minutes"] <= 30])
    print([game["title"] for game in GAMES if quick(game)])
    # On the book's three games every quick game also has more than
    # five players, so this print matches the first. The activity's
    # shows table has a quick show with four episodes, where the
    # compound condition separates the records.
    print([game["title"] for game in GAMES
           if (game["minutes"] <= 30 and game["players"] > 5)])


if __name__ == "__main__":
    main()
