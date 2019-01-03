"""
Script which handles parsing through the HTML source of the webpage, selects the price 
element and writes it along with the corresponding time to priceHistory.csv
"""

from bs4 import BeautifulSoup as bs
import requests
import datetime
import time

"""
# Writing the source code to source.txt
f = open("source.txt", 'w+')
f.write(str(soup.encode('utf-8')))
f.close()
"""

# min30 used to store a time interval of 30 minutes
min30 = datetime.timedelta(minutes = 30)

"""
Program should run for 24 hours with price being written to csv file
every 30 minutes for now.
"""
for i in range(48):
    dt = datetime.datetime.now()
    later_time = dt + min30
    while datetime.datetime.now() < later_time:
       time.sleep(1)
    
    # Change the url to that of the desired product.
    url = "https://www.amazon.in/dp/B07864V6CK/?coliid=I2K8I48NQ1X50P&colid=2TRR7D714XRU4&psc=0&ref_=lv_ov_lig_dp_it"
    r = requests.get(url)
    soup = bs(r.text,features="html.parser")

    # Selecting the price element from the source and formatting it.
    s = soup.select('#priceblock_ourprice')
    price = ""
    for char in str(s):
        if char.isdigit():
            price += char
    price = int(price)/100.0

    # Writing the price along with corresponding time to priceHistory.csv
    # The DateTime data is in the YEAR MONTH DATE DAY HOUR MINUTE SECOND MERIDIAN format.
    now = datetime.datetime.now()
    dt = now.strftime("\n%Y %B %d %A %I %M %S %p")
    with open("priceHistory.csv", 'a+') as f:
        f.write(dt + ', ' + str(price))
