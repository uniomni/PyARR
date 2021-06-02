""" 
After running the 1_sww2maxTIFs.py script, you need to run this script

This script will open a directory of maximum TIF files and calculate
the mean for each duration (from the 10 patterns) and then it will
create the peak of peaks from the means as per ARR2019 requirements

by Petar Milevski - 2021

Note - this has been tested and works perfectly, dont touch the code
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
from ARR2019_config import storms, durations, quantities, data_directory, CellSize, blockage, proc_directory

# create mean from the ten ARR2019 patterns
def maxTIF2meanTIF(filenames, filepattern='*.tif'):
    pattern = os.path.join(filenames, filepattern)
    filenames = glob.glob(pattern) 

    res = []
    for filename in filenames:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    mean = np.mean(stacked, axis=-1)

    path_list = fromdir.split(os.sep) 
    outfile = event + '_' + quantity + '_mean.tif'    
    print ('Creating mean: ', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(mean)
    result = None    

# create peak of peaks from the means
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
    storm_list = proc_directory.split(os.sep)
    #print (storm_list[-2]+'_'+quantity)

    outfile = storm_list[-2] + '_' + quantity + '_max.tif'
    print ('Creating peak of peaks: ', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + '/' + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(maximum)
    result = None


# do stuff

for storm in storms:
    for duration in durations:
        for quantity in quantities:
            for blockage in blockages:
                event = str(storm) + '%AEP' + str(duration) + 'm_' + blockage
                fromdir = proc_directory + event + '/' + quantity
                #print (fromdir)
                check_polys = maxTIF2meanTIF(fromdir)

os.chdir(data_directory)

for storm in storms:
    for quantity in quantities:
        new_dir =  proc_directory + str(storm) + '%AEP_' + quantity + '_mean'
        os.mkdir(new_dir)
        for filename in glob.glob(os.path.join(data_directory, '*_' + quantity + '_mean.tif')):
            shutil.move(filename,new_dir + '/')

# create peak of peaks and move to new directory
for storm in storms:
    new_max_dir = proc_directory + str(storm) + '%AEP_max'
    os.mkdir(new_max_dir)

for storm in storms:
    for quantity in quantities:
        create_max = meanTIF2maxTIF(proc_directory + str(storm) + '%AEP_' +  quantity + '_mean')
        for filename in glob.glob(os.path.join(data_directory, '*_' + quantity + '_max.tif')):
            shutil.move(filename,new_max_dir)

# clean up (delete all xml files)
for filename in listdir(data_directory):
    if filename.endswith('.xml'):
        os.remove(data_directory + filename)
