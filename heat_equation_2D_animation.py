import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
11
11
0.1
0.1
0.1
1
0.01
80
25
3
3
"""
m = int(input())  # 21
n = int(input())  # 11
dx = float(input())  # 0.1
dy = float(input())  # 0.1
D = float(input())  # 0.1
T = float(input())  # 1
dt = float(input())  # 0.01
Th = int(input())
Tc = int(input())
e1 = int(input())  # 5
e2 = int(input())  # 3

dx2, dy2 = dx * dx, dy * dy
c = Tc * np.ones((m + 2, n + 2))

for i in range(m + 2):
    for j in range(n + 2):
        if i in range(int(m / 2 - e1 + 1), int(m / 2 + e1 + 1 + bool(m % 2 == 1))) and j in range(int(n / 2 - e2 + 1),
                                                                                                  int(n / 2 + e2 + 1 + bool(
                                                                                                      m % 2 == 1))):
            c[i][j] = Th


def do_timestep():
    c[1:-1, 1:-1] += D * dt * (
            (c[2:, 1:-1] - 2 * c[1:-1, 1:-1] + c[:-2, 1:-1]) / dx2
            + (c[1:-1, 2:] - 2 * c[1:-1, 1:-1] + c[1:-1, :-2]) / dy2)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axis_off()
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
fig.subplots_adjust(right=0.85)


def animate(i):
    do_timestep()
    im = ax.imshow(c.copy(), cmap=plt.get_cmap('YlOrRd'), vmin=Tc, vmax=Th)
    fig.colorbar(im, cbar_ax)
    return im


anim = FuncAnimation(fig, animate, np.arange(0, int(T / dt + 1)), interval=10, repeat=0, save_count=200)
anim.save('test.mp4')
plt.show()
