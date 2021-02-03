import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#extracts data from data.csv
datafile = pd.read_csv('20210108_data.csv', header = None)
datafile = datafile.T

#extracts data from type.csv
typefile = pd.read_csv('20210108_type.csv', header = None, dtype = 'int32')
typefile = typefile.T

#combines data into one table
combined = pd.concat([datafile, typefile], axis = 1) #axis = 1 tells the program to combine dataframes side by side
combined.reset_index()

#add titles to the columns
combined.columns = ['data', 'type']
print(combined)

#sort the data and plot the graphs


#watch the video and use BORIS, maybe try to synchronize the bar plots to the Python-plotted graphs?