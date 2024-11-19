import game_basics
import login
from cryptography.fernet import Fernet

#
# user_list = login.UserList("users.txt")
# print(user_list.get_list())
# user_list.append(login.User("test", login.encrypt("test")))
# print(user_list.get_list())
# user_list.save()

# u = ["a", "b", "c", "d", "e", "f"]
#
# def search(username):
#     """Returns position of user in list"""
#
#     def binary(pos=0, lst=None):
#         print("test")
#         if lst is None:
#             lst = u
#         mid = len(lst) // 2
#         if username == lst[mid]:
#             pos += mid
#             return pos
#         elif username > lst[mid]:
#             return binary(mid + pos, lst[mid:])
#         elif username < lst[mid]:
#             return binary(pos, lst[:mid])
#
#     return binary()
#
#
# print(search(input(": ")))


# class Encryption:
#     def __init__(self):
#         self.key_file = game_basics.File("key.txt")  # unsecure, key would be stored
#         # differently for any programs that actually need to be secure
#         if self.key_file.get_file_as_string() == "":
#             self.key = Fernet.generate_key()
#             self.key_file.overwrite_file(self.key.decode("utf-8"))
#         else:
#             self.key = self.key_file.get_file_as_string().encode("utf-8")
#         self.f = Fernet(self.key)
#
#     def encrypt(self, to_encrypt):
#         return self.f.encrypt(to_encrypt.encode("utf-8"))
#
#     def decrypt(self, text):
#         return self.f.decrypt(text).decode("utf-8")

s = "I8BfiSNTcqEWYKcG5F-E0IlnY7Zw5mg5o1in-aLu32k="
print(s)
s = s.encode("utf-8")
print(s)
f = Fernet(s)
print(f)
a = f.encrypt(b"")
print(a.decode("utf-8"))
# test1 = login.Data()
# print(test1.user_list.get_list())
# print(test1.user_list.list[0])