#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = []

import os
import kplr
import numpy as np
from multiprocessing import Pool

from k2.centroid import centroid

base_path = "centroids"
try:
    os.makedirs(base_path)
except os.error:
    pass


def process_tpf(tpf):
    fn = os.path.join(base_path, os.path.split(tpf.filename)[1] + ".txt")
    if os.path.exists(fn):
        return
    res = centroid(tpf)
    np.savetxt(fn, np.vstack(res).T)


client = kplr.API()
tpfs = client.target_pixel_files(mission="k2", ktc_target_type="LC",
                                 adapter=kplr.mast.k2_dataset_adapter,
                                 cls=kplr.api.K2TargetPixelFile,
                                 max_records=10000)

pool = Pool()
pool.map(process_tpf, tpfs)
