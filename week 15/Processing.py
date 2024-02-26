import json
import subprocess as sub
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.animation as anim

F_base='PB'
Inp_f=F_base+'.json'
Outp_f=F_base+'_outp.json'
K=10
Ns=range(10, 100, 10)
R=100
PBs=[]
PBsT=[]
for N in Ns:
    JS={"K": K, "N": N, "R": R}
    with open(Inp_f, 'w') as js:
        json.dump(JS, js)
    sub.run(['test.exe', Inp_f, Outp_f])
    with open(Outp_f) as js:
        pb=json.load(js)
    PBs.append(pb["PB"])
fig, ax=plt.subplots()
ax.plot(Ns, PBs)
plt.show()