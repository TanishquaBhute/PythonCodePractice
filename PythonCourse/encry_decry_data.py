import string
import sys

def encrypt_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    with open('key.txt', 'r') as file:
        key = file.read()
        alphabets = string.ascii_lowercase + string.ascii_uppercase
        encry_data = ""
    for char in alphabets:
        index = alphabets.index(char)
        data = data.replace(char, key[index])

        # try:
        #     index = alphabets.index(char)  # index of current character in a-z
        #     encry_data = encry_data+key[index]
        # except:
        #     encry_data = encry_data+' '
        #     continue
    print(f"Encrypted Data :: {data}")
    with open(file_name, 'w') as file:
         file.write(data)


def decrypt_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    with open('key.txt', 'r') as file:
        key = file.read()
        alphabets = string.ascii_lowercase + string.ascii_uppercase
        decry_data = ""
    for char in data:
        # index = key.index(char)
        # data = data.replace(char,alphabets[index])
        try:
            index = key.index(char)  # index of current character in key
            decry_data = decry_data+alphabets[index]
        except:
            decry_data = decry_data + ' '
            continue
    print(f"Decrypted Data :: {decry_data}")
    # with open(file_name, 'w') as file:
    #      file.write(decry_data)


print("1. Encryption")
print("2. Decryption")
ch = int(input("Enter your choice: "))
file_name = input("Enter file name: ")
if ch == 1:
    encrypt_data(file_name)
else:
    decrypt_data(file_name)

# arguments = sys.argv
# file_name = arguments[2]+".txt"
# print(arguments)
# if arguments[1] == "encrypt":
#     encrypt_data(file_name)
# elif arguments[1] == "decrypt":
#     decrypt_data(file_name)
# else:
#     print("Invalid Operation")
