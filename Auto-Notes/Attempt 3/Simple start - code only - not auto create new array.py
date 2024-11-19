allSubjects = [subject1,subject2,subject3]
subject1 = [indicies,algebra,lolidk]
subject2 = []
subject3 = []


def menu():
    menuOption = input("Would you like to:"+"\n"+"1) View Notes"+"\n"+"2)Add notes"+"\n"+"3)Amend notes"+"\n"+"4)Quit"+"\n"+": ")
    match menuOption:
        case "1":
            print("Case1")#testing
            addString()
        case "2":
            print("Case2")#testing
        case "3":
            print("case3")#test
        case "4":
            #print("Case4")#testing
            exit()
            #print("TEST")


def searchArray(subject,desired):
    arrayLength = len(subject)
    for column in range(arrayLength):
        if subject[column] == desired:
            return column


def addString():
    underHeading = input("What heading do you want to add under?")
    subject = input("For what subjecy?")
    searchArray(subject,underHeading)


menu()