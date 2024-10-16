import csv
n=0
####main code to write to csv file
with open('D:\Research and Projects\Localization Robot controlling\Python\AI Robot Sensor Data\DataSet4.csv','w',newline='') as f:
    fieldnames=['Samples','timestamp','Roll','Pitch','Yow','X','Y','Z','RSSI']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)
####get the last line and append next to it(for sample number only)
    thewriter.writeheader()
    
    while True:
        n=n+1
        Samples=2345
        timeStamp=7523
        Roll=0.9
        Pitch=0.9
        Yow=0.9
        X=0.9
        Y=0.9
        Z=0.9
        RSSIdbm=-60
        datapacket={'Samples': n,'timestamp': timeStamp,'Roll': Roll,'Pitch': Pitch,'Yow': Yow,'X': X,'Y': Y,'Z': Z,'RSSI': RSSIdbm}
        thewriter.writerow(datapacket)
