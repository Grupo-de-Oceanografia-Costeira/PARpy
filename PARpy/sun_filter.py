#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pysolar
from datetime import datetime
import numpy as np

<<<<<<< Updated upstream
def filter_solar_angle(lat, lon, value, angle=30, temp=0):
    '''
=======

def filter_solar_angle(lat, lon, value, temp=0):
    """
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        Filtered angles value, greater than 30.
    '''

    angles= []
=======
        Valid PAR values, filtered by valid angles
    """
    angles = []
>>>>>>> Stashed changes

    for h in value:
        if type(h) != datetime:
            angles.append(np.nan)
        else:
            ang = Pysolar.GetAltitude(lat, lon, h,
                                      temperature_celsius=temp)
            angles.append(ang)
            print ang

    angles = np.array(angles)
    value = np.array(value)
<<<<<<< Updated upstream
    valid = value[angles > angle]
=======
    valid = value[angles > 30]
>>>>>>> Stashed changes

    return angles, valid


def day_light(lat, lon, day, altitude=30., temp=0):
    """
    Function to return available day light time, based on specific sun
    altitude angle.

    Parameters
    ----------
    lat: float
        Latitude
    lon: float
        Longitude
    day: datetime object
        Date containing year, month, day
    altitude: float
        Standard value is 30. but you may change it to acquire available
        day time of specific sun altitude sunrise to sunset.
    temp: float
        Air temperature, used on pysolar sun altitude algorithm.
        Default for this code is 0 Celsius degree.

    Returns
    -------

    """
    hours = []
    for h in range(24):
        for m in range(60):
            for s in range(60):
                hours.append(
                    datetime.datetime(day.year, day.month, day.day, h, m, s))

    angles, valid = filter_solar_angle(lat, lon, hours, altitude, temp)

    sunrise = valid[0]
    sunset = valid[-1]
    # TODO
    # Compute difference between sunrise and sunset == Day length.
    return sunrise, sunset
