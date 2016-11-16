#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='PARpy',
    version='0.1.0',
    description='Processing tool for PAR data of Satlantic Radiometers',
    long_description=readme + '\n\n' + history,
    author='Arnaldo Russo',
    author_email='arnaldorusso@gmail.com',
    url='https://github.com/Grupo-de-Oceanografia-Costeira/PARpy',
    packages=[
        'PARpy',
    ],
    #package_dir={'': 'PARpy'},
    #include_package_data=True,
    install_requires=[
        'numpy',
        'h5py',
        'pysolar'
    ],
    license="PSF",
    zip_safe=False,
    keywords='PAR Photosynthetically Active Radiance Light Solar Angle',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
    ],
    test_suite='tests',
)
