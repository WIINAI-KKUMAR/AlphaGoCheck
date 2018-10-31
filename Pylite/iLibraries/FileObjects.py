import time
import os

def check_file(pathOfExcel):
    #time.sleep(45)
    #print("waiting for file to download")
    if os.path.exists(pathOfExcel):return True
    #print("File exist. successfully dowloaded file")
    else: return  False
    #time.sleep(15)#print("Please check in file in download folder")

def delete_file(pathOfExcel):
    if os.path.exists(pathOfExcel):
        os.remove(pathOfExcel)
        return True
        #print("File exist. and Delete local current file")
    else: return False
        #print("The file does not exist..Good to Go")


