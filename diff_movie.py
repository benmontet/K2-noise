#Create a movie of the frames

import numpy as np
from utils_simple import TIME, FLUX, QUALITY

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

#Limit ourselves 10-40 for more detail
FLUX = FLUX[:, 15:35, 15:35]

time = TIME - 1860
diffs = np.diff(FLUX, axis=0)

base = "frames/{:0>3d}.png"

bin = get_cmap("binary")
div = get_cmap("bwr")

def update_qual(qual):
    if qual == 0:
        qual_ant.set_text("")
    else:
        qual_ant.set_text("{:d}".format(qual))
        qual_ant.set_color("red")

fig, ax = plt.subplots(ncols=2, figsize=(8, 4))
img0 = ax[0].imshow(FLUX[1], cmap=bin, origin="upper", interpolation="none", extent=[15, 35, 35, 15])
ax[0].set_title("Frame")
cb0 = plt.colorbar(img0, ax=ax[0])
img1 = ax[1].imshow(diffs[0], cmap=div, origin="upper", interpolation="none", extent=[15, 35, 35, 15])
scale = np.max(np.abs(diffs[0]))
img1.set_clim(-scale, scale)
ax[1].set_title("Difference")
cb1 = plt.colorbar(img1, ax=ax[1])
ant = ax[0].annotate("{:.4f} [BJD - 2456684]".format(time[0]), (17,17), size="x-small")
qual_ant = ax[0].annotate("", (31,17), size="x-small")
update_qual(QUALITY[0])
fig.canvas.draw_idle()
fig.savefig(base.format(0))

for i, (flux, diff, time, qual) in enumerate(zip(FLUX[1:], diffs, time[1:], QUALITY[1:])):
    img0.set_data(flux)
    img0.autoscale()
    ant.set_text("{:.4f} [BJD - 2456684]".format(time))

    img1.set_data(diff)
    scale = np.max(np.abs(diff))
    img1.set_clim(-scale, scale)
    update_qual(qual)

    fig.canvas.draw_idle()
    fig.savefig(base.format(i+1))