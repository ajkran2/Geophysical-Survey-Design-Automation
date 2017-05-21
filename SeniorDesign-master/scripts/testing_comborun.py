# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:26:00 2017
@author: kbiegel and Ashton
"""

""" Runs both sgems and pathing"""

# Import Libraries
import numpy as np
#from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from matplotlib import pyplot as plt
# Import scripts
import testing_pathing
import testing_alltogethernow
import time
import videoScript


#####################################################
# Variables to change
#####################################################

userInputs = True # Whether you will self input data or not (True means user will input, False means to pull from data grid)
iterations = 1 #number of iterations
path = 'C://Users/Katherine/Documents/GitHub/SeniorDesign/Not_Current/current_5-4/current_5-4/' # path to WD
numreal = '100' # number of realizations (needs to be string b/c sgems)
totalCount = 1 # number of points to path at each iteration (keep small)
n = 39  # Grid size - currently needs to be square
current_x=5  # Survey starting point on grid (x)
current_y=5   # Survey starting point on grid (y)
input_location = 'sgems_inputs.txt'
dataname1 = 'gaussdata_40x40.txt' #'test_fullout.txt' 

######################################################
# Don't edit below here
######################################################

# Import gauss data
with open(dataname1) as f: 
    array = [[float(x) for x in line.split()] for line in f]
nparray = np.array(array) 
f.close()
xx = nparray[:,0]
xx = xx.reshape(n+1,n+1)
yy = nparray[:,1]
yy = yy.reshape(n+1,n+1)
data = nparray[:,2] 
data = data.reshape(n+1,n+1)

# Random pointsets for first iteration
file_object = open(input_location, 'w')
file_object.write('objectName \n')
file_object.write('3 \n')
file_object.write('x \n')
file_object.write('y \n')
file_object.write('gravity value \n')
SS = []
if userInputs is False:
    for i in range(3, 6):
        for j in range(3,6):
            file_object.write('%s %s %s \n' % (xx[i][j], yy[i][j], data[i][j]))
            point = (int(xx[i][j]*10), int(yy[i][j]*10))
            SS = np.append(SS, point)
elif userInputs is True:
    numPoints = input('Number of initial scatter points: ')
    for i in range(0, int(numPoints)):
        x = input('Input x location: ')
        y = input('Input y location: ')
        d = input('Input data value: ')
        file_object.write('%s %s %s \n' % (int(x)/10, int(y)/10, int(d)))
        point = (x, y)
        SS = np.append(SS, point)
file_object.close()

# Initialize arrays
videoclips = []
count = np.ones((n+1, n+1))
count[current_x][current_y] = 0
varmaps = np.zeros((n+1,n+1,iterations))
data_new = np.zeros((n+1,n+1))

for i in range(iterations):
    # run Sgems
    [nx,ny,varmaps[:,:,i],gridfile,outfile] = testing_alltogethernow.batchrun(i,n,path,numreal,pointset=input_location)
    # Run pathing
    [current_x,current_y,count,SS,weight,data_new] = testing_pathing.runPathing(userInputs, gridfile, n, totalCount, current_x, current_y, count, SS, data_new, gauss_data=data, data=varmaps[:,:,i], textfile=input_location, loopCount=i)
    
# Output a video file that shows multiple realizations
#final_clip = concatenate_videoclips(videoclips)
#final_clip.write_videofile("iterations_%s.mp4" % iterations)

