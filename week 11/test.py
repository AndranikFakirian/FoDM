import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

r1=[1, 1, 0]
r2=[0, 1, 1]
r3=[1, 0, 1]
Xs=[r1[0], r2[0], r3[0]]
Ys=[r1[1], r2[1], r3[1]]
Zs=[r1[2], r2[2], r3[2]]

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.scatter(Xs, Ys, Zs)

plt.show()
vecs=[[0, 0, 0, 1, 2, 3], [0, 0, 0, 3, 1, 2], [0, 0, 0, 2, 3, 1]]
X, Y, Z, U, V, W=zip(*vecs)
del fig
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])

plt.show()
