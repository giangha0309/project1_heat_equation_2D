import numpy as np
import matplotlib.pyplot as plt
'''hahaha'''
m = n = 21
dx = dy = 0.1
D = 0.1
T = 1
dt = 0.01
dx2, dy2 = dx * dx, dy * dy
u = 25 * np.ones((m + 2, n + 2))

for i in range(m + 2):
    for j in range(n + 2):
        if (i in range(int(m / 2 - 4), int(m / 2 + 7)) and j in range(int(n / 2 - 4), int(n / 2 + 7))): u[i][j] = 80


def do_timestep():
    u[1:-1, 1:-1] += D * dt * (
            (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx2
            + (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dy2)
    return u


mfig = [0, 25, 55, 100]
fignum = 0
fig = plt.figure()
for t in range(int(T / dt) + 1):
    if t in mfig:
        fignum += 1
        ax = fig.add_subplot(220 + fignum)  # column, row, index
        ax.set_axis_off()  # turn off axis
        im = ax.imshow(u.copy(), cmap=plt.get_cmap('YlOrRd'), vmin=25, vmax=80)  # do thi im gan vao khung ax
        ax.set_title('{:.1f} ms'.format(t * dt * 1000))
    u = do_timestep()
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])  # left, bottom, witdh, height
fig.colorbar(im, cbar_ax)
plt.show()
