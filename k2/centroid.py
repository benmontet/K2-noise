# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = []

import numpy as np
from functools import partial
from itertools import izip, imap

from .c3k import find_centroid


def centroid(images, **kwargs):
    f = partial(find_centroid, **kwargs)
    return list(imap(np.array, izip(*(imap(f, images)))))
