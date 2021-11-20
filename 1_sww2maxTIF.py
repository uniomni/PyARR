""" This script is for ARR2019 ANUGA sww post processing.

It will convert a collection of sww files to TIF with maximum values of selected quantities.

"""

import os.path
from ARR2019_config import data_directory, storm
from ARR2019_post_processing import sww2maxTIF

CellSize = 1.0  # change cellsize to what ever grid size you want

sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]

for folder in sub_folders:
    sww2maxTIF(os.path.join(data_directory, folder), 
               os.path.join(data_directory, 'PyARR-postprocessed-data', storm, folder), 
               CellSize = CellSize)
