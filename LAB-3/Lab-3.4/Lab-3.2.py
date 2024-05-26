# Module 2 - File Handling
# Problem 4

even = []
odd = []
numbers = []

with open('integers.txt', "r") as filed:
    filed = [int(x) for x in filed]

print("Numbers:", filed)

for a in filed:
    if a % 2 == 0:
        i = a**2
        even.append(str(i))
    else:
        i = a**3
        odd.append(str(i))

with open("double", "w") as file1:
    file1.write(','.join(even))

with open("triple", "w") as file2:
    file2.write(','.join(odd))

print("Squared values:", even)
print('Cubed values:', odd)
