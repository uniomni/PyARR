"""Second script to compute the ARR2019 post processing
"""

        
from osgeo import gdal
import os, glob, os.path
from os.path import expanduser

from ARR2019_post_processing import post_process, write_ARR_results
from ARR2019_config import storms, durations, quantities, data_directory, locations

for storm in storms:
    for quantity in quantities:        

        points_dict = post_process(durations=durations, locations=locations, storm=storm, quantity=quantity, data_directory=data_directory)
        
        # Write critical storms for each location to a file
        outname = str(storm) + '%AEP_critical_' + quantity + '.txt'
        print('outname', outname)

        write_ARR_results(outname, points_dict)

            
