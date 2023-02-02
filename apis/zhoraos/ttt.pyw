import tkinter as tk
from tkinter import messagebox


class main():
	"""Попытка реализовать крестики-нолики номер 2!"""
	def __init__(self):
		self.w = tk.Tk()
		self.w.resizable(width=False, height=False)
		self.player = 0

		self.btn1 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step1)
		self.btn1.grid(column=1 ,row=1)
		self.btn2 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step2)
		self.btn2.grid(column=1 ,row=2)
		self.btn3 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step3)
		self.btn3.grid(column=1 ,row=3)
		self.btn4 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step4)
		self.btn4.grid(column=2 ,row=1)
		self.btn5 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step5)
		self.btn5.grid(column=2 ,row=2)
		self.btn6 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step6)
		self.btn6.grid(column=2 ,row=3)
		self.btn7 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step7)
		self.btn7.grid(column=3 ,row=1)
		self.btn8 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step8)
		self.btn8.grid(column=3 ,row=2)
		self.btn9 = tk.Button(self.w, text='', width=5, height=2, bg = '#1c1c1c', fg='#ffffff', command = self.step9)
		self.btn9.grid(column=3 ,row=3)
		self.lab = tk.Label(self.w, text='Сейчас \nходит \nкрестик')
		self.lab.grid(column=2, row=4)

		self.w.mainloop()

	def step1(self):
#Кнопка номер 1
		if self.btn1['text'] == '':
			if self.player == 0:
				self.btn1['text'] = 'X'
				self.player = 1
			else:
				self.btn1['text'] = 'O'
				self.player = 0
		self.winner()

	def step2(self):
#Кнопка номер 2
		if self.btn2['text'] == '':
			if self.player == 0:
				self.btn2['text'] = 'X'
				self.player = 1
			else:
				self.btn2['text'] = 'O'
				self.player = 0
		self.winner()

	def step3(self):
#Кнопка номер 3
		if self.btn3['text'] == '':
			if self.player == 0:
				self.btn3['text'] = 'X'
				self.player = 1
			else:
				self.btn3['text'] = 'O'
				self.player = 0
		self.winner()

	def step4(self):
#Кнопка номер 4
		if self.btn4['text'] == '':
			if self.player == 0:
				self.btn4['text'] = 'X'
				self.player = 1
			else:
				self.btn4['text'] = 'O'
				self.player = 0
		self.winner()

	def step5(self):
#Кнопка номер 5
		if self.btn5['text'] == '':
			if self.player == 0:
				self.btn5['text'] = 'X'
				self.player = 1
			else:
				self.btn5['text'] = 'O'
				self.player = 0
		self.winner()


	def step6(self):
#Кнопка номер 6
		if self.btn6['text'] == '':
			if self.player == 0:
				self.btn6['text'] = 'X'
				self.player = 1
			else:
				self.btn6['text'] = 'O'
				self.player = 0
		self.winner()


	def step7(self):
#Кнопка номер 7
		if self.btn7['text'] == '':
			if self.player == 0:
				self.btn7['text'] = 'X'
				self.player = 1
			else:
				self.btn7['text'] = 'O'
				self.player = 0
		self.winner()


	def step8(self):
#Кнопка номер 8
		if self.btn8['text'] == '':
			if self.player == 0:
				self.btn8['text'] = 'X'
				self.player = 1
			else:
				self.btn8['text'] = 'O'
				self.player = 0
		self.winner()


	def step9(self):
#Кнопка номер 9
		if self.btn9['text'] == '':
			if self.player == 0:
				self.btn9['text'] = 'X'
				self.player = 1
			else:
				self.btn9['text'] = 'O'
				self.player = 0
		self.winner()


	def  winner(self):
		if self.btn5['text'] == 'X':
			if self.btn4['text'] == 'X':
				if  self.btn6['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
			if self.btn1['text'] == 'X':
				if self.btn9['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
			if self.btn2['text'] == 'X':
				if self.btn8['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
			if self.btn7['text'] == 'X':
				if self.btn3['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
		elif self.btn5['text'] == 'O':
			if self.btn4['text'] == 'O':
				if  self.btn6['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
			if self.btn1['text'] == 'O':
				if self.btn9['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
			if self.btn2['text'] == 'O':
				if self.btn8['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
			if self.btn7['text'] == 'O':
				if self.btn3['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
		if self.btn1['text'] == 'X':
			if self.btn2['text'] == 'X':
				if self.btn3['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
			if self.btn4['text'] == 'X':
				if self.btn7['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
		if self.btn9['text'] == 'X':
			if self.btn6['text'] == 'X':
				if self.btn3['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
			if self.btn8['text'] == 'X':
				if self.btn7['text'] == 'X':
					tk.messagebox.showinfo('INFO','Победа крестика')
					self.w.destroy()
					
		if self.btn1['text'] == 'O':
			if self.btn2['text'] == 'O':
				if self.btn3['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
			if self.btn4['text'] == 'O':
				if self.btn7['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
		if self.btn9['text'] == 'O':
			if self.btn6['text'] == 'O':
				if self.btn3['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
					
			if self.btn8['text'] == 'O':
				if self.btn7['text'] == 'O':
					tk.messagebox.showinfo('INFO','Победа нолика')
					self.w.destroy()
		else:
			if self.btn9['text'] != '':
				if self.btn8['text'] != '':
					if self.btn7['text'] != '':
						if self.btn6['text'] != '':
							if self.btn5['text'] != '':
								if self.btn4['text'] != '':
									if self.btn3['text'] != '':
										if self.btn2['text'] != '':
											if self.btn1['text'] != '':
												tk.messagebox.showinfo('INFO', 'Ничья кароч')
												self.w.destroy
					
		self.hodit()


	def hodit(self):
		if self.player == 0:
			self.lab['text'] = 'Сейчас\nходит\n X'
		else: 
			self.lab['text'] = 'Сейчас\nходит\n O'



if __name__ == '__main__':
	main()