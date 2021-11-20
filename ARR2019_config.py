""" Config file
    
    Enter quantities and grid resolution (cell size) you want to process for 1_sww2maxTIF.py
    locations are required when using 2_critical_duration_patterns.py
    
"""

import os
from os.path import expanduser
from easygui import *
  
# Set data directory
#root_directory = diropenbox('Select data directory', default=expanduser('~'))
root_directory = '/home/ro/Work/Petar-2021/PyARR-data/1%AEP'

# Get rid of redundant separators
root_directory = os.path.normpath(root_directory)

# Get storm event from tail of data directory (e.g. 1%AEP)
storm = os.path.split(root_directory)[-1]

#mode='median'
mode='mean'
  
quantities = ['WL']#,'D','V','VD']
peaks = 'mean' # can be only 'mean' or 'median'

# List of Easting, Northing coordinates where you want to extract critical data
locations = [
    # # Brooks
    # (299227.614,6180030.808),
    # (298442.103,6180281.279),
    # (298359.289,6180243.119),
    # (298110.037,6180144.068),
    # (298020.728,6180093.730),
    # (297281.902,6179044.590),
    # (297804.298,6178532.325)
#]
     ## Wollongong
     #(306679.877,6187525.723),
     #(305829.954,6188350.062),
     (306954.652,6187838.069),
     (304979.435,6186066.239),
     (304762.441,6186692.149),
#     (306679.387,6186665.085),
#     (305497.573,6187034.980),
#     (305990.960,6188287.694),
#     (304749.056,6188457.339),
#     (305906.461,6187466.665),
#     (305301.157,6187701.923),
#     (306666.197,6187442.171),
#     (306547.764,6187254.406),
#     (304761.537,6186312.072),
#     (306636.123,6186148.427),
#     (305712.674,6186863.814),
#     (305456.766,6187025.880)
    
]
