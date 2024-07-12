sample=[3,0,1,8,7,2,5,4,6,9]



def insertionSort(data):
    for end in range(1,len(data)):
            for i in range(end,0,-1):
                  if data[i-1] > data[i]:
                        data[i-1], data[i] = data[i], data[i-1]

insertionSort(sample)
print(sample)




'''
def insertionSort(data):
      for idx in range(1,len(data)):
            i=idx
            while i> 0 and data[i-1]> data[i]:
                  data[i-1], data[i] = data[i], data[i-1]
                  i-=1

insertionSort(sample)
print(sample)


'''
