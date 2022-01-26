import numpy as np
import matplotlib.pyplot as plt
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
        if i in range(int(m / 2 - e1 + 1), int(m / 2 + e1 + 1 + bool(m % 2 == 1))) and j in range(int(n / 2 - e2 + 1), int(n / 2 + e2 + 1 + bool(m % 2 == 1))): c[i][j] = Th


def do_timestep():
    c[1:-1, 1:-1] += D * dt * (
            (c[2:, 1:-1] - 2 * c[1:-1, 1:-1] + c[:-2, 1:-1]) / dx2
            + (c[1:-1, 2:] - 2 * c[1:-1, 1:-1] + c[1:-1, :-2]) / dy2)


t0 = int(T / dt)
mfig = [0, int(t0 / 8), int(t0 / 4), int(3 * t0 / 8), int(t0 / 2), int(5 * t0 / 8), int(3 * t0 / 4), int(7 * t0 / 8),
        t0]
fignum = 0
fig = plt.figure()
for t in range(t0 + 1):
    if t in mfig:
        fignum += 1, row, index
        ax = fig.add_subplot(330 + fignum)  # column
        ax.set_axis_off()  # turn off axis
        im = ax.imshow(c.copy(), cmap=plt.get_cmap('YlOrRd'), vmin=Tc, vmax=Th)  # do thi im gan vao khung ax
        ax.set_title('{:.1f} ms'.format(t * dt * 1000))
    do_timestep()
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])  # left, bottom, witdh, height
plt.show()
fig.colorbar(im, cbar_ax)
