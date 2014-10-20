#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = []

import kplr
import numpy as np
import matplotlib.pyplot as pl

from k2.centroid import centroid
from k2.c3k import find_centroid

client = kplr.API()
tpfs = client.target_pixel_files(mission="k2", ktc_target_type="SC",
                                 adapter=kplr.mast.k2_dataset_adapter,
                                 cls=kplr.api.K2TargetPixelFile)

m = None
datasets = []
for tpf in tpfs:
    data = tpf.read()

    times = data["TIME"]
    images = data["FLUX"]
    quality = data["QUALITY"]
    print(np.sum(quality != 0))
    if m is None:
        m = np.isfinite(times) * (quality == 0)
    else:
        m *= np.isfinite(times) * (quality == 0)

    datasets.append(images)

print(np.sum(m))

assert 0
# star = client.k2_star(202060145)
tpf = star.get_target_pixel_files()[0]
data = tpf.read()

times = data["TIME"]
images = data["FLUX"]
quality = data["QUALITY"]
m = np.isfinite(times) * (quality == 0)
times = times[m]
images = images[m]
quality = quality[m]
images[np.isnan(images)] = np.median(images[np.isfinite(images)])

cx, cy = centroid(images)
print(cx)
assert 0

img = images[10]
x, y = np.meshgrid(range(img.shape[0]), range(img.shape[1]), indexing="ij")

cx, cy = find_centroid(img)

pl.pcolor(x, y, np.log(img), cmap="gray")
pl.plot(cx + 0.5, cy + 0.5, "+r")
pl.savefig("test.png")
