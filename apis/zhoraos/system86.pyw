import tkinter as tk
import tkinter.messagebox
import os
import webbrowser
import pickledb
import time

db=pickledb.load("saving.db", auto_dump=True)

def off ():
	MsgBox = tk.messagebox.askquestion ('Warning', 'При нажатии кнопки "да" система будет отключена!', icon = 'warning')
	if MsgBox == 'yes':
		window.destroy()
	else:
		tk.messagebox.showinfo('INFO', 'Действие отменено!')
def sysoff():
	MsgBox = tk.messagebox.askquestion ('Warning', 'При нажатии кнопки "да" ваш компьютер будет отключен, и я не шучу!!! Сохраните не сохранённые данные и можно вырубать)', icon = 'warning')
	if MsgBox == 'yes':
		os.system('shutdown /s /t 0')
	else:
		tk.messagebox.showinfo('INFO', 'Действие отменено!')
def lock():
	os.startfile(r'ZhoraOS.pyw')
	window.destroy()

def bgbtn():
	a.pack()
	b.pack()
	c.pack()
	d.pack()
	e.pack()
	f.pack()
	g.pack()
	h.pack()
	i.pack()
	j.pack()
	hidebg.pack()
def hide():
	a.pack_forget()
	b.pack_forget()
	c.pack_forget()
	d.pack_forget()
	e.pack_forget()
	f.pack_forget()
	g.pack_forget()
	h.pack_forget()
	i.pack_forget()
	j.pack_forget()
	hidebg.pack_forget()

def r():
	window['bg']= 'red'
	db.set("bg", "red")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def g():
	window['bg']= 'green'
	db.set("bg", "green")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def b():
	window['bg']= 'blue'
	db.set("bg", "blue")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def pur():
	window['bg']= 'purple'
	db.set("bg", "purple")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def pink():
	window['bg']= 'pink'
	db.set("bg", "pink")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def orng():
	window['bg']= 'orange'
	db.set("bg", "orange")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def yell():
	window['bg']= 'yellow'
	db.set("bg", "yellow")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def aq():
	window['bg']= 'aqua'
	db.set("bg", "aqua")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def gr():
	window['bg']= 'gray10'
	db.set("bg", "gray10")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')
def white():
	window['bg']= 'white'
	db.set("bg", "white")
	tkinter.messagebox.showinfo('INFO', 'цвет фона изменён!')

def webb1():
	webbrowser.open('https://classroom.google.com/u/0/h', new=2)
def webb2():
	webbrowser.open('https://www.youtube.com', new=2)
def webb3():
	webbrowser.open('https://www.flaticon.com', new=2)
def webb4():
	yourweb=db.get("web")
	webbrowser.open(yourweb)

def open1():
	app1=db.get("app1")
	os.startfile(rf'{app1}')
def open2():
	app2=db.get("app2")
	os.startfile(rf'{app2}')
def open3():
	app3=db.get("app3")
	os.startfile(rf'{app3}')

def setapp1():
	os.startfile(r'setapp1.pyw')
	window.destroy()
def setapp2():
	os.startfile(r'setapp2.pyw')
	window.destroy()
def setapp3():
	os.startfile(r'setapp3.pyw')
	window.destroy()

def hide2():
	clos.place_forget()

def setupweb():
	os.startfile(r'setupweb.pyw')
	window.destroy()

def setpin():
	os.startfile(r'setpass.pyw')

def opensysapp1():
	os.startfile(r'stopwatch.pyw')
def opensysapp2():
	os.startfile(r'klicker.pyw')
def opensysapp3():
	os.startfile(r'passwd_gen.pyw')
def opensysapp4():
	os.startfile(r'calc.pyw')
def opensysapp5():
	os.startfile(r'ttt.pyw')

window=tkinter.Tk()
window.geometry('1200x600')
window.resizable(width=False, height=False)
window.title('ZhoraOS V6.0')
backk=db.get("bg")
window['bg']=backk

window.attributes('-fullscreen', True)

txt2=tkinter.Label (window, text='Приложения и файлы:', fg='black')

bg=tk.Button(window, text='Цвет фона', height=2, width=15, command=bgbtn)

webname=db.get("webname")
setweb=tk.Button(window, text='Настроить ⚙', command=setupweb , height=1, width=12, bg='white', fg='black')

poffsys=tk.Button(window, text='Выключение SYSTEM', bg='red', height=2, width=20, fg='white', command=sysoff)
poff=tk.Button(window, text='Выключение', bg='red', height=2, width=20, fg='white', command=off)
lock=tk.Button(window, text='Заблокировать', command=lock, bg='red', height=2, width=20, fg='white')

txt1=tk.Label(window, text='Ссылки на веб-сайты:')

web1=tk.Button(window, text='Google Class', command=webb1, bg='green', height=1, width=12)
web2=tk.Button(window, text='YouTube', command=webb2, bg='red', height=1, width=12)
web3=tk.Button(window, text='Flaticon', command=webb3, bg='#32a88d', height=1, width=12)
web4=tk.Button(window, text=f'{webname}', command=webb4, bg='white', height=1, width=12, fg='black')
web5=tk.Button()

appname1=db.get("appname1")
appname2=db.get("appname2")
appname3=db.get("appname3")

opn1=tk.Button(window, text=f'{appname1}', command=open1, bg='orange', height=1, width=12)
opn2=tk.Button(window, text=f'{appname2}', command=open2, bg='aqua', height=1, width=12)
opn3=tk.Button(window, text=f'{appname3}', command=open3, bg='#4287f5', height=1, width=12)

setopn1=tk.Button(window, text='⚙', command=setapp1, bg='white', height=1, width=2)
setopn2=tk.Button(window, text='⚙', command=setapp2, bg='white', height=1, width=2)
setopn3=tk.Button(window, text='⚙', command=setapp3, bg='white', height=1, width=2)

setpin=tk.Button(window, text='⚙', command=setpin, bg='white', height=2, width=2)

hidebg=tk.Button(window, text='X', command=hide, bg='red', height=1, width=2)

a=tk.Button(window, command=r, bg='red', height=1, width=4)
b=tk.Button(window, command=b, bg='blue', height=1, width=4)
c=tk.Button(window, command=g, bg='green', height=1, width=4)
d=tk.Button(window, command=pur, bg='purple', height=1, width=4)
e=tk.Button(window, command=pink, bg='pink', height=1, width=4)
f=tk.Button(window, command=orng, bg='orange', height=1, width=4)
g=tk.Button(window, command=yell, bg='yellow', height=1, width=4)
h=tk.Button(window, command=aq, bg='aqua', height=1, width=4)
i=tk.Button(window, command=gr, bg='gray10', height=1, width=4)
j=tk.Button(window, command=white, bg='white', height=1, width=4)

sysapp1=tk.Button(window, command=opensysapp1, bg='white', height=1, width=13, text='Секундомер')
sysapp2=tk.Button(window, command=opensysapp2, bg='white', height=1, width=13, text='Кликер')
sysapp3=tk.Button(window, command=opensysapp3, bg='white', height=1, width=13, text='Генератор пароля')
sysapp4=tk.Button(window, command=opensysapp4, bg='white', height=1, width=13, text='Калькулятор')
sysapp5=tk.Button(window, command=opensysapp5, bg='white', height=1, width=13, text='Крестики нолики')

bg.pack()

opn1.place(x=1075, y=20)
opn2.place(x=1075, y=50)
opn3.place(x=1075, y=80)

setopn1.place(x=1170, y=20)
setopn2.place(x=1170, y=50)
setopn3.place(x=1170, y=80)

setpin.place(x=150, y=80)

web1.place(x=0, y=574)
web2.place(x=96,y=574)
web3.place(x=192, y=574)
web4.place(x=288, y=574)

setweb.place(x=288, y=545)

poff.place(x=0, y=0)
poffsys.place(x=0, y=40)
lock.place(x=0, y=80)

txt2.place(x=1070, y=0)
txt1.place(x=0, y=553)

sysapp1.place(x=1108, y=552)
sysapp2.place(x=1108, y=525)
sysapp3.place(x=1108, y=498)
sysapp4.place(x=1108, y=471)
sysapp5.place(x=1108, y=444)

def tick():
	watch.after(1000, tick)
	watch['text']=time.strftime('%H:%M:%S')

watch=tk.Label(window, font="Arial 10", bg='black', fg='white')
watch.place(x=1144, y=578)
tick()

db.dump()
window.mainloop()