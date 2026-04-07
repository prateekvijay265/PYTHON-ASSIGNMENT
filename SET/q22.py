s=set()
for i in range(2,20):
    if all(i%j for j in range(2,i)):
        s.add(i)
print(s)