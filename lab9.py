#lab 9
f=open("randomValues.txt","r")
x=f.readlines()
numbers=[]
for i in x:
    try:
        numbers.append(int(i))
    except:
        pass
print(numbers)


def min_value(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        return min(numbers[0],min_value(numbers[1:]))

def max_value(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        return max(numbers[0],max_value(numbers[1:]))
def extrema(numbers,themin=False,themax=False):
    if themin==True and themax==True:
        return None
    elif themin==True:
        return max_value(numbers)
    elif themax==True:
        return min_value(numbers)
    else:
        return min_value(numbers),max_value(numbers)
    