"""Second script to compute the ARR2019 post processing
"""

import os
from ARR2019_config import quantities, locations, storm, mode, data_directory
from ARR2019_post_processing import post_process, write_ARR_results


for quantity in quantities:
    points_dict = post_process(locations=locations, quantity=quantity, data_directory=data_directory, mode=mode)    
    
    outname = storm + '_' + quantity + '.txt'
    print('Results stored in', outname)
    write_ARR_results(outname, points_dict, mode)
