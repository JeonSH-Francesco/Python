user_input=str(input("Enter a binary number : "))

#사용자가 입력한 문자를 토대로 2진법으로 변환해서
result=int(user_input,2)
#바로 2진법을 int 함수를 통해 10진법으로 출력
print(f"{user_input} in decimal {result}")

# 사용자 입력을 정수로 변환
decimal_input = int(user_input)

# 이진법으로 변환하여 결과 출력
binary_output = bin(decimal_input)[2:]  # bin 함수를 사용하여 이진법으로 변환하고, '0b' 부분을 제외
#10진법을 bin 함수를 통해 2진법으로 출력
print(f"{decimal_input} in binary: {binary_output}")
