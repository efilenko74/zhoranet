import os
import random
import datetime
import pickledb

base = pickledb.load('saving.db', True)
password = base.get('pass')

def handlers(command):
	'''Логика заменяемых сообщений'''
	dataitime = datetime.datetime.today()
	if dataitime.minute < 10:
		time = f'{dataitime.hour}:0{dataitime.minute}'
	else:
		time = f'{dataitime.hour}:{dataitime.minute}'

	data = f'{dataitime.year}/{dataitime.month}/{dataitime.day}'
	

	command = command.replace('!random!', str(random.randint(10000, 99999)))
	command = command.replace('!user!', 'User')
	command = command.replace('!time!', str(time))
	command = command.replace('!date!', str(data))

	return command
def cmd(command):
	'''Логика обработчика команд'''
	if command.lower() == 'help':
		print('calc [ВЫРАЖЕНИЕ] - решает пример')
		print('chat [ТЕКСТ] - выводит текст на экран')
		print('win [команда] - выполняет команды командной строки Windows')
		print('zpm install [модуль] - установщик модулей')
		print('help handlers - помощь по заменяемым сообщениям')
		print('help - Данный список\n')

	elif command.lower() == 'help handlers':
		print('!random! - Заменяеться на случайное пятизначное число')
		print('!user! - Заменяеться на имя пользователя')
		print('!time! - Замеяеться на текущее время')
		print('!date! - заменяеться на текущую дату')

	if 'chat' in command.lower():
		command = command.replace('chat', '')
		print(command)

	elif 'calc' in command.lower():
		command = command.replace('calc', '')
		print(eval(command))
		
	elif 'win' in command.lower():
		command = command.replace('win ', '')
		os.system(command)

	elif 'zpm' in command.lower():
		module(command)


def module(command):
	'''Логика менеджера пакетов zpm'''
	if 'zpm install' in command:
		module = command.replace('zpm install ', '')
		pwd = input('Пароль для User: ')
		if pwd == password:
			confirm = input(f'Вы действительно хотите скачать модуль {module}? [y/n]: ')
			if confirm.lower() == 'y':
				print('Установка модуля началась')
				try:
					os.system(f'pip install {module}')
				except Exception as e:
					print('Ошибка ' + e)
			else:
				print('Вы отменили установку')
		else:
			print('Ошибка ||| Отказано в доступе, неверный пароль!')

while True:
	try:
		command = input('User|PC [~]\n$ ')
		command = handlers(command)
		cmd(command)

	except Exception as e:
		print(e)