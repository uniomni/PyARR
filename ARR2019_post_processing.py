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
#from anuga.file.netcdf import NetCDFFile
#from anuga.geospatial_data.geospatial_data import Geospatial_data
#from anuga.file_conversion import sww2dem
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
	 
    THIS WORKS!!!!!
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
    
    
    
    THIS WORKS!!!!!        
    """
    pattern = os.path.join(fromdir, filepattern)
    filenames = glob.glob(pattern) 

    points_dict = {}  # Dictionary to hold return values (one_up_filename, value, mean) for each point
    for point in locations:
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
            data_value = data[row][col] # Data value at this point

            filename_list.append((filename, data_value))
            
        mean, (one_up_filename, value) = find_average_element(filename_list)
        points_dict[point] = (one_up_filename, value, mean)     
        print (one_up_filename, value, mean)
    return points_dict

    
def find_max_values_across_all_durations(locations, durations, blockages, duration_dict):  
    """Find the highest quantity value for all storm durations at specified locations.
    
    Input
        locations: List of (Easting, Northing) points, e.g. [(306679.877, 6187525.723), (305829.954, 6188350.062)]
        durations: List of storm durations (integers), e.g. [10, 15, 20, 25, 30, 45, 60, 90, 120, 180, 270, 360, 540, 720]
        duration_dict: Dictionary of point information for each duration. E.g.
                duration_dict = 
                {10: 
                    {(306679.877, 6187525.723): ('1%AEP10m_P6_unblocked_stage_max.tif', 1.8806984, 1.8805007934570312), 
                     (305829.954, 6188350.062): ('1%AEP10m_P6_unblocked_stage_max.tif', 17.197166, 17.196933555603028)}, 
                 15: 
                    {(306679.877, 6187525.723): ('1%AEP15m_P7_unblocked_stage_max.tif', 2.0994844, 2.0985819816589357), 
                     (305829.954, 6188350.062): ('1%AEP15m_P7_unblocked_stage_max.tif', 17.277727, 17.27648296356201)}, 

    Output
       max_points_dict: Dictionary of point information with the maximum value and mean. E.g.
       {(306679.877, 6187525.723): ('1%AEP360m_P9_unblocked_stage_max.tif', 2.9336274, 2.9184953212738036), 
        (305829.954, 6188350.062): ('1%AEP45m_P6_unblocked_stage_max.tif', 17.372875, 17.361011505126953)}

    """
    
    max_points_dict = {}
    

    for location in locations:
        # Calculate and store max values across all durations
        max_value = 0
        for duration in durations:
 				
 	        # there is an error here somewhere because it is not returing the MAX from the stored data 
 			
            points_dict = duration_dict[duration]
   
            one_up_filename, value, mean = points_dict[location]
            
            print(location, one_up_filename, value, mean)      
                  
            if value > max_value:
 			
                max_value = value
                max_points_dict[location] = (one_up_filename, max_value, mean)
 	
            one_up_filename, value, mean = max_points_dict[location]
        print('Max found to be', location, one_up_filename, max_value, mean)                
    return max_points_dict

    
def post_process(durations, locations, storm, quantity, proc_directory, blockages):          
    """For each location calculate the maximum value from a given storm and quantity across all durations.
    
    Return points_dict indexed by locations containing one_up_filename, max_value and mean.
    
    THIS WORKS!!!!!
    """
    
    duration_dict = {}
    for duration in durations:
		
        for blockage in blockages:
		
            fromdir = proc_directory+str(storm)+'%AEP'+str(duration)+'m_' + blockage+'/'+quantity
            #print ('fromdir loc', fromdir, locations)
            points_dict = critical_duration_pattern(fromdir, locations)
            
            # Store result for this duration
            duration_dict[duration] = points_dict
       
    max_points_dict = find_max_values_across_all_durations(locations, durations, blockages, duration_dict)  
    return max_points_dict

    
def sww2maxTIF(fromdir, destdir, CellSize=1.0, filepattern='*.sww'):
    """Generate geotiff files from ANUGA sww files for four quantities. 
    The maximum values will be stored in the destination files.
    
    Note this works perfectly, do not touch it
    
    THIS WORKS!!!!!  
    """
    
    # Relate ANUGA quanties to directories with abbreviated names
    output_quantities = {'depth': 'D', 
                         'velocity': 'V',
                         'depthIntegratedVelocity': 'VD',
                         'stage': 'WL'}
    MyTimeStep = 'max' # Used in MakeGeotif and associated filename creation 
    # FIXME (Ole): May move output_quantities and MyTimeStep to the general config section
        
    # Ensure destination directory exists
    os.makedirs(destdir, exists_ok=True)  # succeeds even if directory exists.
    print('Confirmed destdir', destdir)
    
    # Create directories for each quantity
    destdir_quantity = {}
    for Q in output_quantities:
        destdir_quantity[Q] = os.path.join(destdir, output_quantities[Q])
        os.makedirs(destdir_quantity[Q], exists_ok=True)

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
            
	
def write_ARR_results(outname, points_dict):
    """
    THIS WORKS!!!!!  
    """    
    f = open(outname, 'w')
    f.write('Easting, Northing, Max_Value, critical_DUR/PAT, Mean\n')
        
    for point in points_dict:
        one_up_filename, value, mean = points_dict[point]
        
        f.write('%.3f, %.3f, %.3f, %s, %.3f\n' % (point[0], point[1], value, 
                                                    os.path.split(one_up_filename)[1], mean))
    f.close()
