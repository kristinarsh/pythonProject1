import tkinter
from tkinter import *
import re



def cct(event):
    a = text.get(1.0, END)
    text.delete(1.0, END)
    text.tag_config('tag', foreground='red')
    text.tag_config('content', foreground='blue')
    fr = 0
    if list(re.finditer("<[^<>]+>", a))!= []:
        for m in re.finditer("<[^<>]+>", a):
            text.insert(INSERT, a[fr:m.start()-1], 'content')
            text.insert(INSERT, a[m.start():m.end()], 'tag')
            text.insert(INSERT, a[m.end() + 1:], 'content')
            fr = m.end()
    else:
        text.insert(END, a[:-1], 'content')

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
text.bind('<Key>', cct)

root.mainloop()
