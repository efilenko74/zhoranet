from tkinter import *
from datetime import datetime

root=Tk()
root.title('Секундомер')
root.resizable(width=False, height=False)
root.geometry('250x200')
root['bg']='#202020'

temp=0
after_id=''

def tick():
	global temp, after_id
	after_id=root.after(1000, tick)
	f_temp=datetime.fromtimestamp(temp).strftime("%M:%S")
	label1.configure(text=str(f_temp))
	temp+=1

def start():
	btnstart.pack_forget()
	btnstop.pack()
	tick()

def stop():
	btnstop.pack_forget()
	btncontinue.pack()
	btnreset.pack()
	root.after_cancel(after_id)

def continues():
	btncontinue.pack_forget()
	btnreset.pack_forget()
	btnstop.pack()
	tick()

def reset():
	global temp
	temp=0
	label1.configure(text='00:00')
	btncontinue.pack_forget()
	btnstart.pack()
	btnreset.pack_forget()

label1=Label(root, font=('Comic Sans MS', 30), text='00:00', bg='#202020', fg='lime')
label1.pack()

btnstart=Button(root, text='Старт', font=('Comic Sans MS', 20), command=start, width=15)
btnstop=Button(root, text='Стоп', font=('Comic Sans MS', 20), command=stop, width=15)
btncontinue=Button(root, text='Продолжить', font=('Comic Sans MS', 20), command=continues, width=15)
btnreset=Button(root, text='Сброс', font=('Comic Sans MS', 20), command=reset, width=15)

btnstart.pack()

root.mainloop()