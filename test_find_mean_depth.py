import unittest

from find_mean_depth import find_average_element

class TestFindMeanDepth(unittest.TestCase):

    def setUp(self):
        
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

    
    def test_basic(self):
        mean, (filename, depth) = find_average_element(self.X)

        assert mean == 1.07459002, 'Mean value should have been %f, I got %f' % (1.07459002, mean)
        assert filename == '1%AEP10m_P6_unblocked_depth_max', 'Name should have been %s, I got %s' % ('1%AEP10m_P6_unblocked_depth_max', filename)
        assert depth == 1.0747306, 'Depth should have been %f, I got %f' % (1.0747306, depth)

     
if __name__ == '__main__':
    unittest.main()
