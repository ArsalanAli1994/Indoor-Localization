# using time module
from datetime import datetime
import time
DTObj = datetime.now()
lastSec=DTObj.second
lastMsec=float(DTObj.microsecond)
def timeStampCal():
    global lastSec
    global lastMsec
    DTObj = datetime.now()
    nowSec = DTObj.second
    nowMicro = float(DTObj.microsecond)
    dec1 = nowSec-lastSec
    if (dec1<1):
        timeStamp = (nowMicro-lastMsec)/1000
    elif (dec1==1):
        tempOF = float(1000000.00-lastMsec)
        timeStamp = (tempOF+nowMicro)/1000
    else:
        timeStamp = (dec1-1)+(nowMicro/pow(10,len(str(nowMicro))))
    lastSec=nowSec
    lastMsec=nowMicro
    return timeStamp
    
while True:
    """
    # ts stores the time in seconds
    dateTimeObj = datetime.now()
    timeStampsec=dateTimeObj.second
    timeStampmicro=dateTimeObj.microsecond
    # print the current timestamp
    timeStampStr=str(dateTimeObj.year)+'/'+str(dateTimeObj.month)+'/'+str(dateTimeObj.day)+' '+str(dateTimeObj.hour)+':'+str(dateTimeObj.minute)+':'+str(dateTimeObj.second)+'.'+str(dateTimeObj.microsecond)
    print(timeStampStr)
    
    time.sleep(0.02)
    """
    
    timeStamp=timeStampCal()
    # print the current timestamp
    print(timeStamp)
    
    time.sleep(0.2)
