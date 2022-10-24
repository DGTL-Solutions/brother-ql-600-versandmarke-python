from config import *
import shopify
import requests
from pprint import pprint
import json
from Brother600qLableGenerator import *

'''
If you want to use the shopify API you need to create an extra file called config.py
The file needs to contain the following lines:

headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': 'YOUR-API-ACCESS-TOKEN',
}

SHOP_ID = 'YOUR_SHOP_ID'

'''

response = requests.get(f"https://{SHOP_ID}.myshopify.com/admin/api/2022-10/orders.json", headers=headers)

order_list = response.json()['orders']

lable = Brother600qLableGenerator()

for item in order_list:
    pprint(item['shipping_address'])

    lable.set_address({
        "name": item['shipping_address']['first_name'],
        "surename": item['shipping_address']['last_name'],
        "street_and_housenumber": item['shipping_address']['address1'],
        "postalcode": item['shipping_address']['zip'],
        "city": item['shipping_address']['city'],
        "country": item['shipping_address']['country']
    })

    lable.generate()

    #lable.print() # disabled for testing

