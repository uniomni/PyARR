import unittest

from find_mean_depth import find_average_element

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

     
if __name__ == '__main__':
    unittest.main()
