import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#extracts data from data.csv
datafile = pd.read_csv('20210108_data.csv', header = None)
datafile = datafile.T
print(datafile)

#extracts data from type.csv
typefile = pd.read_csv('20210108_type.csv', header = None)
typefile = typefile.T
print(typefile)