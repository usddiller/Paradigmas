class NumberCollection:
    def __init__(self, numbers):
        # Задание 19: инкапсуляция исходных данных
        self._numbers = list(numbers)

    def get_even_numbers(self):
        """Возвращает список чётных чисел."""
        return [n for n in self._numbers if n % 2 == 0]

    def sum_even_squares(self):
        """Вычисляет сумму квадратов чётных чисел."""
        total = 0
        for number in self._numbers:
            if number % 2 == 0:
                total += number ** 2
        return total

    # Задание 18: Добавление новых методов поведения объекта

    def count_even_numbers(self):
        """Возвращает количество чётных чисел в коллекции."""
        return len(self.get_even_numbers())

    def find_maximum(self):
        """Находит максимальное число в коллекции. 
        Возвращает None, если коллекция пуста.
        """
        if not self._numbers:
            return None
        return max(self._numbers)

    def calculate_average(self):
        """Вычисляет среднее арифметическое всех чисел в коллекции.
        Возвращает 0, если коллекция пуста.
        """
        if not self._numbers:
            return 0
        return sum(self._numbers) / len(self._numbers)


# --- Демонстрация работы (Задание 20) ---

# Создание первого объекта (из исходного примера)
collection1 = NumberCollection([4, 7, 2, 9, 12, 5, 8, 3])

print("=== Объект 1 ===")
print("Чётные числа:", collection1.get_even_numbers())
print("Сумма квадратов чётных:", collection1.sum_even_squares())
print("Количество чётных чисел:", collection1.count_even_numbers())
print("Максимальное число:", collection1.find_maximum())
print("Среднее арифметическое:", collection1.calculate_average())

print("\n" + "="*20 + "\n")

# Задание 20: Создание второго объекта с другим набором чисел
collection2 = NumberCollection([10, 15, 23, 42, 4, 8, 11])

print("=== Объект 2 (Новый набор чисел) ===")
print("Чётные числа:", collection2.get_even_numbers())
print("Сумма квадратов чётных:", collection2.sum_even_squares())
print("Количество чётных чисел:", collection2.count_even_numbers())
print("Максимальное число:", collection2.find_maximum())
print("Среднее арифметическое:", collection2.calculate_average())
