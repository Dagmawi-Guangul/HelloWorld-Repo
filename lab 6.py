def Mean(numbers):
    return sum(numbers) / len(numbers)

def Median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]



apples = []
with open('500DayFruitData.txt') as file:
    for line in file:
        amount = line.split()
        type = line.split()
        day= line.split()
        if type == 'apple':
            apples.append(int(amount))

mean_apples = round(Mean(apples), 2)
median_apples = round(Median(apples), 2)

with open('FirstName LastName Output.txt', 'w') as file:
    file.write(f"Mean number of apples eaten: {mean_apples}\n")
    file.write(f"Median number of apples eaten: {median_apples}\n")
