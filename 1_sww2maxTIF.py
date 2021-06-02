""" This script is for ARR2019 ANUGA sww post processing.

It will convert a collection of sww files to TIF with maximum values of selected quantities.

Note - this has been tested and works perfectly, dont touch the code
"""


from ARR2019_post_processing import sww2maxTIF
from ARR2019_config import storms, durations, quantities, data_directory, proc_directory, CellSize, blockages
   
for storm in storms:
    for duration in durations:
        for blockage in blockages:
            event = str(storm) + '%AEP' + str(duration) + 'm_' + blockage
            print('Processing event', event)
            sww2maxTIF(data_directory + event, proc_directory + event, CellSize = CellSize)
