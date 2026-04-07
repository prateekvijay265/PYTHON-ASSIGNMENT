from collections import Counter
d={'a':1,'b':2,'c':2}
print(Counter(d.values()).most_common(2)[1][0])