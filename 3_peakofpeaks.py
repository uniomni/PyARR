""" 
After running the 1_sww2maxTIFs.py script, you need to run this script

This script will open a directory of maximum TIF files and calculate
the mean, median and maximum for each duration (from the 10 patterns) 
and then it will create the peak of peaks from the as per ARR2019 requirements

by Petar Milevski and Ole Nielsen - 2021

"""

import os
import glob
import shutil
from os.path import *
from os import listdir
from ARR2019_config import storm, mode, quantities, root_directory
from ARR2019_post_processing import maxTIF2meanTIF, meanTIF2maxTIF, delete_xml_files

TIF_directory = os.path.join(root_directory, 'TIFS')
MEAN_directory = os.path.join(root_directory, 'MEANS')
PEAK_directory = os.path.join(root_directory, 'PEAKS')
sub_folders = [name for name in os.listdir(TIF_directory) if os.path.isdir(os.path.join(TIF_directory, name))]

for mode in mode:
    print ('Extracting: ', mode)
    	
    for folder in sub_folders:
        for quantity in quantities:
            fromdir = os.path.join(TIF_directory, folder, quantity)
            destdir = os.path.join(MEAN_directory, quantity) + mode
            output_filename = folder + '_' + quantity + '_' + mode + '.tif' 
    
            if os.path.isfile(os.path.join(destdir, output_filename)):
                print('Already computed', output_filename)
            else: 
                print('Computing', output_filename)
            
                maxTIF2meanTIF(fromdir, destdir, output_filename, mode = mode)
            # delete xml files
            delete_xml_files(destdir, output_filename)     
                       
    # create peak of peaks            
    for quantity in quantities:   	
        output_filename = quantity + '_' + mode + '_peakofpeaks.tif' 
        
        if os.path.isfile(os.path.join(PEAK_directory, output_filename)):
            print('Already computed', output_filename)
        else: 
            print('Computing', output_filename)
            meanTIF2maxTIF(MEAN_directory + '/' + quantity + mode, PEAK_directory, quantity, mode = mode)
    
        # delete xml files
        delete_xml_files(PEAK_directory, output_filename)
