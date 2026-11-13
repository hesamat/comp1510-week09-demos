"""
Demo 08, before: the accumulator loop you have written many times.

Start with an empty list, visit each record, append. This shape
built every list so far in the course. Prediction: the titles list,
then the doubled play times, before running.
"""

GAMES = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "Catan", "players": 4, "minutes": 90},
]


def main():
    """Drive the demo."""
    titles = []
    for game in GAMES:
        titles.append(game["title"])
    print(titles)

    doubled = []
    for game in GAMES:
        doubled.append(game["minutes"] * 2)
    print(doubled)


if __name__ == "__main__":
    main()
