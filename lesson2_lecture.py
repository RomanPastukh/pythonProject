# a = [1, 2, 3, 4]
# b = a
#
# print(a is b)


# tuple1 = (1, 2, 3, 4, 5, 6)
#
# # a, b, *_ = tuple1
# # _, a, _, b, *_ = tuple1
# *_, a = tuple1
# print(a)

# a = 2
# b = 5
# my_tuple = a,b
# #
# b, a = my_tuple
#
# s=a, b
#
# print(a, b)
# print(type(s))

dog = {
    'name': 'Max',
    'age': 4
}

# def func(name, age):
#     print(name, age)
#
#
# func(*dog)
#
# dog2 = {*dog}
#
# print(dog2)
#
# print(dog is dog2)
#
# l = [1,2,3,4]
#
# def func(a,b,c,d):
#     print(a, b, c, d)
#
# func(*l)


# def decor(func):
#     def inner(*args,**kwargs):
#         print('*' * 50)
#         func(*args, **kwargs)
#         print('*' * 50)
#
#     return inner
#
#
# @decor
# @decor
# def greeting(name):
#     print('Hello,', name)
#
#
# greeting('Max')
#
# # inner = decor(greeting)
# # decor(greeting)()
#
# # inner()


# for i in range(5):
#     print(i)
#
#
# print(i)
# a = 5
# print(globals())


# def a():
#     b=5
#     print(locals())
#
# a()
# print(globals())
# print(locals())


name = 'Max'

# def a():
#     # name = 'Petia'
#
#     def b():
#         nonlocal name
#         name = 'Alex'
#         print(name)
#
#     print(name)
#     b()
#     print(name)
#
#
# print(name)
# a()

# count2 = 0


# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         # global count2
#         count2 = 4
#         count += 1
#         return count
#
#     return inner


# c1 = counter()
# c2 = counter()
#
# print(c1())
# print(c1())
#
# print(c2())
# print(c2())
#
# print(c1())
# print(c1())
# print(c1())
#
# print(count2)


# const func = ()=>'hello'

# func = lambda name,age: f'hello, {name} - {age}'
#
# print(func('Max', 15))

# users = [
#     {'name': 'max', 'age': 15},
# #     {'name': 'kira', 'age': 18},
# #     {'name': 'olha', 'age': 20},
# # ]
# #
# # def sort_by_age(item):
# #     return item['age']
# #
# # users.sort(key=sort_by_age, reverse=True)
# # print(users)
#
# l = [1, 2, 3, 4]
#
# # m = list(map(lambda x: x + 1, l))
# #
# # for i in m:
# #     print(i)
# #
# #
# # for i in m:
# #     print(i)
#
# # print(type(m))
#
# f = list(filter(lambda x: x % 2, l))
#
# print(f)


# def aaa(name):
#     print(type(name))
#     print(name)
#
#
# aaa('aasd')


# def bbbb(st: str, b: int) -> int | str|list[int]:
#     print('pr')
#     return [1,2,3]


# l: list[int] = [1, 'sss']
#
#
# def ddd(l: list[str]) -> tuple[str]:
#     return 'ddddd',
#
#
# print(ddd(1222))

from typing import Callable, NewType, Any, TypedDict


# def counter() -> Callable[[int, str], int]:
def counter() -> Callable[[], int]:
    count = 0

    def inner() -> int:
        nonlocal count
        # global count2
        count2 = 4
        count += 1
        return count

    return inner


# UserId = NewType('UserId', int)
# MyType = int|str
#
# def check(user_id: MyType):
#     print(user_id)
#
#
# check('sss')


User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)

user: User = {'name': 'max', 'age': 13, 'status': True}