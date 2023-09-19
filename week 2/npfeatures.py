import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(seed=52)
r=rng.integers(low=0, high=7, size=42)
hist, bins=np.histogram(r, bins=np.arange(8))
fig, ax = plt.subplots()
print(hist)
ax.plot(bins[:bins.size-1],hist)
plt.show()
del fig
ru=np.unique(r)
hist, bins=np.histogram(ru, bins=np.arange(8))
fig, ax = plt.subplots()
print(hist)
ax.plot(bins[:bins.size-1],hist)
plt.show()
