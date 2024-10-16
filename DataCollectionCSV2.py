import csv
import random
from datetime import datetime




with open('D:\Research and Projects\Localization Robot controlling\Python\AI Robot Sensor Data\DataSet1.csv', 'r') as file:
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
with open('D:\Research and Projects\Localization Robot controlling\Python\AI Robot Sensor Data\DataSet1.csv','a',newline='') as f:
    fieldnames=['Samples','timestamp','Roll','Pitch','Yow','X','Y','Z','RSSI']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)
    ####get the last line and append next to it(for sample number only)
    if lastRowNo==0:
        thewriter.writeheader()
    i=0
    while True:
        i+=1
        now = datetime.now()
        timeStamp = datetime.timestamp(now)
        n=lastRowNo+i
        #Gyroscope Data
        Roll=random.uniform(0.09,2.00)
        Pitch=random.uniform(0.09,2.00)
        Yow=random.uniform(0.09,2.00)
        #Acclerometer Data
        X=random.uniform(0.09,2.00)
        Y=random.uniform(0.09,2.00)
        Z=random.uniform(0.09,2.00)
        #RSSI data
        RSSI=-random.randint(25,90)
        datapacket={'Samples': n,'timestamp': timeStamp,'Roll': Roll,'Pitch': Pitch,'Yow': Yow,'X': X,'Y': Y,'Z': Z,'RSSI': RSSI}
        thewriter.writerow(datapacket)
        
