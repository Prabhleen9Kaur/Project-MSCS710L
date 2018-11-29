#fileName : Metric.py
#author : Aishwarya Pagalla
# last modified : 11/14/2018
import psutil
import wmi
class Metric():
    SYS = wmi.WMI()
	
    def memUsage():  
        MEMU = psutil.virtual_memory()
        return MEMU
		
    def ProcUsage():
        PROCU = psutil.cpu_percent()
        print(PROCU)
        return PROCU
		
    def Processes(SYS):
        for process in SYS.Win32_Process():
            PID = process.ProcessId
            #print(PID)
            return PID
		
    def Proc(SYS):
        OSINFO = SYS.Win32_OperatingSYStem()[0].Name
        #print(OSINFO)
        return OSINFO
		
    def ProcInfo(SYS):
        PN = SYS.Win32_Processor()[0].Name
        return PN
		
    memUsage()	
    ProcUsage()
    Processes(SYS)
    Proc(SYS)
    ProcInfo(SYS)