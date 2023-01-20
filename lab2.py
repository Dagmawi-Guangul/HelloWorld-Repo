#Part 1

second = int(input("Enter a second: "))
hours = second // 3600
second= second % 3600
minutes= second // 60
second = second % 60
print("is the hour", hours , "is the minute ", minutes ,"is the second" ,second)


#part 2 

population = 334205119
time = 1685720
birth = time // 7
death = time // 13
immigrant=time // 35
change= (birth - death + immigrant)
print("The new population is ", change+population)



