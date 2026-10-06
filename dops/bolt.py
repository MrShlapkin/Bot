k1,l1,m1=map(int, input().split())
k2,l2,m2=map(int, input().split())
u1=k1*l1/100*m1
u2=k2*l2/100*m2
u_obsh1=u1+u2
k1=k1-(k1*l1/100)
k2=k2-(k2*l2/100)
if k1>k2:
    u_obsh2=(k1-k2)*m1
elif k1<k2:
    u_obsh2=(k2-k1)*m2
else:
    u_obsh2=0      
print(int(u_obsh1+u_obsh2))