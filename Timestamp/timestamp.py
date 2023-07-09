from datetime import *

#CONSTANT
UTC_OFFSET_TIMEDELTA = datetime.utcnow()-datetime.now()

def convert_date_string_to_ts(date_string):
    #data_string format is 'YYYY/MM/DD'
    #문자열이 원소인 3인 배열
    #List Comprehension=>리스트를 생성하기 위해 반복문과 조건문을 결합하여 간결하게 작성하는 방법
    #year, month,day 각각의 변수는 int(date_info)로 변환된 값을 받습니다.
    #date_info는 date_string.split("/")로 분리한 결과로
    #date_info = ["2023","07","09"]가 됩니다. 
    # 따라서 int(date_info)는 date_info를 정수형으로 변환되어 변수에 할당됨.    
    year, month, day=[int(date_info) for date_info in date_string.split("/")]
        
    dtime = datetime(year,month,day)+UTC_OFFSET_TIMEDELTA
    ts = int(dtime.timestamp())
    return ts


#print(convert_date_string_to_ts("2023/07/09"))
print(convert_date_string_to_ts("YYYY/MM/DD"))
