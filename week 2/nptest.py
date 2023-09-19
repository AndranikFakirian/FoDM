import numpy as np
import os
os.chdir("..")
dat_dir=os.getcwd()
dat_dir+='\\week 1\\test.txt'
arr=np.genfromtxt(dat_dir, delimiter=' ', dtype= int)
dat_dir=os.getcwd()
dat_dir+='\\week 1\\test.bin'
f=open(dat_dir, 'wb')
np.save(f, arr)
#print(*np.load(dat_dir))