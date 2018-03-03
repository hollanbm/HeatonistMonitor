import datetime
from selenium import webdriver
import schedule
import time
from DB.create_db import Base, Product
from sqlalchemy import create_engine
engine = create_engine("sqlite:///./DB/heatonist_monitor.db")
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def getProductInfo(browser,prod):
    browser.get(prod.url)
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
        if old_stock == prod.instock and old_price != prod.price:
            #send out price change alert
            pass
        elif old_stock == 0 and prod.instock == 1:
            #send now in stock alert
            pass
        elif old_stock == 1 and prod.instock == 0:
            #send out of stock alert
            pass

    browser.close()

def main():
    schedule.every(1).minute.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
