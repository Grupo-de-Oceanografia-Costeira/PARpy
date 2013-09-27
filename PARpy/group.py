#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import numpy as np
#from datetime import datetime, timedelta
#import glob
#import os
#import h5py

'''
group equal days
'''

#from PARpy.parse import extract_hdf

#d = extract_hdf('.')

### Testing Set

g = [{'dates':[0,0,0,0,0], 'name':'set 0'},
    {'dates':[0,2,2,2,2,0], 'name':'set 1'},
    {'dates':[7,3,3,3,3,3,7], 'name':'set 2'},
    {'dates':[2,4,4,4,4,2], 'name':'set 3'},
    {'dates':[2,5,5,5,5,5,2], 'name':'set 4'},
    {'dates':[7,6,6,6,6,7], 'name':'set 5'}]
    ## Answer ('set 0' & 'set 1',
    ##         'set 2' & 'set 5',
    ##         'set 3' & 'set 4')

ini = []
fim = []
value = []
group = []

i_ini = 1
i_fim = 1
    
for ll in g:
    ini = ll['dates'][0]
    fim = ll['dates'][-1]
    
    if i_ini and i_fim == ini and fim:
        for item in g:
            i_ini = item['dates'][0]
            i_fim = item['dates'][-1]
            print(('i_ini = ',i_ini, 'ini', ini))
            
            group.append({'dates':value['dates']+item['dates'],
#                    'hours':value['hours']+item['hours'],
#                    'par':value['par']+item['par'],
                    'name':value['name']+' '+item['name']})
            print((value['name'], item['name']))
            value = item
    
    if i_ini and i_fim != ini and fim:
        i_ini = ll['dates'][0]
        i_fim = ll['dates'][-1]
        value = ll
