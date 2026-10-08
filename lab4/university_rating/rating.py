from .calculations import calculate_average, determine_status
from .validation import validate_scores, validate_student


def build_student_result(student):
    """Формирует итоговый результат для одного студента."""
    validate_student(student)
    scores = validate_scores(student["scores"])
    average = calculate_average(scores)
    return {
        "id": student["id"],
        "name": student["name"],
        "average": average,
        "status": determine_status(average),
    }


def _sort_key(item):
    average = item["average"]
    return average is not None, average or 0


def build_rating(students):
    """Возвращает отсортированный рейтинг, не мутируя исходный список."""
    results = list(map(build_student_result, students))
    return sorted(results, key=_sort_key, reverse=True)
