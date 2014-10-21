# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = ["centroid"]

import numpy as np
from functools import partial
from itertools import izip, imap

from .c3k import find_centroid


def centroid(tpf, **kwargs):
    # Load the data.
    data = tpf.read()
    times = data["TIME"]
    images = data["FLUX"]
    quality = data["QUALITY"]

    # Get rid of the bad times based on quality flags.
    m = np.isfinite(times) * (quality == 0)
    images[~m, :] = np.nan

    f = partial(find_centroid, **kwargs)
    return [times] + list(imap(np.array, izip(*(imap(f, images)))))
