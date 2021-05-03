import bs4 as bs
import urllib.request
from pprint import pprint
import time


def get_value():
    url = "https://mechanicalkeyboards.com/availability.php?sku=MY68N_1PPP88V"
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, "lxml")

    stock_states = soup.find_all("div", class_="stock_state")

    current = stock_states[3]

    print(current)
    return current


next = get_value()
current = get_value()

while next == current:
    time.sleep(60)
    next = get_value()

print("New value found!")
