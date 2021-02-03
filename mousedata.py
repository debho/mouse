import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#extracts data from data.csv
datafile = pd.read_csv('20210108_data.csv', header = None)
datafile = datafile.T
datafile.reset_index()

#extracts data from type.csv
typefile = pd.read_csv('20210108_type.csv', header = None, dtype = 'int32')
typefile = typefile.T
typefile.reset_index()

#combines data into one table
#pd.concat did not join tables in the intended way
#add titles to the columns
#sort the data and plot the graphs
#watch the video and use BORIS, maybe try to synchronize the bar plots to the Python-plotted graphs?