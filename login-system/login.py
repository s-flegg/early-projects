from hashlib import sha256

from cryptography.fernet import Fernet
import game_basics as gb


class User:
    """The class that holder info about users"""

    def __init__(self, username, password, question, answer):
        """
        :param username: should be unique
        :param password: should be hashed included hash function
        :param question: security question, should be encrypted by include encrypt
        function
        :param answer: answer to question, should be hashed by included hash function
        """
        self.username = username
        self.password = password
        self.question = question
        self.answer = answer

    # accessors
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_question(self):
        return Data.encryption.decrypt(self.question)

    def get_answer(self):
        return self.answer

    # modifiers
    def set_username(self, n):
        """Precondition: username contains no commas or backslashes"""
        self.username = n

    def set_password(self, p):
        """Precondition: password is hash, should be a hashed by sha256"""
        self.password = p

    def set_question(self, q):
        self.question = q

    def set_answer(self, a):
        self.answer = a

    # behaviours
    def check_password(self, to_check):
        return self.password == to_check

    def check_answer(self, to_check):
        return self.answer == to_check

    # comparison operators
    # used for comparing objects of class
    def __eq__(self, arg):
        return self.username == arg.get_username()

    def __lt__(self, arg):
        return self.username < arg.get_username()

    def __gt__(self, arg):
        return self.username > arg.get_username()

    def __str__(self):
        return (
            self.username
            + ", "
            + self.password
            + ", "
            + self.get_question()
            + ", "
            + self.answer
        )


class UserList(gb.File):
    def __init__(self):
        super().__init__("users.txt")
        self.list = []
        self.read()
        self.sort()

    def get_list(self):  # for debugging
        return self.list

    def read(self):
        """Updates self.list"""
        temp = self.get_file_as_list()
        for i in range(len(temp)):
            a = temp[i].split(", ")  # attributes
            user = User(a[0], a[1], a[2], a[3])
            self.list.append(user)

    def sort(self, lst=None):
        """Sorts list, don't call with params"""
        if lst is None:
            lst = self.list
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]

            self.sort(left)
            self.sort(right)

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1

    def search(self, username):
        """Returns position of user in list"""

        def binary(pos=0, lst=None):
            if lst is None:
                lst = self.list
            mid = len(lst) // 2
            if username == lst[mid]:
                pos += mid
                return pos
            elif username > lst[mid]:
                return binary(mid + pos, lst[mid:])
            elif username < lst[mid]:
                return binary(pos, lst[:mid])

        return binary()

    def check_password(self, username, password):
        """Precondition: password is hashed"""
        pos = self.search(username)
        return self.list[pos].check_password(password)

    def check_answer(self, username, answer):
        """Precondition: answer is encrypted"""
        pos = self.search(username)
        return self.list[pos].check_answer(answer)

    def append(self, user):
        """Precondition: user is User class"""
        self.list.append(user)
        self.sort()

    def remove(self, username):
        pos = self.search(username)
        self.list.remove(pos)

    def save(self):
        self.overwrite_file(self.list[0])
        for i in range(1, len(self.list)):
            self.append_file(self.list[i])


def hash(password):
    return sha256(password.encode("utf-8"), usedforsecurity=True).hexdigest()


class Encryption:
    def __init__(self):
        self.key_file = gb.File("key.txt")  # unsecure, key would be stored
        # differently for any programs that actually need to be secure
        if self.key_file.get_file_as_string() == "":
            self.key = Fernet.generate_key()
            self.key_file.overwrite_file(self.key.decode("utf-8"))
        else:
            self.key = self.key_file.get_file_as_string().encode("utf-8")
        self.f = Fernet(self.key)

    def encrypt(self, to_encrypt):
        return self.f.encrypt(to_encrypt.encode("utf-8"))

    def decrypt(self, text):
        return self.f.decrypt(text).decode("utf-8")


class PopUpWindow:
    """A simple pop up window for logging in/creating an account"""
    def __init__(self):
        self.width = 400
        self.height = 800

    def run(self):
