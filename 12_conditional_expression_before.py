"""
Demo 12, before: choosing each label with a statement.

Every record appears in the result, and the if-else chooses between
two values for it. The loop works; the choice is just buried in the
body. Prediction: the three labels, before running.
"""

GAMES = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "Catan", "players": 4, "minutes": 90},
]


def main():
    """Drive the demo."""
    labels = []
    for game in GAMES:
        if game["minutes"] <= 30:
            labels.append("quick")
        else:
            labels.append("long")
    print(labels)


if __name__ == "__main__":
    main()
