#Crypto: tool for encrypting and decrypting messages.


#Encrypt message with key
def encrypt(message, key):
    result = ''

    #Iterate letters in message and encrypt each individually.

    for letter in message:
        if letter.isalpha():

            #Letters are numbered like this:
            #A, B, C - Z is 65, 66, 67 - 90
            #a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            else:
                assert letter.islower()
                base = ord('a')

            #The encryption equation:

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            #Encrypting the digits.
            result += letter

        else:
            result += letter

    return result

#We are decrypting message with a key
def decrypt(message, key):
    return encrypt(message, -key)

#Decoding messages without a key
def decode(message):
    pass  

#Geting the key from user
def get_key():
    try:
        text = input('Enter a key (1 - 25): ')
        key = int(text)
        return key
    except:
        print('Invalid key. Using key: 0.')
        return 0


print('Do you wish to encrypt, decrypt, or decode a message?')
choice = input()

if choice == 'encrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Encrypted message:', encrypt(phrase, code))
elif choice == 'decrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Decrypted message:', decrypt(phrase, code))
elif choice == 'decode':
    phrase = input('Message: ')
    print('Decoding message:')
    decode(phrase)
else:
    print('Error: Unrecognized Command')
