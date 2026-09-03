import tkinter as tk
from tkinter import messagebox  # Для красивого вывода сообщений об ошибках

def calculate():
    """Событие: запуск вычислений при нажатии на кнопку 'Вычислить'."""
    # Задание 25: Обработка ошибочного ввода с помощью try/except
    try:
        # Задание 24: Получаем строку из поля ввода, убираем лишние пробелы по краям
        input_text = entry.get().strip()
        
        # Если поле ввода пустое, генерируем ошибку вручную
        if not input_text:
            raise ValueError("Поле ввода пустое.")
            
        # Превращаем строку чисел через пробел в список целых чисел (int)
        user_numbers = [int(x) for x in input_text.split()]
        
        # Функциональное вычисление суммы квадратов чётных чисел
        result = sum(n ** 2 for n in user_numbers if n % 2 == 0)
        
        # Выводим результат в метку
        result_label.config(text=f"Результат (сумма квадратов чётных): {result}", fg="black")
        
    except ValueError:
        # Если пользователь ввёл буквы, спецсимволы или оставил поле пустым
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные целые числа через пробел.")
        result_label.config(text="Ошибка вычислений", fg="red")

# Задание 26: Функция очистки результата и поля ввода
def clear_all():
    """Событие: очистка интерфейса при нажатии на кнопку 'Очистить'."""
    entry.delete(0, tk.END)  # Удаляем текст из поля ввода от начала до конца
    result_label.config(text="Нажмите кнопку 'Вычислить'", fg="black")  # Сбрасываем текст метки


# Настройка главного окна GUI
root = tk.Tk()
root.title("Парадигмы программирования: Событийный стиль")
root.geometry("400x250")  # Задаем базовый размер окна

# Метка-инструкция для пользователя
instruction_label = tk.Label(root, text="Введите целые числа через пробел:")
instruction_label.pack(padx=20, pady=(15, 5))

# Задание 24: Поле ввода чисел (Entry)
entry = tk.Entry(root, width=40)
entry.insert(0, "4 7 2 9 12 5 8 3")  # Подставляем исходный набор чисел по умолчанию
entry.pack(padx=20, pady=5)

# Кнопка для запуска расчетов (Событие 1)
calculate_button = tk.Button(root, text="Вычислить", command=calculate, bg="#e1e1e1")
calculate_button.pack(padx=20, pady=5)

# Задание 26: Кнопка очистки (Событие 2)
clear_button = tk.Button(root, text="Очистить", command=clear_all, bg="#f0dadb")
clear_button.pack(padx=20, pady=5)

# Метка для вывода результатов
result_label = tk.Label(root, text="Нажмите кнопку 'Вычислить'", font=("Arial", 10, "bold"))
result_label.pack(padx=20, pady=15)

# Запуск цикла обработки событий GUI
root.mainloop()
