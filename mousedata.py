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
df = pd.concat([datafile, typefile], axis = 1) 

#add titles to the columns
df.columns = ['data', 'type']

#sort the data and plot the graphs
#sorting data by type
eeg_1 = df[df['type'] == 2].reset_index()
eeg_2 = df[df['type'] == 3].reset_index()
eeg_3 = df[df['type'] == 4].reset_index()
eeg_4 = df[df['type'] == 5].reset_index()
axy_x = df[df['type'] == 7].reset_index()
axy_y = df[df['type'] == 8].reset_index()
axy_z = df[df['type'] == 9].reset_index()
