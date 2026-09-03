from typing import List

# Задание 16: Добавлены аннотации типов (int, List[int])

def is_even(number: int) -> bool:
    """Проверяет, является ли число чётным."""
    return number % 2 == 0

def square(number: int) -> int:
    """Вычисляет квадрат числа."""
    return number ** 2

# Задание 15: Создана отдельная функция для фильтрации чётных чисел
def get_even_numbers(values: List[int]) -> List[int]:
    """Возвращает список только чётных чисел."""
    even_numbers: List[int] = []
    for number in values:
        if is_even(number):
            even_numbers.append(number)
    return even_numbers

def sum_even_squares(values: List[int]) -> int:
    """Вычисляет сумму квадратов чётных чисел."""
    total: int = 0
    # Используем созданную функцию get_even_numbers для разделения подзадач
    even_numbers = get_even_numbers(values)
    for number in even_numbers:
        total += square(number)
    return total

# --- Демонстрация работы программы ---

# Исходные данные
numbers: List[int] = [4, 7, 2, 9, 12, 5, 8, 3]

# Задание 17: Проверка функций is_even() и square() отдельными вызовами
print("--- Тестирование отдельных функций (Задание 17) ---")
test_num1: int = 7
test_num2: int = 6

print(f"Число {test_num1} чётное?: {is_even(test_num1)}")  # Ожидается False
print(f"Число {test_num2} чётное?: {is_even(test_num2)}")  # Ожидается True
print(f"Квадрат числа {test_num2}: {square(test_num2)}")    # Ожидается 36
print("-" * 50)

# Вывод основных результатов алгоритма
print("\n--- Основные результаты ---")
print("Исходный список:", numbers)
print("Только чётные числа (get_even_numbers):", get_even_numbers(numbers))
print("Сумма квадратов чётных чисел:", sum_even_squares(numbers))
