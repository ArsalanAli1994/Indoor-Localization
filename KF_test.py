#def KF_Position(Sk_1_ini,Vk_1_ini,ak_ini,dt_ini,Pki_00,Pki_01,Pki_10,Pki_11,Sk_1_prop,Vk_1_prop,ak_prop,dt_prop,Pk_00,Pk_01,Pk_10,Pk_11,yk_arg,wk_00,wk11,uk_arg,Selector):
#return Sk_ret,Vk_ret,Pk_Po[0][0],Pk_Po[0][1],Pk_Po[1][0],Pk_Po[1][1]
import matplotlib.pyplot as plt
import numpy as np
import KFilter_Position_Est as KFPE
import csv
ak_1=[]
Sk_1=[]
with open('D:\Working Repos\Indoor-Localization\Kalman Filter testing\DataSet2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    lists_from_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)

    for i in range(607):
        ak_1.append(float(lists_from_csv[i+1][5]))
        Sk_1.append(float(lists_from_csv[i+1][9]))

Sini=0
Vini=0
dtini=0.0
aini=0
yk=4
#Pk_1=np.array([[0.01,0],[0,1]])
Pk_1=np.array([[0,0],[0,0]])
a=Pk_1[0][0]
b=Pk_1[0][1]
c=Pk_1[1][0]
d=Pk_1[1][1]
wk=np.array([[0.12,0],[0,0.12]])    #process noise  #select inform of identity matrix and dimensions 2X2 dimension produces [[q2 0],[0,q2]]
uk=2.77                           #measurement noise  #select inform of identity matrix and dimensions 2X2 dimension produces [[q2 0],[0,q2]]
S=1
n=607
S_store=[Sini]
V_store=[Vini]
Pk00=0
Pk01=0
Pk10=0
Pk11=0
dt=0.065
S_obt=0
V_obt=0
#yk=[2.2,2.3,3.4,4.5,5.5,6,7,8.2,9,10]
#ak=[0.5,0.4,0.3,0.2,0.3,0.5,0.3,0.1,0.3,0.3]
for i in range(n):
    S_obt,V_obt,Pk00,Pk01,Pk10,Pk11=KFPE.KF_Position(Sini,Vini,aini,dtini,a,b,c,d,S_obt,V_obt,ak_1[i],dt,Pk00,Pk01,Pk10,Pk11,Sk_1[i],wk[0][0],wk[1][1],uk,S)
    S_store.append(S_obt)
    V_store.append(V_obt)
    S=1

plt.plot(S_store,'r--',V_store,'g--',Sk_1,'m--',ak_1,'y--')
plt.grid()
plt.legend(['Position(meters)KF','Speed(m/s)KF','Position(meters)RSSI','Accl(y)IMU'])
#plt.legend([S_store, V_store], ['label1', 'label2'])
plt.show()

