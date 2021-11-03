import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import *
from function import *


page =133 # initializing the first page for scraping
 # Below is the link to all first page of the mobile adverts.
mobile = "https://tonaton.com/en/ads/ghana/mobile-phones?sort=date&order=desc&buy_now=0&urgent=0&page="

while page < 250:
    
    # The mobile search page
    first_page = get_page_link(mobile, page)
    
    # This gets the whole page data
    soup = get_soup(first_page)

    # this by inspection, this code gets the all the apartment listings and saves the object in a listings variable
    listings = soup.find_all("li", class_="normal--2QYVk gtm-normal-ad") 

   
    
    size = '/1000/1000/fitted.jpg'
    page_list = []
    for links in listings:
        for link in links.find_all("a"):
            if link['href'] != '/en/promotions':
                page_list.append(link['href'])
    #ad_list=[]
    for ads in page_list:
        advert = listing_page_link(ads)
        #ad_list.append(advert)
        ad_soup = get_soup(advert)
        if len(ad_soup.findAll('img')) == 0:
            continue
        elif len(ad_soup.findAll('img')[0].attrs.keys()) <2:
            continue
        text = ad_soup.find("div", class_="title-container--1PPnS").text.split('Posted on ')
        name = text[0]
        price = int(''.join(ad_soup.find("div", class_="amount--3NTpl").text.split()[1].split(',')))
        condition = ad_soup.find("div", class_="word-break--2nyVq value--1lKHt").text
        location = text[1].split(',')[1].strip()
        region = text[1].split(',')[2].strip()
        image = ad_soup.findAll('img')[0].attrs['src'][:-19] + '600/600/fitted.jpg'
        tim = text[1].split(',')[0][7:]
        dt= datetime.strptime(tim, '%I:%M %p')
        times = dt.time()
        dat = text[1].split(',')[0][:6] + ', 2021'
        dt = parse(dat)
        dates = dt.strftime('%Y-%m-%d')
        link = advert
        vendor = 'Tonaton'
        print(name)
        print(price)
        print(condition)
        print(location)
        print(region)
        print(image)
        print(times)
        print(dates)
        print(link)
        print(' ')
        print(' ')


        vendor = 'Tonaton'

        connection, cur = create_connection()
        with connection:
            query = "SELECT id FROM search_region where region='{}'".format(region)
            cur.execute(query)
            if len(cur.fetchall()) == 0:
                continue
            region_id = get_region_id(region, cur)
            condition_id = get_condition_id(condition, cur)
            vendor_id = get_vendor_id(vendor, cur)
            if link_url(link, cur) == None:
                insert_data(name, price, location, image, link, times, dates, condition_id, region_id, vendor_id, cur)
                print( "{} has been inserted into the database ".format(name))
                print("  ")
            else:
                print('Item Already exists')
    


    print(" ")
    print('Page ' + str(page) + ' completed')
    print(" ")
    print(" ")
    print(" ")
    page = page + 1