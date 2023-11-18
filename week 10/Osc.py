import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
F_base=input('Filename base (without file format): ')
Inp_f=F_base+'.txt'
Outp_f=F_base+'_outp.txt'
print('Writing characteristics of differential equation.')
w0=input('w0 = ')
b0=input('b0 = ')
F0=input('F0 = ')
m0=input('m0 = ')
w=input('w = ')
x0=input('x(0) = ')
v0=input('v(0) = ')
dt=input('dt = ')
T=input('T = ')
with open(Inp_f, 'w') as f:
    f.write('5 '+w0+' '+b0+' '+F0+' '+m0+' '+w+' 2 '+x0+' '+v0+' '+dt+' '+T)
sub.run(['Solver.exe', Inp_f, Outp_f])
arr=np.genfromtxt(Outp_f, dtype=float)
Nums=[0]+[i for i in range(1, 9, 3)]+[i for i in range(2, 9, 3)]
Nums.sort()
Time, Ecfx, Ecfv, Hcfx, Hcfv, RK4cfx, RK4cfv=(arr[i] for i in Nums)
fig, ax = plt.subplots()
ax.plot(Time, Ecfx, c='forestgreen', label='Elvowdfx', zorder=1)
ax.plot(Time, Hcfx, c='darkblue', label='Hlvowdfx', zorder=2)
ax.plot(Time, RK4cfx, c='goldenrod', label='RK4lvowdfx', zorder=3)
ax.legend(loc=0)
plt.show()