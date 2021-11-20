"""Functions to implement Australian Rainfall and Runoff post processing of ANUGA flood models. 

"""

import shutil
import numpy
import numpy as np
import os
import glob
import os.path
from os.path import *
from osgeo import gdal
from easygui import *
from os.path import expanduser
from numpy import array, float, resize
from anuga.utilities import plot_utils

""" use easygui to select your data directory
"""

data_directory = '/home/ro/Work/Petar-2021/PyARR-postprocessed-data/1%AEP/'

#data_directory = diropenbox('Select data directory', default=expanduser('~'))
#data_directory = data_directory + '/'
print ('data directory', data_directory) 

"""

1. calculate the average or mean of the 10 numbers.
2. choose the file which is one up from the average (for example it
will be file '1%AEP10m_P6_unblocked_depth_max' and return the value
and filename.

Algorithm is very simplistic but will work well for small data sets.

Ole Nielsen - 2021
"""

def find_average_element(filename_list):
    """ Find element closest to the mean from above
    
    Input: List of 2-tuples where each tuple has the form: (string, float)
    Output: The mean value and the 2-tuple where the float is closest to 
            the mean from above, i.e mean, (string, float) 
     
    Algorithm:
    1. calculate the mean of the 10 numbers.
    2. choose the file which is one up from the average (for example it
    will be file '1%AEP10m_P6_unblocked_depth_max' and return the value
    and filename.
    
    Example
    
    With input 
    
     filename_list = [('1%AEP10m_P4_unblocked_depth_max', 1.0737015),
         ('1%AEP10m_P8_unblocked_depth_max', 1.0736489),
         ('1%AEP10m_P7_unblocked_depth_max', 1.0767846),
         ('1%AEP10m_P6_unblocked_depth_max', 1.0747306),
         ('1%AEP10m_P2_unblocked_depth_max', 1.073645),
         ('1%AEP10m_P10_unblocked_depth_max', 1.0737189),
         ('1%AEP10m_P1_unblocked_depth_max', 1.0760777),
         ('1%AEP10m_P5_unblocked_depth_max', 1.0748001),
         ('1%AEP10m_P9_unblocked_depth_max', 1.0749958),
         ('1%AEP10m_P3_unblocked_depth_max', 1.0737971)]
	 
     The output for filename_list should be 
     mean, (filename, value) e.g.
     1.07459002, (1%AEP10m_P6_unblocked_depth_max, 1.0747306) 
	 
    """
    
    if len(filename_list) == 0:
        raise BaseException('Fix your ARR2019_config.py file list  Got an empty list: %s' % filename_list)
    
    # Sort by value (Schwartzian Transform)
    # Swap order, making 
    # value the first column, filename the second
    Y = [(d[1], d[0]) for d in filename_list]  
    
    # Then sort based on value
    Y.sort()

    # Calculate average
    sum = 0
    for y in Y:
        sum += y[0]
    mean = sum/len(Y)
    
    # Now find element immediately greater than average
    i = 0
    y = Y[0][0] 
    while(y <= mean):
        i += 1
        y = Y[i][0]

    filename = Y[i][1]
    value = Y[i][0]
    
    return mean, (filename, value)
    


        
def critical_duration_pattern(fromdir, locations, filepattern='*.tif'):
    """Calculate filename with value closest to the mean from above 
       at specified locations.
    
    Return dictionary 
            points_dict[point] = (one_up_filename, value, mean)     
            
    Where value is the value of this quantity at this location and 
    mean the average of this value across all storm patterns as calculate by find_average_element()

    """
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 
    
    if len(filenames) == 0:
        raise BaseException(f'Did not find any files matching pattern {pattern}')

    points_dict = {}  # Dictionary to hold return values (one_up_filename, value, mean) for each point
    for point in locations:
        # For each point in the grid compile list of filenames and associated maxima
        filename_list = []
        max_value = 0
        for filename in filenames:
            
            ds = gdal.Open(filename)
            head, file = os.path.split(filename)
            driver = gdal.GetDriverByName('GTiff')
            band = ds.GetRasterBand(1)
            
            cols = ds.RasterXSize
            rows = ds.RasterYSize
            
            transform = ds.GetGeoTransform()
            
            xOrigin = transform[0]
            yOrigin = transform[3]
            pixelWidth = transform[1]
            pixelHeight = -transform[5]
            
            data = band.ReadAsArray(0, 0, cols, rows)
        
            col = int((point[0] - xOrigin) / pixelWidth)
            row = int((yOrigin - point[1]) / pixelHeight)
            data_value = data[row][col] # Data value at this point

            filename_list.append((filename, data_value))
            
        mean, (one_up_filename, value) = find_average_element(filename_list)
        
        assert value >= mean, 'Internal Error, call Ole'
        
        points_dict[point] = (one_up_filename, value, mean)     
        
        print (point, one_up_filename, value, mean)
        
    return points_dict

    
def post_process(locations, quantity, data_directory):          
    """For each location calculate the maximum value for given quantity.
    
    Return points_dict indexed by locations containing one_up_filename, max_value and mean.

    """
    
    max_points_dict = {}
			
    sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]
    
    for point in locations: 
        
        max_value = 0
        for folder in sub_folders:
            fromdir = data_directory + folder + '/' + quantity
            points_dict = critical_duration_pattern(fromdir, locations)
            one_up_filename, value, mean = points_dict[point]
            
            if value > max_value:
                max_value = value
                max_points_dict[point] = (one_up_filename, max_value, mean)

        print(point, max_points_dict[point])
         
    return max_points_dict

    
def sww2maxTIF(fromdir, destdir, CellSize=1.0, filepattern='*.sww'):
    """Generate geotiff files from ANUGA sww files for four quantities. 
    The maximum values will be stored in the destination files.

    """
    
    # Relate ANUGA quanties to directories with abbreviated names
    output_quantities = {'depth': 'D', 
                         'velocity': 'V',
                         'depthIntegratedVelocity': 'VD',
                         'stage': 'WL'}
    MyTimeStep = 'max' # Used in MakeGeotif and associated filename creation 
    # FIXME (Ole): May move output_quantities and MyTimeStep to the general config section
        
    # Ensure destination directory exists
    os.makedirs(destdir, exist_ok=True)  # succeeds even if directory exists.
    print('Confirmed destdir', destdir)
    
    # Create directories for each quantity
    destdir_quantity = {}
    for Q in output_quantities:
        destdir_quantity[Q] = os.path.join(destdir, output_quantities[Q])
        os.makedirs(destdir_quantity[Q], exist_ok=True)

    # Get sww files from data directory
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 

    for filename in filenames:
        head, file = os.path.split(filename)
        print()
        print('Converting %s to %s' % (filename, destdir))
        
        storm_pattern, _ = os.path.splitext(file)
        
        for Q in output_quantities:
            
            output_filename = os.path.join(destdir, 
                                           destdir_quantity[Q], 
                                           storm_pattern + '_' + Q + '_' + MyTimeStep + '.tif')
                                           
            if os.path.isfile(output_filename):
                print('Already computed', output_filename)
            else: 
                print('Computing', output_filename)
           
            
                plot_utils.Make_Geotif(
                    swwFile=filename, 
                    output_quantities=[Q],
                    output_dir=destdir_quantity[Q],
   	            myTimeStep=MyTimeStep,
   	            CellSize=CellSize, 
   	            velocity_extrapolation=True, 
   	            min_allowed_height=0.01, 
   	            EPSG_CODE=28356, # EPSG_CODE=28356 is for UTM -56, codes for other locations search for EPSG_CODE on the web 
   	            verbose=False, 
   	            k_nearest_neighbours=3)
               


def maxTIF2meanTIF(fromdir, folder, quantity, peaks, filepattern='*.tif'):

    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 

    res = []
    for filename in filenames:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    mean = np.mean(stacked, axis=-1)

    #path_list = fromdir.split(os.sep) 
    #print ('pathlist', path_list)
    

    outfile = folder + '_' + quantity + '_' + peaks +'.tif'
    print ('Creating mean:', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(mean)
    result = None    

# median calculations
def maxTIF2medianTIF(fromdir, folder, quantity, peaks, filepattern='*.tif'):

    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 

    res = []
    for filename in filenames:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    median = np.median(stacked, axis=-1)

    #path_list = fromdir.split(os.sep) 
    #print ('pathlist', path_list)
    

    outfile = folder + '_' + quantity + '_' + peaks +'.tif'  
    print ('Creating median: ', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(median)
    result = None  

def meanTIF2maxTIF(fromdir, folder, quantity, peaks, filepattern='*.tif'):

    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 
    
    res = []
    for filename in filenames:
        ds = gdal.Open(filename)
        res.append(ds.GetRasterBand(1).ReadAsArray()) # We assume that all rasters has a single band
    stacked = np.dstack(res) # We assume that all rasters have the same dimensions
    maximum = np.max(stacked, axis=-1)

    path_list = data_directory.split(os.sep)
    #print ('pathlist', path_list, path_list[-2])

    outfile = path_list[-2] + '_' + quantity + '_' + peaks + '_peakofpeaks.tif'
    print ('Creating peak of peaks: ', outfile)
    driver = gdal.GetDriverByName('GTiff')
    result = driver.CreateCopy(data_directory + '/' + outfile, gdal.Open(filenames[0]))
    result.GetRasterBand(1).WriteArray(maximum)
    result = None
    
    
        	
def write_ARR_results(outname, points_dict):
    """

    """    
    f = open(outname, 'w')
    f.write('Easting, Northing, Max_Value, critical_DUR/PAT, Mean\n')
        
    for point in points_dict:
        one_up_filename, value, mean = points_dict[point]
        
        f.write('%.3f, %.3f, %.3f, %s, %.3f\n' % (point[0], point[1], value, 
                                                    os.path.split(one_up_filename)[1], mean))
    f.close()
