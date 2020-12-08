#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:52:38 2020

@author: aditya
"""

from Game import Game

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from bs4 import BeautifulSoup

from chrome_b import chrome_browser


def search_game(link):

    chrome_browser.get(link)
    
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

    g1 = Game(game_name , cracked_status, top_status, release_date, crack_date,protection, scene, price_dict, follow_count, link)

    return g1



