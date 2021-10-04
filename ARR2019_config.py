"""Common parameters for ARR2019
"""

from easygui import *        
from os.path import expanduser
 
storms = [1] #,2,5,10,20,50] # 1=1%AEP, 2=2%AEP etc
durations = [15,20,25,30]#,45,60,90,120,180,270,360,540,720,1440,1800,2160,2880,4320] # do not touch these as they are the standard ARR2019 durations
quantities = ['WL','D','V','VD']  # quantities to process
CellSize = 1 # Resolution of grids 
MyTimeStep = 'max' # this can be time step number eg timestep 5 (not the timestep in seconds) or 'last', or 'max', or 'all'


#### ENTER DIRECTORY LOCATION HERE ###
#root_directory = '/models/1%AEP/' # this is critical for the scripts to run, you must put all your files in a folder called files
#root_directory = '/Work/Petar-2021/'
#data_directory = expanduser('~') + root_directory + 'PyARR-data/1%AEP/' 
#print('data_directory', data_directory)
#proc_directory = expanduser('~') + root_directory + 'PyARR-postprocessed-data/1%AEP/' 
#print('proc_directory', proc_directory)


##### GUI METHOD TO CHOOSE DATA DIRECTORY#####################################################

data_directory = diropenbox('Select data directory', default=expanduser('~'))
data_directory = data_directory + '/'
print ('data directory', data_directory)
proc_directory = data_directory

##############################################################################################


# List of Easting, Northing coordinates
locations = [
            (306679.877,6187525.723)]#,
            # (304761.537,6186312.072), # added new test location
            # (305829.954,6188350.062), 
            # (305497.573,6187034.980), 
            # (304762.441,6186692.149), 
            # (304979.435,6186066.239), 
            # (306679.387,6186665.085), 
            # (306954.652,6187838.069)] 

