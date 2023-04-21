#!/usr/bin/env python3
'''
Task:
– Повторити розглянуті матеріали (функції, аргументи функцій та типи аргументів, різні виклики функцій). В інтерактивній сесії перевірити
  як вони працюють

– Написати ряд корисних функцій для роботи зі словниками:

    * операції, що трактують словник як множину (об'єднання словників, диз'юнкція словників, симетрична різниця словників та інші).
    Повний перелік операцій простіше всього побачити на діаграмах Вієна.

    * функцію для сортування словників

    * функцію для перегортання словників (міняє ключі та значення місцями, якщо це можливо, а в разі якщо неможливо – викидає виключення
    (raise ValueError(...))

– Подумати над аргументами функцій, щоб вони були продуманими, універсальними та зручними у використанні

– Потаймити реалізації. У разі якщо на думку спадає декілька реалізацій однієї з функцій – за результатами таймінгу вибрати найбільш оптимальну

– Задокументувати функції за допомогою docstring (інтерфейс), а де необхідно пояснити неочевидні з коду особливості реалізації –
за допомогою коментарів

– Викласти в репозиторій, в окрему директорію два файли: один – модуль, в якому описані функції; а інший – з прикладом їх використання

– (extra) Встановити пакет wemake-python-styleguide та за допомогою утиліти flake8 перевірити код на відповідність coding style. Виправити помилки.
(За основу нашого Coding Style беремо PEP8 з максимальною довжиною строки збільшеною до 100 символів)
'''
def union(dict1, dict2):
    dict_union = dict1.copy()
    dict_union.update(dict2)
    return dict_union

def symmetric_difference(dict1, dict2):
    dict_symmetric_difference = dict1.copy()
    dict_symmetric_difference.update(dict2)
    dict_symmetric_difference = {key: dict_symmetric_difference[key] for key in dict_symmetric_difference.keys() - (dict1.keys() & dict2.keys())}
    return dict_symmetric_difference

def disjunction(dict1, dict2):
    #function to find unique keys from both dictionaries
    disjunction = {key: dict1[key] for key in dict1 if key not in dict2}
    return disjunction

def common_keys(dict1, dict2):
    #function to find common keys form dictionary
    common_keys = set(dict1.keys()) & set(dict2.keys())
    common_keys_dict = {key: dict1[key] for key in common_keys}
    return common_keys_dict

def dict_sort(dict1, dict2, reverse, flag):
    '''
If flag=1 then function will be sorted by values
If flag=0 then function will be sorted by keys
If reverse=True then function will be sorted by descending
If reverse=False then function will be sorted by ascending
    '''
    united_dict = union(dict1, dict2)
    return dict(sorted(united_dict.items(), key = lambda item: item[flag], reverse=reverse))

def invert_dict(dict1, dict2):
    #prints error if the duplicate is found and skips them all outputing only the first 1
    united_dict = union(dict1, dict2)
    inverted_dict = {}
    for key, value in united_dict.items():
        try:
            if value in inverted_dict:
                raise ValueError(f"Duplicate value '{value}' found")
            inverted_dict[value] = key
        except ValueError as e:
            print(f"Error: {e}")
            continue
    return inverted_dict




