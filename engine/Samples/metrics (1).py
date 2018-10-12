
# coding: utf-8

# This a piece of code works to get processes running on a system along with system info using wmi library 
# programming language : python 

# In[7]:


#metric.py
#Aishwarya Pagalla
# oct 5 2018
import wmi
import psutil
sys = wmi.WMI()
sys_info = sys.Win32_ComputerSystem()[0]
os_info = sys.Win32_OperatingSystem()[0]
proc_info = sys.Win32_Processor()[0]
gpu_info = sys.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
for process in sys.Win32_Process ():
    a= process.ProcessId
    print(a, process.Name, process.executablepath, process.Status,process.ThreadCount,process.VirtualSize, process.UserModeTime)
print(psutil.cpu_percent())
print(psutil.virtual_memory())
print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Graphics Card: {0}'.format(gpu_info.Name))


# In[ ]:




