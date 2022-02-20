"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the FileAES.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is an easy to use, and secure module for encryption, decryption and password management.

This is a module for encryption and decryption of files using AES-CBC-256 encryption. 
It also supports text encryption with AES-CBC-256 encryption, and decryption. 
We also have password generator, that is obviously cryptographically secure so it is unpredictable by the odds. 
You can also check password strengths using this module. 
This module is very secure, and is for password management, and AES encryption and decryption management.

This library is written by Queryzi.

"""

import sys
# try:
import os, random, struct
from hashlib import sha256, scrypt
from base64 import b64decode, b64encode, urlsafe_b64decode, urlsafe_b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tkinter import *
from tkinter.ttk import *
from blake3 import blake3
import secrets
from getpass import getpass
import string
from tkinter.messagebox import *
from hashlib import sha256, sha512, sha384, sha224
# from PyDll import DllError, RetryDllError
from winreg import *

import pwnedpasswords
# except ImportError:
    # mods = [m.__name__ for m in sys.modules.values() if m]
    # message = 'You need the following modules to use this file AES class: '
    # for i in range(len(mods)):
        # message += mods[i] + ', '
    
    # message = message.split(', ')
    # message.pop()

    # message = ", ".join(message)
    # message += '.'
    # raise ImportError(message)

class FileAES():
    """This is a class for encryption and decryption of files using AES-CBC-256 encryption. It also supports text encryption with AES-CBC-256 encryption, and decryption. We also have password generator, that is obviously cryptographically secure so it is unpredictable by the odds. You can also check password strengths using this module. This module is very secure, and is for password management, and AES encryption and decryption management."""

    def __init__(self):
        pass

    def set_password(self, password: str, salt: bytes):
        """This will generate a key from a password, and salt. It does this by hashing the password with the given salt."""

        # if len(salt) != 32:
            # raise ValueError('That is not a valid salt, salt must be a length of 32 bytes.')

        self.key = blake3(bytes(password, encoding='utf-8'), key=salt[:32]).digest()
        self.JgkHfgjfjKGVhjgkdhjfghjG()
    
    def set_key(self, key: bytes):
        """This will set the key for the class. This will be used in encryption and decryption."""

        self.key = key

        if len(self.key) != 32:
            raise ValueError('You must have a key length of exactly 32 bytes.')
        
        self.JgkHfgjfjKGVhjgkdhjfghjG()

    def password_strength(self, password: str):
        """This will test the password, and it will give it is secure. This will do so as it checks specific fields in the password, and if matched adds a certain score. Then, it will match a range of values to Weak, Medium, and Strong, which gives you the ouput as a string."""
        score = 0
        if [c.isdigit() for c in password].count(True) >= 3:
            score += 6
        
        if [c.isdigit() for c in password].count(True) == 1:
            score += 4
        
        lfkflg = []

        if len(password) <= 6:
            score += 1
        elif len(password) > 6 and len(password) <= 12:
            score += 3
        else:
            score += 4

        for i in range(len('!@#$%^&*()_+~`\][|}{\';":/.,?><')):
            for j in range(len(password)):
                if '!@#$%^&*()_+~`\][|}{\';":/.,?><'[i] in password[j]:
                    lfkflg.append(True)
                else:
                    lfkflg.append(False)
        
        if lfkflg.count(True) == 1:
            score += 1
        elif lfkflg.count(True) >= 3:
            score += 4
        
        if [c.isupper() for c in password].count(True) == 1:
            if [c.islower() for c in password].count(True) == 1:
                score += 1

        if [c.isupper() for c in password].count(True) >= 3:
            if [c.islower() for c in password].count(True) >= 3:
                score += 3

        if (pwnedpasswords.check(password, True, True) == 1):
            score = -93

        if score == -93:
            return "Leaked in data breach"
        elif score < 5:
            return "Weak"
        elif score > 5 and score < 9:
            return "Medium"
        else:
            return "Strong"

    def JgkHfgjfjKGVhjgkdhjfghjG(self):

        def encryptor():

            iv = os.urandom(16)
            encryptor = AES.new(b'\x10 ]\x12\x00H\x16\xe5\x1e]<B\x9d:\xe77\x90\xd0A\xd1\nZV\xe5&\x8f\xf8j ]\xc2\x94', AES.MODE_CBC, iv)
            cipher = b''
            cipher += iv
            cipher += encryptor.encrypt(pad(self.key, AES.block_size))
            
            return b64encode(cipher)
        
        self.key = encryptor()

    def JgjJHjftjGJfJghKGHtFJKHFkghGKHG(self):

        def decryptor():
            iv = bytes(b64decode(self.key)[0:16])

            encryptor = AES.new(b'\x10 ]\x12\x00H\x16\xe5\x1e]<B\x9d:\xe77\x90\xd0A\xd1\nZV\xe5&\x8f\xf8j ]\xc2\x94', AES.MODE_CBC, iv)

            # print(urlsafe_b64decode(self.key))

            return unpad(encryptor.decrypt(b64decode(self.key)[16:]), AES.block_size)
        
        self.key = decryptor()

    def generatePassword(self, length: int, punctuation = True, digits = True):
        """This will generate a cryptographically secure password for use. You can set if you want punctuation, digits, and what length is the password."""
        password = ''
        for i in range(length):
            if punctuation and digits:
                password += secrets.choice(string.ascii_letters + string.digits + string.punctuation)
            elif punctuation and not digits:
                password += secrets.choice(string.ascii_letters + string.punctuation)
            elif not punctuation and digits:
                password += secrets.choice(string.ascii_letters + string.digits)
            elif not punctuation and not digits:
                password += secrets.choice(string.ascii_letters)
        
        return password

    def encrypt_file(self, in_filename, chunksize=64*1024*1024):
        """ Encrypts a file using AES-CBC-256 (CBC mode) with the
            given key.

            self.key:
                The encryption key - a string that must be
                either 16, 24 or 32 bytes long. Longer keys
                are more secure.

            in_filename:
                Name of the input file

            out_filename:
                If None, '<in_filename>.encrypted' will be used.

            chunksize:
                Sets the size of the chunk which the function
                uses to read and encrypt the file. Larger chunk
                sizes can be faster for some files and machines.
                chunksize must be divisible by 16.
        """

        if not os.path.exists(in_filename) and not os.path.exists(os.path.split(os.path.realpath(__file__))[0] + '\\' + in_filename):
            return showerror('Error','That file does not exist anymore.')

        self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

        key = self.key

        if self.key.strip() == '' or len(key) != 32:
            return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')

        self.JgkHfgjfjKGVhjgkdhjfghjG()

        out_filename = False

        if not out_filename:
            out_filename = in_filename + '.encrypted'

        iv = os.urandom(16)
        self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        self.JgkHfgjfjKGVhjgkdhjfghjG()
        filesize = os.path.getsize(in_filename)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))
        os.remove(in_filename)

    def decrypt_file(self, in_filename, chunksize=64*1024*1024):
        """ Decrypts a file using AES (CBC mode) with the
            given key. Parameters are similar to encrypt_file,
            with one difference: out_filename, if not supplied
            will be in_filename without its last extension.
        """

        try:

            if not os.path.exists(in_filename) and not os.path.exists(os.path.split(os.path.realpath(__file__))[0] + '\\' + in_filename) and not os.path.exists(in_filename + '.encrypted'):
                return showerror('Error','That file does not exist anymore.')
            elif not os.path.exists(in_filename) and not os.path.exists(os.path.split(os.path.realpath(__file__))[0] + '\\' + in_filename) and os.path.exists(in_filename + '.encrypted'):
                in_filename = in_filename + '.encrypted'

            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            key = self.key

            if self.key.strip() == '' or len(key) != 32:
                return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')

            self.JgkHfgjfjKGVhjgkdhjfghjG()

            out_filename = False

            if not out_filename:
                out_filename = os.path.splitext(in_filename)[0]

            with open(in_filename, 'rb') as infile:
                origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
                iv = infile.read(16)
                self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()
                decryptor = AES.new(key, AES.MODE_CBC, iv)
                self.JgkHfgjfjKGVhjgkdhjfghjG()

                with open(out_filename, 'wb') as outfile:
                    while True:
                        chunk = infile.read(chunksize)
                        if len(chunk) == 0:
                            break
                        outfile.write(decryptor.decrypt(chunk))

                    outfile.truncate(origsize)
            os.remove(in_filename)

            
        except Exception as e:
            pass
    def encrypt_directory(self, in_dir, chunksize=64*1024*1024):
        """This will encrypt the directory in_dir, and it will output all files with /parent/something/folder/folders/...etc/{file_name}.encrypted."""
        if not os.path.exists(os.path.split(os.path.realpath(__file__))[0] + '\\' + in_dir) and not os.path.exists(in_dir):
            return showerror('Error','That is not a valid directory.')
        dirs = os.listdir(in_dir)
        for file in dirs:
            try:
                if os.path.isfile(in_dir + '\\' + file):
                    self.encrypt_file(in_dir + '\\' + file, chunksize)
                else:
                    self.encrypt_directory(in_dir + '\\' + file, chunksize)
            except:
                pass
        
    
    def decrypt_directory(self, in_dir, chunksize=64*1024*1024):
        """This will decrypt the directory in_dir, and it will output all files with /parent/something/folder/folders/...etc/{file_name}."""
        if not os.path.exists(os.path.split(os.path.realpath(__file__))[0] + '\\' + in_dir) and not os.path.exists(in_dir):
            return showerror('Error','That is not a valid directory.')
        dirs = os.listdir(in_dir)
        for file in dirs:
            try:
                if os.path.isfile(in_dir + '\\' + file):
                    self.decrypt_file(in_dir + '\\' + file, chunksize)
                else:
                    self.decrypt_directory(in_dir + '\\' + file, chunksize)
            except:
                pass
        
    def encrypt_with_iv(self, message, iv):
        try:
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            key = self.key

            if self.key.strip() == '' or len(key) != 32:
                return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')
            
            self.JgkHfgjfjKGVhjgkdhjfghjG()
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()
            encryptor = AES.new(key, AES.MODE_CBC, iv)
            self.JgkHfgjfjKGVhjgkdhjfghjG()
            cipher = encryptor.encrypt(pad(bytes(message, encoding='utf-8'), AES.block_size))
            
            return b64encode(cipher)
        except Exception as e:
            pass
    
    def decrypt_with_iv(self, message, iv):
        # try:
        self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

        key = self.key

        if self.key.strip() == '' or len(key) != 32:
            return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')
        
        self.JgkHfgjfjKGVhjgkdhjfghjG()

        self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

        encryptor = AES.new(key, AES.MODE_CBC, iv)

        self.JgkHfgjfjKGVhjgkdhjfghjG()

        return str(unpad(encryptor.decrypt(bytes(message, encoding='utf-8'), AES.block_size).decode()))
        # except Exception as e:
            # print(e)

    def encrypt_bytes(self, message: bytes):
        """This will encrypt text using AES-CBC-256 (CBC mode) (bytes message). Use decrypt_text(self, ciphertext) to decrypt the text with the correct key."""

        try:
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            key = self.key

            if self.key.strip() == '' or len(key) != 32:
                return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')
            
            self.JgkHfgjfjKGVhjgkdhjfghjG()

            iv = os.urandom(16)
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()
            encryptor = AES.new(key, AES.MODE_CBC, iv)
            self.JgkHfgjfjKGVhjgkdhjfghjG()
            cipher = b''
            cipher += iv
            cipher += encryptor.encrypt(pad(message, AES.block_size))
            
            return cipher
        except Exception as e:
            pass

    def encrypt_text(self, message: str):
        """This will encrypt text using AES-CBC-256 (CBC mode). Use decrypt_text(self, ciphertext) to decrypt the text with the correct key."""

        try:
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            key = self.key

            if self.key.strip() == '' or len(key) != 32:
                return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')
            
            self.JgkHfgjfjKGVhjgkdhjfghjG()

            iv = os.urandom(16)
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()
            encryptor = AES.new(key, AES.MODE_CBC, iv)
            self.JgkHfgjfjKGVhjgkdhjfghjG()
            cipher = b''
            cipher += iv
            cipher += encryptor.encrypt(pad(bytes(message, encoding='utf-8'), AES.block_size))
            
            return b64encode(cipher).decode()
        except Exception as e:
            pass
    
    def decrypt_bytes(self, ciphered: bytes):
        """This will decrypt messages encrypted with AES-CBC-256 (CBC mode). If you want to encrypt data, please use encrypt_text(self, message)."""
        try:
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            key = self.key

            if self.key.strip() == '' or len(key) != 32:
                return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')
            
            self.JgkHfgjfjKGVhjgkdhjfghjG()

            iv = ciphered[0:16]

            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            encryptor = AES.new(key, AES.MODE_CBC, iv)

            self.JgkHfgjfjKGVhjgkdhjfghjG()

            return unpad(encryptor.decrypt(ciphered[16:]), AES.block_size)
        except Exception as e:
            pass

    def decrypt_text(self, ciphered: str):
        """This will decrypt messages encrypted with AES-CBC-256 (CBC mode). If you want to encrypt data, please use encrypt_text(self, message)."""
        try:
            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            key = self.key

            if self.key.strip() == '' or len(key) != 32:
                return showerror('Error','How did you get through this, and not submit a valid key. Wait, that\'s illegal.')
            
            self.JgkHfgjfjKGVhjgkdhjfghjG()

            iv = bytes(b64decode(ciphered)[0:16])

            self.JgjJHjftjGJfJghKGHtFJKHFkghGKHG()

            encryptor = AES.new(key, AES.MODE_CBC, iv)

            self.JgkHfgjfjKGVhjgkdhjfghjG()

            return str(unpad(encryptor.decrypt(bytes(b64decode(ciphered)[16:])), AES.block_size).decode())
        except Exception as e:
            pass

    @property
    def __version(self):
        """This will return the version of the software."""
        return 5
    
    @property
    def __version_tuple(self):
        """This will return the version of the software in terms of a tuple."""
        return (1, 3, 1)

if __name__ == '__main__':
    pass