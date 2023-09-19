import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0, 2*np.pi, 1000)
x=np.sin(2*t)
y=np.cos(3*t)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()