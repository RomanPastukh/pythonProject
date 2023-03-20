# class User:
#     # __slots__ = ('_name', 'age')
#
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
#
#     def __str__(self):
#         return f'{self.__name}, {self._age}'
#
#
# # # user = User('Max', 15)
# # # user2 = User('Kira', 18)
# # #
# # # # print(user.name)
# # # # print(user.age)
# # #
# # # # print(user)
# # # print(user)
# # # print(user2)
# # # print(user.count)
# # # print(user2.count)
# # # User.count = 16
# # # print(User.count)
# # user = User('Max', 15)
# # # user.age = 23
# # #
# # # print(user)
# # #
# # # # del user.name
# # user.house = 56
# # print(user.house)
#
#
# user = User('Max', 15)
#
#
# class User2(User):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def get_age(self):
#         print(self._age)
#
#
# user2 = User2('Kira', 18)
#
# user2.get_age()

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#
# class Greeting:
#     def __init__(self, msg):
#         self.msg = msg
#
#     def greeting(self):
#         print(self.msg)
#
#
# class MyCar(Car, Greeting):
#     def __init__(self, brand, msg, seats):
#         super().__init__(brand)
#         super().__init__(msg)
#         self.seats = seats
#
#
# car = MyCar('BMW', 'hi', 5)
# car.greeting()
# print(car.brand)
# print(car.seats)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __set_name(self, new_name):
#         if new_name != 'Thir':
#             self.__name = new_name
#
#     def __del_name(self):
#         del self.__name
#
#     name = property(fset=__set_name, fget=__get_name, fdel=__del_name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         if new_name != 'Thir':
#             self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Kira'
# print(user.name)
# del user.name
# print(user.name)
# # print(user.get_name())
# # user.set_name('Kira')
# # print(user.get_name())
# # user.del_name()
# # print(user.get_name())

#
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b / self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         return self.a * 2 + self.b * 2
#
#     #
#     def area(self):
#         return (self.a + self.b) * 2
#
#
# #
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(2, 3), Triangle(4, 5, 6)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())


# class User:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def get_count(cls):
#         print(cls.__count)
#
#     @classmethod
#     def int_count(cls):
#         cls.__count += 1
#
#
# User.greeting()
# user = User('Max', 15)
# User.greeting()
# User.int_count()
# User.int_count()
# User.int_count()
# User.get_count()


# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user1 = User('Max', 15)
# user2 = User('Max', 15)
# user2.name='Kira'
#
# print(user1 is user2)
# print(id(user1))
# print(id(user2))
#
# user3 = object.__new__(User)
# user3.name = 'Olha'
# user3.age = 3
# print(user1.name)
# print(user2.name)
# print(user3.name)

# class A:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, inc):
#         self.value += inc
#
#
# a = A(5)
# a(6)
# print(a.value)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.__dict__}'
#
#     def __repr__(self):
#         return f'{self.__dict__}'
#         # return self.__str__()
#
#     def __len__(self):
#         return len(self.name)
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __sub__(self, other):
#         return self.age * other.age
#
#     def __mul__(self, other):
#         return self.age * other.age
#
#     def __lt__(self, other):
#         return len(self.name) < len(other.name)
#
#
# user = User('Max', 15)
# user2 = User('Olha', 15)
# # print(user)
# #
# # print([user, User('Olha', 15)])
#
# print(len(user))
# print(user + user2)
# print(user - user2)
# print(user * user2)
# print(user<user2)


class Array:
    length = 0

    def __init__(self, *args):
        self.__arr = [*args]
        Array.length = len(self.__arr)

    def __str__(self):
        return str(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def push(self, item):
        self.__arr.append(item)
        Array.length = len(self.__arr)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])


array = Array(1, 2, 3, 4)
# array[2] = 55
# print(array.length)
# print(array[0])
# array.push(88)
# print(array)
# print(type(array))
# array_map = array.map(lambda x: x * 3)
#
# print(type(array_map))
#
# print(array_map)
#
# map_filter = array_map.filter(lambda x: x % 2 == 0)
#
# print(map_filter)


for i in Array(1, 2, 3, 4):
    print(i)