import string
import sys
import os

def match_lenght(key, message):
    return key*int((len(message)/len(key))) + ''.join([key[i] for i in range(len(message)%len(key))])

def encrypt(key, message):
    lkey = match_lenght(key, message)
    ciphertext = ""
    charset = string.ascii_lowercase
    for i in range(len(message)):
        ciphertext += charset[(charset.index(message[i]) + charset.index(lkey[i])) % 26]
    
    return ciphertext

def decrypt(key, message):
    lkey = match_lenght(key, message)
    cleartext = ""
    charset = string.ascii_lowercase
    for i in range(len(message)):
        cleartext += charset[(charset.index(message[i]) - charset.index(lkey[i])) % 26]

    return cleartext

def main():
    if not 'key.txt' in os.listdir():
        print("Cannnot find key.txt")
        return
    if len(sys.argv) < 3:
        print("Usage: {} [ed] message".format(sys.argv[0]))
        return

    key = open('key.txt','r').read()
    message = sys.argv[2]
    if sys.argv[1] == 'd':
        print(decrypt(key, message))
    else:
        print(encrypt(key, message))

if __name__ == '__main__':
    main()