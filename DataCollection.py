StGyro="GyroRoll: -0.04,Pitch: 0.03,Yaw: 0.01"
StAccl="AccX: 1.57,Y: 0.17,Z: 10.83"
print(StGyro)

GyroSplit=StGyro.split(",")
SubRoll=GyroSplit[0].split(":")
SubPitch=GyroSplit[1].split(":")
SubYow=GyroSplit[2].split(":")
Roll=float(SubRoll[1])
Pitch=float(SubPitch[1])
Yow=float(SubYow[1])

print(Roll,"------",type(Roll))
print(Pitch,"------",type(Pitch))
print(Yow,"------",type(Yow))
print("\n")
print("Roll: ",Roll,"\t","Pitch: ",Pitch,"\t","Yow: ",Yow)
print("\n")
print("\n")
print(StAccl)
AcclSplit=StAccl.split(",")
SubX=AcclSplit[0].split(":")
SubY=AcclSplit[1].split(":")
SubZ=AcclSplit[2].split(":")
X=float(SubX[1])
Y=float(SubY[1])
Z=float(SubZ[1])
print(X,"------",type(X))
print(Y,"------",type(Y))
print(Z,"------",type(Z))
print("\n")
print("X: ",X,"\t","Y: ",Y,"\t","Z: ",Z)
