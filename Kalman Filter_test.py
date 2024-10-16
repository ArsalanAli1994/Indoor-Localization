import numpy as np
import matplotlib.pyplot as plt


#variable initialization
##################################################################
Sk_1=0;
Vk_1=5;
ak=-2;
yk=2.2
Pk_1=np.array([[0.01,0],[0,1]])
dt=0.5
xk_Pi=np.array([[0],[0]])
Ck=np.array([[1,0]])
Vk_store=[Vk_1]
Sk_store=[Sk_1]
xk_Po=np.array([[Sk_1],[Vk_1]])
n=10
t=[]


##################Kalman Gain Ajustment###########################
##################################################################
wk=np.array([[0.1,0],[0,0.1]])    #process noise
uk=0.05                           #measurement noise


for i in range(n):
    #t.append(i)
    ###################Prediction Algorithm###########################
    ##################################################################
    #xk_Po=np.array([[Sk_1],[Vk_1]])
    xk_1=xk_Po
    A=np.array([[1,dt],[0,1]])
    B=np.array([[0],[dt]])
    xk_Pi=(A.dot(xk_1))+B*ak
    Pk_Pi=(A.dot(Pk_1).dot(A.transpose()))+wk

    #print(xk_Pi)
    #print(Pk_Pi)

    #####################Update Algorithm#############################
    ##################################################################

    #Kalman Gain
    ##################################################################
    Kenum=Pk_Pi.dot(Ck.transpose())
    Kdenum=(Ck.dot(Pk_Pi).dot(Ck.transpose()))+uk
    Kdenum_inv=np.linalg.pinv(Kdenum)
    Kk=Kenum.dot(Kdenum_inv)
    #print(Kk)
    #print(Ck.dot(Pk_Pi).dot(Ck.transpose()))
    #Update Equations
    ###################################################################
    y_1=yk-Ck.dot(xk_Pi)
    xk_Po=xk_Pi+Kk.dot(y_1)
    #print(xk_Po)
    I=np.array([[1,0],[0,1]])
    Pk_Po=(I-(Kk.dot(Ck))).dot(Pk_Pi)
    #print(Pk_Po)

    #Further Processing
    Sk_1=xk_Po[0][0]
    Vk_1=xk_Po[1][0]
    Pk_1=Pk_Po

    #print(Sk_1)
    #print(Vk_1)
    Sk_store.append(Sk_1)
    Vk_store.append(Vk_1)

plt.plot(Sk_store,'r--',Vk_store,'gs')
plt.show()
#plt.plot(Vk_store)
#plt.show()
#print(Sk_store)
#print(Vk_store)
