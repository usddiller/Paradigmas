def validate_scores(scores):
    """Проверяет корректность оценок и возвращает их в виде списка float."""
    if not isinstance(scores, (list, tuple)):
        raise TypeError("scores должен быть списком или кортежем")

    def _check(score):
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("Балл должен быть числом")
        if not (0 <= score <= 100):
            raise ValueError("Балл должен быть от 0 до 100")
        return float(score)

    return [_check(s) for s in scores]


def validate_student(student):
    """Проверяет наличие обязательных ключей в словаре студента."""
    if not isinstance(student, dict):
        raise TypeError("Запись студента должна быть словарём")
    required = {"id", "name", "scores"}
    missing = required - student.keys()
    if missing:
        raise ValueError(f"Отсутствуют поля: {sorted(missing)}")
