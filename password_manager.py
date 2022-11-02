#!/usr/bin/env python3.8
from cryptography.fernet import Fernet # imports the Fernet class from the cryptography module. Its used for encryption and decryption


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: # 'wb' is for write bytes
        key_file.write(key) # writes the key to the file
write_key()  # calls the write_key() function   
# (The above code is from the cryptography module documentation. Its used to generate a key for the encryption)

def load_key():
    file = open('key.key', 'rb') # 'rb' is for read bytes
    key = file.read() # reads the key
    file.close()
    return key


# master_pwd = input('What is your master password? ')

key = load_key() # loads the key from the key.key file
fer = Fernet(key) # creates a Fernet object for initializing the encryption


def retrieve(): 
    # Open the file where to add the new account and password
    with open('passwords.txt', 'r') as f: 
    # 'w' is for write, 'r' is for read, 'a' is for append
    # with helps to automatically open and close a file rather than using the open() and close() functions
        for line in f.readlines():
            data = line.rstrip() # rstrip() removes the new line character
            user, passw = data.split(' | ') # splits the line into two variables
            print('User: ', user, '| Password: ', fer.decrypt(passw.encode()).decode()) # decrypts the password and prints it

def add(): 
    name = input('Account name: ')
    pwd = input('Account password: ')

    # Open the file where to add the new account and password
    with open('passwords.txt', 'a') as f: 
    # 'w' is for write, 'r' is for read, 'a' is for append
    # with helps to automatically open and close a file rather than using the open() and close() functions
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n') # encrypts the password in bytes using the encode method and adds it to the file



while True:
    mode = input('Would you like to add a new password or retrieve an existing one? (add/retrieve), press q to quit: ').lower()
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'retrieve':
        retrieve()
    else:
        print('Invalid mode. Please try again.')
        continue


