import tkinter as tk
import tkinter.messagebox
import os
import pickledb

db=pickledb.load("saving.db", auto_dump=True)

window=tk.Tk()
window.geometry("250x100")
window['bg']='#202020'
window.title('Заблокировано')

parol=tkinter.StringVar()

def okkk():
	passs=db.get("pass")
	if (parol.get())==f"{passs}":
		os.startfile(r'system86.pyw')
		window.destroy()
	else:
		passwd['bg']='red'
		tk.messagebox.showinfo('INFO', 'Пароль неверный!')

pwd=tk.Label(window, text="Введите пароль", bg='#202020', fg='white')
passwd=tk.Entry(window, textvariable=parol)
ok=tk.Button(window, text="подтвердить", command=okkk, bg='#4287f5')
stock=tk.Label(window, text="(пароль по умолчанию: zhoraos)", bg='#202020', fg='white')

pwd.pack()
passwd.pack()
ok.pack()
stock.pack()

db.dump()
window.mainloop()
