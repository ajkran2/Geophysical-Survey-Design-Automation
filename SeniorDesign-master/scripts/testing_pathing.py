# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:44:16 2017
@author: Katherine and Ashton
"""

# Import Libraries
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import math


def createDistance(x, y, distance, n):
    """ Function takes in an 
    x and y value (int) 
    distance array (np)
    n (int) grid size
    fills distance array with the physical distance each point is from the current
    point.  Current points set at 1000 to prevent double counting."""
    for i in range(0, n+1):
        for j in range(0, n+1):
            if (math.sqrt((x-i)**2 + (y-j)**2))<= 3.5:
                distance[i][j] = 1
            else: 
                distance[i][j] = 1
    
    distance[x][y] = 0
    return distance

def totalWeighting(distance, count, data, n):
    """Function takes in 
    distance (np.array) - distance weighting
    count (np.array) - if a point has been visited
    data (np.array) - varmap
    n (int) - gridsize
    Function then returns a total weighting array that is calculated using the RMS of the 
    other arrays.  The way this is calculated could be changed later."""

    weighting = (data)*(distance)*count
    weighting = weighting/(np.sum(np.sum(weighting)))    
    return weighting

def newPoint(x, y, weighting, n):
    """Function takes in
    x and y location (int) 
    weighting array (numpy)
    n (int) grid size
    Finds the point with the minimum weighting and then find the point closest to the
    current point to move to."""
    currX=x
    currY=y

    closest = np.argmax(weighting)
    closest_tuple = np.unravel_index(closest, (n+1, n+1))
    closestX, closestY = closest_tuple
    
    # Set x value
    if closestX == x:
        x = closestX
    elif closestX >= x+1:
        x = x+1
    elif closestX <= x-1:
        x = x-1

    # Set y value
    if closestY == y:
        y = closestY
    elif closestY >= y+1:
        y = y+1
    elif closestY <= y-1:
        y = y-1

    try:
        if weighting[x,y]==0:
            # top left corner
            if x==currX-1 and y==currY+1:
                if math.sqrt((currX-closestX)**2+(closestY-currY+1)**2)<=math.sqrt((currX-1-closestX)**2+(closestY-currY)**2) and weighting[x,y+1]!=0:
                    x=currX
                    y=currY+1
                elif weighting[x-1,y]!=0:
                    x=currX-1
                    y=currY
                else:
                    if weighting[x+1,y+1]!=0:
                        x=currX+1
                        y=currY+1
                    elif weighting[x-1,y-1]!=0:
                        x=currX-1
                        y=currY-1
            # top middle
            if x==currX and y==currY+1:
                if weighting[x-1,y+1]!=0:
                    x=currX-1
                    y=currY+1
                elif weighting[x+1,y+1]!=0:
                    x=currX+1
                    y=currY+1
                else:
                    if weighting[x-1,y]!=0:
                        x=currX-1
                        y=currY
                    elif weighting[x+1,y-1]!=0:
                        x=currX+1
                        y=currY
            # top right
            if x==currX+1 and y==currY+1:
                if math.sqrt((closestX-currX)**2+(closestY-currY+1)**2)<=math.sqrt((closestX-currX+1)**2+(closestY-currY)**2) and weighting[x,y+1]!=0:
                    x=currX
                    y=currY+1
                elif weighting[x+1,y]!=0:
                    x=currX+1
                    y=currY
                else:
                    if weighting[x-1,y-1]!=0:
                        x=currX-1
                        y=currY-1
                    elif weighting[x-1,y+1]!=0:
                        x=currX-1
                        y=currY+1
            # middle left
            if x==currX-1 and y==currY:
                if weighting[x-1,y+1]!=0:
                    x=currX-1
                    y=currY+1
                elif weighting[x-1,y-1]!=0:
                    x=currX-1
                    y=currY-1
                else:
                    if weighting[x,y+1]!=0:
                        x=currX
                        y=currY+1
                    elif weighting[x,y-1]!=0:
                        x=currX
                        y=currY-1
            # middle RIGHT
            if x==currX+1 and y==currY:
                if weighting[x+1,y-1]!=0:
                    x=currX+1
                    y=currY-1
                elif weighting[x+1,y+1]!=0:
                    x=currX+1
                    y=currY+1
                else:
                    if weighting[x,y-1]!=0:
                        x=currX
                        y=currY-1
                    elif weighting[x,y+1]!=0:
                        x=currX
                        y=currY+1
            # bottom left corner
            if x==currX-1 and y==currY-1:
                if math.sqrt((currX+1-closestX)**2+(currY-closestY)**2)<=math.sqrt((currX-closestX)**2+(currY-1-closestY)**2) and weighting[x-1,y]!=0:
                    x=currX-1
                    y=currY
                elif weighting[x,y-1]!=0:
                    x=currX
                    y=currY-1
                else:
                    if weighting[x-1,y+1]!=0:
                        x=currX-1
                        y=currY+1
                    elif weighting[x+1,y-1]!=0:
                        x=currX+1
                        y=currY-1
            # bottom middle
            if x==currX and y==currY-1:
                if weighting[x+1,y-1]!=0:
                    x=currX+1
                    y=currY-1
                elif weighting[x-1,y-1]!=0:
                    x=currX-1
                    y=currY-1
                else:
                    if weighting[x-1,y]!=0:
                        x=currX-1
                        y=currY
                    elif weighting[x+1,y]!=0:
                        x=currX+1
                        y=currY
            # bottom right
            if x==currX+1 and y==currY-1:
                if math.sqrt((closestX-currX)**2+(currY-1-closestY)**2)<=math.sqrt((closestX-currX+1)**2+(currY-closestY)**2) and weighting[x,y-1]!=0:
                    x=currX
                    y=currY-1
                elif weighting[x+1,y]!=0:
                    x=currX+1
                    y=currY
                else:
                    if weighting[x-1,y-1]!=0:
                        x=currX-1
                        y=currY-1
                    elif weighting[x+1,y+1]!=0:
                        x=currX+1
                        y=currY+1
    except:
        x=x
        y=y
    
    return x,y

def runPathing(userInputs, gridfile, n, totalCount, current_x, current_y, count, SS, data_new, gauss_data=None, data, textfile, loopCount=1):
    """Function that runs pathing outside of script allowing combination with
    sgems function.
    userInputs (True/False) - if user is inputting data
    gridfile (file location, string) - from batchrun
    n (integer) - grid size, set to maximum grid value
    totalCount (integer) - number of points to be surveyed,
    current_x (int) - starting x location
    current_y (int) - starting y location
    count (numpy) - weight of if point was visited or not
    SS (list) - previously visited points
    data_new -
    gauss_data (numpy.array) - actual gravity data ### edit to become user input at some point ####
    data (np object) - variance map
    textfile (string) - sGemsinput file location
    loopCount (integer) - how many times you want to loop through sgems/pathing,
                default value of 1 for a singular run through script"""

    for i in range(totalCount):
        filename = gridfile #'my_file.dat'
        with open(filename) as f: # with/open/as syntax useful for files
                array1 = [[float(x) for x in line.split()] for line in f]
        nparray = np.array(array1) # convert array to numpy array
        f.close()
        
        x = nparray[:,0] # x is first collumn, y is second
        x = x.reshape(n+1,n+1)
        y = nparray[:,1] 
        y = y.reshape(n+1,n+1)
    
        distance = np.zeros((n+1, n+1))
        
        current = 1

        ##############################################
        # If you want to plot something, do that here:
        ##############################################

        # Ready plot for inside if statement
        fig = plt.figure()
        #plt.subplot(1,2,1)
        plt.imshow(data, cmap='coolwarm',vmin=0,vmax=1.5)
        plt.colorbar(ticks=[0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0],extend='max')
        #plot = plt.scatter([], [])
        
        #plot point of max variance
        #maxi = np.argmax(data)
        #maxi_tuple = np.unravel_index(maxi, (n+1, n+1))
        #ymax, xmax = maxi_tuple
        #plot1 = plt.scatter(xmax,ymax)
        #plot.set_offsets(SS)
        plt.title('100 Realizations')
        
        plt.axis([0, n, 0, n])
        ###############################################
        # End of first part of plotting
        ###############################################
        
        # For statement looping through all points
        #for i in range(current+1, totalCount):
        distance = createDistance(current_x, current_y, distance, n)
        weight = totalWeighting(distance, count, data, n)
        current_x, current_y = newPoint(current_x, current_y, weight, n)
        
        ##############################################
        # Continue plotting if you want to add points
        ##############################################
        # plot new point and save image
        point = (current_y, current_x)
        SS = np.append(SS, point)
        #plot.set_offsets(SS)

        # subplot 2
        #data_new[current_x,current_y] = gauss_data[current_x,current_y]
        #plt.subplot(1,2,2)
        #plt.title('Data Reveal')
        #plt.imshow(data_new, cmap='coolwarm',vmin=0,vmax=1, origin='lower')
        #plt.colorbar(ticks=[0.0,0.25,0.5,0.75,1.0],extend='max')
        path = 'images/img%i%i.png' % (loopCount,i)
        plt.savefig(path, format='png')

        plt.close()
        ##############################################
        # Continue plotting if you want to add points
        ##############################################
    
        # mark point as visited
        count[current_x][current_y] = 0
    
        # Add point to file object
        file_object = open(textfile, 'a')
        if userInputs is False:
            file_object.write('%s %s %s \n' % (x[current_x][current_y], y[current_x][current_y], gauss_data[current_x][current_y]))
        elif userInputs if True:
            collectedData = input('Data collected for point (%s,%s): ' % (current_x, current_y))
            file_object.write('%s %s %s \n' % (x[current_x][current_y], y[current_x][current_y], collectedData))
        file_object.close()

    # Return last point measured
    return current_x, current_y, count, SS, weight,data_new