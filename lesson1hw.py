# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:

def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + '' * (n - 2) + '*')


# st = 'as 23 fdfdg544'
# print([ch for ch in st if ch.isdigit()])

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34'
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'


# записати кожний символ як окремий елемент списку і зробити його заглавним:
# print([ch.upper() for ch in greeting])
#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
#
# print([i ** 2 for i in range(50) if i % 2])
# function
#
# - створити функцію яка виводить ліст
# def show(some_list):
#     for i in some_list:
#         print(i)
#
#
# show([1, 2, 3, 4])

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def maxx(a, b, c):
#     res = max(a, b, c)
#     print(res)
#     return res
#
#
# maxx(1, 2, 3)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_max(*args):
#     m = max(args)
#     print(m)
#     return min(args)
#
#
# min_max(1, 2, 3, 4, 5, 6, 7,8)


# - створити функцію яка повертає найбільше число з ліста
# def max_from_list(numbers):
#
#     return max(numbers)

# - створити функцію яка повертає найменьше число з ліста
# def man_from_list(numbers):
#     return min(numbers)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


# def summa(numbers):
#     s = 0
#     for i in numbers:
#         s += i
#         return s
#     return sum(numbers)
#  створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg(numbers):
#     return sum(numbers) / len(numbers)

#
#
#
#
# ################################################################################################
# 1)Дан list:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# # 4) переробити це завдання під меню
# numbers = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# def min_num():
#     arr = numbers.copy()
#     print(min(arr))

# def dublicate():
#     arr = numbers.copy()
#     print(list(set(arr)))

# noinspection PyTypeChecker
# def to_x():
#     arr = numbers.copy()
#     for i in range(3, len(arr), 4):
#         arr[i] = 'X'
#
#         print(arr)
#         to_x()

def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + '' * (n - 2) + '*')
            return square(n)
