from config import *
import shopify
import requests
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

for order in order_list:

    order_id = order['id']

    lable.set_address({
        "name": order['shipping_address']['first_name'],
        "surename": order['shipping_address']['last_name'],
        "street_and_housenumber": order['shipping_address']['address1'],
        "postalcode": order['shipping_address']['zip'],
        "city": order['shipping_address']['city'],
        "country": order['shipping_address']['country']
    })

    lable.generate()
    lable.print()

    close_order_response = requests.post(f"https://{SHOP_ID}.myshopify.com/admin/api/2022-10/orders/{order_id}/close.json", headers=headers)