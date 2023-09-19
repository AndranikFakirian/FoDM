import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir("..")
dat_dir=os.getcwd()
dat_dir+='\\week 1\\test.txt'
arr=np.genfromtxt(dat_dir, delimiter=' ', dtype= int)
dat_dir=os.getcwd()
dat_dir+='\\week 1\\stdvector.bin'
fiboarr=np.fromfile(dat_dir, sep=' ', dtype=int)
fig, ax = plt.subplots()
ax.scatter(np.arange(arr.size), arr, s=10)
plt.show()
del fig
fig, ax = plt.subplots()
ax.plot(np.arange(fiboarr.size), fiboarr, linewidth=2, c='forestgreen')
plt.show()
del fig
fig, ax = plt.subplots()
narr=fiboarr*arr[:fiboarr.size]
ax.hist(narr, color='gold')
plt.show()