from lib2to3.pgen2 import driver
from time import sleep, strftime
from random import randint, randrange
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart


chromedriver_path = YOUR_CHROME_DRIVER_PATH + 'chromedriver_win32/chrimedriver.exe'

driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)


kayak = "" # kayak URL for scraping

 #closing popup - Starting with the most complex xpath
xp_popup_close = ''
driver.find_element_by_xpath(xp_popup_close)[5].click()

# demonstrate

# load more results to maximize
def load_more():
    try:
        more_results = ''
        driver.find_element_by_xpath(more_results).click()
        print('sleeping.....')
        sleep(randint(25, 35))
    except:
        pass
    
    
    
    # demonstrate
    
more_results = ''
driver.find_element_by_xpath(more_results)

def start_kayak(city_from, city_to, date_start, date_end)

#The main function. This is what activates the bot. 
#city_from, city_too : string(airport IATA codes, three letters)
#date_start, date_end : string(date format is YYYY-MM-DD)

kayak = ('https://_link_goes_here'+ city_from +'_' + city_to +
        '/' + date_start + '-flexible/' + date_end + '-flexible?sort=bestflight_a')
driver.get(kayak)
sleep(randint(8, 10))

try:
    xp_popup_close. = '//body/div[@id='XPXL']/div[@id='c_yKF']/main[@id='c_yKF-pageContent']/div[@id='XPXL-fd']/div[@id='c32lp']/div[@id='AvTv']/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]'
    driver.find_element_by_xpath()[5].click()
except Exception as e:
    pass
sleep(randint(60,95))
print('loading more ......')

#  LOAD MORE()

print('starting first scrape......')
df_flights_best = page_scrape()
df_flights_best['sort'] = 'best'
sleep(randint(60,80))


#get the lowest prices from the matrix on top 