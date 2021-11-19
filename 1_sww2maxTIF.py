""" This script is for ARR2019 ANUGA sww post processing.

It will convert a collection of sww files to TIF with maximum values of selected quantities.

"""

import os.path
from ARR2019_post_processing import data_directory, sww2maxTIF

CellSize = 1.0  # change cellsize to what ever grid size you want

sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]

for folder in sub_folders:
    sww2maxTIF(data_directory + folder, data_directory + 'PyARR-postprocessed-data/' + folder, CellSize = CellSize)
