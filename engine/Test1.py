# TestSys_met.py

# Import statements
import self as self
import unittest
from MetFun import memUsage, ProcUsage
import psutil

#SampleTest.path.append("C:/Users/prabhleen/Project-MSCS710L/engine/Samples")
import time


# from sys_met import *

class UnitTestCase(unittest.TestCase):
    def test_values(self):
        # Capture the results of the functions
        MEM = psutil.virtual_memory()

        result = memUsage()

        self.assertEqual(MEM, result)



    def test_values1(self):
        # Capture the results of the functions

        PROC = psutil.cpu_percent()

        result2 = ProcUsage()

        self.assertEqual(PROC, result2)

  # Check for expected output




 # print("sec ---")

 # Run the test

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
