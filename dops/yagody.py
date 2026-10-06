n=int(input())
yagody=list(map(int,input().split()))
k=0
for i in range(n+1):
    if i+1>len(yagody) and i<len(yagody):
       if yagody[i]+yagody[0]+yagody[i-1]>k:
            k=yagody[i]+yagody[0]+yagody[i-1]
    elif i+1>len(yagody) and i>len(yagody):    
        if yagody[0]+yagody[1]+yagody[i-1]>k:
             k=yagody[i]+yagody[i+1]+yagody[i-1]
print(k)        