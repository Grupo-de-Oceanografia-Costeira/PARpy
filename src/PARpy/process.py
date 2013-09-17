#!/usr/bin/env python

import numpy as np
from scipy.io import loadmat
from datetime import datetime, timedelta
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
        hours = np.int64(dat[0,0][:,1])

        d['name'] = filename
        d['par'] = par
        d['dates'] = dates
        d['hours'] = []
        td = str(np.int(d['dates'][0]))
        ttd = np.int(td[-3::])

        for hour in hours:
            if len(str(hour)) == 3:
                tt = datetime.strptime(str(hour)+'0', "%H%M%S%f")
                d['hours'].append(tt + timedelta(days=ttd))
            else:
                tt = datetime.strptime(str(hour), "%H%M%S%f")
                d['hours'].append(tt + timedelta(days=ttd))

        if d:
            dicts.append(d)
        d = {}

        
    return dicts
