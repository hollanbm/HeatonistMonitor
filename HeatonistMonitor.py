import datetime

from past.builtins import execfile
from selenium import webdriver
import schedule
import time
from DB.create_db import Base, Product
from sqlalchemy import create_engine
from twitter import *

engine = create_engine("sqlite:///./DB/heatonist_monitor.db")
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def getProductInfo(browser,prod):
    browser.get(prod.url)
    prod.name = browser.execute_script("return document.getElementsByClassName('product-details-product-title')[0].innerText")
    prod.instock = 1 if browser.execute_script("return document.getElementById('AddToCartText').innerText") != "SOLD OUT" else 0
    prod.price = browser.execute_script("return document.getElementById('ProductPrice').innerText").replace('$','')
    prod.lastupdate = datetime.datetime.today()
    session.commit()

def job():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=options)
    for prod in session.query(Product).all():
        old_stock = prod.instock
        old_price = prod.price
        getProductInfo(browser, prod)
        if old_stock is None and old_price is None:
            pass
        elif old_stock == prod.instock and old_price != prod.price:
            # send out price change alert
            createTweet('{0} PRICE CHANGE, was {1}, now {2}'.format(prod.name, old_price,prod.price))
        elif old_stock == 0 and prod.instock == 1:
            #send now in stock alert
            createTweet('{0} is now in stock'.format(prod.name))
    browser.close()

def createTweet(message):
    config = {}
    execfile("Twitter/config.py", config)

    # -----------------------------------------------------------------------
    # create twitter API object
    # -----------------------------------------------------------------------
    twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
    twitter.statuses.update(status=message)

def main():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
