import os
import getpass

user_name = getpass.getuser()
user_input1 = os.path.join("C:\\Users",user_name,"바탕 화면")
user_input2= input("바탕화면의 검색할 파일명을 입력하세요 : ")
user_input= os.path.join(user_input1+user_input2)


for (path,dirs,files) in os.walk(user_input):
    print("path : ",path,"\n")
    print("dirs : ",dirs,"\n")
    print("files : ",files,"\n")
    print("="*50)           
    
#os.path.join: 경로(패스)명 조작에 관한 처리를 모아둔 모듈로써 구현되어 있는 함수의 하나이다. 인수에 전달된 2개의 문자열을 결합하여, 1개의 경로를 만든다. 
