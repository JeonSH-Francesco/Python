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
#"cafe_main" ID를 가진 iframe 요소를 식별하고 WebDriver의 포커스를 이 iframe으로 전환합니다. 이로써 이후 작업이 iframe 내에서 수행됩니다..

#iframe 내에서 <td> 요소의 수를 계산하고 출력한 다음 각 <td> 요소의 텍스트 내용을 반복하여 출력합니다.
print(len(browser.find_elements(By.TAG_NAME,"td")))
for td in browser.find_elements(By.TAG_NAME,"td"):
    print(td.text)
#->td 태그는 0이 되서 나온다.
#switching을 해 줘야 된다.



input()


#카페에 BBS(Bulletin Board System)
browser.close()
