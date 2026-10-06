k=int(input())
N=list(map(int, input().split()))
for i in range(0,k):
   h=N[i]
   if h<=437:
      print(f"Crash {i+1}")
      break
   else:
      if i==k-1:
         print("No crash")   