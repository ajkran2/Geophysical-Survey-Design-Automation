# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:23:49 2017
@author: Ashton
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 01:40:33 2017
@author: Ashton
"""

import os
import numpy as np
import random
from string import *
from sgems_script_WRITE_revised import writeSGEMSscript
from testing_reading_control import computeVARmaps
import time

# Creates the 2 files (batch and text) needed to run 
# the SGeMS script outside of the GUI. It needs as input the file name
# of the script for SGeMS to run.  On successful run, it will output the
# output file specified in the SGeMS script to the w-d.

def batchrun(i,n,path,numreal,pointset):
    """i, integer for iteration number.  
       n, integer for grid size (1 side)
       path, string indicating path of W.D. 
       pointset, string indicating txt file of SGEMS input data.
       numreal, number of realizations"""

    ############################################
    # You may need to edit
    ############################################
    # Filenames for running the batch
    scriptname = 'sgems_script%d.py' % (i)
    batchname = 'test%d.bat' % (i)
    runname = 'testrun%d.txt' % (i)
    
    # SGEMS variable names    
    gridname = 'gridxy%d' % (i)
    hardname = 'hardtest%d' % (i)
    propname = 'simtest%d' % (i)
    pointname = 'pointset%d' % (i)
    
    # SGEMS output data file names
    gridfile = 'gridxy_40x40.txt'
    outfile = 'out%d.txt' % (i)
    ###########################################
    # Don't edit below this
    ###########################################
    
    # Running the batch
    fid = open(batchname,'w')
    fid.write('set GSTLAPPLIHOME=C:\\ar2gems-beta \n')
    fid.write('C:\\ar2gems-beta\\ar2gems_com.exe '+runname)
    fid.close()
    
    writeSGEMSscript(path,scriptname,pointset,gridname,hardname,propname,numreal,gridfile,outfile,pointname)
    
    fid = open(runname,'w')
    fid.write('RunScript '+path+scriptname) # C:/Users/Ashton/Documents/School/SeniorDesign/wip/sgems_script_wip.py')
    fid.close()
    
    os.system(batchname)
    time.sleep(2)

    # Computing weight matrix and outputting
    [x, y, varmap] = computeVARmaps(gridfile,outfile,n)
    [nx,ny] = np.shape(varmap)
        
    return nx,ny,varmap,gridfile,outfile