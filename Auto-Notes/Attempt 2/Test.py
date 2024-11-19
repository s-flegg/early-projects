subjects = []
subjectLoop = True
while subjectLoop == True:
    selected = 0
    selected = int(input('Please type the number for the option you want. \n (1)Add new subject \n (2)Remove Subject \n'))
    if selected == 1:
        addSubject = input('What subject do you want to add? \n')
        subjects.append(addSubject)
        print(subjects)
        with open('subjects','a') as subjectsFile:
            subjectsFile.write(addSubject)
    elif selected == 2:
        print('2')
    else:
        subjectLoop = False
