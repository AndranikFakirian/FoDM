import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.animation as anim
import scipy.optimize as so
import time as t
import math as m

def Gauss(x, *p):
    x0, sigma = p
    return 1/(sigma*m.sqrt(2*np.pi))*np.exp(-(x-x0)**2/(2.*sigma**2))
F_base='Offset'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
PB=0.5
NumSteps0=1
NumSteps1=1000
StepNumSteps=10
NumStepss=range(NumSteps0, NumSteps1, StepNumSteps)
Bords=1000
Rep=1000
'''AvC=[]
AvModC=[]
AvSqrC=[]'''
JS={"R": Rep, "N0": NumSteps0, "N1": NumSteps1, "SN": StepNumSteps, "PB": PB, "B": Bords}
with open(Inp_f, 'w') as js:
    json.dump(JS, js)
sub.run(['BRandWalks.exe', Inp_f, Outp_f])
with open(Outp_f) as js:
    Walks = json.load(js)
Coordss=np.array(Walks["Coordss"])
EndCoords=np.array(Coordss[-1])
Hist, Bins = np.histogram(EndCoords, bins=range(-100, 100))
EndCoordsMin=np.min(EndCoords)
EndCoordsMax=np.max(EndCoords)
DEndCoords=EndCoordsMax-EndCoordsMin
AvModC=np.average(EndCoords)
AvCErr=m.sqrt(np.average(np.square(EndCoords))-(np.average(EndCoords))**2)
X=np.linspace(EndCoordsMin-int(DEndCoords*0.1), EndCoordsMax+int(DEndCoords*0.1), 10000)
Y=1/(AvCErr*m.sqrt(np.pi*2))*np.exp(-np.square(X-AvModC)/(2*AvCErr**2))
BC=(Bins[1:]+Bins[:-1])/2
p0=[AvModC, AvCErr]
coeff, var_matrix = so.curve_fit(Gauss, BC, Hist/(Rep), p0=p0)
Hist_fit=Gauss(np.array(BC), *[i for i in coeff])
fig, ax = plt.subplots()
#ax.plot(Reps, AvCErr)
ax.plot(X, Y)
ax.stairs(Hist/(Rep*m.sqrt(np.pi*m.sqrt(2))), Bins)
ax.plot(BC, Hist_fit)
plt.show()
'''for i in range(Shape[0]):
    AvC.append(np.average(Coordss[i]))
    AvModC.append(np.average(np.abs(Coordss[i])))
    AvSqrC.append(np.average(np.square(Coordss[i])))
Coordss=Coordss.T
AvC=np.array(AvC)
AvModC=np.array(AvModC)
AvSqrC=np.array(AvSqrC)
NumStepss=np.array(NumStepss)'''
'''fig, ax = plt.subplots(3, 1)
ax[0].scatter(NumStepss, AvC)
ax[1].plot(NumStepss, AvModC)
ax[2].scatter(NumStepss, AvSqrC)
plt.show()'''
'''fig, ax = plt.subplots()
for i in range(Rep):
    ax.scatter(NumStepss, Coordss[i])
plt.show()'''
'''P=10
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
plt.show()'''