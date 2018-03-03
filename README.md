# HeatonistMonitor
Monitors Heatonist for stock availability

This will work for any product on the heatonist site, just switch out the URL

In order to use, you will need to update HeatonistMonitor.py and add your pushover key/token. Without these, you will not receive notifications.

This is intended to run on a linux system using docker. 
Clone repo
modify file with your pushover keys
run docker-compuse up -d


You can get this working on windows, but you will need to install chromedriver (https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) and add it to your path/



Currently working on twitter integration (beta branch). Eventually, the monitor will tweet out stock and price drop alerts
