sample = ["apple", "Banana", "Cherry", "date", "Elderberry", "fig", "Grape", "honeydew", "Ivy", "jackfruit"]

print(sorted(sample)) #대문자 우선으로 순서대로 정렬 후, 소문자 순서대로 정렬
print(sorted(sample,key=len)) # 단어 길이가 짧은 것 부터 큰 순서대로 정렬

'''
result
['Banana', 'Cherry', 'Elderberry', 'Grape', 'Ivy', 'apple', 'date', 'fig', 'honeydew', 'jackfruit']
['fig', 'Ivy', 'date', 'apple', 'Grape', 'Banana', 'Cherry', 'honeydew', 'jackfruit', 'Elderberry']
'''
