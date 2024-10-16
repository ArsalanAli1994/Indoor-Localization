"""i=0
while True:
    i+=1
    print(i)
"""
import requests
import timerMicro
from datetime import datetime
import time
import math

while True:
    """
    #timerCont=timerMicro.timeMilli()
    dateTimeObj = datetime.now()
    min1=dateTimeObj.minute
    sec=dateTimeObj.second
    msec=dateTimeObj.microsecond
    time=str(min1)+':'+str(sec)+'.'+str(msec)
    StRSSI=requests.get('http://192.168.11.2/RSSI')
    RSSIdbm=float(StRSSI.text)
    #RSSIdbm=-60
    #pi=math.pi
    #d=math.exp((31-RSSIdbm)/20)/(4*pi)
    print("RSSI: ",RSSIdbm)
    GyroDta=requests.get('http://192.168.11.2/gyro')
    Gdata=GyroDta.text
    print(Gdata)
    AcclDta=requests.get('http://192.168.11.2/Accl')
    Adata=AcclDta.text
    print(Adata)
    print(time)
    #time.sleep(0.5)
    """
    num=10**3
    print(num)

"""
from datetime import datetime
import time
dateTimeObj = datetime.now()
timeStamp = datetime.timestamp(dateTimeObj)
sec=dateTimeObj.second
min1=dateTimeObj.minute
msec=dateTimeObj.microsecond
strCan=str(sec)+'.'+str(msec)
datatype=type(strCan)
print(datatype)
"""

"""
gyro='Gyro:,0.03,0.08,0.09'
splitGyrodata=gyro.split(',')
print(splitGyrodata)
Roll=float(splitGyrodata[1])
pitch=float(splitGyrodata[2])
yow=float(splitGyrodata[3])
print(Roll)
print(pitch)
print(yow)
"""
"""
def dataExtract(argStr):
    dataSplit=argStr.split(",")
    subData1=dataSplit[0].split(":")
    subData2=dataSplit[1].split(":")
    subData3=dataSplit[2].split(":")
    Data1=float(subData1[1])
    Data2=float(subData2[1])
    Data3=float(subData3[1])
    return Data1,Data2,Data3

str1="AccX: -9.09,Y: 2.48,Z: 3.65"
Roll,Pitch,Yow=dataExtract(str1)
print(Roll)
print(Pitch)
print(Yow)
"""
