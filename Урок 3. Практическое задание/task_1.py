"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def what_time(func):
    def wrapper(*args):
        time_start = time.time()
        func(*args)
        time_stop = time.time()
        print(f'Время работы функции {func.__name__} {time_stop - time_start}')

    return wrapper


@what_time
def update_list(lst, element):  # O(N)
    lst.insert(0, element)


@what_time
def update_dict(dct, key, val):  # O(1)
    dct[key] = val


new_list = [1, 2, 3, 4]
update_list(new_list, 5)

new_dict = {1: 'name 1', 2: 'name 2', 3: 'name 3', 4: 'name 4'}
update_dict(new_dict, 5, 'name 5')
