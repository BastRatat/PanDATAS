try:
	from bs4 import BeautifulSoup
	import requests
except ImportError:
	print("package not imported")

def soup(url):
	"""
	- do a GET request
	- create a BeautifulSoup object if the GET request status is 200
	"""
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		return soup
	else:
		print('request error has occured')


