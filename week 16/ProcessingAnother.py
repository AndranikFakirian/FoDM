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
def Freq(Res, Phr):
    Res1=Res.copy()
    Num=0
    while (len(Res1)>0):
        Sl=Res1[: len(Phr)]
        if (Sl!=Phr):
            del Res1[0]
        else:
            Num+=1
            for i in range(len(Phr)):
                del Res1[0]
    return Num
F_base='Freq'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
P=20
Voc=[1, 2, 3]
N=1000
Phrs=[]
for x in Voc:
    for y in Voc:
        for z in Voc:
            Phrs.append([x, y, z])
NPhrs=Normalize(Phrs)
Freqss=[]
for i in range(P):
    Freqs=[]
    JS={"N": N, "Voc": Voc}
    with open(Inp_f, 'w') as js:
        json.dump(JS, js)
    sub.run(['testAnother.exe', Inp_f, Outp_f])
    with open(Outp_f) as js:
        data=json.load(js)
    Res=data["Res"]
    for j in Phrs:
        Freqs.append(Freq(Res, j))
    Freqss.append(Freqs)
    t.sleep(i / 13)
Freqss=np.array(Freqss)
Freqsa=np.array([np.average(Freqss.T[i]) for i in range(len(Phrs))])
#print(Freqsa)
Freqserr=np.sqrt(abs(np.array([np.average(np.square(Freqss.T[i])) for i in range(len(Phrs))])-np.square(Freqsa)))
#print(Freqserr)
Freqsmin=Freqsa-Freqserr
Freqsmax=Freqsa+Freqserr
fig, ax=plt.subplots(1, 2)
ax[0].scatter(NPhrs, Freqsa)
#ax[0].errorbar(Ns, PBsa, PBserr)
#ax[0].fill_between(NPhrs, Freqsmin, Freqsmax, alpha=0.5)
#ax[0].plot(Ns, PBsan)
ax[1].plot(NPhrs, Freqserr)
plt.show()
'''
AvLenss=[]
for i in range(P):
    AvLens=[]
    for Phr in Phrs:
        JS={"N": N, "Voc": Voc}
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
plt.show()'''