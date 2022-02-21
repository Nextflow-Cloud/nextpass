"""Main file for Nextpass runtime"""

from dotenv import load_dotenv
#from getpass import getpass
from pwinput import pwinput
from internal import Internal
import os
import sys
import pyotp

from colorama import init, AnsiToWin32, Fore
init()
stream = AnsiToWin32(sys.stderr).stream

print(Fore.GREEN + "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", file=stream)
print("▓  NextPass Password Manager                      ▓", file=stream)
print("▓  version 0.1.0 build 19                         ▓", file=stream)
print("▓  Copyright (c) 2022 Nextflow Technologies Ltd.  ▓", file=stream)
print("▓  All rights reserved.                           ▓", file=stream)
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓" + "\033[0m", file=stream)
print("", file=stream)

print("Welcome to the Nextflow Password Manager CLI.", file=stream)
print("", file=stream)

def prompt(attempt: int = 0):
    """Prompts the user for a password"""
    if attempt == 3:
        print("Too many failed attempts. Exiting.", file=stream)
        exit(1)
    try:
        internal = Internal(pwinput('Enter your master password: '), os.getenv('TOKEN'), os.getenv('SERVER'))
    except ValueError as e:
        if e.args[0] == 'Not the correct password.':
            print("", file=stream)
            print('Incorrect master password. Please try again.', file=stream)
            return prompt(attempt + 1)
        else:
            print("", file=stream)
            print('An unknown error occurred.', file=stream)
            exit(1)
    return internal

def options(internal: Internal):
    print("")
    print('Welcome to NextPass! Please select an option:', file=stream)
    print("", file=stream)
    print("1. Add a new entry", file=stream)
    print("2. View all entries", file=stream)
    print("3. Search for an entry", file=stream)
    print("4. Delete an entry", file=stream)
    print("5. Change master password", file=stream)
    print("6. Exit", file=stream)
    print("", file=stream)
    choice = input("Enter your choice: ")
    if choice == '1': #90% of this code is copilot so imma have to fix what the ai did
        print("", file=stream)
        print("Please enter the following information:", file=stream)
        print("", file=stream)
        site = input("Website: ")
        username = input("Username: ")
        password = pwinput("Password: ")
        code = input("2FA secret: ")
        notes = input("Notes: ")
        internal.add_item(site, username, username, password, code, notes)
        print("", file=stream)
        print("Entry added successfully.", file=stream)
        print("", file=stream)
    elif choice == '2':
        print("", file=stream)
        print("All entries:", file=stream)
        print("", file=stream);
        for entry in internal.fetch_all(): # wdym
            code = None
            try:
                code = pyotp.TOTP(entry[7]).now()
            except:
                code = 'None'
            
            print(f"Site: {entry[0]} | Name: {entry[1]} | Email: {entry[5]} | Password: {entry[6]} | 2FA code: {code} | Notes: {entry[8]}", file=stream)
        print("", file=stream)
    elif choice == '3':
        print("", file=stream)
        website = input('Website: ')
        email = input('Email: ') #wdym
        print("Entries that match the above query: ", file=stream)
        print("", file=stream)
        i = 1
        # cuz why  not
        for entry in internal.search(website, email, 'email', True):
            try:
                if not entry[7] == '': code = pyotp.TOTP(entry[7]).now()
            except:
                code = None
            print(f"#{i}. Site: {entry[0]} | Name: {entry[1]} | Email: {entry[5]} | Password: {entry[6]} | 2FA code: {code} | Notes: {entry[8]}", file=stream)
            i += 1
        print("", file=stream)
    elif choice == '4':
        print("", file=stream)
        website = input('Website: ')
        email = input('Email: ')
        internal.delete(website, email)
        print("That item was deleted", file=stream) # it got deleted :)
        print("", file=stream)
    elif choice == '5':
        # print("", file=stream)
        # print("Please enter the following information:", file=stream)
        # print("", file=stream)
        # old_password = input("Old password: ")
        # new_password = input("New password: ")
        # internal.change_password(old_password, new_password)
        # print("", file=stream)
        # print("Password changed successfully.", file=stream)
        # print("", file=stream)
        # prompt()
        print("", file=stream)
        print("Unimplemented error.", file=stream)
        print("", file=stream) # yeah so I put unimplmented error here
    elif choice == '6':
        print("", file=stream)
        print("Goodbye!", file=stream)
        print("", file=stream)
        internal.close()
        exit(0)
    else:
        print("", file=stream)
        print("Not a valid option", file=stream)
        print("", file=stream)
    return options(internal)
    # this runs no matter what
    
try: 
    load_dotenv()
    internal = prompt()
    options(internal)
except KeyboardInterrupt:
    internal.close()
    print("\nBye!", file=stream)
    exit(0)
except Exception as e:
    print("", file=stream)
    print("An unknown error occurred.", file=stream)
    print(e)
    exit(1)
    #oh you know what the input was website, username, password but the output was website, username, email, password so thats the problem
    #dude look @Queryzi look yeah we can do that and also all we do is replace cli with gui
    #also we need to copy bw browser extension and change it to our system @Queryzi
    #we need to figure out how to do sql in browser extension
    #@queryzi @queryzi
    #uh also passwords are e2e right? so server cant just create another api for it
    #wait dude is the db itself encrypted or the passwords inside it
    # if its only the passwords then we can just let server read db and send encrypted passwords
    # overhttps 
    # *sigh*
    #can we make it only 1dude but instead of a db we send passwords in json
    # client stores json
    # true but you're using a browser
    # which relies heavily on js 
    # so we need to make it a browser extension
    # sure