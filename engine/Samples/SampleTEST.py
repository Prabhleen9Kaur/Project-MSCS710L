import psutil
def memUsage():  
    MEMU = psutil.virtual_memory()
    return MEMU

def ProcUsage():
    PROCU = psutil.cpu_percent()
    return PROCU
memUsage()
ProcUsage()
