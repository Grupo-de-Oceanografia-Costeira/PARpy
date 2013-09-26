#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from datetime import datetime, timedelta
import glob
import os
import h5py

def extract_hdf(indir):
    '''
    This function works with hdf5 (.h5)
    If you have hdf4 files provided from Satlantic processing tools,
    you should convert it using the "h4toh5".
    http://www.hdfgroup.org/h4toh5/
    '''
    dicts = []
    d = {}
    
    for filename in sorted(glob.glob(os.path.join(indir, '*.h5'))):
        f = h5py.File(filename)
        ff = f['Photosynthetically Available Radiation']['Reference_Par_hyperspectral']
        print("Processing File ", filename)
        dates = []
        hours = []
        par = []
        for att in ff:
            dates.append(att[0])
            hours.append(np.int64(att[1]))
            par.append(att[2])
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
