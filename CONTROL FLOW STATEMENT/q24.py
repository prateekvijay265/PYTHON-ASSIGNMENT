n=int(input());p=[1]*(n+1)
p[0]=p[1]=0
for i in range(2,int(n**0.5)+1):
 if p[i]:
  for j in range(i*i,n+1,i):p[j]=0
print([i for i in range(n+1) if p[i]])