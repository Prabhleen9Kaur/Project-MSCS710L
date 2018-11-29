from unittest import TestCase
#import unittest.mock
import psutil
from MetFun import ProcUsage, memUsage


class mock_value(TestCase):

    def test_return1(self):
        def mock_value(self):
            MEM1 = memUsage()
            return MEM1
        MEM = psutil.virtual_memory()
        self.assertEqual(MEM,mock_value(self))

    def test_return1(self):
        def mock_value2(self):
            PROC1 = ProcUsage()
            return PROC1
        PROC = psutil.cpu_percent()
        self.assertEqual(PROC, mock_value2(self))

if __name__ == '__main__':
    unittest.main()
