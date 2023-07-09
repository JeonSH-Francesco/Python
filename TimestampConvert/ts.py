from datetime import *

#CONSTANT
UTC_OFFSET_TIMEDELTA = datetime.utcnow()-datetime.now()

def convert_date_string_to_ts(date_string):
    #data_string format is 'YYYY/MM/DD'
    #문자열이 원소인 3인 배열
    year, month, day=[int(date_info) for date_info in date_string.split("/")]
    
    dtime = datetime(year,month,day)+UTC_OFFSET_TIMEDELTA
    ts = int(dtime.timestamp())
    return ts


#print(convert_date_string_to_ts("2023/07/09"))
print(convert_date_string_to_ts("YYYY/MM/DD"))
