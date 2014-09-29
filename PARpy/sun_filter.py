#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pysolar
from datetime import datetime
import numpy as np


def filter_solar_angle(lat, lon, dates, angle=30, temp=0):
    """
    Filter values of an array by their valid solar elevation angle.
    Satlantic HyperOCR Hyperspectral Radiometer.
    http://satlantic.com/hyperspectral-radiometers

    `Pysolar` is used to calculate sun elevation angle.

    Parameters
    ----------
    lat : Latitude in degrees
    lon : Longitude in degrees
    dates : An array of datetime objects
    angle : Sun elevation angle
        default is 30 degree.
    temp : Temperature of air
        default is 0 celsius degree.

    Output
    ------
    angles : ndarray of boolean values
        filtered valid angles, obtained with Pysolar
    valid : ndarray
        Filtered angles value, greater than 30.
    """
    angles = []

    for h in dates:
        if type(h) != datetime:
            angles.append(np.nan)
        else:
            ang = Pysolar.GetAltitude(lat, lon, h,
                                      temperature_celsius=temp)
            angles.append(ang)
            print ang

    angles = np.array(angles)
    dates = np.array(dates)
    valid = dates[angles > angle]

    return angles, valid


def day_light(lat, lon, day, angle=30., temp=0):
    """
    Function to return available day light time, based on specific sun
    elevation angle.

    Parameters
    ----------
    lat: float
        Latitude
    lon: float
        Longitude
    day: datetime object
        Date containing year, month, day
    angle: float
        Standard value is 30. but you may change it to acquire available
        day time of specific sun elevation angle sunrise to sunset.
    temp: float
        Air temperature, used on pysolar sun altitude algorithm.
        Default for this code is 0 Celsius degree.

    Returns
    -------
    day_length : tuple
        Hours, Minutes and seconds of available day light.
    sunrise : datetime object
        Sunrise datetime of specific sun altitude.
    sunset : datetime object
        Sunset datetime of specific sun altitude.

    Notes
    -----
    More information on sun angles can be accessed at:
    http://www.esrl.noaa.gov/gmd/grad/solcalc/azelzen.gif
    where `h` is the elevation angle.
    """
    hours = []
    for h in range(24):
        for m in range(60):
            for s in range(60):
                hours.append(
                    datetime.datetime(day.year, day.month, day.day, h, m, s))

    angles, valid = filter_solar_angle(lat, lon, hours, angle, temp)

    sunrise = valid[0]
    sunset = valid[-1]
    diff = sunset - sunrise
    hours = divmod(diff.seconds, 3600)
    minutes = divmod(hours[1], 60)
    seconds = minutes[1]
    day_length = [hours, minutes, seconds]

    return day_length, sunrise, sunset
