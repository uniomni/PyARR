DATA STRUCTURE REQUIREMENTS FOR POST PROCESSING WITH PyARR SCRIPTS

This file documents the data structure required to run the PyARR
post processing suite. 

The scripts have been built to allow post processing of ANUGA SWW files
using the new Australian Rainfall and Runoff methodology (ARR2019). 

The new ARR2019 methodology now has 10 patterns to be run for each Storm 
Duration. To determine which Duration/Pattern combination is critical 
for your catchment, the Duration/Pattern one up from the mean (or median) 
for the 10 patterns must be calculated.

Once the user has run their ANUGA model, the files need to be oragnised
in the following order for the scripts to work properly:

Storm event directory -> SWW directory -> directories containing the 
10 SWW files for each pattern.

For example, the directory structure and naming must be as follows:

Root     |          |                    |  
Directory| Directory| Directory          | SWW Files
=======================================================================
1%AEP    |   SWW    | 1%AEP10m_unblocked | 1%AEP10m_P1_unblocked.sww
         |          |                    | 1%AEP10m_P2_unblocked.sww
         |          |                    | 1%AEP10m_P3_unblocked.sww
         |          |                    | 1%AEP10m_P4_unblocked.sww
         |          |                    | 1%AEP10m_P5_unblocked.sww
         |          |                    | 1%AEP10m_P6_unblocked.sww         
         |          |                    | 1%AEP10m_P7_unblocked.sww
         |          |                    | 1%AEP10m_P8_unblocked.sww
         |          |                    | 1%AEP10m_P9_unblocked.sww
         |          |                    | 1%AEP10m_P10_unblocked.sww  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                
         |          | 1%AEP15m_unblocked | 1%AEP15m_P1_unblocked.sww
         |          |                    | 1%AEP15m_P2_unblocked.sww
         |          |                    | 1%AEP15m_P3_unblocked.sww
         |          |                    | 1%AEP15m_P4_unblocked.sww
         |          |                    | 1%AEP15m_P5_unblocked.sww
         |          |                    | 1%AEP15m_P6_unblocked.sww         
         |          |                    | 1%AEP15m_P7_unblocked.sww
         |          |                    | 1%AEP15m_P8_unblocked.sww
         |          |                    | 1%AEP15m_P9_unblocked.sww
         |          |                    | 1%AEP15m_P10_unblocked.sww  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++           
         |          | 1%AEP20m_unblocked | 1%AEP20m_P1_unblocked.sww
         |          |                    | 1%AEP20m_P2_unblocked.sww
         |          |                    | 1%AEP20m_P3_unblocked.sww
         |          |                    | 1%AEP20m_P4_unblocked.sww
         |          |                    | 1%AEP20m_P5_unblocked.sww
         |          |                    | 1%AEP20m_P6_unblocked.sww         
         |          |                    | 1%AEP20m_P7_unblocked.sww
         |          |                    | 1%AEP20m_P8_unblocked.sww
         |          |                    | 1%AEP20m_P9_unblocked.sww
         |          |                    | 1%AEP20m_P10_unblocked.sww          
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++           
         |          | 1%AEP25m_unblocked | 1%AEP20m_P1_unblocked.sww         
etc etc to your last Duration        
         
The 1_sww2maxTIF.py script then goes through the directories and creates
a new directory called TIFS. It then extracts the MAXIMUM quantity (D, V, VD and WL)
from the ANUGA SWW files and stores them in sub directories defined by the quantity 
in the following structure:

Root     |          |                    |  
Directory| Directory| Directory          | Directory |  Maximums TIF file
==================================================================================================================
1%AEP    |   TIFS   | 1%AEP10m_unblocked |    D      |  1%AEP10m_P1_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P2_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P3_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P4_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P5_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P6_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P7_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P8_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P9_unblocked_depth_max.tif
         |          |                    |           |  1%AEP10m_P10_unblocked_depth_max.tif
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++          
         |          |                    |     V     |  1%AEP10m_P3_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP10m_P4_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP10m_P5_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP10m_P6_unblocked_velocity_max.tif        
         |          |                    |           |  1%AEP10m_P7_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP10m_P8_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP10m_P9_unblocked_velocity_max.tif         
         |          |                    |           |  1%AEP10m_P10_unblocked_velocity_max.tif
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++          
         |          |                    |     VD    |  1%AEP10m_P1_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP10m_P2_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP10m_P3_unblocked_depthIntegratedVelocity_max.tif        
         |          |                    |           |  1%AEP10m_P4_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP10m_P5_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP10m_P6_unblocked_depthIntegratedVelocity_max.tif          
         |          |                    |           |  1%AEP10m_P7_unblocked_depthIntegratedVelocity_max.tif        
         |          |                    |           |  1%AEP10m_P8_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP10m_P9_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP10m_P10_unblocked_depthIntegratedVelocity_max.tif           
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++         
         |          |                    |     WL    |  1%AEP10m_P3_unblocked_stage_max.tif
         |          |                    |           |  1%AEP10m_P4_unblocked_stage_max.tif
         |          |                    |           |  1%AEP10m_P5_unblocked_stage_max.tif
         |          |                    |           |  1%AEP10m_P6_unblocked_stage_max.tif        
         |          |                    |           |  1%AEP10m_P7_unblocked_stage_max.tif
         |          |                    |           |  1%AEP10m_P8_unblocked_stage_max.tif
         |          |                    |           |  1%AEP10m_P9_unblocked_stage_max.tif         
         |          |                    |           |  1%AEP10m_P10_unblocked_stage_max.tif
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
         |          | 1%AEP15m_unblocked |    D      |  1%AEP15m_P1_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P2_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P3_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P4_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P5_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P6_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P7_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P8_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P9_unblocked_depth_max.tif
         |          |                    |           |  1%AEP15m_P10_unblocked_depth_max.tif
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++          
         |          |                    |     V     |  1%AEP15m_P3_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP15m_P4_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP15m_P5_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP15m_P6_unblocked_velocity_max.tif        
         |          |                    |           |  1%AEP15m_P7_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP15m_P8_unblocked_velocity_max.tif
         |          |                    |           |  1%AEP15m_P9_unblocked_velocity_max.tif         
         |          |                    |           |  1%AEP15m_P10_unblocked_velocity_max.tif
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++          
         |          |                    |     VD    |  1%AEP15m_P1_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP15m_P2_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP15m_P3_unblocked_depthIntegratedVelocity_max.tif        
         |          |                    |           |  1%AEP15m_P4_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP15m_P5_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP15m_P6_unblocked_depthIntegratedVelocity_max.tif          
         |          |                    |           |  1%AEP15m_P7_unblocked_depthIntegratedVelocity_max.tif        
         |          |                    |           |  1%AEP15m_P8_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP15m_P9_unblocked_depthIntegratedVelocity_max.tif
         |          |                    |           |  1%AEP15m_P10_unblocked_depthIntegratedVelocity_max.tif           
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++         
         |          |                    |     WL    |  1%AEP15m_P3_unblocked_stage_max.tif
         |          |                    |           |  1%AEP15m_P4_unblocked_stage_max.tif
         |          |                    |           |  1%AEP15m_P5_unblocked_stage_max.tif
         |          |                    |           |  1%AEP15m_P6_unblocked_stage_max.tif        
         |          |                    |           |  1%AEP15m_P7_unblocked_stage_max.tif
         |          |                    |           |  1%AEP15m_P8_unblocked_stage_max.tif
         |          |                    |           |  1%AEP15m_P9_unblocked_stage_max.tif         
         |          |                    |           |  1%AEP15m_P10_unblocked_stage_max.tif

etc etc

From the above, the 3_peak_ofpeaks.py script calculates the mean (or median) [defined in the ARR2019_config.py file]
values for each Duration and creates a TIF of the means (or medians)

Root     |          |                     |  
Directory| Directory| Directory           | mean (or median)_TIF file
===========================================================================
1%AEP    |   MEANS  | Dmean (or Dmedian)  |  1%AEP10m_unblocked_D_mean.tif
         |          |                     |  1%AEP15m_unblocked_D_mean.tif
         |          |                     |  1%AEP20m_unblocked_D_mean.tif
         |          |                     |  1%AEP25m_unblocked_D_mean.tif
         |          |                     |  1%AEP30m_unblocked_D_mean.tif
         |          |                     |  1%AEP45m_unblocked_D_mean.tif         
         |          |                     |  1%AEP60m_unblocked_D_mean.tif
         |          |                     |  1%AEP90m_unblocked_D_mean.tif
         |          |                     | 1%AEP120m_unblocked_D_mean.tif
         |          |                     | 1%AEP180m_unblocked_D_mean.tif  
         |          |                     |  etc etc
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                 
         |          | Vmean (or Vmedian)  |  1%AEP10m_unblocked_V_mean.tif
         |          |                     |  1%AEP15m_unblocked_V_mean.tif
         |          |                     |  1%AEP20m_unblocked_V_mean.tif
         |          |                     |  1%AEP25m_unblocked_V_mean.tif
         |          |                     |  1%AEP30m_unblocked_V_mean.tif
         |          |                     |  1%AEP45m_unblocked_V_mean.tif        
         |          |                     |  1%AEP60m_unblocked_V_mean.tif
         |          |                     |  1%AEP90m_unblocked_V_mean.tif
         |          |                     | 1%AEP120m_unblocked_V_mean.tif
         |          |                     | 1%AEP180m_unblocked_V_mean.tif 
         |          |                     |  etc etc  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
         |          |VDmean (or VDmedian) |  1%AEP10m_unblocked_VD_mean.tif
         |          |                     |  1%AEP15m_unblocked_VD_mean.tif
         |          |                     |  1%AEP20m_unblocked_VD_mean.tif
         |          |                     |  1%AEP25m_unblocked_VD_mean.tif
         |          |                     |  1%AEP30m_unblocked_VD_mean.tif
         |          |                     |  1%AEP45m_unblocked_VD_mean.tif        
         |          |                     |  1%AEP60m_unblocked_VD_mean.tif
         |          |                     |  1%AEP90m_unblocked_VD_mean.tif
         |          |                     | 1%AEP120m_unblocked_VD_mean.tif
         |          |                     | 1%AEP180m_unblocked_VD_mean.tif 
         |          |                     |  etc etc  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
         |          |WLmean (or WLmedian) |  1%AEP10m_unblocked_WL_mean.tif
         |          |                     |  1%AEP15m_unblocked_WL_mean.tif
         |          |                     |  1%AEP20m_unblocked_WL_mean.tif
         |          |                     |  1%AEP25m_unblocked_WL_mean.tif
         |          |                     |  1%AEP30m_unblocked_WL_mean.tif
         |          |                     |  1%AEP45m_unblocked_WL_mean.tif         
         |          |                     |  1%AEP60m_unblocked_WL_mean.tif
         |          |                     |  1%AEP90m_unblocked_WL_mean.tif
         |          |                     | 1%AEP120m_unblocked_WL_mean.tif
         |          |                     | 1%AEP180m_unblocked_WL_mean.tif  
         |          |                     |  etc etc  

and finally the peak of peaks from the above data


Root     |          | 
Directory| Directory|   PEAK OF PEAKS
======================================================
1%AEP    |   PEAKS  |   D_mean_peakofpeaks.tif
         |          |   V_mean_peakofpeaks.tif 
         |          |   VD_mean_peakofpeaks.tif
         |          |   WL_mean_peakofpeaks.tif

Technically, these peaks are not exactly one up from the mean (or meadian) but they are 
close enough.

If you want the exact value of the one up fromthe mean (or madian) and the Duration/Pattern
that is resposible for it, you can run 2_critical_duration_patterns.py script.

It will find the critical Storm Duration/Pattern at any location in the catchment.

The user needs to define n number of locations (E,N) in the ARR2019_config.py and the script 
reads ALL SWW files and return the Storm Duration/Pattern one up from the mean (or median) 
at that location.
