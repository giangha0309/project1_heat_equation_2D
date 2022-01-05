import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
giang = 100
m = n = 21
dx = dy = 0.1
D = 0.1
T = 1
dt = 0.01
dx2, dy2 = dx*dx, dy*dy
u = 25 * np.ones((m + 2, n + 2))

for i in range(m + 2):
    for j in range(n + 2):
        if(i in range(int(m / 2 - 4), int(m / 2 + 7)) and j in range(int(n / 2 - 4), int(n / 2 + 7))): u[i][j] = 80

def do_timestep(temp):
    temp[1:-1, 1:-1] += D * dt * (
            (temp[2:, 1:-1] - 2 * temp[1:-1, 1:-1] + temp[:-2, 1:-1]) / dx2
            + (temp[1:-1, 2:] - 2 * temp[1:-1, 1:-1] + temp[1:-1, :-2]) / dy2)
    return temp

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axis_off()
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7]) # left, bottom, witdh, height
fig.subplots_adjust(right=0.85)

def animate(i):
    temp = do_timestep(u)
    im = ax.imshow(temp.copy(), cmap = plt.get_cmap('YlOrRd'), vmin = 25, vmax = 80)
    fig.colorbar(im, cbar_ax)
    return im

anim = FuncAnimation(fig, animate, np.arange(0, 100), interval=10, repeat=0)
plt.show()
