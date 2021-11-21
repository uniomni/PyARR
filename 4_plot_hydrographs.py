import os
import glob
import os.path
import matplotlib.pyplot as plt
from ARR2019_config import root_directory
from anuga.shallow_water.sww_interrogate import get_flow_through_cross_section

# enter location poly here 
polyline = [(299167.162,6180397.967),(299232.924,6180475.358)] #this one is for Brooks Ck outlet
#polyline = [(306632.382,6186448.055),(306680.364,6186443.441)] #this one is for Wollongong City outlet

data_directory = os.path.join(root_directory, 'SWW')
sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]

for folder in sub_folders:
    fromdir = os.path.join(root_directory, 'SWW', folder)
    pattern = os.path.join(fromdir, '*.sww')
    filenames = glob.glob(pattern) 

    for filename in filenames:
        head, file = os.path.split(filename)
        
        time, Q = get_flow_through_cross_section(filename, polyline, verbose=True)

        plt.plot(time/3600., Q, label=file[0:-4])
        plt.title('Hydrographs for '+ folder)
        plt.legend(loc='best')    
    
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (hours)')
    plt.ylabel('Flows (m3/sec)')
    plt.show()

    
