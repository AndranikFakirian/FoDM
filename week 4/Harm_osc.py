import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
print('Filename base (without file format):')
F_base=input()
Inp_f=F_base+'.txt'
Outp_f_Eul=F_base+'_Eul.txt'
Outp_f_Heun=F_base+'_Heun.txt'
Outp_f_An=F_base+'_An.txt'
print('Writing characteristics of differential equation.')
w0=input('w0 = ')
x0=input('x(0) = ')
v0=input('v(0) = ')
dt=input('dt = ')
it=input('Iterations = ')
with open(Inp_f, 'w') as f:
    f.write(w0+' '+x0+' '+v0+' '+dt+' '+it)
os.system(".\Euler_method.exe {0} {1}".format(Inp_f, Outp_f_Eul))
while not os.path.exists(Outp_f_Eul):
    pass
os.system(".\Heun_method.exe {0} {1}".format(Inp_f, Outp_f_Heun))
while not os.path.exists(Outp_f_Heun):
    pass
os.system(".\Analythic_method.exe {0} {1}".format(Inp_f, Outp_f_An))
while not os.path.exists(Outp_f_An):
    pass
arr_Eul=np.genfromtxt(Outp_f_Eul, dtype=float)
arr_Eul=np.transpose(arr_Eul)
x_Eul=arr_Eul[0]
v_Eul=arr_Eul[1]
t_Eul=arr_Eul[2]
arr_Heun=np.genfromtxt(Outp_f_Heun, dtype=float)
arr_Heun=np.transpose(arr_Heun)
x_Heun=arr_Heun[0]
v_Heun=arr_Heun[1]
t_Heun=arr_Heun[2]
arr_An=np.genfromtxt(Outp_f_An, dtype=float)
arr_An=np.transpose(arr_An)
x_An=arr_An[0]
v_An=arr_An[1]
t_An=arr_An[2]
fig, ax=plt.subplots()
ax.plot(t_Eul, x_Eul, c='forestgreen', linewidth=1, zorder=1, label='Интегрирование по Эйлеру')
ax.plot(t_Heun, x_Heun, c='gold', linewidth=3, zorder=2, alpha=0.9, label='Интегрирование по Хойну')
ax.plot(t_An, x_An, c='crimson', linewidth=1, zorder=3, label='Аналитическое решение')
ax.legend(loc=0)
ax.set_xlabel('t, с')
ax.set_ylabel('x, у.е.')
ax.set_title('Гармонический незатухающий осциллятор')
dt=t_An[-1]
dx=max(x_Eul)-min(x_Eul)
ax.set_xlim(-dt*0.005, t_An[-1]+dt*0.02)
ax.set_ylim(min(x_Eul)-0.05*dx, max(x_Eul)+0.05*dx)
ax.yaxis.set_minor_locator(tic.MultipleLocator(dx/50))
ax.xaxis.set_minor_locator(tic.MultipleLocator(dt/100))
ax.yaxis.set_major_locator(tic.MultipleLocator(dx/4))
ax.xaxis.set_major_locator(tic.MultipleLocator(dt/10))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, color='lightgrey', zorder=0, alpha=0.5)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, color='lightgrey', zorder=0, alpha=0.5)
#ax.rcParams.update({'font.size': 22})
plt.show()