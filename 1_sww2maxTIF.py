""" This script is for ARR2019 ANUGA sww post processing.

It will convert a collection of sww files to TIF with maximum values of selected quantities.

by Petar Milevski and Ole Nielsen - 2021
"""

import os.path
from ARR2019_config import root_directory, storm
from ARR2019_post_processing import sww2maxTIF

CellSize = 1.0  # change cellsize to what ever grid size you want

data_directory = os.path.join(root_directory, 'SWW')
sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]

for folder in sub_folders:
    fromdir = os.path.join(root_directory, 'SWW', folder)
    destdir = os.path.join(root_directory, 'TIFS', folder)
    #print (fromdir, destdir)
        
    sww2maxTIF(fromdir, destdir, CellSize = CellSize)
