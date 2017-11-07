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

# test importing a single file
data = pd.read_csv("/home/greg/Documents/Projects/Data-Analysis/Weather Prediction/data/Aardvark 2011-06-01 - 12-31-2011.csv", header=0)
data['Location'] = 'Aardvark'


directory = "/home/greg/Documents/Projects/Data-Analysis/Weather Prediction/data/"
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f=open(file, 'r')
           # print the file name
           print (os.path.splitext(filename)[0])
           f.close()
           
