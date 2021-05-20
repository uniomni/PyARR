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
from ARR2019_config import storms, durations, quantities, data_directory, CellSize, blockage


def maxTIF2meanTIF(directory, filepattern='*.tif'):
    pattern = os.path.join(directory, filepattern)
    directory = glob.glob(pattern) 

    res = []
    for filename in directory:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    mean = np.mean(stacked, axis=-1)

    path_list = fromdir.split(os.sep) 
    outfile = path_list[5]+'_'+path_list[6]+'_mean.tif'    
    print ('Creating mean: ', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory+outfile, gdal.Open(directory[0]))
    result.GetRasterBand(1).WriteArray(mean)
    result = None    

def meanTIF2maxTIF(fromdir, filepattern='*.tif'):
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 
    
    res = []
    for filename in filenames:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    maximum = np.max(stacked, axis=-1)

    path_list = fromdir.split(os.sep)   
    #print (fromdir)
    outfile = path_list[4] + '_'+path_list[5][0:-5] + '_max.tif'
    print ('Creating peak of peaks: ', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + '/' + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(maximum)
    result = None


# do stuff

for storm in storms:
	for duration in durations:
		for quantity in quantities:
			event = str(storm) + '%AEP' + str(duration) + 'm_' + blockage
			fromdir = data_directory + event + '/' + quantity
			#print (fromdir)
			check_polys = maxTIF2meanTIF(fromdir)
   

# move created files into respective directories
os.chdir(data_directory)

D_mean = 'D_mean'
VD_mean = 'VD_mean'
V_mean = 'V_mean'
WL_mean = 'WL_mean'

os.mkdir(D_mean)   
os.mkdir(VD_mean)
os.mkdir(V_mean)
os.mkdir(WL_mean)


for filename in glob.glob(os.path.join(data_directory,'*_' + D_mean + '.tif')):
    shutil.copy(filename,data_directory + D_mean + '/') 


for filename in glob.glob(os.path.join(data_directory,'*_' + VD_mean + '.tif')):
    shutil.copy(filename,data_directory + VD_mean + '/') 


for filename in glob.glob(os.path.join(data_directory,'*_' + V_mean + '.tif')):
    shutil.copy(filename,data_directory + V_mean + '/')      


for filename in glob.glob(os.path.join(data_directory,'*_' + WL_mean + '.tif')):
    shutil.copy(filename,data_directory + WL_mean + '/') 
    


# delete tifs
for filename in listdir(data_directory):
    if filename.endswith('.tif'):
        os.remove(data_directory + filename)

# create peak of peaks
create_Dmax = meanTIF2maxTIF(data_directory + D_mean)
create_VDmax = meanTIF2maxTIF(data_directory + VD_mean)
create_Vmax = meanTIF2maxTIF(data_directory + V_mean)
create_WLmax = meanTIF2maxTIF(data_directory + WL_mean)

# delete all xml files
for filename in listdir(data_directory):
    if filename.endswith('.xml'):
        os.remove(data_directory + filename)
