import csv
import requests
import timerMicro
import math
i=0
def dataExtract(argStr):
    dataSplit=argStr.split(",")
    subData1=dataSplit[0].split(":")
    subData2=dataSplit[1].split(":")
    subData3=dataSplit[2].split(":")
    Data1=float(subData1[1])
    Data2=float(subData2[1])
    Data3=float(subData3[1])
    return Data1,Data2,Data3

SheetNum=input('Please Enter the Sheet Number in Integer: ')
root='D:\Research and Projects\Localization Robot controlling\Python\AI Robot Sensor Data\DataSet'+str(SheetNum)+'.csv'
####main code to write to csv file
with open(root,'w',newline='') as f:
    fieldnames=['Samples','timestamp','Roll','Pitch','Yow','X','Y','Z','RSSI']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)
####get the last line and append next to it(for sample number only)
    thewriter.writeheader()
    
    while True:
        i+=1
        timeStamp = timerMicro.timeMilli()
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
        datapacket={'Samples': i,'timestamp': timeStamp,'Roll': Roll,'Pitch': Pitch,'Yow': Yow,'X': X,'Y': Y,'Z': Z,'RSSI': RSSIdbm}
        thewriter.writerow(datapacket)
