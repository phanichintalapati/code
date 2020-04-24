# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""
from biosppy.signals import ecg
from biosppy.signals import ecg1
import numpy as np
import matplotlib.pyplot as plt
import wfdb

record=wfdb.rdsamp('D:/Technical-1/algorithms/test/AV-Block/A0650')
                   #ecgdatabase/Person_12/rec_1')
                   #mit-atrialfibrilation/05091')
                   #/af-termination-challenge-database-1.0.0/test-set-a/a01')
                   #mit-bih-normal-sinus-rhythm-database-1.0.0/19830')
                   #ecgdatabase/Person_15/rec_1')
a,b=record
w=0
signal=a[:,w]
#print(record)
lenght=len(signal)
signal1=[]
for y in range(lenght):
    signal1.append(signal[y])
#signal = np.loadtxt('D:/anacondapyfiles/main/raw1.txt')
sampling_rate=500

#signal1 = np.loadtxt('D:/ecgpicsimp/text.txt')
sampling_rate=500
ts,filtered,rpeaks,ts_tmpl,templates, ts_hr, hr= ecg.ecg(signal=signal1, sampling_rate=sampling_rate, show=True)
ts,filtered1,rpeaks1= ecg1.ecg(signal=signal1, sampling_rate=sampling_rate, show=True)

filterlen=len(filtered)
filterlenq=len(filtered1)
x=len(rpeaks)
c1=len(rpeaks1)
wavel=(filterlen/x)
waveql=filterlenq/c1
waverateq=waveql/sampling_rate
waverate=(wavel/sampling_rate)
y1=[]
qr=[]
qr1=[]
s1=int(0)
s2=int(0)
t4=[]
qre=0
x11=[]
qrsdist=[]
#qrs calculation for ecg.ecg

for i in range(len(rpeaks)):
    y=0
    y1=0
    j=1
    while(np.logical_or(((filtered[rpeaks[i]])-(filtered[[rpeaks[i]-j]])>0),((filtered[rpeaks[i]]-filtered[[rpeaks[i]+j]]))>0)):
                value=(filtered[rpeaks[i]])-(filtered[[rpeaks[i]-j]])
                value1=(filtered[rpeaks[i]])-(filtered[[rpeaks[i]+j]])
                #yz=np.diff(rpeaks)
                j=j+1
                if(np.logical_or((value>y),(value1>y1))):
                    y=value
                    y1=value1
                elif(np.logical_or((y>value),(y1>value1))):
                    s1=(rpeaks[i])
                    qre=s1-j
                    qr.append(qre)#set of q points
                    s2=rpeaks[i]
                    rse=s2+j
                    qr1.append(rse)#set of s points
                    t2=rse-qre
                    t4.append(t2)
                    actual=(((t4[i]*waverate)/wavel)*1000)
                    qrsdist.append(actual)
                    
                   # x1=np.array(qrsdist)
                    break


a=1
t31=[]
t6=0
t31.append(t6)
while(a<x):
    t5=t4[a]-t4[a-1]
    t31.append(t5)
    a=a+1
board=[]
narrow=[]
normal=[]
for x in qrsdist:
    if(80<=x<100):
      normal.append(x)
        
    if(x>=100):
        bo=board.append(x)
       
    if(x<80):
         narrow.append(x)

                    
#print("QRS normal Range",len(normal))
#print("QRS Board Range",len(board))
#print("QRS Narrow Range",len(narrow))

#qrs calculation for ecg1.ecg
qse1=[] 
qse3=[]
tq4=[]
tq31=[] 
#actualq1=[]
s11=[]
qypositions=[]
for c in range((len(rpeaks1))):
    
    yq=0
    yq1=0
    h=1
    while(np.logical_or(((filtered1[rpeaks1[c]])-(filtered1[[rpeaks1[c]-h]])>0),((filtered1[rpeaks1[c]]-filtered1[[rpeaks1[c]+h]]))>0)):
                valueq=(filtered1[rpeaks1[c]])-(filtered1[[rpeaks1[c]-h]])
                valueq1=(filtered1[rpeaks1[c]])-(filtered1[[rpeaks1[c]+h]])
                h=h+1
                if(np.logical_or((valueq>yq),(valueq1>yq1))):
                    yq=valueq
                    yq1=valueq1
                elif(np.logical_or((yq>valueq),(yq1>valueq1))):
                    qs=(rpeaks1[c])
                    s11.append(qs)
                    qse=qs-h
                    qse1.append(qse)#set of q points
                    qyp=filtered[qse]
                    qypositions.append(qyp)
                    qs2=rpeaks1[c]
                    qse2=qs2+h
                    qse3.append(qse2)#set of s points
                    tq2=qse2-qse
                    tq4.append(tq2)
                    break
 
b=1
q31=[]
q6=0
q31.append(q6)
while(b<c1):
    tq5=tq4[b]-tq4[b-1]
    tq31.append(tq5)
    b=b+1
prdist1=[]
#pqdist=[]
we=[]

pyposition=[]
#pqdist1=[]
pr=[]
#pq=[]
for k in range (len(rpeaks1)):
    yqr=0
    l=1
    while((filtered1[[qse1[k]-l]])-(filtered1[qse1[k]])>0):
        valueqr=(filtered1[[qse1[k]-l]])-(filtered1[[qse1[k]]])
        l=l+1
        if((valueqr>=yqr)):
            yqr=valueqr
        elif(yqr>valueqr):
            s12=(qse1[k])
            qre1=(s12-l)
            #py=filtered1[qre1]
           # pyposition.append(qre1)
            we.append(qre1)#set of p points
            prdist=s11[k]-we[k]
            prdist1.append(prdist)
            p=(((prdist1[k]*waverateq)/waveql)*1000)
            pr.append(p)
            break
block=[]
white_sx=[]

for xp in pr:
    
    if(xp>200):
        block.append(xp)
       
       
    if(xp<=120):
        white_sx.append(xp)
h1=[]
h2=[]
for h in hr:
    if(60<=h<100):
        h1.append(h)
    if(h>100):
        h2.append(h)
#print(len(h1))
#print(len(h2))
#print("block :",len(block))
#print("white_sx:",len(white_sx))
if(len(board)>len(normal) )  :
    print("Diagonsis: block")
if(len(h1)>len(h2) and len(normal)>len(board)):
    print("Diagonsis: normal sinus rhytm")
if(len(block)>len(white_sx)  ):
    print("Diagonsis: first degree AV Block")
