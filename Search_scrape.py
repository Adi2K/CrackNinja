#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:52:38 2020

@author: aditya
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
chrome_browser = webdriver.Chrome(executable_path='./chromedriver',options=options)
chrome_browser.get("https://crackwatch.com/search")
bar = chrome_browser.find_element_by_class_name('bar-search')
bar.clear()
gname = "Counter Strike"
for i in gname:
    bar.send_keys(i)
    time.sleep(0.08)
bar.click()

time.sleep(1)   #time to load the result in the driver

page_source = chrome_browser.page_source


    
soup = BeautifulSoup(page_source, 'lxml')

game_dict = {}
site = "https://crackwatch.com"

    
games_selector = soup.find_all('div', class_='main-title main-title-cap')
for game_selector in games_selector:
    atag = game_selector.find('a')
    link = atag.get('href')
    name = atag.get_text()
    game_dict[name] = site+link


for g in game_dict.items():
    print(g)

