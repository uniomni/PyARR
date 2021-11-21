""" 
After running the 1_sww2maxTIFs.py script, you need to run this script

This script will open a directory of maximum TIF files and calculate
the mean for each duration (from the 10 patterns) and then it will
create the peak of peaks from the means or medians as per ARR2019 requirements

by Ole Nielsen - 2021

"""

import os
import glob
import shutil
from os.path import *
from ARR2019_config import storm, mode, quantities, root_directory
from ARR2019_post_processing import maxTIF2meanTIF, meanTIF2maxTIF

TIF_directory = os.path.join(root_directory, 'TIFS')
MEAN_directory = os.path.join(root_directory, 'MEANS')
PEAK_directory = os.path.join(root_directory, 'PEAKS')
sub_folders = [name for name in os.listdir(TIF_directory) if os.path.isdir(os.path.join(TIF_directory, name))]


for folder in sub_folders:
    for quantity in quantities:
        fromdir = os.path.join(TIF_directory, folder, quantity)
        output_filename = folder + '_' + quantity + '_' + mode + '.tif' 

        if os.path.isfile(os.path.join(MEAN_directory + '/' + quantity + mode, output_filename)):
            print('Already computed', output_filename)
        else: 
            print('Computing', output_filename)
        
            maxTIF2meanTIF(fromdir, MEAN_directory + '/' + quantity + mode, output_filename, mode=mode)
            
                    
            
print('Computing Peak of Peaks!')
for quantity in quantities:
	# FIXME need a check here to skip already created peak of peaks
    print(quantity)
    meanTIF2maxTIF(MEAN_directory + '/' + quantity + mode, PEAK_directory, quantity, mode=mode)
