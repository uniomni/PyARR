"""Test script that 

1. calculate the average or mean of the 10 numbers.
2. choose the file which is one up from the average (for example it
will be file '1%AEP10m_P6_unblocked_depth_max' and return the value
and filename.

Algorithm is very simplistic but will work well for small data sets

Ole Nielsen - 2021
"""

def find_average_element(X):
    """ Find element closest to the mean from above
    
    Input: List of 2-tuples where each tuple has the form: (string, float)
    Output: The mean value and the 2-tuple where the float is closest to the mean from above, i.e mean, (string, float) 
     
    Algorithm:
    1. calculate the mean of the 10 numbers.
    2. choose the file which is one up from the average (for example it
    will be file '1%AEP10m_P6_unblocked_depth_max' and return the value
    and filename.
    
    Example
    
    With input 
     
     X1 = [('1%AEP10m_P1_unblocked_stage_max', 1.8705895),
     ('1%AEP10m_P10_unblocked_stage_max', 1.8682307),
     ('1%AEP10m_P5_unblocked_stage_max', 1.8693119),
     ('1%AEP10m_P6_unblocked_stage_max', 1.8692424),
     ('1%AEP10m_P2_unblocked_stage_max', 1.8681568),
     ('1%AEP10m_P4_unblocked_stage_max', 1.8682132),
     ('1%AEP10m_P8_unblocked_stage_max', 1.8681607),
     ('1%AEP10m_P7_unblocked_stage_max', 1.8712964),
     ('1%AEP10m_P9_unblocked_stage_max', 1.8695077),
     ('1%AEP10m_P3_unblocked_stage_max', 1.868309)]


     X2= [('1%AEP15m_P6_unblocked_stage_max', 2.0678904),
     ('1%AEP15m_P10_unblocked_stage_max', 2.0737209),
     ('1%AEP15m_P7_unblocked_stage_max', 2.0701876),
     ('1%AEP15m_P5_unblocked_stage_max', 2.0745227),
     ('1%AEP15m_P8_unblocked_stage_max', 2.0659935),
     ('1%AEP15m_P3_unblocked_stage_max', 2.0676861),
     ('1%AEP15m_P2_unblocked_stage_max', 2.0643792),
     ('1%AEP15m_P4_unblocked_stage_max', 2.0719421),
     ('1%AEP15m_P1_unblocked_stage_max', 2.0655258),
     ('1%AEP15m_P9_unblocked_stage_max', 2.0719631)]
     
     
     X3 = [('1%AEP20m_P7_unblocked_stage_max', 2.1977205),
     ('1%AEP20m_P6_unblocked_stage_max', 2.199913) ,
     ('1%AEP20m_P2_unblocked_stage_max', 2.1961679),
     ('1%AEP20m_P10_unblocked_stage_max', 2.2024157),
     ('1%AEP20m_P8_unblocked_stage_max', 2.2004216),
     ('1%AEP20m_P1_unblocked_stage_max', 2.1974928),
     ('1%AEP20m_P3_unblocked_stage_max', 2.196106) ,
     ('1%AEP20m_P9_unblocked_stage_max', 2.1966093),
     ('1%AEP20m_P5_unblocked_stage_max', 2.1961856),
     ('1%AEP20m_P4_unblocked_stage_max', 2.1971824)]
													
													
     X4 = [('1%AEP25m_P1_unblocked_stage_max', 2.2817981),
     ('1%AEP25m_P2_unblocked_stage_max', 2.2838025),
     ('1%AEP25m_P10_unblocked_stage_max', 2.2838564),
     ('1%AEP25m_P9_unblocked_stage_max', 2.2913594),
     ('1%AEP25m_P8_unblocked_stage_max', 2.2897279),
     ('1%AEP25m_P6_unblocked_stage_max', 2.2846599),
     ('1%AEP25m_P5_unblocked_stage_max', 2.2868171),
     ('1%AEP25m_P4_unblocked_stage_max', 2.2838123),
     ('1%AEP25m_P7_unblocked_stage_max', 2.2835138),
     ('1%AEP25m_P3_unblocked_stage_max', 2.2858226)]


     X5 = [('1%AEP30m_P10_unblocked_stage_max', 2.334852),
     ('1%AEP30m_P3_unblocked_stage_max', 2.34512)  ,
     ('1%AEP30m_P9_unblocked_stage_max', 2.3298388),
     ('1%AEP30m_P1_unblocked_stage_max', 2.3440502),
     ('1%AEP30m_P2_unblocked_stage_max', 2.3385532),
     ('1%AEP30m_P5_unblocked_stage_max', 2.3390689),
     ('1%AEP30m_P4_unblocked_stage_max', 2.3450401),
     ('1%AEP30m_P7_unblocked_stage_max', 2.345221) ,
     ('1%AEP30m_P8_unblocked_stage_max', 2.3392143),
     ('1%AEP30m_P6_unblocked_stage_max', 2.3396771)]


     X6 = [('1%AEP45m_P2_unblocked_stage_max', 2.4898553),
     ('1%AEP45m_P5_unblocked_stage_max', 2.5014749),
     ('1%AEP45m_P10_unblocked_stage_max', 2.4797029),
     ('1%AEP45m_P8_unblocked_stage_max', 2.4828348),
     ('1%AEP45m_P6_unblocked_stage_max', 2.5024498),
     ('1%AEP45m_P7_unblocked_stage_max', 2.4725015),
     ('1%AEP45m_P1_unblocked_stage_max', 2.4850721),
     ('1%AEP45m_P4_unblocked_stage_max', 2.4975798),
     ('1%AEP45m_P3_unblocked_stage_max', 2.4944859),
     ('1%AEP45m_P9_unblocked_stage_max', 2.4721892)]


     X7 = [('1%AEP60m_P1_unblocked_stage_max', 2.5318513),
     ('1%AEP60m_P7_unblocked_stage_max', 2.5526414),
     ('1%AEP60m_P6_unblocked_stage_max', 2.5852857),
     ('1%AEP60m_P5_unblocked_stage_max', 2.5407801),
     ('1%AEP60m_P10_unblocked_stage_max', 2.5924399),
     ('1%AEP60m_P2_unblocked_stage_max', 2.5630639),
     ('1%AEP60m_P9_unblocked_stage_max', 2.5771348),
     ('1%AEP60m_P8_unblocked_stage_max', 2.6025951),
     ('1%AEP60m_P4_unblocked_stage_max', 2.5810723),
     ('1%AEP60m_P3_unblocked_stage_max', 2.5558038)]


     X8 = [('1%AEP90m_P8_unblocked_stage_max', 2.6522701),
     ('1%AEP90m_P10_unblocked_stage_max', 2.6165695),
     ('1%AEP90m_P4_unblocked_stage_max', 2.6732743),
     ('1%AEP90m_P5_unblocked_stage_max', 2.6817479),
     ('1%AEP90m_P6_unblocked_stage_max', 2.6929593),
     ('1%AEP90m_P2_unblocked_stage_max', 2.7378044),
     ('1%AEP90m_P1_unblocked_stage_max', 2.6929703),
     ('1%AEP90m_P7_unblocked_stage_max', 2.5993655),
     ('1%AEP90m_P9_unblocked_stage_max', 2.674263) ,
     ('1%AEP90m_P3_unblocked_stage_max', 2.7333629)]


     X9 = [('1%AEP120m_P4_unblocked_stage_max', 2.7062404),
     ('1%AEP120m_P9_unblocked_stage_max', 2.7350609),
     ('1%AEP120m_P6_unblocked_stage_max', 2.8127959),
     ('1%AEP120m_P2_unblocked_stage_max', 2.7296493),
     ('1%AEP120m_P1_unblocked_stage_max', 2.6948118),
     ('1%AEP120m_P5_unblocked_stage_max', 2.6873662),
     ('1%AEP120m_P10_unblocked_stage_max', 2.6844959),
     ('1%AEP120m_P7_unblocked_stage_max', 2.7297156),
     ('1%AEP120m_P8_unblocked_stage_max', 2.7039683),
     ('1%AEP120m_P3_unblocked_stage_max', 2.7310781)]


     X10 = [('1%AEP180m_P7_unblocked_stage_max', 2.8557935),
     ('1%AEP180m_P6_unblocked_stage_max', 2.8398173),
     ('1%AEP180m_P1_unblocked_stage_max', 2.8502693),
     ('1%AEP180m_P8_unblocked_stage_max', 2.8356352),
     ('1%AEP180m_P10_unblocked_stage_max', 2.8072174),
     ('1%AEP180m_P3_unblocked_stage_max', 2.8140657),
     ('1%AEP180m_P4_unblocked_stage_max', 2.599273),
     ('1%AEP180m_P9_unblocked_stage_max', 2.8607934),
     ('1%AEP180m_P2_unblocked_stage_max', 2.8043351),
     ('1%AEP180m_P5_unblocked_stage_max', 2.7329125)]


     X11 = [('1%AEP270m_P5_unblocked_stage_max', 2.8194346),
     ('1%AEP270m_P4_unblocked_stage_max', 2.8228433),
     ('1%AEP270m_P7_unblocked_stage_max', 2.8541172),
     ('1%AEP270m_P9_unblocked_stage_max', 2.7063468),
     ('1%AEP270m_P10_unblocked_stage_max', 2.8155825),
     ('1%AEP270m_P6_unblocked_stage_max', 2.8288534),
     ('1%AEP270m_P8_unblocked_stage_max', 2.8039665),
     ('1%AEP270m_P2_unblocked_stage_max', 2.7202041),
     ('1%AEP270m_P1_unblocked_stage_max', 2.8208802),
     ('1%AEP270m_P3_unblocked_stage_max', 2.9916115)]


     X12 = [('1%AEP360m_P4_unblocked_stage_max', 2.86917) ,
     ('1%AEP360m_P3_unblocked_stage_max', 2.719059),
     ('1%AEP360m_P7_unblocked_stage_max', 2.8243089),
     ('1%AEP360m_P2_unblocked_stage_max', 3.033473),
     ('1%AEP360m_P1_unblocked_stage_max', 2.914763),
     ('1%AEP360m_P10_unblocked_stage_max', 2.8446043),
     ('1%AEP360m_P9_unblocked_stage_max', 2.8922281),
     ('1%AEP360m_P5_unblocked_stage_max', 2.7801676),
     ('1%AEP360m_P8_unblocked_stage_max', 3.0484824),
     ('1%AEP360m_P6_unblocked_stage_max', 2.846952)]


     X13 = [('1%AEP540m_P8_unblocked_stage_max', 3.0152571),
     ('1%AEP540m_P4_unblocked_stage_max', 2.7234151),
     ('1%AEP540m_P10_unblocked_stage_max', 2.5826631),
     ('1%AEP540m_P2_unblocked_stage_max', 2.9444456),
     ('1%AEP540m_P3_unblocked_stage_max', 2.8446078),
     ('1%AEP540m_P9_unblocked_stage_max', 2.6812329),
     ('1%AEP540m_P1_unblocked_stage_max', 2.7062206),
     ('1%AEP540m_P7_unblocked_stage_max', 2.8981698),
     ('1%AEP540m_P6_unblocked_stage_max', 2.8440082),
     ('1%AEP540m_P5_unblocked_stage_max', 2.7292616)]


     X14 = [('1%AEP720m_P4_unblocked_stage_max', 3.0164073),
     ('1%AEP720m_P6_unblocked_stage_max', 2.9830968),
     ('1%AEP720m_P8_unblocked_stage_max', 2.901221),
     ('1%AEP720m_P10_unblocked_stage_max', 2.8586011),
     ('1%AEP720m_P9_unblocked_stage_max', 2.7740173),
     ('1%AEP720m_P1_unblocked_stage_max', 2.7482364),
     ('1%AEP720m_P7_unblocked_stage_max', 2.7208292),
     ('1%AEP720m_P2_unblocked_stage_max', 2.8927264),
     ('1%AEP720m_P5_unblocked_stage_max', 2.7370315),
     ('1%AEP720m_P3_unblocked_stage_max', 2.7983155)]

    at this location: 
    
    points_list = [(306679.877,6187525.723)]
    
    the results are:
    
    The output for X1 should be 1.8692424, (1%AEP10m_P6_unblocked_stage_max, 1.8692424)

    The output for X2 should be 2.0701876, ('1%AEP15m_P7_unblocked_stage_max', 2.0701876)

    The output for X3 should be 2.199913, ('1%AEP20m_P6_unblocked_stage_max', 2.199913)
    
    The output for X4 should be 2.2858226, ('1%AEP25m_P3_unblocked_stage_max', 2.2858226)
    
    The output for X5 should be 2.3440502, ('1%AEP30m_P1_unblocked_stage_max', 2.3440502)

    The output for X6 should be 2.4898553, ('1%AEP45m_P2_unblocked_stage_max', 2.4898553)

    The output for X7 should be 2.5771348, ('1%AEP60m_P9_unblocked_stage_max', 2.5771348)
    
    The output for X8 should be 2.6817479, ('1%AEP90m_P5_unblocked_stage_max', 2.6817479)

    The output for X9 should be 2.7296493, ('1%AEP120m_P2_unblocked_stage_max', 2.7296493)

    The output for X10 should be 2.8043351, ('1%AEP180m_P2_unblocked_stage_max', 2.8043351)
    
    The output for X11 should be 2.8194346, ('1%AEP270m_P5_unblocked_stage_max', 2.8194346)
    
    The output for X12 should be 2.8922281, ('1%AEP360m_P9_unblocked_stage_max', 2.8922281)
    
    The output for X13 should be 2.8440082, ('1%AEP540m_P6_unblocked_stage_max', 2.8440082)
    
    The output for X14 should be 2.8586011, ('1%AEP720m_P10_unblocked_stage_max', 2.8586011)

    """
    
    # Sort by depth (Schwartzian Transform)
    Y = [(d[1], d[0]) for d in X]  # Swap order, making depth the first column
    Y.sort()

    # Calculate average
    sum = 0
    for y in Y:
        sum += y[0]
    mean = sum/len(Y)

    # Now find element immediately greater than average
    i = 0
    y = Y[0][0] 
    while(y <= mean):
        i += 1
        y = Y[i][0]

    filename = Y[i][1]
    depth = Y[i][0]
    
    # FIXME: Speak to Petar about variable names in this context
    return mean, (filename, depth)
    


