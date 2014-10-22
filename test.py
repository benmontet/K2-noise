#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = []

import glob
import numpy as np
import matplotlib.pyplot as pl

fns = glob.glob("centroids/*.fits.gz.txt")
times, X = None, None
for i, fn in enumerate(fns):
    print(fn)
    t, cx, cy = np.loadtxt(fn, unpack=True)
    if times is None:
        times = t
        X = np.empty((len(fns), 2, len(times)))
    assert len(times) == len(t)
    X[i, 0, :] = cx
    X[i, 1, :] = cy
