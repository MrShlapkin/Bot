k=1
n=int(input())
if n==0:
    k=1
else:     
    for i in range(1,n+1):
        k=k*i
print(k)    