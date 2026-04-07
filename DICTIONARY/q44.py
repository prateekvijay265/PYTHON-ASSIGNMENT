d1={'a':1,'b':2}
d2={'b':2,'c':3}
print({k:v for k,v in d1.items() if k not in d2})