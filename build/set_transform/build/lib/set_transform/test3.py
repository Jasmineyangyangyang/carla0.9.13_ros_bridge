#!/usr/bin/env python3
from transforms3d.euler import euler2quat
import math
import time

xfile1=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/ego_x.txt")
data1=xfile1.read()
ego_x=data1.split(",")
del ego_x[len(ego_x)-1]
xfile1.close()

xfile2=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/ego_y.txt")
data1=xfile2.read()
ego_y=data1.split(",")
del ego_y[len(ego_y)-1]
xfile2.close()

xfile3=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/ego_yaw.txt")
data1=xfile3.read()
ego_yaw=data1.split(",")
del ego_yaw[len(ego_yaw)-1]
xfile3.close()

xfile4=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/tra_x.txt")
data1=xfile4.read()
tra_x=data1.split(",")
del tra_x[len(tra_x)-1]
xfile4.close()

xfile5=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/tra_y.txt")
data1=xfile5.read()
tra_y=data1.split(",")
del tra_y[len(tra_y)-1]
xfile5.close()

xfile6=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/tra_yaw.txt")
data1=xfile6.read()
tra_yaw=data1.split(",")
del tra_yaw[len(tra_yaw)-1]
xfile6.close()

xfile7=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/Centerroad_x.txt")
data1=xfile7.read()
centerroad_x=data1.split(",")
del centerroad_x[len(centerroad_x)-1]
xfile7.close()

xfile8=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/Centerroad_y.txt")
data1=xfile8.read()
centerroad_y=data1.split(",")
del centerroad_y[len(centerroad_y)-1]
xfile8.close()

Init_dis=float(80/5)
Ref_len=0
for i in range(0,len(centerroad_x)-1):
    x1=float(centerroad_x[i])
    x2=float(centerroad_x[i+1])
    y1=float(centerroad_y[i])
    y2=float(centerroad_y[i+1])    
    dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
    Ref_len=Ref_len+dis
# dis0=0
# idx0=0
# start_frex=0
# for i in range(0,len(centerroad_x)-2):
#     x1=float(centerroad_x[i])
#     x2=float(centerroad_x[i+1])
#     y1=float(centerroad_y[i])
#     y2=float(centerroad_y[i+1])    
#     dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
#     print(dis)
#     if Init_dis<dis0+dis:
#         idx0=i
#         start_frex=round(Init_dis-dis0,2)
#         break
#     dis0+=dis

FreX=[]
Tra_X=[]
Tra_Y=[]
FreX.append(Init_dis)

def Frenet2Cartesian(x):
    if x>Ref_len:
        x=x-Ref_len
    dis1=0
    for idx1 in range(0,len(centerroad_x)-1):
        idx2=idx1+1
        x1=float(centerroad_x[idx1])
        x2=float(centerroad_x[idx2])
        y1=float(centerroad_y[idx1])
        y2=float(centerroad_y[idx2])    
        dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
        if x<dis1+dis:
            Lane_yaw=math.atan2((y2-y1),(x2-x1))
            cartesian_x=x1+(x-dis1)*math.cos(Lane_yaw)-2*math.sin(Lane_yaw)
            cartesian_y=y1+(x-dis1)*math.sin(Lane_yaw)+2*math.cos(Lane_yaw)
            Tra_X.append(round(cartesian_x,4))
            Tra_Y.append(round(cartesian_y,4))
            break
        dis1+=dis

def Cal_yaw():
    if len(Tra_X)>2:
        yaw=math.atan2((float(Tra_Y[-1])-float(Tra_Y[-2])),(float(Tra_X[-1])-float(Tra_X[-2])))
    else:
        yaw=1.5708
    return yaw

i=int(0)
while True:
        x1=float(ego_x[i])
        y1=float(ego_y[i])
        yaw1=math.degrees(float(ego_yaw[i]))
        x2=float(ego_x[i-1])
        y2=float(ego_y[i-1])
        v1=float(3.6*math.sqrt((x1-x2)**2+(y1-y2)**2)/0.02)
        print(v1)
        v2="%.1fkm/h"%v1
        x3=float(FreX[-1])
        print(x3)
        x4=x3+float(0.02)*v1/float(3.6)
        Frenet2Cartesian(x3)
        FreX.append(x4)
        x4=float(Tra_X[-1])
        y4=float(Tra_Y[-1])
        yaw4=Cal_yaw()
        yaw4=math.degrees(float(yaw4))
        i=i+1
        if i == len(ego_x)-1:
            i=int(0)
        time.sleep(0.02)

