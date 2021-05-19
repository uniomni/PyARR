""" 
After running the 1_sww2maxTIFs.py script, you need to run this script

This script will open a directory of maximum TIF files and calculate
the mean for that duration as per ARR2019 requirements

by Petar Milevski - 2021

"""

import shutil
from os import listdir
from osgeo import gdal
import numpy as np
import numpy
import os
import glob
import os.path
from os.path import *

#### ENTER DIRECTORY LOCATION HERE ###
data_directory = expanduser('~') + '/models/1%AEP/' # location of you files
######################################

def maxTIF2meanTIF(directory, filepattern='*.tif'):
    pattern = os.path.join(directory, filepattern)
    directory = glob.glob(pattern) 

    res = []
    for filename in directory:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    mean = np.mean(stacked, axis=-1)
    
    # Finally save a new raster with the result. 
    # This assumes that all inputs have the same geotransform since we just copy the first
    #print (fromdir)

    path_list = fromdir.split(os.sep) 
    outfile = path_list[5]+'_'+path_list[6]+'_mean.tif'    
    print ('Creating mean tif from maximums of each dur/pat', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory+outfile, gdal.Open(directory[0]))
    result.GetRasterBand(1).WriteArray(mean)
    result = None    



storms = [1]#,2,5,10,20] # 1=1%AEP, 2=2%AEP etc
durations = [10,15,20,25,30,45,60,90,120,180,270,360,540,720,1080,1440,1800,2160,2880,4320]
quantities = ['WL','D','V','VD']
blockage = 'unblocked'


for storm in storms:
	for duration in durations:
		for quantity in quantities:
			event = str(storm) + '%AEP' + str(duration) + 'm_' + blockage
			fromdir = data_directory + event + '/' + quantity
			#print (fromdir)
			check_polys = maxTIF2meanTIF(fromdir)
   
# delete all xml files
for filename in listdir(data_directory):
    if filename.endswith('.xml'):
        os.remove(data_directory + filename)


# move created files into respective directories
os.chdir(data_directory)
  

os.mkdir('D_mean')   
os.mkdir('VD_mean')
os.mkdir('V_mean')
os.mkdir('WL_mean')


for filename in glob.glob(os.path.join(data_directory,'*_D_mean.tif')):
    shutil.move(fname,data_directory + 'D_mean/') 


for fname in glob.glob(os.path.join(data_directory,'*_VD_mean.tif')):
    shutil.move(filename,data_directory + 'VD_mean/')


for filename in glob.glob(os.path.join(data_directory,'*_V_mean.tif')):
    shutil.move(filename,data_directory + 'V_mean/')        


for filename in glob.glob(os.path.join(data_directory,'*_WL_mean.tif')):
    shutil.move(filename,data_directory + 'WL_mean/')
