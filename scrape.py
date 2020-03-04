#web scraping for airport TSA times

import requests
from bs4 import BeautifulSoup

def get_website(url):
    """Attemptes to get content at url with HTTP get req and return content """
    page = requests.get('https://orlandoairports.net/')
    print(page)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        print(html)

def log_error(e):
    """Prints out error if occurs"""
    print(e)

