
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
chrome_browser = webdriver.Chrome(executable_path='./chromedriver', options=options)