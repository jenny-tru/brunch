#web scraping for airport TSA times

import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())



""" 
def get_website(url):
    #Attemptes to get content at url with HTTP get req and return content
    page = requests.get('https://orlandoairports.net/')
    soup = BeautifulSoup(page.content, 'html5lib')
    # print(soup)
    wait_time = []
    # soup.find()
    return;
 """

def log_error(e):
    """Prints out error if occurs"""
    print(e)

