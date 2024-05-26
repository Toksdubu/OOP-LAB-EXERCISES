# Module 2 - File Handling
# Problem 3

response = ("y", 'n')

with open("Text", "w") as file:
    while True:
        a = input("Enter a line:  ")
        file.write(a)
        while True:
            b = input("Are there more lines y/n?  ")
            if b in response:
                while b == 'n':
                    quit()
                else:
                    break
            else:
                print("Wrong input\n")
                continue
