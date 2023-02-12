"""#lab4
number = int(input("Enter an upper bound for a check: "))

sum = 0
abundant_count = 0
deficient_count = 0
perfect_count = 0

for j in range(1, number + 1):
    for i in range(1, int(j ** 0.5) + 1):
        if j % i == 0:
            sum += i
            if i != j // i:
                sum += j // i
    
    if sum > j:
        abundant_count += 1
    elif sum < j:
        deficient_count += 1
    else:
        perfect_count += 1
    
    sum = 0

print("\nAbundant numbers found:", abundant_count)
print("Deficient numbers found:", deficient_count)
print("Perfect numbers found:", perfect_count)
"""
s="dagmawi"



for i in range(len(s)):
    
    
    for j in range(1):
        
        
        print(s[i])
   