from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('название программы')
root.wm_attributes('-alpha', 0.7)
root.geometry('450x400')

root.resizable(width=False, height=False)

canvas = Canvas (root, height=450, width=400)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow')
btn.pack()

root.mainloop()