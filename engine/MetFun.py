import psutil
#import win32com.client
#from Metric import gpu_info #, proc_info, os_name, os_version, system_ram

def memUsage():

    MEMU = psutil.virtual_memory()

    return MEMU

def ProcUsage():
    

    PROCU = psutil.cpu_percent()
    print(PROCU)
    return PROCU

#def Ginfo():
    #gpu_info = sys.Win32_VideoController()[0]
    #return gpu_info.Name

#def Cinfo():
  #  CpuInfo = proc_info.Name
   # print(CpuInfo)
memUsage()

ProcUsage()
#Ginfo()
