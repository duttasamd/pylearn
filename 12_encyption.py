from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os

def encrypt(filename, key):
    chunksize = 64*1024
    output = "[encrypted]" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)

    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, "rb") as infile:
        with open(output, "wb") as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' '* (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def decrypt(filename, key):
    chunksize = 64 * 1024
    output = "[decrypted]" + filename[11:]

    with open(filename, "rb") as infile:

        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(output, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)


def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()




password = input("Enter Passkey: ")
key = getKey(password)

infile = input("Enter a filename (along with its extension) present in this directory: ")

encrypt(infile, key)

outfile = "[encrypted]" + infile

decrypt(outfile, key)

