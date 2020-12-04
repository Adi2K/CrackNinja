#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:52:38 2020

@author: aditya
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import time
from bs4 import BeautifulSoup



def search_scrape(gname,stat = 0,rel_d = 0,gtype = 0):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(executable_path='./chromedriver',options=options)
    chrome_browser.get("https://crackwatch.com/search")
    bar = chrome_browser.find_element_by_class_name('bar-search')
    bar.clear()
    for i in gname:
        bar.send_keys(i)
        time.sleep(0.08)
    bar.click()


    status_set = Select(chrome_browser.find_element_by_xpath("//div[@class='bar-grid']/select[@class='form-control bar-selector'][1]"))
    status_set.select_by_value(str(stat))
    
    date_set = Select(chrome_browser.find_element_by_xpath("//div[@class='bar-grid']/select[@class='form-control bar-selector'][2]"))
    date_set.select_by_value(str(rel_d))
    
    gametype_set = Select(chrome_browser.find_element_by_xpath("//div[@class='bar-grid']/select[@class='form-control bar-selector'][3]"))
    gametype_set.select_by_value(str(gtype))

    
    timeout = 30
    try:
        WebDriverWait(chrome_browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "game-row")))
        time.sleep(0.8)
    except TimeoutException:
        chrome_browser.quit()
    
    
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

    #chrome_browser.quit()
    return game_dict

ans = search_scrape("Halo",1,0,1)

