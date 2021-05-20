""" 
After running the 2_maxTIFs2meanTIF.py script, you need to run this script
to create a single maximum TIF file from the mean
for each duration as per ARR2019 requirements

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
    print (fromdir)
    outfile = path_list[4] + '_'+path_list[5][0:-5] + '_max.tif'
    print ('creating peak of peaks', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + '/' + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(maximum)
    result = None

create_Dmax = meanTIF2maxTIF(data_directory + 'D_mean')
create_VDmax = meanTIF2maxTIF(data_directory + 'VD_mean')
create_Vmax = meanTIF2maxTIF(data_directory + 'V_mean')
create_WLmax = meanTIF2maxTIF(data_directory + 'WL_mean')

# delete all xml files
for filename in listdir(data_directory):
    if filename.endswith('.xml'):
        os.remove(data_directory + filename)
