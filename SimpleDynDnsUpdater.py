import requests
import time

username = 'username'
password = 'password'
hostname = 'hostname.example.com'
time_to_repeat = 60*3 #3 minutes
#ipv4 = '123.456.789.012'
#ipv6 = '2001:1ab8:2102:f4c1:ca0e:145f:2ee9:8366'

while True:
	try:
		ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php').text
		print(ipv4)
		ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php').text
		print(ipv6)
		#ipv4v6 = requests.get('http://v4v6.ipv6-test.com/api/myip.php').text
		#print(ipv4v6)

		r = requests.get('https://members.dyndns.org/v3/update?hostname=' + hostname + '&myip=' + ipv4 + ',' + ipv6, auth=(username, password))
		print(r.text)
	except Exception as e:
		print('error: ' + e)
	time.sleep(time_to_repeat)
