import os

try: 
    os.system('cmd /k "datetime"')
    os.system('cmd /k "sfc /scannow" ')
    os.system('cmd /k "DISM /Online /Cleanup-Image /CheckHealth" ')
    os.system('cmd /k "DISM /Online /Cleanup-Image /ScanHealth" ')
    os.system(
        'cmd /k "Dism /Online /Cleanup-Image /RestoreHealth /Source:c:\test\mount\windows" ')
except:
    print("There is an error in the system check")