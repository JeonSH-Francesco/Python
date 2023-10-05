# 셀레니움 웹드라이버 모듈
from selenium import webdriver
# 셀레니움의 각 원소 의 속성 class, tag, id, name 등을 접근하기 위한 모듈
from selenium.webdriver.common.by import By
# 슬립 모듈
import time
# 랜덤 함수 모듈
import random 
# 셀레니엄 웹 드라이버 모듈 호출
browser = webdriver.Chrome()
# 에러 제어를 위한 변수
error_count = 0
# 무한으로 중고나라 접근
while True:
    try:
        # 중고나라 카페 접근
        browser.get("https://cafe.naver.com/joonggonara")
        # 화면 전체 사이즈
        browser.maximize_window()
        # 묵시적 대기
        browser.implicitly_wait(random.randint(3, 5))
        # 슬립 대기
        time.sleep(random.randint(3,5))
        break
    except Exception as e:
        error_count += 1
        # 예외처리 에러가 100번 이상 났으면
        if error_count > 100:
            # 관리자에게 문자 전송
            #sendSMS(str(e))
            # 시스템 종료
            #sys.exit()
            break
        if browser:
            # browser 닫음
            browser.close()
        # 셀레니움 웹 드라이버 재 호출
        browser = webdriver.Chrome()
# 카페 왼쪽의 사이드바를 찾아 찾고자 하는 게시판의 범위를 축소
sidebar = browser.find_element(By.ID, "group-area")
# 사이드바에서 li 태그들의 text 값이 내가 원하는 게시판 이름과 동일하면 해당 li 태그 클릭
for li in sidebar.find_elements(By.TAG_NAME, "li"):
    if len(li.text.strip()) == 0:
        continue    
    if li.text.strip() == "[도서] 소설/만화 도서":
        # li text 가 [도서] 소설/만화 도서 tag를 찾아서 해당 tag 를 클릭하여 
        # 메인 프레임에 해당 게시판을 로드한다. 
        li.click()
        browser.implicitly_wait(random.randint(3, 5))
        time.sleep(random.randint(3,5))
        break
### 중요 가운데 메인 iframe 찾음
cafe_main_frame = browser.find_element(By.ID, "cafe_main")
# 해당 iframe 으로 스위치
browser.switch_to.frame(cafe_main_frame)
count = 0
# 50개씩 변경하기 위해 select_box 클릭
select_box = browser.find_element(By.CLASS_NAME, "select_box")
select_box.click()
time.sleep(1)
# select_list 에 x개씩 접근
select_list = browser.find_element(By.CLASS_NAME, "select_list")
for li in select_list.find_elements(By.TAG_NAME, "li"):
    if len(li.text.strip()) == 0:
        continue
    if li.text.strip() == "50개씩":
        # 50개씩 찾았으면 해당 li 클릭
        li.click()
        browser.implicitly_wait(random.randint(3,5))
        time.sleep(random.randint(3,5))
        break        

sw = True
while sw:
    # article-board 의 첫번째는 공지사항 두번째는 실제 판매 게시물
    article_board = browser.find_elements(By.CLASS_NAME, "article-board")[1]
    sw = True
    # article-board 에서 tr 각 열을 탐색 하고 사용자아이디란의 tr 태그를 무시하기 위해 sw 변수를 두어
    # 한번씩 분석하고 안하고를 반복한다.
    for tr in article_board.find_elements(By.TAG_NAME, "tr"):        
        if sw:
            # 각 게시물의 번호, 게시물이름, 닉네임, 작성일, 조회수를 파악
            inner_number = tr.find_element(By.CLASS_NAME, "inner_number")
            article = tr.find_element(By.CLASS_NAME, "article")
            # 게시물이름에서 href 속성을 가져와 실제 개시내용의 URL 주소를 획득
            href = article.get_attribute("href")
            p_nick = tr.find_element(By.CLASS_NAME, "p-nick")
            td_date = tr.find_element(By.CLASS_NAME, "td_date")
            td_view = tr.find_element(By.CLASS_NAME, "td_view")
            # bot 탐지를 회피하기 위한 아래 옵션 입력
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
            
            new_browser = webdriver.Chrome(options = options)
            # 실제 게시물에 접근
            new_browser.get(href)
            new_browser.implicitly_wait(random.randint(3,5))
            time.sleep(random.randint(3,5))
            # 메인 프레임으로 이동
            cafe_main_frame = new_browser.find_element(By.ID, "cafe_main")
            new_browser.switch_to.frame(cafe_main_frame)
            # 이메일 획득을 위한 메일 클래스 접근
            mail = new_browser.find_elements(By.CLASS_NAME, "mail")
            # 전화번호 접근 위한 텔 클래스 접근
            tell = new_browser.find_elements(By.CLASS_NAME, "tell")
            # tell 클래스는 없을수있음
            if len(tell) > 0:
                # tell 클래스의 innerHTML 에 휴대전화가 있으며 마스킹 되어 있으면 안전번호임
                print(tell[0].get_attribute('innerHTML').strip())
            print(inner_number.text, article.text, p_nick.text, td_date.text, td_view.text, mail[0].get_attribute("text").strip(), href)
            new_browser.close()            
            sw = False            
        else:
            sw = True
    # 다음 페이지 선택위한 각페이지 정보가 담겨있는 prev-next 접근  
    prev_next = browser.find_element(By.CLASS_NAME, "prev-next")
    # 현재 페이지는 on class 에 존재
    current_page = prev_next.find_element(By.CLASS_NAME, "on").text
    print(current_page)
    # prev-next 에서 각 a 태그 접긎ㄴ
    for a in prev_next.find_elements(By.TAG_NAME, "a"):
        # 이전 페이지로 접근할 일이 없음
        if a.text == "이전":
            continue
        # 현재 페이지에서 10을 나눈 나머지가 0일 경우 10, 20 페이지 같은 상태이며 다음 버튼을 클릭
        # 일의자리가 1~9페이지 일 경우 해당 페이지에서 1을 더한 페이지 값을 찾아 해당 엘리먼트를 클릭하여
        # 다음 페이지로 이동
        if int(current_page) % 10 != 0 and int(current_page) + 1 == int(a.text):
            a.click()
            browser.implicitly_wait(random.randint(3,5))
            time.sleep(random.randint(3,5))
            break
        # 중고나라 게시판은 999가 마지막 페이지
        if int(current_page) == 999:
            sw = False
            break
        if int(current_page) % 10 == 0 and a.text == "다음":
            a.click()
            browser.implicitly_wait(random.randint(3,5))
            time.sleep(random.randint(3,5))
            break
    print("break")
    
'''2. 1~9 현재페이지 + 1 에해당하는 페이지를 찾고 클릭
3. 10 페이지 일경우 다음 클릭
if current_page % 10 == 0 
    next_button click
3. 21 페이지가 되면 종료
'''

# 카페의 "[도서] 소설/만화 도서" BBS 를 대상으로

browser.close()
