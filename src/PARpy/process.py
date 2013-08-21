#!/usr/bin/env python

import numpy as np
from scipy.io import loadmat
import glob
import os


def extract_mat(indir)
    for filename in sorted(glob.glob(os.path.join(indir, '*.mat'))):
        f = loadmat(filename)
        d = f['hdfdata']['Reference_Par_hyperspectral_data']
        par = d[0.0][:,2]

