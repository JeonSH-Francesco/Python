from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random

# 크롬 웹 브라우저를 오픈한다
browser=webdriver.Chrome()
# 특정 페이스북에 접근한다
browser.get("https://www.facebook.com/HeungMinSonOfficial/?locale=ko_KR")
# 묵시적대기
browser.implicitly_wait(random.randint(3,5))
time.sleep(random.randint(3,5))
# 로그인 창 닫기 클릭
#현재 브라우저의 스크롤 크기를 가져온다.
current_height=browser.execute_script("return document.body.scrollHeight")

while True :
    # 브라우저를 0, 세로길이 로 이동하여 자동으로 페이지를 추가 로딩
    browser.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    #5초 대기
    time.sleep(5)
    # 브라우저의 바디를 찾고 키보드의 END 버튼을 눌러 페이지를 추가 로딩
    browser.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
    # 추가로딩 후 세로길이를 다시 찾는다
    height = browser.execute_script("return document.body.scrollHeight")
    print(current_height, height)
    #만약 기존 새로 길이와 현재 새로 길이를 찾은 후 비교하여 같다면 로딩이 없는 것으로 판단
    if current_height == height:
        #무한 반복문을 탈출
        break
    #현재 길이를 기존 새로 길이에 대입
    current_height = height
    
for element in browser.find_elements(By.CLASS_NAME,"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"):
    print(element.text)

input()



# browser.execute_script('''var a = document.getElementsByClassName("x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f");for(i = 0; i < a.length; i++){if(a[i].innerText == "더 보기"){a[i].click();}}''')

# input()
    
    

#browser.find_elements(By.CLASS_NAME, "MyView-module__link_login___HpHMW")[0]
#browser.find_elements(By_CLASS_NAME,"")


