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
from monthly_mat_classifier import monthly_rain_classifier

#Region 77.4684E, 12.7098N, 77.7129E, 13.1081N

#--------------------------------------Station 1 Data-----------------------------------------

list01_11 = ['AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ'] #include 'AM' for 2007
list12_22 = ['AR', 'AS','AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']


bang_stat1_df4 = pd.DataFrame()
bang_stat1_df5 = pd.DataFrame()


for m in list01_11:
    bang_stat1_4 = pd.read_excel('DataSheet1.xlsx', usecols=m)
    bang_stat1_df4 = pd.concat([bang_stat1_df4, (bang_stat1_4[1:369])], axis = 0, ignore_index= True)
bang_stat1_df4 = bang_stat1_df4.stack().reset_index()


for n in list12_22:
    bang_stat1_5 = pd.read_excel('DataSheet1.xlsx', usecols=n)
    bang_stat1_df5 = pd.concat([bang_stat1_df5, (bang_stat1_5[1:369])], axis = 0, ignore_index= True)
bang_stat1_df5 = bang_stat1_df5.stack().reset_index()

bang_stat1_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat1_df5.rename(columns = {0: 'Rainfall'}, inplace=True)


bang_stat1_df4['Rainfall'] = pd.to_numeric(bang_stat1_df4['Rainfall'], errors = 'coerce')
df4_rarr = bang_stat1_df4['Rainfall'].array
df4_rarr = np.insert(df4_rarr, 0, 0.0)
#df4_rarr = np.delete(df4_rarr, 4017)   #include when including 2007

bang_stat1_df5['Rainfall'] = pd.to_numeric(bang_stat1_df5['Rainfall'], errors = 'coerce')
df5_rarr = bang_stat1_df5['Rainfall'].array
df5_rarr = np.insert(df5_rarr, 0, 0.0)
df5_rarr = np.delete(df5_rarr, 3288)

bang_stat1_4_month2001 = dc.month_rain_getter(df4_rarr[1:369])
bang_stat1_4_array = np.array(bang_stat1_4_month2001)
bang_stat1_4_array_test = np.array(bang_stat1_4_month2001)

for num1 in range(1, 11):
    num2 = num1 + 1
    if num2/4 ==1 or num2/7 == 1:
        bang_stat1_4_iter = dc.month_rain_getter(df4_rarr[(369*num1):(369*num2)], leap = True)
        bang_stat1_4_array_test = np.append(bang_stat1_4_array_test, bang_stat1_4_iter)
    else:
        bang_stat1_4_iter = dc.month_rain_getter(df4_rarr[(369*num1):(369*num2)])
        bang_stat1_4_array_test = np.append(bang_stat1_4_array_test, bang_stat1_4_iter)


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

