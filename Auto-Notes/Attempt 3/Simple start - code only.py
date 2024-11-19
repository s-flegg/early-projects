allSubjects = [subject1,subject2,subject3]



def menu():
    menuOption = input("Would you like to:"+"\n"+"1) View Notes"+"\n"+"2)Add notes"+"\n"+"3)Amend notes"+"\n"+"4)Quit"+"\n"+": ")
    match menuOption:
        case "1":
            print("Case1")#testing
            newNotes()
        case "2":
            print("Case2")#testing
        case "3":
            print("case3")#test
        case "4":
            #print("Case4")#testing
            exit()
            #print("TEST")


def newNotes():
    underHeading = input("What heading is it to be under?")
    note = input("What is the note?")
    length = len(underHeading)
    print(length)#testing
    underHeading.append(note)
    #allSubjects.append(input("What is the subject?"))
    print(allSubjects)#testing
    menu()


def amendNotes():
    underHeading = input("What headig is it under?")



def searchArray(subject,desired):
    arrayLength = len(subject)
    for column in range(arrayLength):
        if subject[column] == desired:
            return column




menu()