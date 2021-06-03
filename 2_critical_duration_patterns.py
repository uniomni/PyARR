"""Second script to compute the ARR2019 post processing
"""

        
from osgeo import gdal
import os, glob, os.path
from os.path import expanduser

from ARR2019_post_processing import post_process, write_ARR_results
from ARR2019_config import storms, durations, quantities, proc_directory, locations, blockages

for storm in storms:
    for quantity in quantities:

        print('Postprocessing storm %s for quantity %s at all specified locations' % (storm, quantity))
        points_dict = post_process(durations=durations, locations=locations, storm=storm, quantity=quantity, proc_directory=proc_directory, blockages=blockages)

        # Write critical storms for each location to a file
        outname = str(storm) + '%AEP_critical_' + quantity + '.txt'
        print('Results stored in', outname)

        write_ARR_results(outname, points_dict)
