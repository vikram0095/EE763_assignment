# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:05:09 2020

@author: Vikram
"""


import numpy as np
import matplotlib.pyplot as plt

jjas_prec=np.load('JA_1981_2010.npy')

lat_sta=(np.array([10,13,19])-6.5)*4
lon_sta=(np.array([76.25,74.75,72.75])-66.5)*4

name_sta=['Kochi','Mangalore','Mumbai']
#plt.plot(data_imd[:,29,42])

#plt.plot(jjas_prec[:,int(lat_sta[0]),int(lon_sta[0])])
phase_mon=np.zeros((29*11))
iter_phase=0
iter_data=0
for yeaR in range(1981,2010):
    for week in range(11):
        phase_mon[iter_phase]=np.sum(jjas_prec[iter_data:iter_data+3,int(lat_sta[2]),int(lon_sta[2])])
        iter_phase=iter_phase+1
        iter_data=iter_data+3
        
plt.plot(phase_mon)
phase_mon_states=np.zeros((29*11))
q67=np.quantile(phase_mon,0.67)
q33=np.quantile(phase_mon,0.33)
for i in range(29*11):
    if phase_mon[i]>q67:
        phase_mon_states[i]=3
    elif phase_mon[i]<=q67 and phase_mon[i]>q33:
        phase_mon_states[i]=2
    else:
        phase_mon_states[i]=1
plt.figure()
plt.plot(phase_mon_states)
np.save("monsoon_states_mumbai",phase_mon_states)
np.savetxt("monsoon_states_mumbai_1.txt",list(map(int, phase_mon_states)),fmt='%0i')
#plt.plot(jjas_prec[:,int(lat_sta[1]),int(lon_sta[1])])