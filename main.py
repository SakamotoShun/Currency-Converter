# Python program to get the real-time
# currency exchange rate
import re
key= 'H0HXLOMX3NAECH11'
url_s = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='
print('Welcome to currency converter\nConvert between crypto currency and physical currency\n')
from_currency = input('What currency to convert from?: ')
to_currency = input('What currency to convert to?: ')
amount = input('How much to exchange?: ')

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = url_s + from_currency + '&to_currency=' + to_currency + '&apikey=demo' + key
r = requests.get(url)
data = r.json()
s_data = str(data)
ex_rate = re.findall('\d*\.?\d+', s_data)[5]

try:
    ex_amt = float(ex_rate) * float(amount)
except Exception as e:
    print('Number out of range, try flipping the conversion')


print('1 ' + from_currency + ' : ' + ex_rate + ' ' + to_currency)
print(amount + ' ' + from_currency + ' : ' + str(ex_amt) + ' ' + to_currency)
