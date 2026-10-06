a1=100
b1=0
c1=0
for a in range(a1, 1, -1):
    for b in range(b1,1,-1):
        for c in range(1, c1):
            price=a1*10+b1*5+c1*0.5
            if price==100 and a1+b1+c1==100:
                break
                print(f"{a1} быков, {b1} коров, {c1} телят") 
      