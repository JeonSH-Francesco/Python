import os

user_input=input("검색할 디렉터리 명을 입력하세요 : ")
files=os.listdir(user_input)

for (path,dir,files) in os.walk(user_input): 
    for file in files:
        name, ext = os.path.splitext(file)
        file_path = os.path.join(path,file)
        if ext =='.pdf':
            print("Find PDF File : ", file_path)
