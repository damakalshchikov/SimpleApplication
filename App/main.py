# Импортируем необходимые библиотеки
import tkinter as tk
from tkinter import ttk

# Счётчик
COUNTER = 0


# Функция, которая увеличивает значение счётчика
def plus_some_value(value):
    def wrapper():
        global COUNTER

        COUNTER += value
        counter["text"] = f"{COUNTER}"

        if COUNTER >= 10:
            btn2.pack()

    return wrapper


# Инициализация окна
window = tk.Tk()
window.title("Clicker")
window.iconbitmap(default="icon.ico")
window.geometry("400x350")
window.resizable(False, False)

# Кнопка, для отображения счётчика
counter = ttk.Button(text=f"{COUNTER}", width=10, state="disabled")
counter.pack()

# Кнопка, которая увеличивает значение счётчика на единицу
btn1 = ttk.Button(text=f"+1", command=plus_some_value(1), width=10)
btn1.pack()

# Кнопка, которая увеличивает значение счётчика на десять
btn2 = ttk.Button(text="+10", command=plus_some_value(10), width=10)

# Отображение окна
window.mainloop()
