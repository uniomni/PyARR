import os
import glob
import time
import os.path
from ARR2019_config import root_directory
from ARR2019_post_processing import plot_hydrographs
import matplotlib.pyplot as plt
from anuga.shallow_water.sww_interrogate import get_flow_through_cross_section
from anuga.caching import cache

# Enter location poly here 
#polyline = [(299167.162,6180397.967),(299232.924,6180475.358)] #this one is for Brooks Ck outlet
#polyline = [(306632.382,6186448.055),(306680.364,6186443.441)] #this one is for Wollongong City outlet
polyline = [(314029.861,6214403.147),(314011.461,6214459.153)] #Walker St Helensburgh
#polyline = [(314092.661,6214427.176),(314070.568,6214428.145)] #Buldo Lane Helensburgh

# Directories
data_directory = os.path.join(root_directory, 'SWW')
sub_folders = [name for name in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, name))]
destdir = os.path.join(root_directory, 'PLOTS')

print(f'Making {destdir}')
os.makedirs(destdir, exist_ok=True)

for folder in sub_folders:

    # Get all events from this folder
    fromdir = os.path.join(root_directory, 'SWW', folder)
    pattern = os.path.join(fromdir, '*.sww')
    filenames = glob.glob(pattern) 
    
    # Sort filenames by P1, P2, ..., P10
    filenames = sorted(filenames, key=lambda x: int("".join([i for i in x if i.isdigit()])))
    
    # Create name for this plot
    target = os.path.join(destdir, folder + '.png')
    print(f'Saving to {target}')
    
    # Set up new plot for this folder
    plt.clf() # Clear figure
    plt.title('Hydrographs for '+ folder)
    plt.xlabel('Time (hours)')
    plt.ylabel('Flows (m3/sec)')    
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)    

    # Plot all hydrographs for this folder
    t0 = time.time()        
    for filename in filenames: 
        # Extract the event (P1, P2, ...., P10) from the filename to be used as label
        # This assumes a filename of the form '1%AEP540m_P4_unblocked.sww'
        _, event = os.path.split(filename)        
        i = event.find('_P') 
        j = i + 2
        while event[j].isdigit():
            j += 1
            
        if i >= 0:
            label = event[i+1:j]
        else:
            label = event[0:-4]
        
        # Check if it has already been cached and make a note in the output stream
        if cache(get_flow_through_cross_section, 
                 args=(filename, polyline), 
                 kwargs={'verbose': False},
                 dependencies=filename,
                 verbose=False,
                 test=True):
            flag = 'cached'
        else:
            flag = 'computing'

        # Compute Hydrograph or retrieve from cache    
        print(f'Processing {filename} - ({flag})')
        t, Q = cache(get_flow_through_cross_section, 
                     args=(filename, polyline), 
                     kwargs={'verbose': False},
                     dependencies=filename,
                     verbose=False)
        plt.plot(t/3600., Q, label=label)
        plt.legend(loc='best')    
        plt.title('Qmax = %.3f m3/s' %(max(Q)))        
        
    plt.savefig(target)
    print(f'finished plotting {folder} in {(time.time() - t0):.2f} seconds')
    #plt.show()
