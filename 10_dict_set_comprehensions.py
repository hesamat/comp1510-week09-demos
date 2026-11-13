"""
Demo 10: the same idea builds the other two containers.

A dictionary comprehension writes key: value before the for clause;
a set comprehension writes one expression in braces. The repeated
title is the point of the prediction: the list keeps both copies in
order, the set keeps one, and the dictionary keeps one value under
the key, where the later record replaced the earlier one.
"""

ROWS = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "King of Tokyo", "players": 2, "minutes": 20},
]


def main():
    """Drive the demo."""
    print([game["title"] for game in ROWS])
    print({game["title"] for game in ROWS})
    print({game["title"]: game["players"] for game in ROWS})
    print({game["minutes"] for game in ROWS})


if __name__ == "__main__":
    main()
