# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:25:29 2017
@author: Ashton
"""
import matplotlib.pyplot as plt
import numpy as np

# This script accepts a grid file (my_file.dat) and a data file (containing N
# realizations for a single hard data set), and computes the variance map to be
# used for pathing weights.
def computeVARmaps(gridfile,outfile,n):
        
    # Import X Y coordinates of grid
    filename = gridfile #'my_file.dat'
    with open(filename,'r') as f: # with/open/as syntax useful for files
            array1 = [[float(x) for x in line.split()] for line in f]
    nparray = np.array(array1) # convert array to numpy array
    f.close()
    
    x = nparray[:,0] # x is first collumn, y is second
    x = x.reshape(n+1,n+1)
    y = nparray[:,1] 
    y = y.reshape(n+1,n+1)
    
    #%% Importing data file
    with open(outfile,'r') as f: 
            array = [[float(x) for x in line.split()] for line in f]
    nparray1 = np.array(array) 
    f.close()
    
    #%% Computing mean of realizations
    datamean1 = []
    for i in range(len(nparray1[:,0])):
        datamean1.append(np.mean(nparray1[i,:]))
    
    datamean1 = np.array(datamean1)
    
    #%% Calculating variances
    datalist1 = []
    STDdata1 = []
    for i in range(len(nparray1[:,0])):
            datalist1.append(nparray1[i])
            STDdata1.append((datalist1[i]-datamean1[i])*(datalist1[i]-datamean1[i]))
    STDdata1= np.array(STDdata1)
    
    nR = len(nparray1[0,:])
    nD = len(nparray1[:,0])
    varmap1 = np.zeros((nD,1))
    for ii in range(len(nparray1[:,0])):
        varmap1[ii] = np.mean(STDdata1[ii,:])        
    varmap1 = varmap1.reshape(n+1,n+1)
    
    # Normalize to a PDF (for combining with other weights)
    varmap1_pdf = varmap1/(np.sum(np.sum(varmap1)))

    return x,y,varmap1