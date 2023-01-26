import tkinter as tk
import tkinter.messagebox
import os
import pickledb

db=pickledb.load("saving.db", auto_dump=True)

window=tk.Tk()
window.geometry("250x110")
window['bg']='#202020'
window.title('Настройка веб ссылки')

adress=tkinter.StringVar()
nnames=tkinter.StringVar()

def ok():
	aboba=adress.get()
	db.set("web", f"{aboba}")
	aboba1=nnames.get()
	db.set("webname", f"{aboba1}")
	tk.messagebox.showinfo('INFO', 'Успешно сохранено!')
	os.startfile(r'system86.pyw')
	window.destroy()

pwd=tk.Label(window, text="Введите веб адрес", bg='#202020', fg='white')
passwd=tk.Entry(window, textvariable=adress)
name=tk.Label(window, text="Введите название", bg='#202020', fg='white')
names=tk.Entry(window, textvariable=nnames)
ok=tk.Button(window, text="Сохранить", command=ok, bg='#4287f5')

pwd.pack()
passwd.pack()
name.pack()
names.pack()
ok.pack()

db.dump()
window.mainloop()
