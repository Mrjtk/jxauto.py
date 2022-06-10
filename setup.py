import os
if os.geteuid() == 0:
                  try:
                      os.system("apt install sublist3r")
                      os.system("apt install dirsearch")
                      os.system("apt install spiderfoot")
                      os.system("apt install photon")
                      os.system("apt install arjun")
                  except:
                      pass
else:
    print("Please run as root")