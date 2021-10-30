import requests
from bs4 import BeautifulSoup

# this function gets the link for each page and returns it
def get_page_link(link, pages):
    page_link = link + str(pages)
    return page_link

# this function gets the link for each property
def listing_page_link(href):
    property_page = 'https://tonaton.com' + str(href)
    return property_page

# this function makes a request to get the page parses it through beautiful soup and returns the content
def get_soup(link):
    req = requests.get(link)
    src = req.content
    soup = BeautifulSoup(src, "lxml")
    return soup