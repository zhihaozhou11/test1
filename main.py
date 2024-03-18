import requests
from bs4 import BeautifulSoup

def crawl_baidu():
    url = 'https://www.baidu.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

crawl_baidu()