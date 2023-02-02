from tkinter import *
from tkinter import messagebox
from random import *

clicks=0

def randomize():
	global clicks
	btnclick.place(x=randint(10, 650), y=randint(10, 550))
	clicks+=1
	labelclick['text']=str(clicks)
	labelclick.pack

root=Tk()
root.title('Кликер')
root.geometry('700x600')
root.resizable(width=False, height=False)
root['bg']='black'

labelclick=Label(root, text='0', font=('Comic Sans MS', 30, 'bold'), bg='black', fg='white')
labelclick.pack()

btnclick=Button(root, text='Клик', bg='lime', fg='black', padx='20', pady='8', font=('Comic Sans MS', 13, 'bold'), command=randomize)
btnclick.place(x=randint(10, 650), y=randint(10, 550))

root.mainloop()