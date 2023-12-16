import sympy as s
from sympy.physics.mechanics import *
import numpy as np
T1, T2 = dynamicsymbols('T1 T2')
T1d, T2d = dynamicsymbols('T1 T2', 1)
l1, l2, m1, m2, g = s.symbols('l1 l2 m1 m2 g')
x1=l1*s.sin(T1)
y1=-l1*s.cos(T1)
#print(x1, ' ', y1)
x2=l1*s.sin(T1)+l2*s.sin(T2)
y2=-l1*s.cos(T1)-l2*s.cos(T2)
#print(x2, ' ', y2)
v12=(l1*T1d)**2
v22=(l1*T1d)**2+(l2*T2d)**2+2*l1*l2*T1d*T2d*s.cos(T1-T2)
#print(v12, ' ', v22)
K=m1*v12/2+m2*v22/2
P=m1*g*y1+m2*g*y2
#print(K, ' ', P)
L=K-P
LM=LagrangesMethod(L, [T1, T2])
LE=LM.form_lagranges_equations()
LE=s.simplify(LE)
LE=np.array(LE)
print(LE)
with open('Equations.txt', 'w') as e:
    for i in LE:
        e.write(str(i[0])+'\n\n')