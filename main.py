from Brother600qLableGenerator import *

'''
Example
'''

lable = Brother600qLableGenerator()

lable.set_address({
    "name": "Testname",
    "surename": "Testnachname",
    "street_and_housenumber": "Blablubstraße 10",
    "postalcode": "12345",
    "city": "Musterstadt",
    "country": "Deutschland"
})

lable.generate()

lable.print()

