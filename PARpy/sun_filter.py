#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pysolar

def filter_solar_angle(Value, Lat, Lon, Temp):
    '''
    Input:
    ------
    Value: An array of datetime objects
    Lat: Latitude in degrees
    Lon: Longitude in degrees
    temp: Temperature of air
    
    '''
    filt = []
    
    for h in value:
        ang = Pysolar.GetAltitude(Lat, Lon, h, temperature_celsius=Temp)
        if ang > 30:
            filt.append[h]
        
    
