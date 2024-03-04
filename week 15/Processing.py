import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.animation as anim
import time as t

def AnSalv(K, Nmin, Nmax):
    AR=1
    R=0
    ANS=np.unique(np.array(range(1, K+1)))
    p1=[[]]
    p2=[[]]
    PB=[]
    for i in range(1, Nmax+1):
        AR*=K
        R*=K
        for j in p1:
            for h in range(1, K+1):
                p2.append(j+[h])
            del p2[p2.index(j)]
        p1=p2.copy()
        inds=[]
        for j in p1:
            if np.array_equal(np.unique(np.array(j)),ANS):
                R+=1
                inds.append(j)
        for j in inds:
            del p1[p1.index(j)]
            del p2[p2.index(j)]
        if (i>=Nmin):
            PB.append(R/AR)
    return PB
F_base='PB'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
P=10
K=4
Nmin=4
Nmax=9
Ns=range(Nmin, Nmax, 1)
R=100000
PBss=[]
#PBsan=AnSalv(K, Nmin, Nmax-1)
for i in range(P):
    PBs = []
    for N in Ns:
        JS={"K": K, "N": N, "R": R}
        with open(Inp_f, 'w') as js:
            json.dump(JS, js)
        sub.run(['test.exe', Inp_f, Outp_f])
        with open(Outp_f) as js:
            pb=json.load(js)
        PBs.append(pb["PB"])
    PBss.append(PBs)
    t.sleep(i/13)
PBss=np.array(PBss)
PBsa=np.array([np.average(PBss.T[i]) for i in range(len(Ns))])
#print(PBsa)
PBserr=np.sqrt(abs(np.array([np.average(np.square(PBss.T[i])) for i in range(len(Ns))])-np.square(PBsa)))
#print(PBserr)
PBsmin=PBsa-PBserr
PBsmax=PBsa+PBserr
fig, ax=plt.subplots(1, 2)
ax[0].plot(Ns, PBsa)
#ax[0].errorbar(Ns, PBsa, PBserr)
ax[0].fill_between(Ns, PBsmin, PBsmax, alpha=0.5)
#ax[0].plot(Ns, PBsan)
ax[1].plot(Ns, PBserr)
plt.show()