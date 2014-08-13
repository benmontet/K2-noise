#Create a movie of the frames

import numpy as np
from utils import TIME, FLUX

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

time = TIME - 1860
diffs = np.diff(FLUX, axis=0)

base = "frames/{:0>3d}.png"

bin = get_cmap("binary")
div = get_cmap("bwr")


fig, ax = plt.subplots(ncols=2, figsize=(8, 4))
img0 = ax[0].imshow(FLUX[1], cmap=bin, origin="upper")
ax[0].set_title("Frame")
cb0 = plt.colorbar(img0, ax=ax[0])
img1 = ax[1].imshow(diffs[0], cmap=div, origin="upper")
ax[1].set_title("Difference")
cb1 = plt.colorbar(img1, ax=ax[1])
ant = ax[0].annotate("{:.4f}".format(time[0]), (5,5))
fig.savefig(base.format(0))

for i, (flux, diff, time) in enumerate(zip(FLUX[1:], diffs, time[1:])):
    img0.set_data(flux)
    img0.autoscale()

    img1.set_data(diff)
    img1.autoscale()

    ant.set_text("{:.4f}".format(time))
    fig.canvas.draw_idle()
    fig.savefig(base.format(i))