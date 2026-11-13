"""
Demo 09, before: the filter is a test before the append.

Only the games that finish inside half an hour should contribute,
and the compound condition asks two questions at once. Three parts
in loop order: for each game, if the condition holds, take the
expression. Prediction: which titles remain if <= 30 becomes < 30?
"""

GAMES = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "Catan", "players": 4, "minutes": 90},
]


def main():
    """Drive the demo."""
    quick_titles = []
    for game in GAMES:
        if game["minutes"] <= 30:
            quick_titles.append(game["title"])
    print(quick_titles)

    big_and_quick = []
    for game in GAMES:
        if game["minutes"] <= 30 and game["players"] > 5:
            big_and_quick.append(game["title"])
    print(big_and_quick)


if __name__ == "__main__":
    main()
