from Path_test import * 
import unittest




class TestClarkWrite(unittest.TestCase):
    def test_CW_is_instance_CW(self):
        CW = ClarkandWrite()
        self.assertIsInstance(CW,ClarkandWrite)
    
    def test_initial_Nb_edges(self):
        self.CW = ClarkandWrite()
        self.assertAlmostEqual(self.CW.NbEdges,0)
        

if __name__ == "__main__":
    unittest.main()