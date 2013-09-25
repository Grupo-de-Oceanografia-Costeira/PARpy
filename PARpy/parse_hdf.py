#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from datetime import datetime, timedelta
import glob
import os

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
