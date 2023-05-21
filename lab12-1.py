from tkinter import *

root = Tk()

root['bg'] = '#000000'
root.title('Кафе-мороженное')
root.wm_attributes('-alpha', 1)
root.geometry('200x200')

root.resizable(width=False, height=False)

canvas = Canvas (root, height=200, width=200)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Виды мороженного', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Vanille', bg='yellow')
btn.pack()

btn = Button(frame, text='Chocolate', bg='brown')
btn.pack()

btn = Button(frame, text='Strawberry', bg='blue')
btn.pack()

btn = Button(frame, text='Mint', bg='green')
btn.pack()
root.mainloop()