import math
lenth = list(map(float, input().split()))
degs = list(map(float, input().split()))
deg=math.pi
x=0
z=0

for i in range(0,len(degs)):
    degs[i]=degs[i]*math.pi/180
for i in range(0,len(degs)):
    deg=deg+degs[i]-math.pi
    x=x+lenth[i]*math.cos(deg)
    z=z+lenth[i]*math.sin(deg)
print(f"{x:.3f} {z:.3f}")