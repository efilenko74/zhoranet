import tkinter as tk
import tkinter.messagebox
import os
import pickledb

db=pickledb.load("saving.db", auto_dump=True)

window=tk.Tk()
window.geometry("250x110")
window['bg']='#202020'
window.title('Изменение пароля')

passlog=tkinter.StringVar()

def ok():
	aboba=passlog.get()
	db.set("pass", f"{aboba}")
	tk.messagebox.showinfo('INFO', 'Пароль успешно изменён!')
	window.destroy()

pwd=tk.Label(window, text="Введите новый пароль", bg='#202020', fg='white')
passwd=tk.Entry(window, textvariable=passlog)
ok=tk.Button(window, text="Сохранить", command=ok, bg='#4287f5')

pwd.pack()
passwd.pack()
ok.pack()

db.dump()
window.mainloop()
