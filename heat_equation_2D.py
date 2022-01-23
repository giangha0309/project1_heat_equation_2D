import numpy as np
import matplotlib.pyplot as plt
'hahah'
m = n = 21
dx = dy = 0.1
D = 0.1
T = 1
dt = 0.01
dx2, dy2 = dx * dx, dy * dy
c = 25 * np.ones((m + 2, n + 2))

for i in range(m + 2):
    for j in range(n + 2):
        if i in range(6, 17) and j in range(6, 17): c[i][j] = 80


def do_timestep():
    c[1:-1, 1:-1] += D * dt * (
            (c[2:, 1:-1] - 2 * c[1:-1, 1:-1] + c[:-2, 1:-1]) / dx2
            + (c[1:-1, 2:] - 2 * c[1:-1, 1:-1] + c[1:-1, :-2]) / dy2)
    return c


mfig = [0, 10, 20, 30, 40, 50, 60, 70, 100]
fignum = 0
fig = plt.figure()
for t in range(101):
    if t in mfig:
        fignum += 1
        ax = fig.add_subplot(330 + fignum)  # column, row, index
        ax.set_axis_off()  # turn off axis
        im = ax.imshow(c.copy(), cmap=plt.get_cmap('YlOrRd'), vmin=25, vmax=80)  # do thi im gan vao khung ax
        ax.set_title('{:.1f} ms'.format(t * dt * 1000))
    c = do_timestep()
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])  # left, bottom, witdh, height
fig.colorbar(im, cbar_ax)
plt.show()
