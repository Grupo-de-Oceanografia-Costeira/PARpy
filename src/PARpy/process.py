#!/usr/bin/env python

import numpy as np
from scipy.io import loadmat
from datetime import datetime
import glob
import os


def extract_mat(indir):
    dicts = []
    d = {}

    for filename in sorted(glob.glob(os.path.join(indir, '*.mat'))):
        f = loadmat(filename)
        print filename
        dat = f['hdfdata']['Reference_Par_hyperspectral_data']
        par = dat[0,0][:,2]
        dates = dat[0,0][:,0]
        hours = np.int64(dat[0,0][:,0])

        d['name'] = filename
        d['par'] = par
        d['dates'] = dates
        d['hours'] = []

        for hour in hours:
            if len(str(hour)) == 3:
                d['hours'].append(datetime.strptime(str(hour)+'0', "%H%M%S%f"))
            else:
                d['hours'].append(datetime.strptime(str(hour), "%H%M%S%f"))

        if d:
            dicts.append(d)
        d = {}

        
    return dicts
