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

#->td 태그는 0이 되서 나온다.
#switching을 해 줘야 된다.
print(len(browser.find_elements(By.TAG_NAME,"td")))
for td in browser.find_elements(By.TAG_NAME,"td"):
    print(td.text)

sw=True
#현재 페이지를 찾는다.
while sw:
    article_board=browser.find_elements(By.CLASS_NAME,"article-board")[1]
    sw=True
    for tr in article_board.find_elements(By.TAG_NAME,"tr"):
        
        if sw:
            inner_number=tr.find_element(By.CLASS_NAME,"inner_number")
            article=tr.find_element(By.CLASS_NAME,"article")
            href=article.get_attribute("href")
            p_nick=tr.find_element(By.CLASS_NAME,"p-nick")
            td_date=tr.find_element(By.CLASS_NAME,"td_date")
            td_view=tr.find_element(By.CLASS_NAME,"td_view") 
            print(inner_number.text, article.text, p_nick.text, td_date.text, td_view.text, href)
            new_browser=webdriver.Chrome()
            new_browser.get(href)
            
            browser.implicitly_wait(random.randint(3,5))
            time.sleep(random.randint(3,5))
            
            cafe_main_frame = new_browser.find_element(By.ID,"cafe_main")
            new_browser.switch_to.frame(cafe_main_frame)
            
            mail=new_browser.find_elements(By.CLASS_NAME,"mail")
            tell=new_browser.find_elements(By.CLASS_NAME,"tell")
            print(len(mail),len(tell))
            
            if len(mail)>0:
                print(mail[0].get_attribute("text"))
            if len(tell)>0:
                print(tell[0].get_attribute("innerHTML").strip())
            #print(mail.text,tell.text)
            sw=False
        else:
            sw=True    

#2. 1~9일 경우 현재 페이지 +1에 해당하는 페이지를 찾고 클릭
#3. 10페이지 일 경우 다음 클릭
#4. 마찬가지

input()


#카페에 BBS(Bulletin Board System)
browser.close()



'''
 prev_next = browser.find_element(By.CLASS_NAME,"prev-next")
    current_page = browser.find_element(By.CLASS_NAME,"on").text
    print(current_page)
    
    for a in prev_next.find_elements(By.TAG_NAME,"a"):
        if a.text=="이전":
            continue
        if int(current_page)%10 !=0 and int(current_page)+1 ==int(a.text):
            a.click()
            browser.implicitly_wait(random.randint(3,5))
            time.sleep(random.randint(3,5))
            break
        if(int(current_page)%10==0 and a.text=="다음"):
            a.click()
            browser.implicitly_wait(random.randint(3,5))
            time.sleep(random.randint(3,5))
            break

'''
