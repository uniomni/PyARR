"""Functions to implement Australian Rainfall and Runoff post processing of ANUGA flood models. 

"""

import shutil
import numpy
import os
import glob
import os.path
from os.path import *
from osgeo import gdal

from numpy import array, float, resize
from anuga.file.netcdf import NetCDFFile
from anuga.geospatial_data.geospatial_data import Geospatial_data
from anuga.file_conversion import sww2dem
from anuga.utilities import plot_utils


"""

1. calculate the average or mean of the 10 numbers.
2. choose the file which is one up from the average (for example it
will be file '1%AEP10m_P6_unblocked_depth_max' and return the value
and filename.

Algorithm is very simplistic but will work well for small data sets

Ole Nielsen - 2021
"""

def find_average_element(filename_list):
    """ Find element closest to the mean from above
    
    Input: List of 2-tuples where each tuple has the form: (string, float)
    Output: The mean value and the 2-tuple where the float is closest to the mean from above, i.e mean, (string, float) 
     
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
	 
     The output for filename_list should be 1.0747306, (1%AEP10m_P6_unblocked_depth_max, 1.0747306) 
	 

    """
    
    if len(filename_list) == 0:
        raise BaseException('Got an empty list: %s' % filename_list)
    
    # Sort by value (Schwartzian Transform)
    Y = [(d[1], d[0]) for d in filename_list]  # Swap order, making depth the first column
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
    


        
def crit_DUR_PAT(fromdir, locations, filepattern='*.tif'):
    """Calculate filename with value closest to the mean from above at specified locations.
    
    Return dictionary 
            points_dict[point] = (one_up_filename, value, mean)     
    """
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 

    points_dict = {}  # Dictionary to hold return values (one_up_filename, value, mean) for each point
    print('locations', locations)
    for point in locations:
        print()
        # For each point in the grid compile list of filenames and associated maxima
        filename_list = []
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
            #X = file[0:-4]
            data_value = data[row][col] # Data value at this point
            #print (X, Y)

            filename_list.append((filename, data_value))
            
        mean, (one_up_filename, value) = find_average_element(filename_list)
            
        print('Found filename: ', one_up_filename)
        print('Value: ', value)
        print('Mean: ', mean)
        print('Location: ', point)
    
        points_dict[point] = (one_up_filename, value, mean)     
    
    return points_dict

def post_process(durations, locations, storm, quantity, data_directory):          
    """For each location calculate the maximum value from a given storm and quantity across all durations.
    
    Return points_dict indexed by locations containing one_up_filename, max_value and mean.
    """
    
    duration_dict = {}
    for duration in durations:                
        event = str(storm)+'%AEP'+str(duration)+'m_unblocked'
            
        fromdir = data_directory+event+'/'+quantity
        points_dict = crit_DUR_PAT(fromdir, locations)
        
        # Store result for this duration
        duration_dict[duration] = points_dict
            
        
    for location in locations:
                        
        # Calculate and store max values across all durations
        max_value = 0
        for duration in durations:
            points_dict = duration_dict[duration]
            one_up_filename, value, mean = points_dict[location]
            #print('Duration', duration, one_up_filename, value, mean)
            if value > max_value:
                max_value = value
                points_dict[location] = (one_up_filename, max_value, mean)
                
    return points_dict

    
def sww2maxTIF(fromdir, CellSize=1.0, filepattern='*.sww'):
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 
    	
    for filename in filenames:
        head, file = os.path.split(filename)
        #print ('fromdir',fromdir)
        print ('Converting: ', file)
        plot_utils.Make_Geotif(
            swwFile=filename, 
            output_quantities=['depth', 'velocity', 'depthIntegratedVelocity', 'stage'],
            output_dir=fromdir,
   	    myTimeStep='max',
   	    CellSize=CellSize, 
   	    velocity_extrapolation=True, 
   	    min_allowed_height=0.01, 
   	    EPSG_CODE=28356, # EPSG_CODE=28356 is for UTM -56, codes for other locations search for EPSG_CODE on the web 
   	    verbose=False, 
   	    k_nearest_neighbours=3)
    
    os.chdir(fromdir)
        
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

    
    for fname in glob.glob(os.path.join(fromdir, "*depth_max.tif")):
        shutil.copy(fname, dest_dir_d) 
  
    for fname in glob.glob(os.path.join(fromdir, "*depthIntegratedVelocity_max.tif")):
        shutil.copy(fname, dest_dir_vd) 
    
    for fname in glob.glob(os.path.join(fromdir, "*velocity_max.tif")):
        shutil.copy(fname, dest_dir_v)        
    
    for fname in glob.glob(os.path.join(fromdir, "*stage_max.tif")):
        shutil.copy(fname, dest_dir_wl)
    
    # deletes tif's from fromdir after they have been copied to their respective directories
    files_in_directory = os.listdir(fromdir)

    filtered_files = [file for file in files_in_directory if file.endswith(".tif")]

    for file in filtered_files:
	    path_to_file = os.path.join(fromdir, file)
	    os.remove(path_to_file)	

	
	
def write_ARR_results(outname, points_dict):
    
    f = open(outname, 'w')
    f.write('Easting, Northing, critical_DUR/PAT, Value, Mean\n')
        
    for point in points_dict:
        one_up_filename, value, mean = points_dict[point]
        
        f.write('%f, %f, %s, %f, %f\n' % (point[0], point[1], 
                                              os.path.split(one_up_filename)[1], value, mean))
    f.close()

        
                        
