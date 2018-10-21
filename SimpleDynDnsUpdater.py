import requests
import time

username = 'username'
password = 'password'
hostname = 'domain.example.com'
time_to_repeat = 60*3 #3 minutes
enable_ipv6 = False #On docker you might not have ipv6 and thus get an error instead of updating things. Can somebody correct that for me?

while True:
        try:
                ipv4 = requests.get('http://v4.ipv6-test.com/api/myip.php').text
                print(ipv4)
                if not enable_ipv6:
                        r = requests.get('https://members.dyndns.org/v3/update?hostname=' + hostname + '&myip=' + ipv4, auth=(username, password))
                        print(r.text)
                else:
                        ipv6 = requests.get('http://v6.ipv6-test.com/api/myip.php').text
                        print(ipv6)
                        r = requests.get('https://members.dyndns.org/v3/update?hostname=' + hostname + '&myip=' + ipv4 + ',' + ipv6, auth=(username, password))
                        print(r.text)
        except Exception as e:
                print('error: ' + str(e))
        time.sleep(time_to_repeat)
