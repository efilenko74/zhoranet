from tkinter import *
from random import choice

def generate():
	lenghtpass=e.get()
	e.delete(0, END)
	for i in range(int(lenghtpass)):
		e.insert(0, choice(alphabet))

root=Tk()
root.title('Генератор пароля')

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '8', '9']

e=Entry(root, font='Arial 13')
e.pack()

btn=Button(root, text='Сгенерировать', command=generate)
btn.pack()

root.mainloop()