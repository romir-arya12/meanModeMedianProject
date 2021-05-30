import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newData=[]
for i in range(len(file_data)):
    n_num=file_data[i][2]
    newData.append(float(n_num))
n=len(newData)
data=Counter(newData)
getMode=dict(data)
mode=[]
mode1=[]
mode2=[]
mode3=[]
mode4=[]
mode5=[]
mode6=[]
mode7=[]
for a,v in getMode.items():
    a=float(a)
    if 75<a<85:
        if v==max(list(data.values())):
            mode.append(a)
    elif 85<a<95:
        if v==max(list(data.values())):
            mode1.append(a)
    elif 95<a<105:
        if v==max(list(data.values())):
            mode2.append(a)
    elif 105<a<115:
        if v==max(list(data.values())):
            mode3.append(a)
    elif 115<a<125:
        if v==max(list(data.values())):
            mode4.append(a)
    elif 125<a<135:
        if v==max(list(data.values())):
            mode5.append(a)
    elif 135<a<145:
        if v==max(list(data.values())):
            mode6.append(a)
    elif 145<a<150:
        if v==max(list(data.values())):
            mode7.append(a)
if len(mode)>len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode)))
elif len(mode1)>len(mode) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode1)))
elif len(mode2)>len(mode1) and len(mode) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode2)))
elif len(mode3)>len(mode1) and len(mode2) and len(mode) and len(mode4) and len(mode5) and len(mode6) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode3)))
elif len(mode4)>len(mode1) and len(mode2) and len(mode3) and len(mode) and len(mode5) and len(mode6) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode4)))
elif len(mode5)>len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode) and len(mode6) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode5)))
elif len(mode6)>len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode) and len(mode7):
    print("mode is "+ ", ".join(map(str,mode6)))
elif len(mode7)>len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode):
    print("mode is "+ ", ".join(map(str,mode7)))