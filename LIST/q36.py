lst = [1,2,2,3]
seen = set()
res = []
for x in lst:
    if x not in seen:
        res.append(x)
        seen.add(x)
print(res)