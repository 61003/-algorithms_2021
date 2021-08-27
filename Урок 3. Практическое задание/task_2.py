"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import hashlib
import uuid
import json

my_dict = {}
MY_ID = str(uuid.uuid1())
in_str = input('Введите пароль: ')
my_hash = hashlib.sha256(in_str.encode('utf-8') + MY_ID.encode('utf-8'))
my_dict[in_str] = my_hash.hexdigest()
with open('data.txt', 'w', encoding='utf-8') as outfile:
    json.dump(my_dict, outfile)
print('Пароль сохранен в базу')

my_new_dict = {}
new_str = input('Введите пароль еще раз для проверки: ')
new_hash = hashlib.sha256(new_str.encode('utf-8') + MY_ID.encode('utf-8'))
with open('data.txt', 'r', encoding='utf-8') as infile:
    my_new_dict = json.load(infile)
my_hash = my_new_dict['123']
print(f'В базе данных хранится строка: {my_hash}')
if new_hash.hexdigest() == my_hash:
    print('Вы ввели правильный пароль')
