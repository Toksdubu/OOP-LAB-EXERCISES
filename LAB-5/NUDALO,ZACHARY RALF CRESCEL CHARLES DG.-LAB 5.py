#Nudalo,Zachary Ralf Crescel Charles DG.
#BSCPE 1-6
#Laboratory 5

try:
    # Read the file
    with open('leaves.txt', 'r') as file:
        originaltext = file.read()

    # Convert all text to uppercase
    change = originaltext.upper()

    # Count the total number of characters
    charcount = len(change)

    # Replace all vowels with an asterisk
    vowels = ['A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        change = change.replace(vowel, '*')
    with open('output.txt', 'w') as final:
        final.write(change)

    #print the needed information to see
    print('The final output:',change)
    print('The total number of characters in the text:',charcount)

# for Exceptions
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occur, please try again.")
except Exception:
    print("An error occur, please try again.")
