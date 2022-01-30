import numpy as np
import matplotlib.pyplot as plt

m = int(input())
n = int(input())
dx = float(input())
dy = float(input())
D = float(input())
T = float(input())
dt = float(input())
Th = int(input())
Tc = int(input())
e1 = int(input())
e2 = int(input())
dx2, dy2 = dx * dx, dy * dy
t0 = int(T / dt)

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

mfig = [0, int(t0 / 8), int(t0 / 4), int(3 * t0 / 8), int(t0 / 2), int(5 * t0 / 8), int(3 * t0 / 4), int(7 * t0 / 8),
        t0]
fignum = 0
for t in range(t0 + 1):
    if t in mfig:
        fignum += 1
        ax = fig.add_subplot(330 + fignum)
        ax.set_axis_off()
        im = ax.imshow(c.copy(), cmap=plt.get_cmap('YlOrRd'), vmin=Tc, vmax=Th)
        ax.set_title('{:.1f} ms'.format(t * dt * 1000))
    do_timestep()
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
fig.colorbar(im, cbar_ax)
plt.show()

fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
fig.colorbar(im, cbar_ax)