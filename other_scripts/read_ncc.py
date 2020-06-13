# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:56:49 2020

@author: Vikram
"""

from matplotlib import pyplot as plt
import netCDF4
fp='air.mon.mean.nc'
nc = netCDF4.Dataset(fp)
plt.imshow(nc['air'][1,:,:])
plt.show()