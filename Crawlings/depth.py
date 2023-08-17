from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random
import sys

#url = sys.argv[1]
url="https://www.boannews.com"
depth = 2
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options = options)


def get_urls(url, hrefs, dp, total_hrefs, check_hrefs):
    
    hrefs.append([])
    browser.get(url)
    print(url + " 접속 [dp = "+str(dp)+"]" )
    if dp >= depth:
        return 0    
    browser.implicitly_wait(random.randint(1,1))
    time.sleep(random.randint(1,1))

    href = url
    for a in browser.find_elements(By.TAG_NAME, "a"):
        try:
            href = a.get_attribute("href")
            if href.startswith("http://") or href.startswith("https://"):
                if(href not in total_hrefs):
                    hrefs[int(dp)].append(href)
                    total_hrefs.append(href)
        except:
            continue
    
    for href in hrefs[int(dp)]:
        if(dp < depth and (href not in check_hrefs)):
            check_hrefs.append(href)
            get_urls(href, hrefs, dp+1, total_hrefs, check_hrefs)
        

hrefs = []
total_hrefs = []
check_hrefs = []
get_urls(url, hrefs, 0, total_hrefs, check_hrefs)
