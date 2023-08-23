from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from konlpy.tag import *

from socket import *

kkma = Kkma()
browser = webdriver.Chrome()
browser.get("https://n.news.naver.com/article/comment/088/0000828242")
browser.implicitly_wait(5)
time.sleep(3)


while True:
    try:
        btn_more = browser.find_element(By.CLASS_NAME, "u_cbox_btn_more")
        if not btn_more:
            break
        btn_more.send_keys(Keys.END)
        btn_more.click()
        time.sleep(1)        
    except:
        break
    

    
for c_box_area in browser.find_elements(By.CLASS_NAME, "u_cbox_area"):
    try:
        nick = c_box_area.find_element(By.CLASS_NAME, "u_cbox_nick")
        date = c_box_area.find_element(By.CLASS_NAME, "u_cbox_date")        
        try:
            contents = c_box_area.find_element(By.CLASS_NAME, "u_cbox_contents")
        except:
            contents = None
        if not contents:
            
            try:
                contents = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cleanbot_contents")
            except:
                contents = c_box_area.find_element(By.CLASS_NAME, "u_cbox_delete_contents")
            
        recomm = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cnt_recomm")
        unrecomm = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cnt_unrecomm")
        #print(kkma.pos(contents.text))
        print(nick.text, date.text, contents.text, recomm.text, unrecomm.text)
        #btn = c_box_area.find_element(By.CLASS_NAME, "u_cbox_btn_totalcomment")
        #btn.click()
        #time.sleep(7)
        #close_btn = c_box_area.find_element(By.CLASS_NAME, "u_cbox_userpage_closeicont")
        
        
    except:
        continue
# '''
# for btn in browser.find_elements(By.CLASS_NAME, "u_cbox_btn_totalcomment"):
#     try:
#         btn.click()
#         browser.implicitly_wait(5)        
#         webdriver.ActionChains(browser).key_down(Keys.ESCAPE).perform()
#     except:
#         pass
# '''

# # fd=open("a.csv","a")
# # fd.write('"","" ,"" , , ')
# # fd.close()
# # input()
