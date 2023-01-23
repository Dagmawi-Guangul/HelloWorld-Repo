
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


#part 3
sec = int(input("Enter the seconds int to the year "))
sectime= int(sec)

days = sectime // 86400
sectime = sectime % 86400
hours = sectime // 3600
sectime = sectime % 3600
minutes = sectime // 60
sectime = sectime % 60
population = 334205119
birth = sec // 7
death = sec // 13
immigrant = sec // 35
change = (birth - death + immigrant)
population += change
print("Time after the start of the year: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, sectime))
print("New Population:", population)

#part 4
population = 334205129

flapjacks = ((population+350)**2 - 12)**(1/5)//(50)**(1/5)

print("the average amount of flapjacks eatean is ", flapjacks)
