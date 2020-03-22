#web scraping for airport TSA times

import requests
from bs4 import BeautifulSoup

url = 'https://orlandoairports.net/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
wait_time = soup.find("div", {"class": 'wait-time'}).get_text()
result = soup.find("h6")
#print(soup.prettify())
#print(wait_time.strip())
print(result.text)

"""
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text + company_elem.text)
    print("\n")
    print(location_elem.text) 
"""
   


def log_error(e):
    """Prints out error if occurs"""
    print(e)

