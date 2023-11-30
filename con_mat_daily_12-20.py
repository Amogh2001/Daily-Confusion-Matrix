import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc

import day_classify as dc
#from rainfall_sep import Rainfall_Sep
#from rain_classify import rain_classifier
from conmat_classify import mat_rain_classifier
from month_classifier import Rainfall_Year

#Region 77.4684E, 12.7098N, 77.7129E, 13.1081N

df5_rarr = RAINFALL_DATA

#----------------------------------- IMERG Data ------------------------------------

list_year = (2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020)

r_2001 = Rainfall_Year('Year_IMERG_2012.nc', leap = True)
r_2001.monthly_mean()
r_arr01 = np.array(r_2001.monthly_rain)
r_arr = np.array(r_arr01)

for inc_imerg in list_year:
    if inc_imerg % 4 == 0:
        r_imerg = Rainfall_Year('Year_IMERG_' + str(inc_imerg) + '.nc', leap = True)
        r_imerg.monthly_mean()
        r_arr_imerg = np.array(r_imerg.monthly_rain)
        r_arr = np.append(r_arr, r_arr_imerg)

    else:
        r_imerg = Rainfall_Year('Year_IMERG_' + str(inc_imerg) + '.nc')
        r_imerg.monthly_mean()
        r_arr_imerg = np.array(r_imerg.monthly_rain)
        r_arr = np.append(r_arr, r_arr_imerg)

df_gpm = pd.DataFrame(r_arr)

print(len(r_arr))

#------------------------------------Plotting---------------------------------------

plt.hist(df5_rarr)
plt.title = '2012-2020 Rainfall'
plt.show()

#----------------------------------Confusion Matrix--------------------------------

con_mat = np.zeros((15,15))
for r_days in range(0,3288):
    con_mat[mat_rain_classifier(r_arr[r_days]), mat_rain_classifier(r_arr[r_days])] =(con_mat[mat_rain_classifier(r_arr[r_days]), mat_rain_classifier(r_arr[r_days])]) + 1.0
print(con_mat)

