from datetime import datetime

DTObj = datetime.now()
lastSec=DTObj.second
lastMsec=float(DTObj.microsecond)
def timeMilli():
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

def timeMicro():
    DTObj = datetime.now()
    nowSec = DTObj.second
    nowMicro = float(DTObj.microsecond)
    dec1 = nowSec-lastSec
    if (dec1<1):
        timeStamp = (nowMicro-lastMsec)
    elif (dec1==1):
        tempOF = float(1000000.00-lastMsec)
        timeStamp = (tempOF+nowMicro)
    else:
        timeStamp = (dec1-1)+(nowMicro)
    lastSec=nowSec
    lastMsec=nowMicro
    return timeStamp
    return timeStamp
