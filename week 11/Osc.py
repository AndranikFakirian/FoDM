import Builder as B
import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic

F_base='tt'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
w0=1
b0=0.1
F0=1
m0=1
x0=0
v0=0
dt=0.01
T=100
ws=[0.01, 0.1, 1, 10, 100]
for w in ws:
    Build=B.Builder(F_base, 'w0 b0 F0 m0 w', [w0, b0, F0, m0, w], 't x0 v0', [0, x0, v0], dt, T)
    del Build
    sub.run(['Solver.exe', Inp_f, Outp_f])
    with open(Outp_f) as js:
        arr=json.load(js)
    E=np.array(arr['Euler'])
    H=np.array(arr['Heun'])
    RK4=np.array(arr['RK4'])
    Time=E[0, :]
    Ecfx, Ecfv= E[1, :], E[2, :]
    Hcfx, Hcfv= H[1, :], H[2, :]
    RK4cfx, RK4cfv= RK4[1, :], RK4[2, :]
    fig, ax = plt.subplots()
    ax.plot(Time, Ecfx, c='forestgreen', label='Ecfx', zorder=1)
    ax.plot(Time, Hcfx, c='darkblue', label='Hcfx', zorder=2)
    ax.plot(Time, RK4cfx, c='goldenrod', label='RK4cfx', zorder=3)
    ax.legend(loc=0)
    ax.set_title('w = {0}, w0 = {1}'.format(w, w0))
    plt.show()