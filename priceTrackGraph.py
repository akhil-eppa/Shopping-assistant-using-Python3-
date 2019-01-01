"""
Script which handles the visualising part. For now it display a graph detailing the price vs time in days.
"""

import matplotlib.pyplot as plt
import pandas as pd

DateTime = []
month = []
date = []
hour = []
price = []

try:
    w = pd.read_csv("priceHistory.csv")
    DateTime = list(w["DateTime"].values)
    price = list(w["Price"].values)
except FileNotFoundError:
    print("Error: The file is missing")
except KeyError:
    print("Error: One or more column names are incorrect.")
except:
    print("Unexpected Error.")

date = [d.split()[2] for d in DateTime]
price = [float(p) for p in price]

plt.plot(date, price)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Price History")
plt.show()