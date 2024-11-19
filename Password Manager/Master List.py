def removePasswords():
    #ask name to remove
    #searchtxt file for requested to remove
    # get line no.
    # delete from all
    toRemove = input("What website/application is the password for? ")
    count = 0
    with open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt', 'r') as f:
        linesInFile = f.readlines()
        numberOfLines = len(linesInFile)
        print(numberOfLines)
    while count < numberOfLines:
        with open('D:/Coding/Projects/Password Manager/listTexts/whatForList.txt') as f:
            lines = f.readlines()
        if toRemove in lines:
            lineToRemove = count
            print("gggggHHHHH")
        else:
            count =+ 1
            print("rip")

removePasswords()