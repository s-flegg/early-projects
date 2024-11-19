import numpy as np

whatForList = []
userNameList = []
emailList = []
passwordList = []
noteList = []

def store():
    whatFor = input("What application/website is the password for? ")
    userName = input("What is your username? ")
    email = input("What is your email? ")
    correct = False
    while correct == False:
        password= input("What is your password? ")
        check = input("Please retype your password. ")
        if check == password:
            correct = True
        else:
            print("You mis-typed your password. Please try again.")
    notes= input("If you have any notes, type them here. ")
    whatForList.append(whatFor)
    userNameList.append(userName)
    emailList.append(email)
    passwordList.append(password)
    noteList.append(notes)

store()