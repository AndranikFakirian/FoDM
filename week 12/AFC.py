import Builder as B
import AFC_funcs as AFC
import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import scipy.interpolate as si

F_base='tt'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
w0=1
b0=2**(1/2)
F0=1
m0=1
x0=0
v0=0
dt=0.1
T=1000
ws=[i for i in np.linspace(0.1, 2, 50)]
A=[]
for w in ws:
    Build=B.Builder(F_base, 'w0 b0 F0 m0 w', [w0, b0, F0, m0, w], 't x0 v0', [0, x0, v0], dt, T)
    del Build
    sub.run(['Solver.exe', Inp_f, Outp_f])
    with open(Outp_f) as js:
        arr=json.load(js)
    RK4=np.array(arr['RK4l'])
    Time, RK4cfx, RK4cfv=RK4[0, :],  RK4[1, :], RK4[2, :]
    A.append(AFC.Ampl(Time, RK4cfx))
Spline=si.CubicSpline(ws, A)
wss=np.linspace(ws[0]-ws[-1]*0.02, ws[-1]*1.02, 10000)
spline=Spline(wss)
fig, ax = plt.subplots()
ax.scatter(ws, A, marker='+', s=200)
ax.plot(wss, spline, alpha=0.5)
plt.show()