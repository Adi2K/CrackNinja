#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:52:38 2020

@author: aditya
"""


from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from chrome_b import chrome_browser
import time
from bs4 import BeautifulSoup

def search_scrape(gname,stat = 0,rel_d = 0,gtype = 0):




    bar = chrome_browser.find_element_by_class_name('bar-search')
    bar.clear()
    for i in gname:
        bar.send_keys(i)
        # time.sleep(0.08)
    bar.click()

    time.sleep(1)

    timeout = 10
    try:
        WebDriverWait(chrome_browser, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, "game-row-release-date")))
        time.sleep(1)
    except TimeoutException:
        #Exceptions needs to be handled properly
        chrome_browser.quit()
        return 1

    page_source = chrome_browser.page_source 
    soup = BeautifulSoup(page_source, 'lxml')
    
    game_dict = {}
    site = "https://crackwatch.com"
    
    game_sel_class_name = 'main-title main-title-cap'
    games_selector = soup.find_all('div', class_=game_sel_class_name)
    for game_selector in games_selector:
        atag = game_selector.find('a')
        link = atag.get('href')
        name = atag.get_text()
        game_dict[name] = site+link

    return game_dict

# ans = search_scrape("Halo",1,0,1)

