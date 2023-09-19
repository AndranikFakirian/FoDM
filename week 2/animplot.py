import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
t=np.linspace(0, 10, 100)
vy=20.0
g=-9.81
h=g*t**2/2+vy*t
fig, ax = plt.subplots()
trace=ax.scatter(t, h, s=10, c='crimson')
def update(frame):
    x=t[:frame]
    y=h[:frame]
    data=np.stack([x, y]).T
    trace.set_offsets(data)
    return trace
an=anim.FuncAnimation(fig=fig, func=update, frames=100, interval=50)
plt.show()
