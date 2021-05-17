""" 
This script is for ARR2019 ANUGA sww post processing
"""


from ARR2019_post_processing import sww2maxTIF
from ARR2019_config import storms, durations, quantities, data_directory, CellSize, blockage
   
for storm in storms:
    for duration in durations:
        event = str(storm) + '%AEP' + str(duration) + 'm_' + blockage
        print(event)
        sww2maxTIF(data_directory + event, CellSize = CellSize)
