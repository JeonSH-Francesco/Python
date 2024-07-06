sample = [[0,4],[0,2],[1,3],[2,1]]

def second(x):
    return x[1]

print(sorted(sample,key=second))
print(sorted(sample, key=lambda x:x[1]))


#요점은 key값에 어떤 함수를 할당하는가 입니다.
#second() 함수와 lambda x:x[1]은 모두 동일하게 동작하는 함수로, 주어진 배열의 두번째 항목을 기준으로 정렬합니다.
#second 함수와 lambda x: x[1]는 모두 동일한 동작->둘 다 sorted 함수에 전달되어 리스트를 각 내부 리스트의 두 번째 요소를 기준으로 정렬합니다.
#람다 함수는 작은 일회성 함수를 정의할 때 유용하며, 간결하게 코드를 작성할 수 있습니다.
#second 함수는 코드의 가독성을 높이고 재사용성을 제공합니다.

