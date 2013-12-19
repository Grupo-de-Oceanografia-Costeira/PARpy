#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from datetime import datetime, timedelta
import glob
import os
import h5py
from scipy.io import loadmat

def genfilelist(indir):
    """
    Get specific files in directory to be parsed

    Parameters
    ----------
    indir : str

    Returns
    -------
    genlist : list of strings
        List contains names of specific filenames and extension

    Example
    -------
    files = genfilelist('*.h5')
    files2 = genfilelist('../*.mat')
    files3 = genfilelist('~/Documents/*.mat')
    """
    genlist = []
    for filename in sorted(glob.glob(os.path.join(indir))):
        genlist.append(filename)

    return genlist

def h5_extract(filelist):
    """
    Parameters
    ----------
    filelist : list of filenames (str)

    Returns
    -------
    Dictionary of elements
        'name' : File name
        'latitude'  : Degrees parsed only if RAW file is together
        'longitude' : Degrees parsed only if RAW file is together
        'par'  : PAR (Photosynthetical Active Radiance) value
        'dates': Dates with number of running days
        'hours': Datetime object with parsed dates.

    See Also
    --------
    This function works with hdf5 (.h5)
    If you have hdf4 files provided from Satlantic processing tools,
    you should convert it using the "h4toh5".
    http://www.hdfgroup.org/h4toh5/
    """
    dicts = []
    d = {}
    for filename in filelist:
        f = h5py.File(filename)
        ff = f['Photosynthetically Available Radiation']['Reference_Par_hyperspectral']
        print("Processing File ", filename)
        # Processing Raw file
        try:
            raw = open(filename.replace('_L4.h5', '.raw'), "rb")
            rawd = raw.read()
            raw.close()
            lat_part = rawd[775:777]
            lat_minute = rawd[778:784]
            lat = np.float(lat_part) + np.float(lat_minute)*0.0166666667

            lon_part = rawd[903:905]
            lon_minute = rawd[906:912]
            lon = np.float(lon_part) + np.float(lon_minute)*0.0166666667

            if rawd[786] == 'S':
                lat  = -lat
            if rawd[914] == 'W':
                lon = -lon
            else:
                pass

            d['latitude'] = lat
            d['longitude'] = lon

        except:
            d['latitude'] = np.nan
            d['longitude'] = np.nan

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
        for i,hour in enumerate(hours):
            if len(str(hour)) >= 8:
                if par[i] <= 1:
                    d['hours'].append(np.nan)
                else:
                    td = str(np.int(d['dates'][i]))
                    ttd = np.int(td[-3::]) # running day
                    tty = np.int(td[:4])   # year
                    tt = datetime.strptime(str(hour), "%H%M%S%f")
                    at = (tt + timedelta(days=ttd-1)).replace(year=tty)
                    d['hours'].append(at)
            else:
                d['hours'].append(np.nan)
        # TODO!
        # Classify dicts as OrderedDict.
        if d:
            dicts.append(d)
        d = {}

    return dicts

def mat_extract(indir):
    """
    Parameters
    ----------
    indir : Directory as string

    Returns
    -------
    Dictionary of elements
            'name' : File name
            'par'  : PAR value
            'dates': Dates with number of running days
            'hours': Datetime object with parsed dates.
    """

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

    return dicts
