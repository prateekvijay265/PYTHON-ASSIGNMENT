n=int(input())
for i in range(n):
 row=[1]*(i+1)
 for j in range(1,i): row[j]=prev[j-1]+prev[j]
 print(row);prev=row