import sys
import requests
import os
import urllib3
from colorama import Fore

#verify if the host is vulnerable to off-by-one

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

banner ='''

+++   +++ ++++  +++       +++  ++++++       +++++     
+++   ++   ++     ++     ++    ++    ++   ++     ++
++ +  ++   ++      ++   ++     ++     ++  ++     ++
++  + ++   ++       ++ ++      +++++++    ++     ++
++   +++   ++      ++   ++     ++         ++     ++
+++   +++ ++++  +++       +++  ++           +++++

            Fuck you all motherfuckers!
                    
					
'''

print(Fore.RED+banner) 



if len(sys.argv) != 2:
	print('Not enough arguments for the function')
	sys.exit()
if sys.argv[1].endswith("/"):
	print('Remove last slash of the host URL')
	sys.exit()

test_host= sys.argv[1]


def host_ffchk(hst):
	proto = ['http://', 'https://']
	dirs = ['/assets/','/static/','/exploit/', '/api/', '/js/']
	cfil = ['settings.py', 'nginx.conf', '', '', '', '']
	host_args = hst.strip(' /')

	for pr in proto:
		try:
			for di in dirs:
		    		uri = pr + host_args + di
					req = requests.get(uri, timeout=4.0, verify=False)
					print('Host answer: {}'.format(req.status_code))
		else:  
			continue
	
					
'''					
			if req.status_code == 403:
		   		print('Host returned 403 code. Could be vulverable. Making more tests')
		   		uri = proto + host_args + '/' + di.strip('/') + '../'
		   		req = requests.get(uri, timeout=4.0, verify=False)
			if req.status_code == 200:
		   		print('\t [+] HOST HAS VULNERABLE ENDPOINT IN  ''{}'.format(uri))
			with open ('./nginx_vulnerable_endpoints.txt', 'a+') as results: 
		     			results.write(uri+'\n')
		     
		     
		except requests.exceptions.HTTPError:
			if req.status_code == 404 or req.status_code == 502:
	           		continue 
		except requests.exceptions.ConnectionError:
			continue
			print('\t {}: Excessive retries:'.format(protocol))
	
		except requests.exceptions.Timeout:
			continue
			print('\t {} Max timeout exceeded:'.format(protocol))
		
		else:
			continue

try:
	print(Fore.BLUE+"Testing host : [{}]". format(test_host))
	host_ffchk(test_host)
except Exception as err:
	print(Fore.RED+'## Fatal error! ## [{}]  .... Skipping ...'. format(err))'''
	
	
    except KeyboardInterrupt:
		print('Interrupted by user request')
		sys.exit(0)
