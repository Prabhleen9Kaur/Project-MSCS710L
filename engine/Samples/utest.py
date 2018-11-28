# TestSys_met.py

#Import statements

import unittest
import sys_met
import psutil
from SampleTest import PROCU , MEMU
import time 
#from sys_met import *

class UnitTestCase(unittest.TestCase):
    """Test for 'sys_met.py'"""
    
    def setUp(self):
        self.MEM = psutil.virtual_memory()
        self.PROC = psutil.cpu_percent()
        self.start_time = time.time()

    def test_values(self):
        # Capture the results of the funcyions
        result = sys_met

        # Check for expected output
     
        self.assertEqual(MEM, MEMU)
        self.assertEqual(PROC, PROCU)

    def tearDown(self):
        if self.failed:
            return
        if self.reportStatus_:
            self.log.info("=== Test %s completed normally (%d sec)", self.name_, time_taken

        print("--- %s sec ---" %(time.time() - start_time))

    # Run the test
   
    if __name__== '__main__':
        unittest.main()