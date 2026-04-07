lst = [3,1,5,2]
max_idx = 0
for i in range(len(lst)):
    if lst[i] > lst[max_idx]:
        max_idx = i
print(max_idx)