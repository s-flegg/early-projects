class Client():
    def __init__(self, last_name, first_name, password, question = "Press enter", answer = ""):
        self.last_name = last_name
        self.first_name = first_name
        self.password = password
        self.question = question
        self.answer = answer

    #accessers
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_password(self):
        return self.password
    def get_question(self):
        return self.question
    def get_answer(self):
        return self.answer

    #modifiers
    def set_first_name(self, new):
        self.first_name = new
    def set_last_name(self, new):
        self.last_name = new
    def set_pasword(self, new):
        self.password = new
    def set_question(self, new):
        self.question = new
    def set_answer(self, new):
        self.answer = new

    #behaviours
##    def update_user(self):
##        set_first_name(input("What is your first name" + "\n" + ": "))
##        set_last_name(input("What is your last name" + "\n" + ": "))
##        set_password(input("What is your first name" + "\n" + ": "))
##        set_first_name(input("What is your first name" + "\n" + ": "))
##        set_first_name(input("What is your first name" + "\n" + ": "))

    def check_password(self, to_check):
        return self.password == to_check
    def check_answer(self, ans):
        return self.answer == ans
        

    #comaprison operators
    def __eq__(self, arg):
        return self.first_name == arg.get_first_name() and self.last_name == arg.get_last_name()
    def __lt__(self, arg):
        if self.last_name == arg.get_last_name():
            return self.first_name < arg.get_first_name()
        else:
            return self.last_name < arg.get_last_name()
    def __gt__(self, arg):
        if self.last_name == arg.get_last_name():
            return self.first_name > arg.get_first_name()
        else:
            return self.last_name > arg.last_name()
    def __str__(self):
        return self.last_name + ", " + self.first_name + ", " + self.password + ", " + self.question + ", " + self.answer + "\n"
    
        
        
class ClientList():
    def __init__(self, file="client_file.txt"):
        self.file = file
        
        self.list = []
        self.count = 0

        with open(self.file, "r") as f:
            for line in f:
                temp_1 = line.rstrip()
                if len(temp_1) > 0:
                    temp_2 = temp_1.rsplit(", ")
                    last_name = temp_2[0]
                    first_name = temp_2[1]
                    password = temp_2[2]
                    question = temp_2[3]
                    answer = temp_2[4]
                    self.list.append(
                        Client(
                            last_name, first_name, password, question, answer
                            )
                        )
                    self.count += 1
        self.sort_list()

    def sort_list(self, L=None):
        """Don't give any params when calling"""
        if L is None:
            L = self.list
        if len(L) > 1:
            #repeatedly split list until len=0
            mid = len(L) // 2
            left = L[:mid]
            right = L[mid:]

            #repeatedly merges
            self.sort_list(left)
            self.sort_list(right)

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    L[k] = left[i]
                    i += 1
                else:
                    L[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                L[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                L[k] = right[j]
                j += 1
                k += 1
                
    def append(self, client):
        self.list.append(client)
        self.count += 1
        self.sort_list()
            
    def save_list(self):
        with open(self.file, "w") as f:
            for index in range(0, self.count):
                f.write(str(self.list[index]) + "\n")

    def __str__(self):
        temp = ""
        for i in self.list:
            temp += str(i) + "\n"
        return temp
        

        
def main():
    c_list = ClientList()
    print(c_list)
    test = Client("2", "test", "p5", "why?", "why not")
    c_list.append(test)
    print(c_list)
    c_list.save_list()
    
    
main()
    
        
        
                       
