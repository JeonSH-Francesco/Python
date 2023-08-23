from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random, requests
from PIL import Image
import os

options=webdriver.ChromeOptions()
browser=webdriver.Chrome(options =options)
no=1

while True:
    url="https://comic.naver.com/webtoon/detail?titleId=650305&no="+str(no)
    browser.get(url)
    browser.implicitly_wait(random.randint(3,5))
    time.sleep(random.randint(3,5))
    
    image_files=[]
    file_paths=[]
    
    for img_element in browser.find_elements(By.TAG_NAME,"img"):
        image_link=img_element.get_attribute("src")
        
        if not image_link:
            continue
        if "data:image/" in image_link:
            continue
        if not image_link.startswith("https://image-comic.pstatic.net"):
            continue
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.18 Safari/537.36"
            ,"Referrer":"url"
        }
        #print(image_link)
        
        response=requests.get(image_link,headers=headers)
        response.close()
        file_path=".\\webtoon\\호랑이 형님"+str(no)+"_"+image_link.split("/")[-1]
        fd=open(file_path,"wb")
        fd.write(response.content)
        fd.close()
        file_paths.append(file_path)
        img_list = []
        height=0
     
    for file_path in file_paths:
        img = Image.open(file_path)
        print(file_path, img.width, img.height)
        # 웹툰의 가로사이즈가 690 이 아닌 썸네일일 경우 무시
        if img.width != 690:
            continue
        # 이미지리스트안에 해당 이미지 객체를 담는다        
        
        img_list.append(img)
        # 또한 이미지 파일들의 높이를 계속 더해 전체 높이를 통해 새 이미지파일을 생성하고자 한다
        height += img.height
        new_height=0
         # 새로운 이미지 파일을 생성, 가로는 690으로 고정 높이는 이전에 구한 png 파일들의 전체 높이를 더한값
        new_img=Image.new("RGB",(690,height),(256,256,256))
    for img in img_list:
        # 각각의 이미지파일을 paste 붙여넣는데 그 위치는 0에서부터 각 png 파일들의 높이를 더한 offset 결정된다
        new_img.paste(img, box = (0, new_height))
        # 각 png 파일들을 더한 offset 을 계산하기 위해 이미지파일의 높이를 더한다
        new_height += img.height
    
    new_img.save(".\\webtoon\\호랑이 형님_" + str(no) + ".png")
    new_img.close()
    for file_path in file_paths:
        os.remove(file_path)
    print("Save Finish", ".\\webtoon\\호랑이 형님_" + str(no) + ".png")
   
    no+=1
    if"&no=" not in browser.current_url:
        break
