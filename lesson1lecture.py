# '''
# skjhfd
# lsjdhfkjs
# jsdfkj
# '''
#
# """
# ksjhdfksjf
# lsdhfkjshf
#
# """
# # dfsdfsfs
# (кометн)
#
# # print('Hello world')
# # print(1, 2, 3, sep='-', end=' finish\n')
# (вивід інформації)

# i = 3
# f = 3.1
# b = True  # False
# s = "text"  # 'text'
# n = None

# type-тип

# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# int1 = int(f)
#
# print(type(int1))
# print(int1)
#
# a = b = c = 10
#
# print(a,b,c)

# int()-конвертнути в цілечислене значення

# float()-конвертнути в поаваючі числа(f = 3.1)
# str()-(конвертувати в стрінгу)
# bool()-(конвертувати в логічні значення)


# a = a + 1


# a = b = c = 10
#
# c = 20
#
# print(a, b, c)

# a++ error
# a = 0
# a += 1
# a = a + 1

# a = 5
# b = 2
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)-ділення в інтове значення
# print(a % b)-залишок від ділення
# print(a ** b)-приведення в сетпінь
#
# # print(2525**2525)
# input- отримує від користувача рядок тексту
# num = input('Enter num: ')
# num = int(num)
# print(num)
# print(type(num))


# a=2
# b=3
#
# print(a < b) - менше
# print(a > b) - більше
# print(a <= b)- менше дорівнює
# print(a >= b) - більше дорівнює
# print(a == b)
# print(a is b)
# print(a != b) не дорівнює
# print(a is not b)

# isinstance() - перевірка значення , си належть до того чи іншого типу
# print(isinstance(1, int))
# num = int(input('Enter num: '))
# # if num is not 5 and num==0 or num :
# if not num: блок if
#     print('num>5')
# elif num not in [1,2,3,4]:
#     print('some logic')
# else:
#     print('ddddddddd')

# num = int(input('Enter num: '))
#
# res = 'yes' if num > 5 else 'no'


# list

# l = [1, 2, 3, 5, 'sd', 33, True]
# # print(l[-222])
# l[3]=555
# print(l)
#
# print(len(l))
#
# l.append(333)
#
# print(l)
#
# del l[1]
# print(l)

# l2= l
# l3 = l.copy()


# l = [1, 2, 3,2]
# l2 = [4, 5, 6]
#
# l.insert(0,77)
#
# print(l)

# l.remove(222)
# pop = l.pop(0)
# print(pop)
# l.extend(l2)
# l += l2
# print(l)
# ind = l.index(2,4,55)
#
# print(ind)

# l.reverse()
# l.sort(reverse=True)
# print(l.count(1))
# l.clear()
# print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print(l[::-2])

# s = 'asdf'
# print(list(s))

# tuple

my_tuple = (1, 2, 3, 4, 6, 7)

#
# print(my_tuple[3])
# del my_tuple[5]

# my_tuple.
# l = list(1, 2, 3, 4, 5)
#
# print(l)

# dict
# user2={
#     'name':'Ihor'
# }
#
# user = {
#     my_tuple: 'max',
#     1: 'sss',
#     # True: False,
#     # user2:'ddd',
#     1.1:'sss5',
#     'name':'max'
# }

# print(user)
# print(user[my_tuple])
#
# print(user['name'])
# print(user['dddd'])

# print(user.get('name1', 55))

# del user[my_tuple]
# user.clear()
# copy = user.copy()
# items = user.items()
# print(user.keys())
# print(user.values())
# pop = user.pop('name2', 55)
# print(pop)
# print(user)
# print(list(items))

# popitem = user.popitem()
#
# print(popitem)
#
# print(user)

# user = {
#     'name': 'max',
#     'age': 15
# }
#
# user.setdefault('age2', 25)
#
# # user.update({'street':'street'})
# user |= {'street': 'street'}
#
# print(user)

# user = dict(name='max', age=18)
#
# print(user)


# SET

# l = [1, 2, 3, 4, 6, 2, 3, 1, 3]
#
# s = set(l)
#

# s = {1,2,3,4,5,1,5,3}
# print(s)

# s = {}
# s = set()
# # print(s)
# # print(type(s))
# s.add(3)
# s.add(6)
# s.add(22)
# s.add(22)
# s.add(3)
# print(s)

# set1 = {1, 2, 3, 4, 5}
# set2 = {6,7,8,1}
#
# # print(set1.issuperset(set2))
# # print(set1.issubset(set2))
# # print(set1.isdisjoint(set2))
# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # print(set1.difference(set2))
# # print(set1.symmetric_difference(set2))
# # set1.update(set2)
# # print(set1)
# # set1.remove(22)
# set1.discard(222)
# pop = set1.pop()
# print(set1)


# strings

# st = '-'*20
#
# print(st)

# string = "Hello, my name is Max, I\"m 18 and my weight 70.5 kg"
#
# name = 'Max'
# age = 18
# weight = 70.5
#
# string = "Hello, my name is Max, I`m 18 and my weight 70.5 kg"
# string = "Hello, my name is " + name + ", I`m " + str(age) + " and my weight " + str(weight) + " kg"
# string = "Hello, my name is %s, I`m %i and my weight %f kg" % (name, age, weight)
# string = "Hello, my name is {}, I`m {} and my weight {} kg".format(name, age, weight)
# string = "Hello, my name is {name}, I`m {age} and my weight {weight} kg".format(age=age, name=name, weight=weight)
# string = f"hello, my name is {name}, I`m {age} and my weight {weight} kg"
#
# # print(string)
# # print(string.index('n'))
# # print(string.find('leeeee'))
# # print(string.count('l'))
# # print(string.capitalize())
# # print(string.upper())
# string = string.lower()
# print(string.islower())
# print(string.isupper())
# print('hello world'.title())
# print('Hello World'.swapcase())
# print('asd'.isalpha())
# print('12s'.isdigit())
# print('12s '.isalnum())
# print('hello'.startswith('e'))
# print('hello'.endswith('lo'))
#
# print(['    aaaa         '.strip()])
# print(['dd    aaaa         dd'.strip('d ')])
# print(['    aaaa         '.lstrip()])
# print(['    aaaa         '.rstrip()])
# print('hello world hello'.split(' '))
# print('hello-world-hello'.split('-'))
# print('hello is hello'.partition('ll'))
#
# # l = ['hello', 'car', 'one'.]
#
# # print('-'.join(l))
#
# print('  d   '.isspace())
# print('hello world hello'.replace('l', 'L', 3))
#
# print('hello world hello'[::2])
#
# print(min([6, 1, 2, 3, 4]))
# print(max([6, 1, 2, 3, 4]))
# print(sorted([2, 1, 3, 2, 1]))
# print(sorted([2, 1, 3, 2, 1], reverse=True))
# print(pow(25, 25))


# def func():
#     print('Hello')
#
#
# func()
#
#
# def func2(a, b, c=3, *args, **kwargs):
#     print(a + b + c)
#     print(args)
# #     print(kwargs)
# #
# #
# # func2(1, 2, 5, 3, 5, 6, 7, age=34, name='Max')
#
# # l = [1, 2]
# #
# #
# # def func(a, b):
# #     print(a, b)
# #
# #
# # func(*l)
#
#
# # i = 5
# # while i > 0:
# #     i -= 1
# #     print(i)
# # else:
# #     print('finish')
#
# # l = [33,66,88,1,3,7,8]
# #
# # for i, item in enumerate(l):
# #     print(i, item, sep='-')
#
# # s = 'asdfg'
# # for i, ch in enumerate(s):
# #     print(i, ch)
# # # for i in range(5,10,2):
# # #     print(i)
#
#
# user = {
#     'name': 'max',
#     'age': 18
# }
#
# # for key in user.keys():
# #     print(key)
# #
# # for key in user.values():
# #     print(key)
#
# for k, v in user.items():
#     print(f'{k=} - {v=}')


# l = [i for i in range(5)]
#
# print(l)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
#
# res = [i if i != 6 else 'ops' for i in l if i % 2 == 0]
#
# print(res)

# dict1 = {'NaMe': 'Max', 'aGe': 19}
#
# res = {k.lower(): v for k, v in dict1.items()}
#
# print(res)

l = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]

# res = [i for j in l for i in j]
res = []
for j in l:
    for i in j:
        res.append(i)





print(res)