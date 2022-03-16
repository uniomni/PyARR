"""Second script to compute the ARR2019 post processing
"""

import os
from ARR2019_config import quantities, locations, storm, mode, root_directory
from ARR2019_post_processing import post_process, write_ARR_results

data_directory = os.path.join(root_directory, 'TIFS')

for quantity in quantities:
    points_dict = post_process(locations = locations, quantity = quantity, data_directory = data_directory, mode = mode)       
    outname = os.path.join(root_directory, storm) + '_' + quantity + '_' + mode + '.txt'
    print('Results stored in', outname)
    write_ARR_results(outname, points_dict, mode)
