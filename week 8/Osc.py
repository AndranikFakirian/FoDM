import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
F_base=input('Filename base (without file format): ')
Inp_f=F_base+'.txt'
Outp_f=F_base+'_outp.txt'
print('Writing characteristics of differential equation.')
w0=input('w0 = ')
x0=input('x(0) = ')
v0=input('v(0) = ')
dt=input('dt = ')
T=input('T = ')
with open(Inp_f, 'w') as f:
    f.write('1 '+w0+' 2 '+x0+' '+v0+' '+dt+' '+T)
sub.run(['Solver.exe', Inp_f, Outp_f])
arr=np.genfromtxt(Outp_f, dtype=float)
Nums=[0]+[i for i in range(1, 12, 3)]+[i for i in range(2, 12, 3)]
Nums.sort()
Time, Esox, Esov, Elvox, Elvov, Hsox, Hsov, Hlvox, Hlvov=(arr[i] for i in Nums)
fig, ax = plt.subplots()
ax.plot(Time, Esox, c='forestgreen', label='Esox')
ax.plot(Time, Elvox, c='salmon', label='Elvox')
ax.plot(Time, Hsox, c='crimson', label='Hsox')
ax.plot(Time, Hlvox, c='magenta', label='Hlvox')
ax.legend(loc=0)
plt.show()