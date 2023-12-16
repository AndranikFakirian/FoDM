import Builder as B
import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.animation as anim

F_base='tt'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
Theta10=30/180*np.pi
Theta20=60/180*np.pi
dTheta10=0
dTheta20=0
m1=1/100
m2=1
l1=1
l2=1/2
g=9.81
mu=m2/(m1+m2)
dt=0.01
T=10
Build=B.Builder(F_base, 'mu l1 l2 g', [mu, l1, l2, g], 't Theta10 Theta20 dTheta10 dTheta20', [0, Theta10, Theta20, dTheta10, dTheta20], dt, T)
del Build
sub.run(['Solver.exe', Inp_f, Outp_f])
with open(Outp_f) as js:
    arr=json.load(js)
x11=np.array(arr['x1'])
y11=np.array(arr['y1'])
x21=np.array(arr['x2'])
y21=np.array(arr['y2'])
x01=np.zeros(x11.shape)
y01=np.zeros(y11.shape)
x1=[x01, x11, x21]
y1=[y01, y11, y21]

Theta10=30/180*np.pi
Theta20=90/180*np.pi
dTheta10=0
dTheta20=0
m1=1/100
m2=1
l1=1
l2=1/2
g=9.81
mu=m2/(m1+m2)
dt=0.01
T=10
Build=B.Builder(F_base, 'mu l1 l2 g', [mu, l1, l2, g], 't Theta10 Theta20 dTheta10 dTheta20', [0, Theta10, Theta20, dTheta10, dTheta20], dt, T)
del Build
sub.run(['Solver.exe', Inp_f, Outp_f])
with open(Outp_f) as js:
    arr=json.load(js)
x12=np.array(arr['x1'])
y12=np.array(arr['y1'])
x22=np.array(arr['x2'])
y22=np.array(arr['y2'])
x02=np.zeros(x11.shape)
y02=np.zeros(y11.shape)
x2=[x02, x12, x22]
y2=[y02, y12, y22]

fig, ax = plt.subplots()
point01=ax.scatter(x01, y01, s=10, zorder=1)
point11=ax.scatter(x11, y11, s=10, zorder=2)
point21=ax.scatter(x21, y21, s=10, zorder=3)
pts1=ax.scatter(x21, y21, s=3, zorder=4)
lins1, =ax.plot([], [], zorder=5)

point02=ax.scatter(x02, y02, s=10, zorder=1)
point12=ax.scatter(x12, y12, s=10, zorder=2)
point22=ax.scatter(x22, y22, s=10, zorder=3)
pts2=ax.scatter(x22, y22, s=3, zorder=4)
lins2, =ax.plot([], [], zorder=5)

def init():
    lins1.set_xdata([])
    lins1.set_ydata([])
    lins2.set_xdata([])
    lins2.set_ydata([])
    return (lins1, lins2, )
def update(frame):
    p1=[i[frame] for i in x1]
    q1=[i[frame] for i in y1]
    pp1=x21[max(0, frame-9):frame-1]
    pq1=y21[max(0, frame-9):frame-1]
    data1=[np.stack([p1[i], q1[i]]).T for i in range(len(p1))]
    pdat1=np.stack([pp1, pq1]).T
    point01.set_offsets(data1[0])
    point11.set_offsets(data1[1])
    point21.set_offsets(data1[2])
    pts1.set_offsets(pdat1)
    lins1.set_xdata(p1)
    lins1.set_ydata(q1)

    p2=[i[frame] for i in x2]
    q2=[i[frame] for i in y2]
    pp2=x22[max(0, frame-9):frame-1]
    pq2=y22[max(0, frame-9):frame-1]
    data2=[np.stack([p2[i], q2[i]]).T for i in range(len(p2))]
    pdat2=np.stack([pp2, pq2]).T
    point02.set_offsets(data2[0])
    point12.set_offsets(data2[1])
    point22.set_offsets(data2[2])
    pts2.set_offsets(pdat2)
    lins2.set_xdata(p2)
    lins2.set_ydata(q2)
    return (point01, point11, point21, pts1, lins1, point02, point12, point22, pts2, lins2, )
ani=anim.FuncAnimation(fig=fig, init_func=init, func=update, frames=int(T/dt), interval=30)
ax.set_xlim(-1*1491/729, 1*1491/729)
ax.set_ylim(-2, 0)
plt.show()