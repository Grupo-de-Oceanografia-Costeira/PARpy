#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pysolar
from datetime import datetime

def filter_solar_angle(Lat, Lon, Value, Temp):
    '''
    Filter values of an array by their valid solar angle.
    Satlantic HyperOCR Hyperspectral Radiometer.
    http://satlantic.com/hyperspectral-radiometers
    
    Pysolar is used to calculate elevation angles greater than 30 deg.
        
    Parameters
    ----------
    Lat : Latitude in degrees
    Lon : Longitude in degrees
    Value : An array of datetime objects
    temp : Temperature of air
    
    Returns
    -------
    
    temp : ndarray of boolean values
    filt : Filtered values
    '''
    
    filt = []
    temp = []
    
    for h in Value:
        if type(h) != datetime:
            temp.append(np.nan)
        else:
            ang = Pysolar.GetAltitude(Lat, Lon, h, temperature_celsius=Temp)
            temp.append(ang)
            print ang
    
    temp = np.array(temp)
    Value = np.array(Value)    
    filt = Value[temp>30]    
    
    return temp,filt
    
