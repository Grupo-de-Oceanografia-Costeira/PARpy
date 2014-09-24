#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pysolar
from datetime import datetime
import numpy as np

def filter_solar_angle(lat, lon, value, angle=30, temp=0):
    '''
    Filter values of an array by their valid solar angle.
    Satlantic HyperOCR Hyperspectral Radiometer.
    http://satlantic.com/hyperspectral-radiometers

    Pysolar is used to calculate elevation angles greater than 30 deg.

    Parameters
    ----------
    lat : Latitude in degrees
    lon : Longitude in degrees
    value : An array of datetime objects
    temp : Temperature of air
        default is 0 celsius degree.

    Output
    ------

    angles : ndarray of boolean values
        filtered valid angles, obtained with Pysolar
    valid : ndarray
        Filtered angles value, greater than 30.
    '''

    angles= []

    for h in value:
        if type(h) != datetime:
            temp.append(np.nan)
        else:
            ang = Pysolar.GetAltitude(lat, lon, h, 
                                        temperature_celsius=temp)
            angles.append(ang)
            print ang

    angles = np.array(angles)
    value = np.array(value)
    valid = value[angles > angle]

    return angles, valid

