from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
#browser.maximize_window()
browser.get("https://m.boannews.com/html/index.html")
browser.implicitly_wait(5)
time.sleep(3)

title_list=[]
#print(len(browser.find_elements(By.CLASS_NAME,"headline4_title")))
for headline4_title in browser.find_elements(By.CLASS_NAME,"headline4_title"):
    title=headline4_title.find_element(By.TAG_NAME,"a")
    #soup.select('a')
    browser.implicitly_wait(5)
    time.sleep(3)
    title_list.append(title.get_attribute("text"))
    print(title.get_attribute("text"))
    
print(title_list)
