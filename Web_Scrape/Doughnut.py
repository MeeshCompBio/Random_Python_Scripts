from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import datetime

'''This is just a script to check when a douhnut shop is going to open...'''

# set your site and user
site = "https://www.duckdonuts.com/location/woodbury-mn/"
hdr = {'User-Agent': 'Mozilla/5.0'}

# Initialize current results since it has not opened yet
current = []

# This will always be true so it will run contantly
while True:
    # pull request and page contents
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    # Subset by the class that has locations current status
    news = soup.find_all(class_='location-news__inner')
    update = soup.find_all(class_='location-news__check-back')

    # initilaize the current object from first scrape
    if current == []:
        current = update = soup.find_all(class_='location-news__check-back')
        print(current)
        # Wait until tomorrow to check
        time.sleep((24*3600))
    # If the status has not changed it will equal new scrape
    else:
        if current == update:
            print("No doughnuts yet", datetime.datetime.now(), sep="\t")
            time.sleep((24*3600))
        else:
            # I could set up mail server, I just wanted to do this for fun
            print("Order doughnuts", datetime.datetime.now(), sep="\t")
