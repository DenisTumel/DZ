# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# Работу загружаем в репозиторий гита. Скидываем ссылку НА ФАЙЛ!
def addition(a, b):return a + b
def subtraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b): return a / b
def division_by_zero(a, b):return ('На ноль делить нельзя!')

while True:
    sign = str(input('Введите операцию (для выхода введите 0): '))
    if sign == '0':
        break
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    if b=='0':print(division_by_zero)
    if sign=='+': print(addition(a,b))
    elif sign=='-':print(subtraction(a,b))
    elif sign=='*':print(multiplication(a,b))
    elif sign=='/':print(division(a,b))
    else: print('Такой операции нет!')
