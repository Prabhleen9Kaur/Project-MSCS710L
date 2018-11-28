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
        return PROCU
    def Processes(SYS):
        for process in SYS.Win32_Process():
            PID = process.ProcessId
        return PID
    Processes(SYS)