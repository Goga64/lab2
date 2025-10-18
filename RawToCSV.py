##############################################################
# RawToCSV.py
# Python script to convert LTSpice simulation to csv format
# Requires PyLTSpice https://pypi.org/project/PyLTSpice/
# Version 
##############################################################
from PyLTSpice import RawRead
import csv
import numpy as np

datafile    = "RLC.raw"
outputfile  = "RLC.csv"

# Import data file
Data = RawRead(datafile)

# Get the names of all traces
TraceNames = Data.get_trace_names()
num_traces = len(TraceNames)
size = len((Data.get_wave(TraceNames[0])))

# Prepare array
AllData = np.empty(shape=(num_traces,size),dtype=(complex,complex))

# Store every trace in an array
i = 0
for name in TraceNames:
    print(name)
    AllData[i,:] = Data.get_wave(name)
    i = i + 1

# Print data on command line
print(AllData)

# Write to csv
with open(outputfile, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(TraceNames)
    for i in range(size):
        writer.writerow(AllData[:,i])
    
