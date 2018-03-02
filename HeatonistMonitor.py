from selenium import webdriver
from pushover import Client
import schedule
import time


def isAvailable(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    cart_text = browser.execute_script("return document.getElementById('AddToCartText').innerText")
    browser.close()
    return cart_text != 'SOLD OUT'

def job():
    last_dab_url = 'https://heatonist.com/collections/hot-ones-hot-sauces/products/hot-ones-the-last-dab-reaper-edition'
    if isAvailable(last_dab_url):
        #MAKE SURE TO UPDATE THIS FILE WITH THE PUSHOVER KEY/TOKEN
		pushoverUserKey = "pushover user key goes here"
		pushoverApiToken = "pushover api token goes here"
		client = Client(pushoverUserKey, api_token=pushoverApiToken)
        client.send_message(last_dab_url, title="Last Dab Available")

def main():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


main()
