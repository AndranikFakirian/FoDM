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
print('w0 =', end=' ')
w0=input()
print('x(0) =', end=' ')
x0=input()
print('v(0) =', end=' ')
v0=input()
print('dt =', end=' ')
dt=input()
print('Iterations =', end=' ')
it=input()
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
arr_Heun=np.genfromtxt(Outp_f_Heun, dtype=float)
arr_Heun=np.transpose(arr_Heun)
x_Heun=arr_Heun[0]
v_Heun=arr_Heun[1]
arr_An=np.genfromtxt(Outp_f_An, dtype=float)
arr_An=np.transpose(arr_An)
x_An=arr_An[0]
v_An=arr_An[1]
fig, ax=plt.subplots()
ax.plot(x_Eul, c='forestgreen', linewidth=1, zorder=1)
ax.plot(x_Heun, c='gold', linewidth=2, zorder=2)
ax.plot(x_An, c='crimson', linewidth=1, zorder=3)
plt.show()