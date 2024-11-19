

def showAll():
    count = 0
    totalPasswords = len(whatForList)
    while count < totalPasswords:
        print("For " + whatForList[count] + " your details are:")
        print("Username: " + userNameList[count])
        print("Email: " + emailList[count])
        print("Password: " + passwordList[count])
        print("Notes: " + noteList[count])
        count =+ 1







linesInFile = open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt', 'r').readlines()
numberOfLines = len(linesInFile)