# -*- coding: utf-8 -*-
"""
This script builds a single dataset of weather data collected from stations around the Colorado 
    Springs and Monument areas. This dataset will be used to build ML algorithms to short term predictions
    of out of limits flying conditions at the USAFA Academy airfield.
    
    Written Nov 2017
"""

# Pandas allows us to create dataframes.
import pandas as pd
# os allows us to interact with the operating system
import os

# Specify the location of the folder containing all the data files
directory = "/home/greg/Documents/Projects/Data-Analysis/Weather Prediction/data/"


# Format every .csv file and add it to a single master file.
for root,dirs,files in os.walk(directory):
    print (str(len(files)) + " files will be formatted and added to the final dataset.")
    for file in files:
        if file.endswith(".csv"):
            f=open(root+file, 'r')
            data = pd.read_csv(root + file, header=0)   #read the csv file
            # print the file name
            print ("Reading... " + os.path.splitext(file)[0])
            station = file[:file.find(" ")]
            # Add the station name to every variable in the dataset, excluding time
            for i in list(data)[1:]: #skip the first variable, time
                data = data.rename(columns={i : station + '_' + i})
            f.close()
            # append the formatted file to the master
           
