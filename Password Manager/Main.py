import sys
import numpy as np
import time


whatForList = []
userNameList = []
emailList = []
passwordList = []
noteList = []


def begin():
    print("You have" , str(len(whatForList)) , "stored passwords.")
    optionSelect()


def optionSelect():
    print("")
    print("Please select, via typing a number, which option below you wish to select.")
    print("(1)     See all passwords")
    print("(2)     Add passwords")
    print("(3)     Remove passwords")
    print("(4)     Edit passwords")
    print("(5)     End program")
    selected = 0
    selected = int(input("Selected:  "))
    if selected == 1:
        showAll()
    elif selected == 2:
        addPasswords()
    elif selected == 3:
        removePasswords()
    elif selected == 4:
        editPasswords()
    elif selected == 5:
        endProgram()


def showAll():
    count = 0
    with open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt', 'r') as f:
        linesInFile = f.readlines()
        numberOfLines = len(linesInFile)
    print("You have " + str(numberOfLines) + " saved passwords.")
    while count < numberOfLines:
            print("For " + lines[count] + " your details are:")
        with open('D:/Coding/Projects/Password Manager/listTexts/userNameList.txt') as f:
            lines = f.readlines()
            print("Username: " + lines[count])
        with open('D:/Coding/Projects/Password Manager/listTexts/emailList.txt') as f:
            lines = f.readlines()
            print("Email: " + lines[count])
        with open('D:/Coding/Projects/Password Manager/listTexts/passwordList.txt') as f:
            lines = f.readlines()
            print("Password: " + lines[count])
        with open('D:/Coding/Projects/Password Manager/listTexts/notesList.txt') as f:
            lines = f.readlines()
            print("Notes: " + lines[count])
        print("")
        print("")
        print("")
        count += 1
    optionSelect()


def addPasswords():
    whatFor = input("What application/website is the password for? ")
    userName = input("What is your username? ")
    email = input("What is your email? ")
    correct = False
    while correct == False:
        password = input("What is your password? ")
        check = input("Please retype your password. ")
        if check == password:
            correct = True
        else:
            print("You mis-typed your password. Please try again.")
    notes = input("If you have any notes, type them here. ")
    whatForList.append(whatFor)
    lines = [str(whatForList)]
    with open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    userNameList.append(userName)
    lines = [str(userNameList)]
    with open('D:/Coding/Projects/Password Manager/listTexts/userNameList.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    emailList.append(email)
    lines = [str(emailList)]
    with open('D:/Coding/Projects/Password Manager/listTexts/emailList.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    passwordList.append(password)
    lines = [str(passwordList)]
    with open('D:/Coding/Projects/Password Manager/listTexts/passwordList.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    noteList.append(notes)
    lines = [str(noteList)]
    with open('D:/Coding/Projects/Password Manager/listTexts/notesList.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    optionSelect()



def endProgram():
    print("Ending program in three seconds. Goodbye.")
    time.sleep(3)
    sys.exit()


begin()