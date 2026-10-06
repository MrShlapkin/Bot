import math

L1, L2, h = map(float, input().split())
x, y, z = map(float, input().split())

gamma = math.atan2(y,x)
s = math.hypot(x,y)
z_ = z-h
d = math.hypot(s,z_)
beta = math.acos((L1*L1 + L2*L2 - d*d)/(2*L1*L2))
delta = math.atan2(z_,s)
psi = math.atan2(L2*math.sin(beta), L1 - L2*math.cos(beta))
alpha=delta+psi
print(f"{math.degrees(alpha):.3f} {math.degrees(beta):.3f} {math.degrees(gamma):.3f}")