from random import randint
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
UPALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '.,?!"£%^&*()-_\'@#~[]{}:;+=/\\|`¬'

def generate_otp(sheets, length):
     for sheet in range(sheets):
         with open("otp" + str(sheet) + ".txt", "w") as f:
             for i in range(length):
               f.write(str(randint(0, 26)) + "\n")
# Generates OTP's
# Sheets ~ Number of indivitdual OTP's
# Lengths ~ Length of OTP's
# Creates the txt's the iterates the random numbers(0-25) to them for the length given.
# \n ~ new line

def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents
# Displays the numbers in the file as strings in vector.

def get_plaintext():
    plaintext = input('Please type your message ')
    return plaintext
# Asks user for message.

def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents
# Reads a file

def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
# Saves the contents of data to a file filename
# data ~ Content that is written.

def encrypt(plaintext, sheet):
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET or UPALPHABET or PUNCTUATION:
            ciphertext += character
        elif character in ALPHABET :
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
        elif character in UPALPHABET :
            encrypted = (UPALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += UPALPHABET[encrypted]
        else :
            encrypted = (PUNCTUATION.index(character) + int(sheet[position])) % 31
            ciphertext += PUNCTUATION[encrypted]
    return ciphertext
# Encrpts text
# plaintext ~ unencrypted text
# sheet ~ OTP

def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET or UPALPHABET or PUNCTUATION:
            plaintext += character
        elif character in ALPHABET:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
        elif character in UPALPHABET:
            decrypted = (UPALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += UPALPHABET[decrypted]
        else:
            decrypted = (PUNCTUATION.index(character) - int(sheet[position])) % 31
            plaintext += PUNCTUATION[decrypted]

    return plaintext
# Decrpts text

def kwencrypt(plaintext, keyword):
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET and character not in UPALPHABET:
            ciphertext += character
        elif character in ALPHABET:
            letter = keyword[position % len(keyword)]
            ciphertext += ALPHABET[(ALPHABET.find(character) + ALPHABET.find(letter) + 1) % 26 ]
        else :
            letter = keyword[position % len(keyword)]
            ciphertext += UPALPHABET[(UPALPHABET.find(character) + UPALPHABET.find(letter) + 1) % 26]
    return ciphertext

def kwdecrypt(ciphertext, keyword):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET and character not in UPALPHABET:
            plaintext += character
        elif character in ALPHABET:
            letter = keyword[position % len(keyword)]
            plaintext += ALPHABET[(ALPHABET.find(character) - ALPHABET.find(letter) - 1) % 26 ]
        else :
            letter = keyword[position % len(keyword)]
            plaintext += UPALPHABET[(UPALPHABET.find(character) - UPALPHABET.find(letter) - 1) % 26]
    return plaintext



def menu():
    choices = ['1', '2', '3', '4', '5', '6']
    choice = '0'
    while True:
        while choice not in choices:
            print('What would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a message using a one-time pad.')
            print('3. Encrypt a message using a keyword.')
            print('4. Encrypt a message using a one-time pad and a Keyword.')
            print('5. Decrypt a message using a one-time pad.')
            print('6. Decrypt a .txt using a keyword.')
            print('7. Decrypt a message using a one-time pad and a keyword.')
            print('8. Quit the program')
            choice = input('Please type 1, 2, 3, 4, 5, 6, 7 or 8 and press Enter ')
            if choice == '1':
                sheets = int(input('How many one-time pads would you like to generate? '))
                length = int(input('What will be your maximum message length? '))
                generate_otp(sheets, length)
                print('your one-time pads are saved as otp*.txt, with * being a different number for each pad.')
            elif choice == '2':
                filename = input('Type in the filename of the OTP you want to use ')
                sheet = load_sheet(filename)
                plaintext = get_plaintext()
                ciphertext = encrypt(plaintext, sheet)
                filename = input('What will be the name of the encrypted file? ')
                save_file(filename, ciphertext)
            elif choice == '5':
                filename = input('Type in the filename of the OTP you want to use ')
                sheet = load_sheet(filename)
                filename = input('Type in the name of the file to be decrypted ')
                ciphertext = load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                print('The message reads:')
                print('')
                print(plaintext)
            elif choice == '8':
                exit()
            elif choice == '3':
                plaintext = get_plaintext()
                keyword = input('Type the keyword.')
                ciphertext = kwencrypt(plaintext, keyword)
                filename = input('What will be the name of the encrypted file? ')
                save_file(filename, ciphertext)
            elif choice == '4':
                filename = input('Type in the filename of the OTP you want to use ')
                sheet = load_sheet(filename)
                plaintext = get_plaintext()
                ciphertext = encrypt(plaintext, sheet)
                keyword = input('Type the keyword.')
                ciphertext2 = kwencrypt(ciphertext, keyword)
                filename = input('What will be the name of the encrypted file? ')
                save_file(filename, ciphertext2)
            elif choice == '6':
                filename = input('Type in the name of the file to be decrypted ')
                ciphertext = load_file(filename)
                keyword = input('Type the keyword.')
                plaintext = kwdecrypt(ciphertext,keyword)
                print('The message reads:')
                print('')
                print(plaintext)
            elif choice == '7':
                filename = input('Type in the filename of the OTP you want to use ')
                sheet = load_sheet(filename)
                filename = input('Type in the name of the file to be decrypted ')
                ciphertext = load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                keyword = input('Type the keyword.')
                plaintext2 = kwdecrypt(plaintext, keyword)
                print('The message reads:')
                print('')
                print(plaintext2)



            choice = '0'



menu()