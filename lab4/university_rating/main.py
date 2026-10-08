from .rating import build_rating
from .report import format_rating


def load_demo_data():
    return [
        {"id": 101, "name": "Amina", "scores": [88, 92, 79]},
        {"id": 102, "name": "Dias", "scores": [45, 52, 48]},
        {"id": 103, "name": "Mira", "scores": []},
    ]


def main():
    students_data = load_demo_data()
    leaderboard = build_rating(students_data)
    print(format_rating(leaderboard))


if __name__ == "__main__":
    main()
