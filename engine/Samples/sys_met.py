
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
  SYS = wmi.WMI()
  OSINFO = SYS.Win32_OperatingSYStem()[0]
  PROCINFO = SYS.Win32_Processor()[0]
  GPUINFO = SYS.Win32_VideoController()[0]
  
  PROCU = psutil.cpu_percent()
  MEMU = psutil.virtual_memory()
  OSNAME = OSINFO.Name
  OSVERSION = OSINFO.Version
  SYSRAM = float(OSINFO.TotalVisibleMemorySize) / 1048576  # KB to GB
  for process in SYS.Win32_Process():
    PID = process.ProcessId
    PN = process.Name
    PE = process.executablepath
    PS = process.Status
    #print(PID, PN, PE, PS)
  #print(PROCU)
  met["OS Name"] = OSNAME
  met["OS Version"] = OSVERSION
  met["memory usage"] = MEMU
  met["processor Usage"] = PROCU
  met["systemRam"] = SYSRAM
  met["processInfo"] = PROCINFO.Name
  met["GPUInfo"] = GPUINFO.Name
  #met["date and time"] = 
  #print(met)
  #print(MEMU)
  #print('OS Name: {0}'.format(OSNAME))
  #print('OS Version: {0}'.format(OSVERSION))
  #print('CPU: {0}'.format(PROCINFO.Name))
  
  #print('RAM: {0} GB'.format(SYSRAM))
  #print('Graphics Card: {0}'.format(GPUINFO.Name))





