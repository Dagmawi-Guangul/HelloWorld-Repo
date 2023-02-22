#dictionary of students
s={"Marrie":92,"Ria":88,"Dagi":89,"Sam":78,"Alex":80}

# length of dictionary
print(len(s))

#average score
total = 0
count = 0
for value in s.values():
    total += value
    count += 1

average = total // count
print(average)

#number of students above average
numav=0
for i in s.values():
    if i>=average:
        numav+=1
    else:
        break
print(numav)
# max value
print(max(s.values()))


#update score 
s.update({"marrie": 95})
print(s["marrie"])




