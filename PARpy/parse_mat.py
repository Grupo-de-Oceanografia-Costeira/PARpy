#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        print("Processing File:", filename)
        dat = f['hdfdata']['Reference_Par_hyperspectral_data']
        dates = dat[0,0][:,0]
        hours = np.int64(dat[0,0][:,1])
        par = dat[0,0][:,2]

        d['name'] = filename
        d['par'] = par
        d['dates'] = dates
        d['hours'] = []
        td = str(np.int(d['dates'][0]))
        ttd = np.int(td[-3::])
        tty = np.int(td[:4])

        for i,hour in enumerate(hours):
            if len(str(hour)) >= 8:
                if par[i] <= 1:
                    d['hours'].append(np.nan)
                else:
                    tt = datetime.strptime(str(hour), "%H%M%S%f")
                    at = (tt + timedelta(days=ttd)).replace(year=tty)
                    d['hours'].append(at)
                    print('igual maior que 8', hour)
            
            else:
                d['hours'].append(np.nan)
                print('nan', hour)        

        if d:
            dicts.append(d)
        d = {}
