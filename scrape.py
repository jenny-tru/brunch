#web scraping for airport TSA times

import requests
from bs4 import BeautifulSoup

url = 'https://orlandoairports.net/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
wait_time = soup.find("div", {"class": 'wait-time'}).get_text()
#result = soup.find("span", {"class": 'gate1'}).get_text()
print(wait_time.strip())
#print (result)

def log_error(e):
    """Prints out error if occurs"""
    print(e)

