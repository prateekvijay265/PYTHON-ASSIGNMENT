lst = [1,2,3,4,5]
n = 2
chunks = [lst[i:i+n] for i in range(0,len(lst),n)]
print(chunks)