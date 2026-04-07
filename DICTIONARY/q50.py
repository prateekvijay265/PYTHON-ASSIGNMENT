d={'a':1,'b':2}
print(all(isinstance(v,(int,float)) for v in d.values()))