""" 
After running the 2_maxTIFs2meanTIF.py script, you need to run this script
to create a single maximum TIF file from the mean
for each duration as per ARR2019 requirements

hacked by Petar Milevski 28 April 2021

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
#location = '/models/1%AEP/' # this is critical for the scripts to run, you must put all your files in a folder called files
location = '/Work/Petar-2021/PyARR-data/1%AEP/' # this is critical for the scripts to run, you must put all your files in a folder called files
######################################

def meanTIF2maxTIF(fromdir, filepattern='*.tif'):
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 
    
    res = []
    for filename in filenames:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    maximum = np.max(stacked, axis=-1)
    
    # Finally save a new raster with the result. 
    # This assumes that all inputs have the same geotransform since we just copy the first

    path_list = fromdir.split(os.sep)   
    print (path_list)
    #outfile = path_list[4]+'_'+path_list[5][0:-5]+'_max.tif'
    outfile = path_list[-2]+'_'+path_list[-1][0:-5]+'_max.tif'
    print ('creating peak of peaks', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(maximum)
    result = None

    
# enter the data directory where the model runs are located
data_directory = expanduser("~")+location


  
src_dir = data_directory
os.chdir(src_dir)
  
try:	  
    os.mkdir('D_mean')   
    os.mkdir('VD_mean')
    os.mkdir('V_mean')
    os.mkdir('WL_mean')
except:
    pass

dest_dir_d = data_directory+'D_mean'
dest_dir_vd = data_directory+'VD_mean'
dest_dir_v = data_directory+'V_mean'
dest_dir_wl = data_directory+'WL_mean'

print (dest_dir_d)
print (dest_dir_vd)
print (dest_dir_v)
print (dest_dir_wl)

for fname in glob.glob(os.path.join(src_dir,"*_D_mean.tif")):
    shutil.move(fname,dest_dir_d) 


for fname in glob.glob(os.path.join(src_dir,"*_VD_mean.tif")):
    shutil.move(fname,dest_dir_vd)


for fname in glob.glob(os.path.join(src_dir,"*_V_mean.tif")):
    shutil.move(fname,dest_dir_v)        


for fname in glob.glob(os.path.join(src_dir,"*_WL_mean.tif")):
    shutil.move(fname,dest_dir_wl)





try: 
    fromdir = dest_dir_d
    check_polys = meanTIF2maxTIF(fromdir)
except:
    pass

try: 
    fromdir = dest_dir_vd
    check_polys = meanTIF2maxTIF(fromdir)
except:
    pass

try: 
    fromdir = dest_dir_v
    check_polys = meanTIF2maxTIF(fromdir)
except:
    pass

try: 
    fromdir = dest_dir_wl
    check_polys = meanTIF2maxTIF(fromdir)
except:
    pass


# delete all crap xml files
for filename in listdir(data_directory):
    if filename.endswith('.xml'):
        os.remove(data_directory  + '/' +  filename)
