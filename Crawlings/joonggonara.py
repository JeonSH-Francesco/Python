from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

browser = webdriver.Chrome()
browser.get("https://cafe.naver.com/joonggonara.cafe")
browser.implicitly_wait(random.randint(3,5))
time.sleep(random.randint(3,5))

#hrefs=[]

sidebar=browser.find_element(By.ID,"group-area")
for li in sidebar.find_elements(By.TAG_NAME,"li"):
    if len(li.text.strip())==0:
        continue
    if li.text.strip()=="[도서] 인문/교양 도서":
        browser.implicitly_wait(random.randint(3,5))
        time.sleep(random.randint(3,5))
        li.click()
        #print(li.text,len(li.text),haslib.md5(li.text.encode("utf-8")).hexdigest())
        break

cafe_main_frame=browser.find_element(By.ID,"cafe_main")
browser.switch_to.frame(cafe_main_frame)

print(len(browser.find_elements(By.TAG_NAME,"td")))
for td in browser.find_elements(By.TAG_NAME,"td"):
    print(td.text)
#->td 태그는 0이 되서 나온다.
#switching을 해 줘야 된다.



input()


#카페에 BBS(Bulletin Board System)
browser.close()
