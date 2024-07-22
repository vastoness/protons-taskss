def caesar_cipher(message, shift):
    encrypted_message = "" 
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_message += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                encrypted_message += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            encrypted_message += char
    return encrypted_message
message = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))
encrypted_message = caesar_cipher(message, shift)
print("The encrypted message is:", encrypted_message)