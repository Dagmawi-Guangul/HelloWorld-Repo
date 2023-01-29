#Dagmawi Guangul Lab 3
amount=float(input("Enter the amount you earned in 2022:"))
clients=float(input("How many clients did you add in 2022? "))
associate=input("Are you a senior or junior associate, Type in S for senior and J for junior: ")
if associate=="J":
        if amount<0:
            print("You made less than $0. Contact HR ")
        if amount >0 and amount<=5000:
            amount=amount*0.03
             
            print("Total commission:",amount)
        if amount >5001 and amount<=25000:
            amount=((amount-5000)*0.04)+ 150
            print("Total commission:",amount)
            
        if amount >25001 and amount<=100000:
            amount=(amount-25000)*0.05+ 150+ 1000
            print("Total commission:",amount)
        if amount >100001:
              
            amount=(amount-100000)*0.07+150+1000+5000
            print("Total commission:",amount)
    
elif associate=="S":
        if amount<0:
            print("You made less than $0. Contact HR ")
        if amount >0 and amount<=5000:
            amount=amount*0.04 
            amount += clients * 500
            print("Total commission amount including bonus:", amount)
        if amount >5001 and amount<=25000:
            amount=(amount-5000)*0.05+200
            amount += clients * 500
            print("Total commission amount including bonus:", amount)
        if amount >25001 and amount<=100000:
            amount=((amount-25000)*0.07)+200+1250
            amount += clients * 500
            print("Total commission amount including bonus:", amount)
        if amount >100001:
            amount=(amount-100000)*0.10+200+1250+7000
            amount += clients * 500
            print("Total commission amount including bonus:", amount)
    
else:
    print("Invalid Input")   
