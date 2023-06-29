list = []
total = 0
num = int(input('How many numbers:'))
for n in range(num):
    numbers = int(input('Enter number:'))
    list.append(numbers)
for a in range(0, len(list)):
    total = total + list[a]
print("The Sum of user input value is :", total)
