#Step 1
groceryList=[]
costOfItem=[]
while True:
    grocery=input("Enter the name of the grocery you want to buy: ")
    
    if grocery=="DONE":
        break
    else:
        groceryList.append(grocery)
        cost=input("Enter the cost of the grocery: ")
        costOfItem.append(cost)
print(groceryList)
print(costOfItem)
#Step 2
groceryDict=dict(zip(groceryList,costOfItem))
print(groceryDict)
#Step 3
total=0
for i in costOfItem:
    total+=int(i)
print("The total amount you spend on grocery shopping is: ",total)
#Step 4
groceryList2=[]
costOfItem2=[]
while True:
    grocery=input("Enter the name of the grocery you want to buy ")
    
    if grocery=="DONE":
        break
    else:
        groceryList2.append(grocery)
        print("Enter the cost of the grocery")
        cost=input()
        costOfItem2.append(cost)
print(groceryList2)
print(costOfItem2)
#Step 5
def compareDict(dict1,dict2):
    if dict1==dict2:
        return True
    else:
        return False
print(compareDict(groceryDict,dict(zip(groceryList2,costOfItem2))))
#Step 6
def compareDict2(dict1,dict2):
    if dict1==dict2:
        return True
    else:
        for i in dict1.keys():
            if i not in dict2.keys():
                print("The item",i,"is not in the second list")
            else:
                if dict1[i]!=dict2[i]:
                    print("The price of",i,"is different in the two lists")
        return False
print(compareDict2(groceryDict,dict(zip(groceryList2,costOfItem2))))
#Step 7
purchase={"apple":(2,3),"banana":(3,4),"orange":(4,5)}
for i in purchase.keys():
    print("purchase",purchase[i][0],i,"at cost",purchase[i][1],"dollars each")
#Step 8
for i in purchase.keys():
    if purchase[i][0]==1:
        print("purchase",purchase[i][0],i,"at cost",purchase[i][1],"dollars each")
    else:
        print("purchase",purchase[i][0],i+"s","at cost",purchase[i][1],"dollars each")

                            

# WRITE A Program that writes to a file "myFile.txt" , chooses 100 random numbers from 250 to 500 and writes them to the file if they are even or odd.


import random
f=open("myFile.txt","w")
for i in range(100):
    num=random.randint(250,500)
    if num%2==0:
        f.write(str(num)+" is even")


