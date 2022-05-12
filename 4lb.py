import tkinter
from tkinter import *
import re

# Объект окна верхнего уровня создается от класса Tk
# модуля tkinter. Переменную, связываемую с объектом,
# часто называют root (корень):
root = tkinter.Tk()
root.title("Текстовый редактор")
# Размеры окна
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
# создаем текстовое поле
text = tkinter.Text(root, width=400, height=400, wrap="word")
# Настройка скролл бара
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
root.mainloop()
