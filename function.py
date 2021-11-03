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


# this function creates the url for jiji 
def url_maker(url_base, number):
    url = url_base + str(number)
    return url


# This function creates the connection to the database
def create_connection():
    import psycopg2
    connection = psycopg2.connect(user="postgres",
                              password="STpass@9",
                              host="localhost",
                              port="5432",
                              database="phone")
    cur =connection.cursor()
    return connection, cur
    

# ths functions gets the id for region    
def get_region_id(region, cur):
    query = "SELECT id FROM search_region where region='{}'".format(region)
    cur.execute(query)
    key = cur.fetchone()[0]
    return key
    

# ths functions gets the id for condition  
def get_condition_id(condition, cur):
    query = "SELECT id FROM search_condition where condition='{}'".format(condition) 
    cur.execute(query)
    key = cur.fetchone()[0]
    return key


# ths functions gets the id for site  
def get_vendor_id(vendor, cur):
    query = "SELECT id FROM search_vendor where vendor='{}'".format(vendor)
    cur.execute(query)
    key = cur.fetchone()[0]
    return key


# this function inserts the data into the database
def insert_data(name, price, location,image, link, time, date, condition_id, region_id, vendor_id, cur):
    quer = "INSERT INTO search_phone(name, price, location, image, link, time, date, condition_id, region_id, vendor_id)"
    val = "VALUES('{}', {}, '{}', '{}', '{}', '{}', '{}', {}, {}, {})".format(name, price, location, image, link, time, date, condition_id, region_id, vendor_id)
    query = quer+val
    cur.execute(query)
    print('Data Inserted')
    return

# this function checks to see if 
def link_url (link, cur):
    query = "SELECT link FROM search_phone where link ='{}'".format(link)
    cur.execute(query)
    key = cur.fetchone()
    return key

# This function gets the url for the jiji site
def url_maker(url_base, number):
    url = url_base + str(number)
    return url