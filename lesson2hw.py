# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from typing import Callable

# def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
# def notebook():
#     todo_list: list[str] = []
# 
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
# 
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list
# 
#     return add_todo, get_all
# 
# 
# add, get = notebook()
# add('go to work')
# add('go to sleep')
# l = get()
# print(l)
# 2) протипізувати перше завдання

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
## Приклад:
#
 # expanded_form(12) # return '10 + 2'
 # expanded_form(42) # return '40 + 2'
 # expanded_form(70304) # return '70000 + 300 + 4'
 # def expanded_form(num:int) -> str:
 #
 #     st = str(num)
 #
 #     return ' + '.join(ch + '0'*(len(st)-i-1) for i, ch in enumerate(st) if ch != '0')+f' = {st}'
 #
 #
 # print(expanded_form(10102255159))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій

def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        res = func(*args, **kwargs)
        print(f'{count}')
        print('*'*20)
        return res
    return inner

@count_decor

def expanded_form(num: int) -> str:
    st = str(num)
    print(st)

    return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0') + f' = {st}'


expanded_form(2525)
expanded_form(10)
expanded_form(1)
expanded_form(1000010)


