v='aeiou';st='hello';s=set()
for c in st:
    if c not in v:s.add(c)
print(s)