
# coding: utf-8
#metric.py
#Aishwarya Pagalla
# oct 5 2018
import wmi
import psutil
import datetime
'''
 This a piece of code works to get processes running on a SYStem along with SYStem info using wmi library 
programming language : python 

'''
class sys_met():
  met = {}
  sett = {}
  inf = {}
  PID, PN, PE, PS = ([] for i in range(4))
  SYS = wmi.WMI()
  OSINFO = SYS.Win32_OperatingSYStem()[0]
  PROCINFO = SYS.Win32_Processor()[0]
  GPUINFO = SYS.Win32_VideoController()[0]
  PROCU = psutil.cpu_percent()
  MEMU = psutil.virtual_memory()
  OSNAME = OSINFO.Name
  OSVERSION = OSINFO.Version
  SYSRAM = float(OSINFO.TotalVisibleMemorySize) / 1048576  # KB to GB
  inf["OSName"] = OSNAME
  inf["OSVersion"] = OSVERSION
  inf["SystemRam"] = SYSRAM
  inf["ProcessInfo"] = PROCINFO.Name
  inf["GPUInfo"] = GPUINFO.Name
  for process in SYS.Win32_Process():
    PID.append(process.ProcessId)
    PN.append(process.Name)
    PE.append(process.executablepath)
    PS.append(process.Status)
    met["ProcessID"] = PID
    met["ProcessName"] = PN
    met["ProcessExePath"] = PE
    met["ProcessStatus"] = PS	
    #print(PID, PN, PE, PS)
  sett["MemoryUsage"] = MEMU
  sett["ProcessorUsage"] = PROCU
  #print(sett)
  
  