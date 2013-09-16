#!/usr/bin/env python

import numpy as np
from scipy.io import loadmat
from datetime import datetime
import glob
import os

<<<<<<< HEAD
def extract_mat(indir):
    dicts = []
    d = {}
=======
hours_proc = []

def extract_mat(indir):
>>>>>>> ecda31fa4351999aa5a0a7811d0523e9a1f8d7a9
    for filename in sorted(glob.glob(os.path.join(indir, '*.mat'))):
        f = loadmat(filename)
        dat = f['hdfdata']['Reference_Par_hyperspectral_data']
        par = dat[0,0][:,2]
        dates = dat[0,0][:,0]
        hours = np.int64(dat[0,0][:,0])
        if d:
            dicts.append(d)
        d = {}
        d['name'] = filename
        d['par'] = par
        d['dates'] = dates
        d['hours'] = [] 
        for hour in hours:
            if len(str(hour)) == 3:
                d['hours'].append(datetime.strptime(str(hour)+'0', "%H%M%S%f"))
            else:
<<<<<<< HEAD
                d['hours'].append(datetime.strptime(str(hour), "%H%M%S%f"))
        
    return dicts

=======
                hours_proc.append(datetime.strptime(str(i), "%H%M%S%f"))
    
    return par, dates, hours 
>>>>>>> ecda31fa4351999aa5a0a7811d0523e9a1f8d7a9
