"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
(Хеш то що з ліва записувати не потрібно)
"""


# try:
#
#      with open('emails.txt') as source:
#          with open('res.txt', 'w') as res:
#      with open('emails.txt') as source, open('res.txt', 'w') as res:
#         for line in source:
#             email = line.split()[-1]
#             if email.endswith('@gmail.com'):
#                  print(email, file=res)
#
# except Exception as err:
#     print(err)
"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""
import json



class Purchases:
    def __int__(self, file_name):
        self.__file_name= file_name
        self.__purchases_list = []
        self.__id=self.__den__id()
        self.__read_file()



    def __show_all(self):
        for item in self.__purchases_list:
            print(f'{item["id"]} {item["name"]} - {item["cost"]} ')

    def __add__(self):
        name = input("Ввудіть назву покупки: ")
        while True:
            try:
                cost = int(input("Ввудіть ціну: "))
                break
            except (Exception,):
                pass



        new_purchase = {'id': next(self.__id), 'name': name, 'cost': cost}
        self.__purchases_list.append(new_purchase)
        self.__write_file()

    def __find_by(self):
        keys = ['id', 'name','cost']

        for i, v in enumerate(keys):
            print(f'{i}) {v} ')


        choice = int(input("По чому буде шукати :"))
        search = input("пошук: ")


        for item in self.__purchases_list:
            if str(item[keys[choice]]) == search:
                print(item)


        def __most_expensive(self):
            print(max(self.__purchases_list, key=lambda item:item['cost']))


        def __delete_by_id(self):
            self.__show_all()
            _id = input("Введіть id ")


            index = next((i for i, v in enumerate(self.__self.__purchases_list) if str(v['id']) == _id), None)

            if index is not None:
                self.__purchases_list.pop(index)
                self.__write_file()
                return

            print("Error")

        def menu(self):
            while True:
                print("1) вивід всіх покупок")
                print("2) додавати покупки в книгу")
                print("3) шукати по будь якому полю покупки")
                print("4) показати найдорожчу покупку")
                print("5) видаляти покупку по id")
                print("9) Вихід")


                choice = input("Зробіть свій вибір: ")

                print("*" * 50)


                match choice:
                    case '1':
                        self.__show_all()
                    case '2':
                        self.__add()
                    case '3':
                        self.__find_by()
                    case '4':
                        self.__most_expensive()
                    case '5':
                        self.__delete_by_id()
                    case '9':
                        break

        @staticmethod
        def __gen_id():
            _id = 1
            while True:
                yield _id
                _id += 1

        def __read_file(self):
            try:
                with open(self.__file_name) as file:
                    self.__purchases_list = json.load(file)
            except (Exception, ):
                self.__write_file()


        def __write_file(slf):
            try:
                with open(self.__file_name, 'w') as file:
                     json.dump(self.__purchases_list, file)
            except Exception as err:
                print(err)


purchases = Purchases('first.txt')
purchases.menu()

"""
*********Кому буде замало ось завдання з співбесіди
Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},
    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},
    ]
]
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку 
# то брати наступне з того ж підсписку
# в результат має записатись тільки 5 id
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]
# """

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


def cut(arr):
    res =[]
    gen =[]
    for item in arr:
        gen.append((i['id'] for i in item if i['id'] not in res))
    gens = [(i['id'] for i in item if i ['id'] not in res ) for item in arr]

    while True:
        for g in gens:
            if len(res) ==5:
                return res
            res.append(next(g))


print(cut(data))
