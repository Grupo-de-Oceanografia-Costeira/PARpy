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

        for hour in hours:
            if len(str(hour)) <= 5:
                tt = datetime.strptime('00'+str(hour), "%H%M%S%f")
                at = (tt + timedelta(days=ttd)).replace(year=tty)
                d['hours'].append(at)
                                
            elif len(str(hour)) == 6:
                xs = str(hour)
                ps = '-'.join(xs[:2])+'-'.join(xs[2:4])+'-'.join(xs[4:6])
                if int(ps[-4:-2]) > 59:
                    ps = '-'.join(xs[:2])+'-'.join(xs[2:4])+'-'+xs[-2:]
                tt = datetime.strptime(ps, "%H-%M-%S-%f")
                at = (tt + timedelta(days=ttd)).replace(year=tty)
                d['hours'].append(at)
                            
            elif len(str(hour)) > 6:
                xs = str(hour)
                ps = xs[:2] +'-'+ xs[2:4] +'-'+ xs[4:6] +'-'+ xs[6:]
                if int(ps[6:8]) > 59:
                    ps = xs[:2]+'-'+ xs[2:4] +'-'+xs[4:5] +'-'+ xs[5:]
                    if ps[:2] == '24':
                        ps = ps.replace(ps[:2],'00')
                    elif int(ps[:2]) > 24:
                        ps = '00-00-00-00' 
                elif int(ps[:2]) == 24:
                    ps = '00' +'-'+ xs[2:4] +'-'+xs[4:6] +'-'+ xs[6:]
                    if int(ps[6:8]) > 59:
                        ps = '00'+'-'+ xs[2:4] +'-'+xs[4:5] +'-'+ xs[5:]
                elif int(ps[:2]) > 24:
                    ps = '00-00-00-00'
                        
                tt = datetime.strptime(ps, "%H-%M-%S-%f")
                at = (tt + timedelta(days=ttd)).replace(year=tty)
                d['hours'].append(at)               

        if d:
            dicts.append(d)
        d = {}

        
    return dicts
