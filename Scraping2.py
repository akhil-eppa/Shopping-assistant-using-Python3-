"""
My attempt at parsing the HTML source of a sample amazon product.
"""

from bs4 import BeautifulSoup as bs
import requests

url = "https://www.amazon.in/dp/B07864V6CK/?coliid=I2K8I48NQ1X50P&colid=2TRR7D714XRU4&psc=0&ref_=lv_ov_lig_dp_it"
price = ""

r = requests.get(url)
soup = bs(r.text, 'html.parser')

"""
# Writing the source code to source.txt
f = open("source.txt", 'w+')
f.write(str(soup.encode('utf-8')))
"""

# Selecting the price element from the source and fortmatting it.
s = soup.select('#priceblock_ourprice')
for char in str(s):
    if char.isdigit():
        price += char

price = int(price)/100.0
print("The price is", price)