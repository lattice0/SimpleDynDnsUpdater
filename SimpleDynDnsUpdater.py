#To make it run on startup, clone into the home directory and put this in /etc/rc.local before 'exit' if present
#/usr/bin/python3 /home/YOUR_USERNAME/SimpleDynDnsUpdater/SimpleDynDnsUpdater.py &>> /home/YOUR_USERNAME/SimpleDynDnsUpdater/log &
#Todo: see the right >> syntax for sh, this is for bash

import requests
import time

username = 'username'
password = 'password'
hostname = 'domain.example.org'
time_to_repeat = 60*3 #3 minutes

while True:
	try:
		ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php').text
		print(ipv4)
		ip_info = '&myip=' + ipv4
		try: #See if ipv6 is supported by machine
			ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php').text
			print(ipv6)
			ip_info = '&myip=' + ipv4 + ',' + ipv6
		except Exception as e:
			print('ipv6 probably not supported')
		r = requests.get('https://members.dyndns.org/v3/update?hostname=' + hostname + ip_info, auth=(username, password))
		print(r.text)
	except Exception as e:
		print('error: ' + str(e))
	time.sleep(time_to_repeat)
