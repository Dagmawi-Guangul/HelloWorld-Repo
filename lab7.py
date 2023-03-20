"""#Dagmawi_Guangul_Stats 
f=open("50DayFruitData.txt","r")
x=f.readlines()
amountofappleseaten=[]
applecount=0

for i in x:
    index=i.split()
    if index[1]=="apple":
        applecount+=1
        amountofappleseaten.append(int(index[2]))
print(amountofappleseaten)

#for mean (apple)
total=0
for i in amountofappleseaten:
    total+=i
mean=total/len(amountofappleseaten)
print("This is the mean for apple: ",mean)
#for median (apple)
amountofappleseaten.sort()
if len(amountofappleseaten)%2==0:
    median1=amountofappleseaten[len(amountofappleseaten)//2]
    median2=amountofappleseaten[len(amountofappleseaten)//2-1]
    median=(median1+median2)/2
else:
    median=amountofappleseaten[len(amountofappleseaten)//2]
print("This is the median for apple: ",median)
#for mode(apple)
from collections import Counter
data=Counter(amountofappleseaten)
mode=data.most_common(1)[0][0]
print("This is the mode fir apple: ",mode)
#Dagmai Guangul My Program

amountofbananaseaten=[]
bananacount=0
for i in x:
    index=i.split()
    if index[1]=="banana":
        bananacount+=1
        amountofbananaseaten.append(int(index[2]))
print(amountofbananaseaten)

#for mean (banana)
total=0
for i in amountofbananaseaten:
    total+=i
mean=total/len(amountofbananaseaten)
print("This is the mean for banana: ",mean)
#for median (banana)
amountofbananaseaten.sort()
if len(amountofbananaseaten)%2==0:
    median1=amountofbananaseaten[len(amountofbananaseaten)//2]
    median2=amountofbananaseaten[len(amountofbananaseaten)//2-1]
    median=(median1+median2)/2
else:
    median=amountofbananaseaten[len(amountofbananaseaten)//2]
print("This is the median for banana: ",median)

#for mode (banana)
from collections import Counter
data=Counter(amountofbananaseaten)
mode=data.most_common(1)[0][0]
print("This is the mode for banana ",mode)


amountofstrawberriesseaten=[]
strawberriescount=0
for i in x:
    index=i.split()
    if index[1]=="strawberry":
        strawberriescount+=1
        amountofstrawberriesseaten.append(int(index[2]))
print(amountofstrawberriesseaten)

#for mean (strawberries)
total=0
for i in amountofstrawberriesseaten:
    total+=i
mean=total/len(amountofstrawberriesseaten)
print("This is the mean for strawberries: ",mean)
#for median (strawberries)
amountofstrawberriesseaten.sort()
if len(amountofstrawberriesseaten)%2==0:
    median1=amountofstrawberriesseaten[len(amountofstrawberriesseaten)//2]
    median2=amountofstrawberriesseaten[len(amountofstrawberriesseaten)//2-1]
    median=(median1+median2)/2
else:
    median=amountofstrawberriesseaten[len(amountofstrawberriesseaten)//2]
print("This is the median for strawberries: ",median)

#for mode (strawberries)
from collections import Counter
data=Counter(amountofstrawberriesseaten)
mode=data.most_common(1)[0][0]
print("This is the mode for strawberries ",mode)
"""
def fun1(num):
    return num+15
fun1(10)
print(num)











