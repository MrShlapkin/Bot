k, n = map(int, input().split())
stranica=n//k+1    
stroka=n%k
if stroka==0: 
    stroka+=1
print(f"{stranica} {stroka}")
