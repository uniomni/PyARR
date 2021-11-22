import os
import glob
import os.path
from ARR2019_config import root_directory
from ARR2019_post_processing import plot_hydrographs

# enter location poly here 
polyline = [(299167.162,6180397.967),(299232.924,6180475.358)] #this one is for Brooks Ck outlet
#polyline = [(306632.382,6186448.055),(306680.364,6186443.441)] #this one is for Wollongong City outlet

data_directory = os.path.join(root_directory, 'SWW')
sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]



# cant get this to work
# for folder in sub_folders:
    # fromdir = os.path.join(root_directory, 'SWW', folder)
    # destdir = os.path.join(root_directory, 'PLOTS')
    # #print (fromdir, destdir)
        
    # plot_hydrographs(fromdir, destdir, polyline = polyline) 
    
    
import matplotlib.pyplot as plt
from anuga.shallow_water.sww_interrogate import get_flow_through_cross_section


for folder in sub_folders:
    
    fromdir = os.path.join(root_directory, 'SWW', folder)
    destdir = os.path.join(root_directory, 'PLOTS', folder)    
    
    pattern = os.path.join(fromdir, '*.sww')
    filenames = glob.glob(pattern) 
    print (folder)
    
    for filename in filenames: 

        head, file = os.path.split(filename)
        print (file)
        time, Q = get_flow_through_cross_section(filename, polyline, verbose=True)

        plt.plot(time/3600., Q, label=file[0:-4])
        plt.title('Hydrographs for '+ folder)
        plt.legend(loc='best')        
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        plt.xlabel('Time (hours)')
        plt.ylabel('Flows (m3/sec)')
    
    plt.savefig(folder + '.png')
      
    print('finished plotting: ', folder)
        #plt.show()