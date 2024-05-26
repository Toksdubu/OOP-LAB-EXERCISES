# Module 1 - String Manipulation
# Problem 3

def vigenere_cipher(message, key):
    # Convert the message and key to numerical values
    message_values = [ord(c) - ord('a') for c in message]
    key_values = [ord(c) - ord('a') for c in key]

    # Encrypt the message using the Vigenere cipher
    ciphertext_values = []
    for i in range(len(message_values)):
        val = (message_values[i] + key_values[i % len(key)]) % 26
        ciphertext_values.append(val)

    # Convert the ciphertext numerical values back to letters
    ciphertext = ''.join([chr(val + ord('a')) for val in ciphertext_values])
    return ciphertext

message = input("Message: ")
key = input("Key: ")
ciphertext = vigenere_cipher(message, key)
print("Ciphertext:", ciphertext)