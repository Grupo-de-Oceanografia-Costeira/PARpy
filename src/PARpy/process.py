#!/usr/bin/env python

import numpy as np
from scipy.io import loadmat
from datetime import datetime
import glob
import os

hours_proc = []

def extract_mat(indir)
    for filename in sorted(glob.glob(os.path.join(indir, '*.mat'))):
        f = loadmat(filename)
        d = f['hdfdata']['Reference_Par_hyperspectral_data']
        par = d[0.0][:,2]
        dates = d[0,0][:,0]
        hours = np.int64(d[0,0][:,0])
        for hour in hours:
            hours_proc.append(datetime.strptime(str(i), "%H%M%S%f"))

