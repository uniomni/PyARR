import unittest

from ARR2019_post_processing import find_average_element, find_max_values_across_all_durations

class TestFindMeanDepth(unittest.TestCase):

    def setUp(self):
        
        # Depth based scenario
        self.X = [('1%AEP10m_P4_unblocked_depth_max', 1.0737015),
                  ('1%AEP10m_P8_unblocked_depth_max', 1.0736489),
                  ('1%AEP10m_P7_unblocked_depth_max', 1.0767846),
                  ('1%AEP10m_P6_unblocked_depth_max', 1.0747306),
                  ('1%AEP10m_P2_unblocked_depth_max', 1.073645),
                  ('1%AEP10m_P10_unblocked_depth_max', 1.0737189),
                  ('1%AEP10m_P1_unblocked_depth_max', 1.0760777),
                  ('1%AEP10m_P5_unblocked_depth_max', 1.0748001),
                  ('1%AEP10m_P9_unblocked_depth_max', 1.0749958),
                  ('1%AEP10m_P3_unblocked_depth_max', 1.0737971)]
                  
                  
        # Level based scenario                  
        self.X1 = [('1%AEP10m_P1_unblocked_stage_max', 1.8705895),
                   ('1%AEP10m_P10_unblocked_stage_max', 1.8682307),
                   ('1%AEP10m_P5_unblocked_stage_max', 1.8693119),
                   ('1%AEP10m_P6_unblocked_stage_max', 1.8692424),
                   ('1%AEP10m_P2_unblocked_stage_max', 1.8681568),
                   ('1%AEP10m_P4_unblocked_stage_max', 1.8682132),
                   ('1%AEP10m_P8_unblocked_stage_max', 1.8681607),
                   ('1%AEP10m_P7_unblocked_stage_max', 1.8712964),
                   ('1%AEP10m_P9_unblocked_stage_max', 1.8695077),
                   ('1%AEP10m_P3_unblocked_stage_max', 1.868309)]
                  

    
    def test_depth(self):
        mean, (filename, depth) = find_average_element(self.X)

        assert mean == 1.07459002, 'Mean value should have been %f, I got %f' % (1.07459002, mean)
        assert filename == '1%AEP10m_P6_unblocked_depth_max', 'Name should have been %s, I got %s' % ('1%AEP10m_P6_unblocked_depth_max', filename)
        assert depth == 1.0747306, 'Depth should have been %f, I got %f' % (1.0747306, depth)    
        
    def test_level1(self):
        mean, (filename, stage) = find_average_element(self.X1)

        assert mean == 1.86910183, 'Mean value should have been %f, I got %f' % (1.86910183, mean)
        assert filename == '1%AEP10m_P6_unblocked_stage_max', 'Name should have been %s, I got %s' % ('1%AEP10m_P6_unblocked_stage_max', filename)
        assert stage == 1.8692424, 'Stage should have been %f, I got %f' % (1.8692424, stage)

        
    def test_maximum_value_over_all_durations(self):
    
        locations = [(306679.877, 6187525.723), (305829.954, 6188350.062)]
        durations = [10, 15, 20, 25, 30, 45, 60, 90, 120, 180, 270, 360, 540, 720]
        duration_dict = {10: 
                         {(306679.877, 6187525.723): ('1%AEP10m_P6_unblocked_stage_max.tif', 1.8806984, 1.8805007934570312), 
                          (305829.954, 6188350.062): ('1%AEP10m_P6_unblocked_stage_max.tif', 17.197166, 17.196933555603028)}, 
                         15: 
                         {(306679.877, 6187525.723): ('1%AEP15m_P7_unblocked_stage_max.tif', 2.0994844, 2.0985819816589357), 
                          (305829.954, 6188350.062): ('1%AEP15m_P7_unblocked_stage_max.tif', 17.277727, 17.27648296356201)}, 
                         20: 
                         {(306679.877, 6187525.723): ('1%AEP20m_P6_unblocked_stage_max.tif', 2.2385228, 2.2365264654159547), 
                          (305829.954, 6188350.062): ('1%AEP20m_P6_unblocked_stage_max.tif', 17.321676, 17.320402908325196)}, 
                         25: 
                         {(306679.877, 6187525.723): ('1%AEP25m_P3_unblocked_stage_max.tif', 2.3262367, 2.3259199619293214), 
                          (305829.954, 6188350.062): ('1%AEP25m_P5_unblocked_stage_max.tif', 17.344303, 17.342819213867188)}, 
                         30: 
                         {(306679.877, 6187525.723): ('1%AEP30m_P1_unblocked_stage_max.tif', 2.3853638, 2.381312394142151), 
                          (305829.954, 6188350.062): ('1%AEP30m_P6_unblocked_stage_max.tif', 17.34834, 17.346133995056153)}, 
                         45: 
                         {(306679.877, 6187525.723): ('1%AEP45m_P2_unblocked_stage_max.tif', 2.5309923, 2.528971242904663), 
                          (305829.954, 6188350.062): ('1%AEP45m_P6_unblocked_stage_max.tif', 17.372875, 17.361011505126953)}, 
                         60: 
                         {(306679.877, 6187525.723): ('1%AEP60m_P9_unblocked_stage_max.tif', 2.6182287, 2.609315609931946), 
                          (305829.954, 6188350.062): ('1%AEP60m_P6_unblocked_stage_max.tif', 17.355389, 17.347461318969728)}, 
                         90: 
                         {(306679.877, 6187525.723): ('1%AEP90m_P5_unblocked_stage_max.tif', 2.7221494, 2.7157947540283205), 
                          (305829.954, 6188350.062): ('1%AEP90m_P6_unblocked_stage_max.tif', 17.352478, 17.35140190124512)}, 
                         120: 
                         {(306679.877, 6187525.723): ('1%AEP120m_P2_unblocked_stage_max.tif', 2.7695992, 2.7615134000778196), 
                          (305829.954, 6188350.062): ('1%AEP120m_P4_unblocked_stage_max.tif', 17.33819, 17.325239181518555)}, 
                         180: 
                         {(306679.877, 6187525.723): ('1%AEP180m_P2_unblocked_stage_max.tif', 2.844389, 2.840434193611145), 
                          (305829.954, 6188350.062): ('1%AEP180m_P9_unblocked_stage_max.tif', 17.310911, 17.306969261169435)}, 
                         270: 
                         {(306679.877, 6187525.723): ('1%AEP270m_P5_unblocked_stage_max.tif', 2.8592784, 2.858631157875061), 
                          (305829.954, 6188350.062): ('1%AEP270m_P7_unblocked_stage_max.tif', 17.290796, 17.288502883911132)}, 
                         360: 
                         {(306679.877, 6187525.723): ('1%AEP360m_P9_unblocked_stage_max.tif', 2.9336274, 2.9184953212738036), 
                          (305829.954, 6188350.062): ('1%AEP360m_P1_unblocked_stage_max.tif', 17.284647, 17.28453483581543)}, 
                         540: 
                         {(306679.877, 6187525.723): ('1%AEP540m_P6_unblocked_stage_max.tif', 2.88416, 2.8374516487121584), 
                          (305829.954, 6188350.062): ('1%AEP540m_P3_unblocked_stage_max.tif', 17.264376, 17.26335048675537)}, 
                         720: 
                         {(306679.877, 6187525.723): ('1%AEP720m_P10_unblocked_stage_max.tif', 2.899273, 2.883800721168518), 
                          (305829.954, 6188350.062): ('1%AEP720m_P2_unblocked_stage_max.tif', 17.251663, 17.241789054870605)}}

        max_points_dict = find_max_values_across_all_durations(locations, durations, duration_dict)
        
        assert len(max_points_dict) == 2
        assert (306679.877, 6187525.723) in max_points_dict
        assert (305829.954, 6188350.062) in max_points_dict
        
        one_up_filename, value, mean = max_points_dict[(306679.877, 6187525.723)]
        assert '360m' in one_up_filename
        assert value == 2.9336274
        assert mean == 2.9184953212738036
        
        one_up_filename, value, mean = max_points_dict[(305829.954, 6188350.062)]
        assert '45m' in one_up_filename
        assert value == 17.372875
        assert mean == 17.361011505126953  
        
        #for 
                               
if __name__ == '__main__':
    unittest.main()

    
# More test data

"""     Note by PM: I have added WL instead of depth below
     
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
