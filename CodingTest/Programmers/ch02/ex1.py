from random import choices
from collections import Counter

data= choices(range(1,10), k=10000)
data1=sorted(data)
print(data1)


data1_counts = Counter(data1)

for number, count in data1_counts.items():
    print(f"숫자 {number}는 {count}번 나타납니다.")
