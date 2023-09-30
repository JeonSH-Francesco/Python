import time, random

#주어진 숫자부터 9단까지 출력
def printAllTimeTable(time):
    for start in range(time,10):
        for multiply in range(10):
            print("%d x %d = %d"%(start,multiply,start*multiply))
    print("1 end\n")

#주어진 숫자의 단만 출력
def printTimeTable(time):
    for i in range(10):
        print("%d x %d = %d"%(time,i,time*i))
    print("2 end\n")   

data=[random.randrange(1,10) for i in range(1000)] # X개의 무작위 숫자 생성
startTime=time.time()

#n단 구구단 출력
for num in data:
    printTimeTable(num)
print("----------------------------")
print('elapsed time : %f' %(time.time()-startTime))
print("----------------------------")

#주어진 숫자의 9단까지만 출력하는 경우 1번 입력하고 9번 연산을 수행합니다.
#입력이 10만 개라면 10만개 x 9이고 이는 곧, 9n이므로 O(n)으로 나타낼 수 있습니다.

startTime=time.time()

#n단~9단 구구단 출력
for num in data:
    printAllTimeTable(num)
print("----------------------------")
print('elapsed time : %f' %(time.time()-startTime))
print("----------------------------")


#또한 주어진, 숫자부터 9단까지 출력하는 함수의 경우 1~9 중 하나의 값이 필요하므로, 최악의 경우를 상정하여
#1이 입력이라면 10만개 x 9 x 9 = 81n 이므로, O(n)으로 표시할 수 있습니다. 평균적으로 45n
