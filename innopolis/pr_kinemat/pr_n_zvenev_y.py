import math
h=float(input())
gamma=float(input())
lenth = list(map(float, input().split()))
degs = list(map(float, input().split()))
deg=math.pi
x=0
y=0
z=h

gamma=gamma*math.pi/180
for i in range(0,len(degs)):
    degs[i]=degs[i]*math.pi/180
for i in range(0,len(degs)):
    deg=deg+degs[i]-math.pi
    x=x+lenth[i]*math.cos(deg)
    y=y+lenth[i]*math.cos(deg)
    z=z+lenth[i]*math.sin(deg)
print(f"{x*math.cos(gamma):.3f} {y*math.sin(gamma):.3f} {z:.3f}")