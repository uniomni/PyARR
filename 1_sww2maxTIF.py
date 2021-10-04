""" This script is for ARR2019 ANUGA sww post processing.

It will convert a collection of sww files to TIF with maximum values of selected quantities.

"""

import os
import os.path
from os.path import *
from easygui import *
from os.path import expanduser
from ARR2019_post_processing import sww2maxTIF
from ARR2019_config import data_directory, proc_directory, CellSize, quantities, MyTimeStep


sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]

for folder in sub_folders:
    sww2maxTIF(data_directory + folder, proc_directory + 'PyARR-postprocessed-data/' + folder, CellSize = CellSize, MyTimeStep = MyTimeStep)
