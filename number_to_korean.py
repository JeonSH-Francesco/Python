import sys

def number_to_korean(number):
    units = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    tens = ['', '십', '백', '천']
    large_units = ['', '만', '억', '조', '경', '해', '자', '양', '구', '간']

    result = ''
    number = str(number)
    length = len(number)

    
    # 4자리씩 끊어서 처리
    chunks = (length + 3) // 4  # 올림 처리
   
    for i in range(chunks):
        start = length - (i + 1) * 4
        end = length - i * 4
        #print("start=",start)
        #print("end",end)
        chunk = number[max(0, start):end]
        #4자리씩 끊고
        
        #print("chunk=",chunk)
        
        # 각 chunk를 한글로 변환
        chunk_result = ''
        for j in range(len(chunk)):
            digit = int(chunk[j])
            #print("digit=",digit)
            #chunk에서 한 자리씩 끊어서 digit을 얻은 후
            unit = units[digit]
            #units에서 숫자별로 읽은 후
            #tens에서 십, 백, 천 붙인다.
            if digit != 0:
                chunk_result += unit + tens[len(chunk) - j - 1]

        # chunk의 한글 결과에 단위 추가를 하고 4자리씩 끊었을 때 그 이상의 처리가 있는 경우 chunk_result에 추가를 하여 large_units에 읽힌다.
        #여기서 tens[0]으로 되기 떄문에 상관 없음.
        if chunk_result:
            chunk_result += large_units[i]
        
        #만 이상의 단위도 다 4자리씩 끊어서 읽는 것이 완료가 되면
        # 이전 chunk 결과와 합치기
        result = chunk_result + result
        #print("result=",result)
    return result

number = int(input('숫자를 입력하세요: '))
result = number_to_korean(number)
print(result)
