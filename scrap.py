#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:52:38 2020

@author: aditya
"""

from Game import Game
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from bs4 import BeautifulSoup
#import time


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
chrome_browser = webdriver.Chrome(executable_path='./chromedriver',options=options)
chrome_browser.get("https://crackwatch.com/game/halo-spartan-assault")

timeout = 30
try:
    WebDriverWait(chrome_browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "game-title")))
except TimeoutException:
    chrome_browser.quit()


#chrome_browser.implicitly_wait(3)
page_source = chrome_browser.page_source

soup = BeautifulSoup(page_source, 'lxml')

cracked_class_name = 'status-bottom'
cracked_status = soup.find('div', class_= cracked_class_name).get_text()


top_class_name = 'status-top-right'
top_status = soup.find('div', class_= top_class_name ).get_text()


game_class_name = 'game-title'
game_name = soup.find('h1', class_= game_class_name ).get_text()


data_class_name = 'info-data'
Data_finder = soup.find_all('div', class_=data_class_name)
release_date = Data_finder[0].get_text()
crack_date = Data_finder[1].get_text()
protection = Data_finder[2].get_text()
scene = Data_finder[3].get_text()


follower_class_name = 'follow-counter'
follow_count = soup.find('div',class_= follower_class_name ).get_text()


price_dict = {}
offer_class_name = 'game-box-hot-buy-btn'
store_selectors = soup.find_all('div', class_=offer_class_name)
for store_selector in store_selectors:
    atag = store_selector.find('a')
    store_name = atag.get('href').split("?",1)[0][28:]
    price = store_selector.find('div', class_='inline-block').get_text()
    price_dict[store_name] = price

#here we are only getting the partial price list for the full price list we will have to use selenium



print("Name : ",game_name)
print("Status :",cracked_status)
print("Top Status : ",top_status)
print("Release Date : ",release_date)
print("Crack Date : ",crack_date)
print("Protection : ",protection)
print("Scene Group : ",scene)
print("Followers : ",follow_count)

print("Prices :")
for p in price_dict.items():
    print(p)


g1 = Game(game_name , cracked_status, top_status, release_date, crack_date,protection, scene, price_dict, follow_count,"https://crackwatch.com/game/halo-spartan-assault")

#//*[@id="react-root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]
##react-root > div > div.App > div:nth-child(2) > div > div > div.container > div:nth-child(1) > div.sc-bxivhb.cMJOaY > div.game-page-header-over > div:nth-child(2) > div.sc-ifAKCX.eWTlLz > div.grid > div:nth-child(1) > div.info-data
#https://crackwatch.com/goto/uplay-shop