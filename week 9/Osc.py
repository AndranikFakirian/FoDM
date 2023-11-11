import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
'''def Period(t, p):
    tt=[]
    for i in range(p.size-1):
        if (p[i]*p[i-1]<=0):
            tt.append(t[i])
        if len(tt)==2:
            break
    return 2*(tt[1]-tt[0])'''
F_base=input('Filename base (without file format): ')
Inp_f=F_base+'.txt'
Outp_f=F_base+'_outp.txt'
print('Writing characteristics of differential equation.')
w0=input('w0 = ')
b0=input('b0 = ')
x0=input('x(0) = ')
v0=input('v(0) = ')
dt=input('dt = ')
T=input('T = ')
with open(Inp_f, 'w') as f:
    f.write('2 '+w0+' '+b0+' 2 '+x0+' '+v0+' '+dt+' '+T)
sub.run(['Solver.exe', Inp_f, Outp_f])
arr=np.genfromtxt(Outp_f, dtype=float)
Nums=[0]+[i for i in range(1, 12, 3)]+[i for i in range(2, 12, 3)]
Nums.sort()
Time, Elvowdfx, Elvowdfv, Hlvowdfx, Hlvowdfv, RK4lvowdfx, RK4lvowdfv, Anlvowdfx, Anlvowdfv=(arr[i] for i in Nums)
fig, ax = plt.subplots()
ax.plot(Time, Elvowdfx, c='forestgreen', label='Elvowdfx', zorder=1)
ax.plot(Time, Hlvowdfx, c='darkblue', label='Hlvowdfx', zorder=2)
#ax.plot(Time, RK4lvowdfx, c='goldenrod', label='RK4lvowdfx', zorder=3)
ax.plot(Time, Anlvowdfx, c='crimson', label='Anlvowdf', zorder=4)
ax.legend(loc=0)
plt.show()
