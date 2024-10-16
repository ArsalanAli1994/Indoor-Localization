#Reading and Writing CSV file using pandas
"""
import pandas as pd
d={'a': (1,101),'b': (2,202),'c': (3,303)}
pd.DataFrame.from_dict(d,orient="index")
pd.to_csv("data.csv")
"""

"""
import csv
with open('/tmp/output.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['name', 'field'])
    tsv_writer.writerow(['Dijkstra', 'Computer Science'])
    tsv_writer.writerow(['Shelah', 'Math'])
    tsv_writer.writerow(['Aumann', 'Economic Sciences'])
"""

"""
import csv
with open('innovators.csv', 'w', newline='') as file:
    #SN=1
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    for i in range(1,101):
        writer.writerow([i, "Arsalan Ali", "World Forcasting language"])
"""

"""
import csv

with open('mycsv.csv','a',newline='') as f:
    fieldnames=['column1','column2','column3']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)

    thewriter.writeheader()
    for i in range(1,100):
        thewriter.writerow({'column1':'one','column3':'three','column2':'two'})
        thewriter.writerow({'column1':'four','column3':'six','column2':'nine'})
    
"""
#reading from the same csv file dict method
"""
import csv
with open('mycsv.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['column1'], row['column2'])
"""
#reading from csv file using specific line method
"""
import csv
with open('innovators.csv', 'r') as file:
    data=file.readlines()
    lastrow=data[-1].split(",")
    counter=int(lastrow[0])
    print(counter)
"""
#reading empty csvfile behaviour
"""
import csv
with open('empty.csv', 'r') as file:
    data=file.readlines()
    lastrow=data[-1].split(",")
    if lastrow[0]=='\n':
        print(type(lastrow[0]))
"""
#combine code reading and appending test
"""
import csv
with open('innovators.csv', 'r') as file:
    data=file.readlines()
    lastrow=data[-1].split(",")
    counter=int(lastrow[0])
import csv
with open('innovators.csv', 'a', newline='') as file:
    #SN=1
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    for i in range(1,101):
        n=i+counter
        writer.writerow([n, "Arsalan Ali", "World Forcasting language"])
"""
#combine code for reading last row and append next to it using dict method
import csv
import random
from datetime import datetime
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

with open('mycsv.csv', 'r') as file:
    data=file.readlines()
    lastrow=data[-1].split(",")
    global lastRowNo
    lastRowNo=lastrow[0]
    if lastRowNo=='\n':
        lastRowNo=0
    else:
        lastRowNo=int(lastrow[0])


####main code to write to csv file
with open('mycsv.csv','a',newline='') as f:
    fieldnames=['Samples','timestamp','Roll','Pitch','Yow','X','Y','Z','RSSI']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)
    ####get the last line and append next to it(for sample number only)
    if lastRowNo==0:
        thewriter.writeheader()
    for i in range(1,101):
        timeStamp = timeStampCal()
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
        
