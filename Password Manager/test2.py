import numpy as np


def removePasswords():
    toRemove = input("What website/application is the password for? ")
    with open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt', 'r') as f:
        linesInFile = f.readlines()
        numberOfLines = len(linesInFile)
        count = 0
        while count < numberOfLines:
            with open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt', 'r') as f:
                lines = f.readlines()
                check = lines[count]
                print(str(toRemove))
                for line in lines:
                    if lines == toRemove:
                        lineToRemove = count
                        print(count)
                        count = numberOfLines
                    else:
                        count = count + 1
                        print(check)





removePasswords()