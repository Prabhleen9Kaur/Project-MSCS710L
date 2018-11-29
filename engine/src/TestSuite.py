#fileName : TestCase1.py
#author : Aishwarya Pagalla
# last modified : 11/28/2018
import unittest
import psutil
import wmi
from Metric import *
 
class TestUM(unittest.TestCase):
	
    def test_MemUsage(self):
        self.z = psutil.virtual_memory()
        self.assertEqual(Metric.memUsage(), self.z)
		
    def test_OSInfo(self):
        OSINFO = wmi.WMI().Win32_OperatingSYStem()[0]
        self.y = OSINFO.Name
        self.assertEqual(Metric.Proc(wmi.WMI()), self.y)
        	
    def test_processInfo(self):
        self.w = wmi.WMI().Win32_Processor()[0].Name
        self.assertEqual(Metric.ProcInfo(wmi.WMI()), self.w)
	
    def test_ProcUsage(self):
        self.z = psutil.cpu_percent()
        print(self.z)
        self.assertEqual(Metric.ProcUsage(), self.z)
			
	
if __name__ == '__main__':
    unittest.main()

