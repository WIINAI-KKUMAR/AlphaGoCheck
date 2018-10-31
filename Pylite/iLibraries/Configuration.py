import os
import  getpass
from datetime import datetime

#global CURRENT_DIR ,ROOT_DIR,DRIVER_DIR,CHROME_DRIVER_PATH,IE_DRIVER_PATH
#APP_URL="https://google.com"


username = getpass.getuser()
currentTimeStamp_format = (datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
SDirectory  = "".join(["C:\\Temp",str(username),'\\Desktop\\Temp\\'+currentTimeStamp_format])
MAX_WAIT_TIME = 10

try: os.mkdir(SDirectory)
except OSError: print ("Creation of the directory %s failed" % SDirectory)
else:           print ("Successfully created the directory %s " % SDirectory)


print("currentTimeStamp_format : "+str(currentTimeStamp_format))
print("SDirectory              :" +str(SDirectory))



