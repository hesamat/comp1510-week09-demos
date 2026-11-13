"""
Demo 08, after: the loop folded into the list itself.

The comprehension has two parts: the expression says what each item
of the new list is, and the for clause says where the values come
from. Read it in the same order the loop ran. It always builds a
new list; GAMES still refers to the untouched original. Compare
with 08_loop_to_expression_before.py.
"""

GAMES = [
    {"title": "King of Tokyo", "players": 6, "minutes": 30},
    {"title": "Codenames", "players": 8, "minutes": 15},
    {"title": "Catan", "players": 4, "minutes": 90},
]


def main():
    """Drive the demo."""
    print([game["title"] for game in GAMES])
    print([game["minutes"] * 2 for game in GAMES])


if __name__ == "__main__":
    main()
