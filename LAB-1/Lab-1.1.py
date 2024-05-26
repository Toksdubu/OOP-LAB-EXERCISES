# Module 1 - String Manipulation
# Problem 1

Letters = ('a', 'e', 'i', 'o', 'u')

getText = str(input("Input Text: "))
getText.lower()

a = getText.replace('a','*')
b = a.replace('e', '&')
c = b.replace('i','#')
d = c.replace('o', '+')
e = d.replace('u', '!')


print('New Text: ', e)