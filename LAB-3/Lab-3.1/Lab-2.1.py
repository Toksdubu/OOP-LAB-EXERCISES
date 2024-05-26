# Module 2 - File Handling
# Problem 1

even = []
odd = []
numbers = []

with open('Numbers.txt', "r") as filed:
    filed = [int(x) for x in filed]

print("Numbers:", filed)

for a in filed:
    if a % 2 == 0:
        even.append(str(a))
    else:
        odd.append(str(a))

with open("Even", "w") as file1:
    file1.write(','.join(even))

with open("Odd", "w") as file2:
    file2.write(','.join(odd))

print("Even numbers:", even)
print("Odd numbers:", odd)
