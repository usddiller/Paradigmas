numbers = [4, 7, 2, 9, 12, 5, 8, 3]
total = 0
even_numbers = []
iterations = 0  # Счётчик итераций для задания 13

for number in numbers:
    iterations += 1  # Явное увеличение счётчика на каждой итерации
    
    if number % 2 == 0:
        square = number ** 2  # Квадрат текущего чётного числа
        even_numbers.append(number)
        
        # Задание 12: вывод квадратов выбранных чисел
        print(f"Чётное число: {number}, его квадрат: {square}")
        
        # Явное изменение переменной-накопителя total
        total = total + square

print("\nРезультаты:")
print("Чётные числа:", even_numbers)
print("Сумма квадратов (total):", total)
# Задание 13: вывод количества итераций
print("Количество итераций цикла:", iterations)
