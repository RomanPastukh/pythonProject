# # for i in range(5):
# #     print(i)
#
# def iterator():
#     arr = []
#     for i in range(5):
#         arr.append(i)
#         print(i)
#
#
# print("hello")
# iterator()

# try:
#     lksjflksjfd
# except NameError as err:
#     print(str(err))
#
# print('sdfkhskdf')

# try:
#
#     print(100 /2)
#     while True:
#         pass
#     # sdfsdfsf
# except ZeroDivisionError:
#     print("На нуль ділити не можна")
# except NameError:
#     print("something wrong")
# except Exception as err:
#     print("other expssssssssssssssssssssssssssssssssssssssssss")
# else:
#     print("ok")
# finally:
#     print("finish")
# print('sdfkhskdf')

# l = [i for i in range(50000000)]
# input()

# g = (i for i in range(50000000))
# # print(type(g))
# #
# # for i in g:
# #     print(i)
# print(next(g))
# print('sljdfhskjfhksjhfdjk')
# print(next(g))

# g = (i for i in range(5))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# users = [
#     {"name": 'max', 'age': 15},
#     {"name": 'Olha', 'age': 20},
#     {"name": 'IWan', 'age': 25},
#     {"name": 'Kira', 'age': 28},
#     {"name": 'Kamila', 'age': 30},
# ]

# findUser = next((user for user in users if user['age'] == 45), None)
#
# print(findUser)

# def gen(name: str):
#     for ch in name:
#         yield ch
#         print("next")
#
#
# g = gen("Max")
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# # print(type(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return "sdfsdfsdf"
#
#
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# try:
#     print(next(g))
# except StopIteration as err:
#     print(err)


# def team1(n):
#     for man in range(n):
#         yield f'Man{man} - Team1'
#
#
# def team2(n):
#     for man in range(n):
#         yield f'Man{man} - Team2'
#
#
# teams = [team1(5), team2(3)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass

# def gen_jpeg_file_name():
#     index = 1
#     while True:
#         yield f'file-{index}.jpeg'
#         index += 1
#
#
# gen = gen_jpeg_file_name()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration
#
# # for i in MyRange(7):
# #     print(i)
#
#
# my_range = MyRange(5)
#
# # print(type(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#
#
# g = my_range(8)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# file = open('111.txt', 'r')
#
# print(file.readline())
# print('hsdfjhsgfj')
# print(file.readline())
# print(file.readline())
#
# file.close()

# try:
#     file = open('111.txt', 'r')
#     try:
#         read = file.read()
#         print(read)
#     finally:
#         file.close()
#
# except Exception as err:
#     print(err)

# try:
#
#     with open('111.txt', 'w') as file:
#         # print(file.read())
#         # file.write('hello from write\n')
#         file.writelines(['first\n', 'second\n'])
#
# except Exception as err:
#     print(err)

import json

# user = {"name": "max", "age": 15}

# try:
#     with open('users.json', 'w') as file:
#         json.dump(user, file)
#
# except Exception as err:
#     print(err)

# try:
#     with open('users.json') as file:
#         user = json.load(file)
#         print(user['age'])
#
# except Exception as err:
#     print(err)

import pickle


# def show():
#     print('hello')


# try:
#     with open('users.db', 'wb') as file:
#         pickle.dump(show, file)
#
# except Exception as err:
#     print(err)

# try:
#     with open('users.db', 'rb') as file:
#         a = pickle.load(file)
#         a()
#
# except Exception as err:
#     print(err)


# try:
#     with open('test.txt', 'w') as file:
#         print('Hello1', file=file)
#         print('Hello2', file=file)
#         print('Hello3', file=file)
# except Exception as err:
#     print(err)

# choice = input('Enter num: ')
#
# match choice:
#     case '1':
#         print(1)
#     case '2':
#         print(2)
#     case _:
#         print('default')


# p = ['right', '200', 33]
#
# match p:
#     case 'left' as action, value:
#         print(f'{action=} {value=}')
#
#     case 'left'|'top' as action, value, other:
#         print(action, value, other)
#     case _:
#         print("default")


class User:
    __match_args__ = 'name', 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age


karina = {"name": "Karina", "age": 5}
max = User("Max", 3)


# def matcher(item: User | dict):
#     if isinstance(item, dict):
#         print(item['name'])
#     elif isinstance(item, User):
#         print(item.name)
#
# matcher(max)

# def matcher(item: User | dict):
#     match item:
#         case User(name='Max' | 'olha' as name, age=3 | 16 | 18 as age) if len(name) != age:
#             print(name, age)
#         case {'age': int(age)} if age in range(1, 6):
#             print(age)
#         case _:
#             print('default')
#
#
# matcher(karina)


try:
    with open('111.txt') as file:
        for line in file:
            print(line)
except Exception as err:
    print(err)