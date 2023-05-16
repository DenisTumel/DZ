# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.

def my_tuple(a):
    simvol=0
    for i in a:
        if type(i)==str:
            simvol+=len(i)
    print(f'В строках кортежа {simvol} символов')

# Если список, то посчитать кол-во букв и чисел в нём.
def my_list(a):
    a=str(a)
    liters = 0
    number=0
    for i in a:
        if i.isalpha()== True:
            liters+=1
        elif i.isdigit()==True:
            number+=1
    print(f'Чисел в списке:{number}, букв в списке:{liters}')
# Число – кол-во нечётных цифр.
def numbers(a):
    odd=0
    while a > 0:
        if a % 2 != 0:
            odd += 1
        a = a // 10
    print(f'В числе {odd} нечетных чисел')

# Строка – кол-во букв.
def my_str(a):
    liters = 0
    for i in a:
        if i.isalpha()== True:
            liters+=1
        else:
            liters+=0
    print(f'Букв в строке:{liters}')

import time
def function_info(fn):
    def wrapper(arg):
        print(f'Аргументы функции: {arg}, является {type(arg)}')
        start_time = time.time()
        fn(arg)
        end_time = time.time()
        print(f'Функция выполнена за {end_time-start_time} секунд')
    return wrapper
@function_info
def function(a):
    if type(a)==tuple:
        my_tuple(a)
    elif type(a)==list:
        my_list(a)
    elif type(a)==str:
        my_str(a)
    elif type(a) == int or float:
        numbers(a)
    else:print('Не верный тип данных!')








