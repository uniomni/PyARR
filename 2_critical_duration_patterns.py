"""Second script to compute the ARR2019 post processing
"""

from easygui import *       
from osgeo import gdal
import os, glob, os.path
from os.path import expanduser
from ARR2019_post_processing import post_process, write_ARR_results
from ARR2019_config import data_directory, proc_directory, quantities, locations

for quantity in quantities:

    points_dict = post_process(locations=locations, quantity=quantity, proc_directory=proc_directory)
    
    # Write critical storms for each location to a file
    outname = quantity + '.txt'
    print('Results stored in', outname)
    
    write_ARR_results(outname, points_dict)
