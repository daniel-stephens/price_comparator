from function import *
from datetime import datetime
from datetime import date

import requests

def url_maker(url_base, number):
    url = url_base + str(number)
    return url

base = "https://jiji.com.gh/api_web/v1/listing?po=6.2&lsmid=1634035073706&webp=true&slug=mobile-phones&page="
number = 49

while number > 0:
    site = url_maker(base, number)
    r = requests.get(site)
    items = r.json()
    for data in items['adverts_list']['adverts']:
        name = data['title']
        price = int("".join(data['price_obj']['view'].split()[1].split(',')))
        condition = data['attributes'][0][1]
        location = data['region_name']
        region = data['region_parent_name']
        link = 'https://jiji.com.gh' + data['url']
        image = data['image_obj']['url']
        
        dates = date.today().strftime("%Y-%m-%d")
        times = datetime.now().strftime("%H:%M:%S")
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

        vendor = "Jiji"

        if region == None:
            continue
        
        if "Region" in region:
            region = region[-7]

    

        if "NEW" in condition.upper():
            condition  = 'New'

        elif "USED" in condition.upper():
            condition = 'Used'

        else:
            continue



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
    
        
        
        
    print(' ')
    print(' ')
    print('page ' + str(number) + ' completed')
    number = number - 1
