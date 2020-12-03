#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:52:38 2020

@author: aditya
"""

#from Game import Game
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
chrome_browser.get("https://crackwatch.com/game/watch-dogs-legion")

timeout = 30
try:
    WebDriverWait(chrome_browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "game-title")))
except TimeoutException:
    chrome_browser.quit()

#chrome_browser.implicitly_wait(3)
page_source = chrome_browser.page_source

soup = BeautifulSoup(page_source, 'lxml')

cracked_class_name = 'status-bottom'
cracked_status = soup.find('div', class_= cracked_class_name)
status = str(cracked_status)[len(cracked_class_name)+14:-6]

top_class_name = 'status-top-right'
top_status = soup.find('div', class_= top_class_name )
top = str(top_status)[len(top_class_name)+14:-6]

game_class_name = 'game-title'
game_n = soup.find('h1', class_= game_class_name )
game_name = str(game_n)[len(game_class_name)+13:-5] #here the index number changed because it is h1 tag



print(status)
print(top)
print(game_name)


#//*[@id="react-root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]
