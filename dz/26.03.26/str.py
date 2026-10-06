k, n = map(int, input().split())
if n%k==0:
    stranica=n//k
else:
    stranica=n//k+1    
stroka=n%k
print(f"{stranica} {stroka}")