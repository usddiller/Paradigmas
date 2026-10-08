PASSING_AVERAGE = 50


def calculate_average(scores):
    """Вычисляет средний балл или возвращает None для пустой последовательности."""
    return sum(scores) / len(scores) if scores else None


def determine_status(average):
    """Определяет допуск студента на основе среднего балла."""
    if average is None:
        return "нет данных"
    return "допущен" if average >= PASSING_AVERAGE else "не допущен"
