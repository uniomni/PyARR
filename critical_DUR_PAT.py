from osgeo import gdal
import os, glob, os.path
from os.path import *

from find_mean_depth import find_average_element

#### ENTER DIRECTORY LOCATION HERE ###
#location = '/models/1%AEP/' # this is critical for the scripts to run, you must put all your files in a folder called files
location = '/Work/Petar-2021/PyARR-data/1%AEP/' # this is critical for the scripts to run, you must put all your files in a folder called files
######################################

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

def calculate_max_one_up_value_for_each_location_across_all_durations(durations, locations, storm, quantity):          
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
                    

# enter the data directory where the model runs are located

data_directory = expanduser("~")+location
print (data_directory)
storms = [1]#,2,5,10,20] # 1=1%AEP, 2=2%AEP etc
durations = [10,15,20,25] #,30,45,60,90,120,180,270,360,540,720,1080,1440,1800,2160,2880,4320] # do not touch these as they are the standard ARR2019 durations
quantities = ['WL']#,'D','V','VD'] # but we probably are only interested in WL only which dur/pat is critical for max water level

#List of Easting, Northing coordinates
locations = [(306679.877,6187525.723), 
             (305829.954,6188350.062), 
             (305497.573,6187034.980), 
             (304762.441,6186692.149), 
             (304979.435,6186066.239), 
             (306679.387,6186665.085), 
             (306954.652,6187838.069)] 
        


for storm in storms:
    for quantity in quantities:        

        points_dict = calculate_max_one_up_value_for_each_location_across_all_durations(durations=durations, locations=locations, 
                                                                                        storm=storm, quantity=quantity)
        
                           
        # Write critical storms for each location to a file
        outname = str(storm)+'%AEP_critical_'+quantity+'.txt'
        print('outname', outname)
            
        f = open(outname, 'w')
        f.write('Easting, Northing, critical_DUR/PAT, Value, Mean\n')
        
        for point in points_dict:
            one_up_filename, value, mean = points_dict[point]
            
            f.write('%f, %f, %s, %f, %f\n' % (point[0], point[1], 
                                              os.path.split(one_up_filename)[1], value, mean))
        f.close()


            
