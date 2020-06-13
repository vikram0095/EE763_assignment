# -*- coding: utf-8 -*--
"""
Created on Wed Jun  3 17:45:47 2020

@author: Vikram
"""
import numpy as np
import matplotlib.pyplot as plt

mat=np.load('MAM_mean_1981_2010.npy')

plt.matshow(mat[0,:,:])
#index_lat=np.which(lat==13)
#index_lon=np.which(lon==70)
lat_sta=(np.array([10,13,19,8.25,10,13,13.25,14.25,16,19])-6.5)*4
#8.25,10,13,13.25,14.25,16,19  
print(lat_sta)
#77.5,76.25,74.75,74.75,74.75,73.75,72.75
lon_sta=(np.array([76.25,74.75,72.75,77.5,76.25,74.75,74.75,74.75,73.75,72.75])-66.5)*4
print(lon_sta)
name_sta=['Kochi','Mangalore','Mumbai']
plt.figure()
#plt.plot(data_imd[:,29,42])
for i in range(10):
    plt.scatter(lat_sta[i],np.mean(mat[:,int(lat_sta[i]),int(lon_sta[i])]))
#plt.plot(np.arange(1981,2010),mat[:,int(lat_sta[1]),int(lon_sta[1])])
#plt.plot(np.arange(1981,2010),mat[:,int(lat_sta[2]),int(lon_sta[2])])
plt.legend([10,13,19,8.25,10,13,13.25,14.25,16,19])
#plt.xticks(ticks=np.arange(1981,2010,2))
