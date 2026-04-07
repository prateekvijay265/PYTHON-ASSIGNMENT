lst = [1,2,2,3]
d = {}
for x in lst:
    d[x] = d.get(x,0)+1
print(d)