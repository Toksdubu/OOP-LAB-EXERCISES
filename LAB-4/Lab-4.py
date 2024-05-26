# Module 3 - Exception Handling
# Problem 1

choices = ('1', '2', '3', '4')


def calculate(operation, no1, no2):
    if operation == '1':
        return no1 + no2
    if operation == '2':
        return no1 - no2
    if operation == '3':
        return no1 * no2
    if operation == '4':
        return no1 / no2
    else:
        print('invalid operation')


try:
    print("Calculator")
    print("\nMenu:\nPress 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division")
    while True:
        operation = str(input("\nWhat operation do you want to perform?  "))
        if operation in choices:
            no1 = float(input("Enter number 1:  "))
            no2 = float(input("Enter number 2:  "))

            answer = calculate(operation, no1, no2)
            print(answer)
        else:
            print("\nWrong input")
            continue

        getResponse = input("\nDo you want to retry?""\n""Enter (Yes) to restart, Enter any keys to exit:  ")
        while getResponse == 'Yes':
            print("Resetting...")
            break
        else:
            print("\nResetting...")
            quit()

except ValueError:
    print('Invalid input')
except TypeError:
    print('Invalid input')
except Exception:
    print('Invalid, please try again')

finally:
    print("\nThank you for using this program")
