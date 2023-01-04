import os

user_input = input("검색할 디렉토리명(전체경로)을 입력해 주세요 : ") #os.listdir(): 디렉토리 내 모든 파일을 리스트 해주는 함수
files =os.listdir(user_input)
print(files)
searchstring = input("파일 내 찾고자 하는 키워드를 입력해 주세요 : ") #input()함수를 사용하여 사용자의 디렉토리 명을 받아 user_input에 저장

#os.walk() : os.listdir()과 비슷하나, 하위 디렉토리까지 돌면서 모든 파일을 리스트 해주는 함수 

for (path,dir,files) in os.walk(user_input):      #파일들 목록에서 하나씩 꺼내서
    print(path,dir,files)
    for filename in files:
        with open(path+os.sep+filename,'r',encoding='UTF8') as f:
            try:
                if searchstring in f.read():
                    print("===========================================================")
                    print(path,os.sep+filename+"파일에 '",searchstring,"' 단어가 포함되어 있습니다.")
                else:
                    pass
                f.close()
            except:
                pass
        
#os.listdir(): 디렉토리 내 모든 파일을 리스트 해주는 함수
#os.sep : OS의 폴더 경로 구분자(윈도우는 \,/ 둘다 상관 없음)
#os.path_isfile(): 경로에 파일이 존재하면 참
#with open(file,'r')as f: 파일을 읽기 모드로 열때 사용
#encoding='UTF8' : 한글 표준으로 사용 [깨짐 방지]
#os.walk() : os.listdir()과 비슷하나, 하위 디렉토리까지 돌면서 모든 파일을 리스트 해주는 함수 
#os.listdir()함수는 자신의 첫번째 디렉토리의 모든 파일만 리스트 함.file_chekc_keyword.py
