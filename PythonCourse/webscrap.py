import requests
from bs4 import BeautifulSoup

url = "http://allthingslife.xyz/"

data = requests.get(url).text
print(data)

clean_data = BeautifulSoup(data)
print(clean_data)
