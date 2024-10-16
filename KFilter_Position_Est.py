import numpy as np

#################variable intialization Kalman###############
#############################################################

def KF_Position(Sk_1_ini,Vk_1_ini,ak_ini,dt_ini,Pki_00,Pki_01,Pki_10,Pki_11,Sk_1_prop,Vk_1_prop,ak_prop,dt_prop,Pk_00,Pk_01,Pk_10,Pk_11,yk_arg,wk_00,wk_11,uk_arg,selector):

    ########################Argumental values########################
    if selector==0:
        Sk_1=Sk_1_ini;
        Vk_1=Vk_1_ini;
        ak=ak_ini;
        dt=dt_ini;
        Pk_1=np.array([[Pki_00,Pki_01],[Pki_10,Pki_11]]);
        
    else:
        Sk_1=Sk_1_prop;
        Vk_1=Vk_1_prop;
        ak=ak_prop;
        dt=dt_prop;
        Pk_1=np.array([[Pk_00,Pk_01],[Pk_10,Pk_11]]);
    
    yk=yk_arg
    #Pk_1=np.array([[0.01,0],[0,1]])
    #Propagation Values Sk_1 Vk_1
    xk_1=np.array([[Sk_1],[Vk_1]]);
    #Ck=np.array([[1,0]])
    Ck=np.array([[1,0]]);
    
    ##################Kalman Gain Ajustment###########################
    ##################################################################
    #wk=np.array([[0.1,0],[0,0.1]])    #process noise
    #uk=0.05                           #measurement noise
    wk=np.array([[wk_00,0],[0,wk_11]]);
    uk=uk_arg;
    ####################End of Argumental values######################

    
    ###################Prediction Algorithm###########################
    ##################################################################
    #xk_1=xk_Po
    A=np.array([[1,dt],[0,1]])
    B=np.array([[(dt**dt)*0.5],[dt]])
    #B=np.array([[0],[dt]])
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
    Sk_ret=xk_Po[0][0]
    Vk_ret=xk_Po[1][0]

    #print(Sk_1)
    #print(Vk_1)
    
    return Sk_ret,Vk_ret,Pk_Po[0][0],Pk_Po[0][1],Pk_Po[1][0],Pk_Po[1][1]
