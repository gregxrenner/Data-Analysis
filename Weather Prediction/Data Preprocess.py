# -*- coding: utf-8 -*-
"""
This script builds a single dataset of weather data collected from stations around the Colorado 
    Springs and Monument areas. This dataset will be used to build ML algorithms for short term predictions
    of out of limits flying conditions at the USAFA Academy airfield.
    
    Written Nov 2017
"""

# Pandas allows us to create dataframes.
import pandas as pd
# os allows us to interact with the operating system
import os
# sys allows access to system variable attributes
import sys
# numpy will be used to the time variable
import numpy as np

# Specify the location of the folder containing all the data files
directory = "/home/greg/Documents/Projects/Data-Analysis/Weather Prediction/data/"

# Format every .csv file and add it to a single master file.
def loadCSVs(directory):
    #Initialize a maset file to merge the datasets into
    master = pd.DataFrame({'Date_Time' : ["2014-01-22 23:42:00"]})
    for root,dirs,files in os.walk(directory):
        print (str(len(files)) + " files will be formatted and added to the final dataset.")
        for file in files:
            if file.endswith(".csv"):
                f=open(root+file, 'r')
                data = pd.read_csv(root + file, header=0,
                                   dtype={"Date_Time": str, "Wind_Direction": str, "Wind_Speed": str, 
                                          "Wind_Gust": str, "Air_Temperature": str, "Relative_Humidity": str,
                                          "Barometric_Pressure": str, "Precipitation_3Hr": str, 
                                          "Precipitation_6Hr": str, "Windchill": str,
                                          "Heat_Stress": str, "fits": str})   #read the csv file
                #data = pd.read_csv(root + file, header=0)
                #print the file name
                print ("Reading... " + os.path.splitext(file)[0])
                station = file[:file.find(" ")]
                # Add the station name to every variable in the dataset, excluding time
                for i in list(data)[1:]: #skip the first variable, time
                    data = data.rename(columns={i : station + '_' + i})
                f.close()
                # append the formatted file to the master
                master = pd.merge(master, data, how='outer', on="Date_Time")
    return master
    print ("Load complete.")

        
loadCSVs(directory=directory)
           
#check column data types in dataframe with .dtypes
            #rampart 12-01-01 has the first instance of the error



#import errrors due to dtype. Lets troubleshoot
data2 = pd.read_csv("/home/greg/Documents/Projects/Data-Analysis/Weather Prediction/data/"+"Airfield 2014-01-01 - 2014-12-31.csv", header=0,
                    dtype={"Date_Time": str, "Wind_Direction": str, "Wind_Speed": str,"Wind_Gust": str,
                           "Air_Temperature": str, "Relative_Humidity": str, "Barometric_Pressure": str,
                           "Precipitation_3Hr": str, "Precipitation_6Hr": str, "Windchill": str,
                           "Heat_Stress": str, "fits": str})  
print(sys.getsizeof(data2)) #size of dataframe in bytes
print(data2.dtypes) 
# Change the varible types from objects to less memory intense dtypes
data2[['Wind_Direction', 'Air_Temperature', 'Relative_Humidity', 'Windchill']] = data2[['Wind_Direction', 'Air_Temperature', 'Relative_Humidity', 'Windchill']].astype(int)
data2[['Wind_Speed', 'Wind_Gust', 'Barometric_Pressure', 'Precipitation_3Hr', 'Precipitation_6Hr', 'Heat_Stress', 'fits']] = data2[['Wind_Speed', 'Wind_Gust', 'Barometric_Pressure', 'Precipitation_3Hr', 'Precipitation_6Hr', 'Heat_Stress', 'fits']].astype(float)
data2['Date_Time'] = pd.to_datetime(data2['Date_Time'])
# Changing the varible types reduced memory usage by 87%
 


master = pd.DataFrame({'Date_Time' : ["2014-01-22 23:42:00"]})
master = pd.merge(master, data2, how='outer', on="Date_Time")
