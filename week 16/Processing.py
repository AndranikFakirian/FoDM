import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.animation as anim
import time as t

def Normalize(Phrs):
    NPhrs=[]
    for i in Phrs:
        Phr=''
        for j in i:
            Phr=Phr+str(j)
        NPhrs.append(int(Phr))
    return NPhrs
F_base='PB'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
P=10
Voc=[1, 2]
R=1000
Phrs=[]
for x in Voc:
    for y in Voc:
        Phrs.append([x, y])
NPhrs=Normalize(Phrs)
AvLenss=[]
for i in range(P):
    AvLens=[]
    for Phr in Phrs:
        JS={"R": R, "Voc": Voc, "Phr": Phr}
        with open(Inp_f, 'w') as js:
            json.dump(JS, js)
        sub.run(['test.exe', Inp_f, Outp_f])
        with open(Outp_f) as js:
            al = json.load(js)
        AvLens.append(al["AvLen"])
    AvLenss.append(AvLens)
    t.sleep(i/13)
AvLenss=np.array(AvLenss)
AvLensa=np.array([np.average(AvLenss.T[i]) for i in range(len(Phrs))])
#print(AvLensa)
AvLenserr=np.sqrt(abs(np.array([np.average(np.square(AvLenss.T[i])) for i in range(len(Phrs))])-np.square(AvLensa)))
#print(AvLenserr)
AvLensmin=AvLensa-AvLenserr
AvLensmax=AvLensa+AvLenserr
fig, ax=plt.subplots(1, 2)
ax[0].plot(NPhrs, AvLensa)
#ax[0].errorbar(Ns, PBsa, PBserr)
ax[0].fill_between(NPhrs, AvLensmin, AvLensmax, alpha=0.5)
#ax[0].plot(Ns, PBsan)
ax[1].plot(NPhrs, AvLenserr)
plt.show()