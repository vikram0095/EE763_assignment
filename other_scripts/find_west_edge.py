import numpy as np
import matplotlib.pyplot as plt

mat=np.load('MAM_sum_1981_2010.npy')

#plt.matshow(mat[0,:,:])

for lati in range(0,int((25-6.5)*4)):
    for loni in range(134,0,-1):
        if mat[0,lati,loni]>-1:
            print(lati,loni)
            plt.scatter(lati/4+6.5,np.mean(mat[:,lati,loni]))
            break
plt.xlabel("Latitude")
plt.ylabel("Rainfall(mm)")
plt.title("Interannual mean (1981-2010) of total MAM rainfall mm")
#lat_sta=(np.array([10,13,19,8.25,10,13,13.25,14.25,16,19])-6.5)*4
#print(lat_sta)
#lon_sta=(np.array([76.25,74.75,72.75,77.5,76.25,74.75,74.75,74.75,73.75,72.75])-66.5)*4
#print(lon_sta)
#name_sta=['Kochi','Mangalore','Mumbai']
#plt.figure()
##plt.plot(data_imd[:,29,42])
#for i in range(10):
#    plt.scatter(lat_sta[i],np.mean(mat[:,int(lat_sta[i]),int(lon_sta[i])]))
##plt.plot(np.arange(1981,2010),mat[:,int(lat_sta[1]),int(lon_sta[1])])
##plt.plot(np.arange(1981,2010),mat[:,int(lat_sta[2]),int(lon_sta[2])])
#plt.legend([10,13,19,8.25,10,13,13.25,14.25,16,19])
##plt.xticks(ticks=np.arange(1981,2010,2))
#
