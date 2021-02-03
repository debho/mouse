import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

datafile = pd.read_csv('20210108_data.csv', header = None)
datafile = datafile.T
print(datafile)

typefile = pd.read_csv('20210108_type.csv', header = None)
print(typefile)