"""Second script to compute the ARR2019 post processing
"""

from ARR2019_config import quantities, locations
from ARR2019_post_processing import post_process, write_ARR_results

data_directory = '/home/ro/Work/Petar-2021/PyARR-postprocessed-data/1%AEP/'

for quantity in quantities:
    points_dict = post_process(locations=locations, quantity=quantity, data_directory=data_directory)    
    outname = quantity + '.txt'
    print('Results stored in', outname)
    write_ARR_results(outname, points_dict)
