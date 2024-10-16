import csv
import requests
import timerMicro
import math

def dataExtract(argStr):
    dataSplit=argStr.split(",")
    subData1=dataSplit[0].split(":")
    subData2=dataSplit[1].split(":")
    subData3=dataSplit[2].split(":")
    Data1=float(subData1[1])
    Data2=float(subData2[1])
    Data3=float(subData3[1])
    return Data1,Data2,Data3


with open('D:\Research and Projects\Localization Robot controlling\Python\AI Robot Sensor Data\DataSet3.csv', 'r') as file:
    data=file.readlines()
    lastrow=data[-1].split(",")
    global lastRowNo
    lastRowNo=0
    lastRowNo=lastrow[0]
    if lastRowNo=='\n':
        lastRowNo=0
    else:
        lastRowNo=int(lastrow[0])


####main code to write to csv file
with open('D:\Research and Projects\Localization Robot controlling\Python\AI Robot Sensor Data\DataSet3.csv','a',newline='') as f:
    fieldnames=['Samples','timestamp','Roll','Pitch','Yow','X','Y','Z','RSSI']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)
####get the last line and append next to it(for sample number only)
    if lastRowNo==0:
        thewriter.writeheader()
    i=0
    while True:
        i+=1
        timeStamp = timerMicro.timeMilli()
        n=lastRowNo+i
        #----------------------Gyroscope Data Collection-------------------#
        GyroPacket=requests.get('http://192.168.11.2/gyro')
        #print(GyroPacket.text)
        StGyro=GyroPacket.text
        Roll,Pitch,Yow=dataExtract(StGyro)
        #print("3-axis Gyroscope Data")
        #print("Roll: ",Roll,"\t","Pitch: ",Pitch,"\t","Yow: ",Yow)
        #---------------------Acclerometer Data Collection-------------------#
        AcclPacket=requests.get('http://192.168.11.2/Accl')
        #print(AcclPacket.text)
        StAccl=AcclPacket.text
        X,Y,Z=dataExtract(StAccl)
        #print("3-axis Acclerometer Data")
        #print("X: ",X,"\t","Y: ",Y,"\t","Z: ",Z)
        #-------------------------RSSI Data Collection----------------------#
        StRSSI=requests.get('http://192.168.11.2/RSSI')
        RSSIdbm=float(StRSSI.text)
        dist=math.exp((31-RSSIdbm)/20)/(4*3.14)
        #print("RSSI: ",RSSIdbm)
        #print("\n")
        datapacket={'Samples': n,'timestamp': timeStamp,'Roll': Roll,'Pitch': Pitch,'Yow': Yow,'X': X,'Y': Y,'Z': Z,'RSSI': RSSIdbm,'Distance',dist}
        thewriter.writerow(datapacket)
