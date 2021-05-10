""" 
This scritp is for ARR2019 ANUGA sww post processing

This script will open a directory of sww files and extract maximum
'depth', 'velocity', 'depthIntegratedVelocity', 'stage' quantities from 
each sww file and place these quantities in their own directories called D, VD, V and WL

This script MUST sit indide the directory where all your run files are located
enter the location of the dir on line 27

hacked by Petar Milevski 28 April 2021
"""

import shutil
import numpy
import os
import glob
import os.path
from os.path import *
from numpy import array, float, resize
from anuga.file.netcdf import NetCDFFile
from anuga.geospatial_data.geospatial_data import Geospatial_data
from anuga.file_conversion import sww2dem
from anuga.utilities import plot_utils
   
#### ENTER DIRECTORY LOCATION HERE ###
location = '/models/1%AEP/' # this is critical for the scripts to run, you must put all your files in a folder called files
######################################

def sww2maxTIF(directory, filepattern='*.sww'):
    pattern = os.path.join(directory, filepattern)
    files = glob.glob(pattern) 
    	
    for filename in files:
        head, file = os.path.split(filename)
        #print ('fromdir',fromdir)
        print ('Converting: ', file)
        plot_utils.Make_Geotif(
            swwFile=filename, 
            output_quantities=['depth', 'velocity', 'depthIntegratedVelocity', 'stage'],
            output_dir=fromdir,
   		    myTimeStep='max',
   		    CellSize=1.0, 
   		    velocity_extrapolation=True, 
   		    min_allowed_height=0.01, 
   		    EPSG_CODE=28356, #EPSG_CODE=28356 is for UTM -56, codes for other locations search for EPSG_CODE on the web 
   		    verbose=False, 
   		    k_nearest_neighbours=3)
    
    src_dir = fromdir
    os.chdir(src_dir)
        
    try:  
        os.mkdir('D')   
        os.mkdir('VD')
        os.mkdir('V')
        os.mkdir('WL')
    except:
        pass
		
    dest_dir_d = fromdir+'/D/'
    dest_dir_vd = fromdir+'/VD/'
    dest_dir_v = fromdir+'/V/'
    dest_dir_wl = fromdir+'/WL/'

    
    for fname in glob.glob(os.path.join(src_dir,"*depth_max.tif")):
        shutil.move(fname,dest_dir_d) 
  
    for fname in glob.glob(os.path.join(src_dir,"*depthIntegratedVelocity_max.tif")):
        shutil.move(fname,dest_dir_vd)
    
    for fname in glob.glob(os.path.join(src_dir,"*velocity_max.tif")):
        shutil.move(fname,dest_dir_v)        
    
    for fname in glob.glob(os.path.join(src_dir,"*stage_max.tif")):
        shutil.move(fname,dest_dir_wl)

        
# enter the data directory where the model runs are located

data_directory = expanduser("~")+location

storms = [1]#2,5,10,20] # 1=1%AEP, 2=2%AEP etc
durations = [10,15,20,25,30,45,60,90,120,180,270,360,540,720,1080,1440,1800,2160,2880,4320]

for storm in storms:
	for duration in durations:
		event = str(storm)+'%AEP'+str(duration)+'m'
		try:
			fromdir = data_directory+event
			check_polys = sww2maxTIF(fromdir)
			
		except:
			print (event+' does not exist')
			pass   
