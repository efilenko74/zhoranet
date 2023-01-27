import requests
import urllib.request
import os

a=requests.get('https://efilenko74.github.io/zhoranet/apis/zhoraos/version.txt').text

if int(a)==2:
	print('Установлена актуальная версия, обновление не требуется')
	print('для выхода нажмите Enter...')
	input()
	os.startfile(r'system86.pyw')
else:
	print('Доступна новая версия, если хотите установить введите "y", если нет "n"')
	var=input(': ')
	if (var)=='y':
		print('Доступна новая версия, выполняется скачивание, подождите...')
		destination = 'system86.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/system86.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 1/9')
		destination = 'ZhoraOS.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/ZhoraOS.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 2/9')
		destination = 'setapp1.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/setapp1.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 3/9')
		destination = 'setapp2.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/setapp2.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 4/9')
		destination = 'setapp3.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/setapp3.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 5/9')
		destination = 'setpass.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/setpass.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 6/9')
		destination = 'setupweb.pyw'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/setupweb.pyw'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 7/9')
		destination = 'terminalemulator.py'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/terminalemulator.py'
		urllib.request.urlretrieve(url, destination)
		print('Dowloaded 8/9')
		destination = 'updater.py'
		url = 'https://efilenko74.github.io/zhoranet/apis/zhoraos/updater.py'
		urllib.request.urlretrieve(url, destination)
		print('Файлы загружены, обновление успешно, для выхода нажмите Enter...')
		input()
		os.startfile(r'system86.pyw')
	else:
		print('exit')
