# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:17:28 2020

@author: Vikram
"""
def isleapyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
    

import numpy as np
yeaR_st=1981
yeaR_en=2010
N_years=yeaR_en-yeaR_st
count_leap=0
for yeaR in range(yeaR_st,yeaR_en):
    count_leap=count_leap+isleapyear(yeaR)
    
mat=np.zeros((365*N_years+count_leap,129,135))
index_mat=0   
for yeaR in range(yeaR_st,yeaR_en):
    print(yeaR)
    matrix1=np.loadtxt("C:/Users/Vikram/Desktop/MASTER DATA PT25 (1901-2018)/MASTER DATA PT25 (1901-2018)/ASCII_DATA_PT25/RF/IND"+str(yeaR)+"_rfP25.txt")
    step=365+isleapyear(yeaR)
    for i in range(step):
        mat[index_mat+i,:,:]=matrix1[130*i+1:130*(i+1),1:]
    index_mat=index_mat+ step

np.save('imd_rain_2015',mat)