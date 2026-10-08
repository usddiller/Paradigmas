def format_average(value):
    return "-" if value is None else f"{value:.2f}"


def format_rating(rows):
    header = ["Рейтинг группы"]
    entries = [
        f"{idx}. {item['name']}: {format_average(item['average'])} {item['status']}"
        for idx, item in enumerate(rows, start=1)
    ]
    return "\n".join(header + entries)
