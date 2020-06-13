import numpy as np
import matplotlib.pyplot as plt
lon=np.arange(66.50,100.25,0.25)
lat=np.arange(6.50, 38.75,0.25)
#imd_rain=np.load('imd_rain.npy')

data_imd=np.load('imd_rain_2015.npy')
#plt.matshow(data_imd[0,:,:])

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
    
# sesason MAM
yeaR_st=1981
yeaR_en=2010
index_mat=0
mat=np.zeros(((yeaR_en-yeaR_st)*63,129,135))
mat=np.zeros(((yeaR_en-yeaR_st)*63,129,135))
#mat=np.zeros(((yeaR_en-yeaR_st),129,135))
for yeaR in range(yeaR_st,yeaR_en):
    print(yeaR)
    step=365+isleapyear(yeaR)
   # mat[yeaR-yeaR_st,:,:]=np.sum(data_imd[index_mat+59+isleapyear(yeaR):index_mat+59+92+isleapyear(yeaR),:,:],0)
    #mat[(yeaR-yeaR_st)*122:(yeaR-yeaR_st+1)*122,:,:]=data_imd[index_mat+151+isleapyear(yeaR):index_mat+273+isleapyear(yeaR),:,:]
    mat[(yeaR-yeaR_st)*63:(yeaR-yeaR_st+1)*63,:,:]=data_imd[index_mat+151+30+isleapyear(yeaR):index_mat+273-29+isleapyear(yeaR),:,:]
    index_mat=index_mat+ step
np.save('JA_1981_2010',mat)
#np.save('JJAS_1981_2010',mat)
#np.save('MAM_sum_1981_2010',mat)