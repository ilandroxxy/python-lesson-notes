
# УРОК 01. ОСНОВЫ PYTHON. ЧАСТЬ 1

# - однострочный комментарий

'''
- блочный комментарий
'''

"""
name = 'ilya'
age = 28
print(type(age), type(name))
# <class 'int'> <class 'str'>

# Типы данных переменных

a = 5  # int (integer) - целочисленные значения

b = 5.0  # float (число с плавающей точкой) - вещественные значения (дроби)
print(type(4 + 5.0))  # <class 'float'>
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

c = '5'  # str (string) - строковый тип данных для хранения текста и символов
print(a * 4, c * 4)  # 20 5555

print('Hello ' * 4)  # Hello Hello Hello Hello  - при умножении строки на целое число - строка дублируется

c1 = 'Hello, '
c2 = 'world!'
c = c1 + c2  # - операция конкатенации строк (склеивание)
print(c)  # Hello, world!

s = '7' + '5' * 10 + '6'
print(s)  # 755555555556


d1 = True  # bool - математическая логика
d0 = False

print(4 < 10)  # True
print(4 == 10)  # False
"""


# Конвертация типов данных
'''
a = 5
print(type(a), a)  # <class 'int'> 5

a = str(a)
print(type(a), a)  # <class 'str'> 5

a = float(a)
print(type(a), a)  # <class 'float'> 5.0

a = int(a)
print(type(a), a)  # <class 'int'> 5
'''


# Ввод данных с клавиатуры
'''
age = int(input('Введите возраст пользователя: '))
name = input('Введите имя пользователя: ')  # - позволяет ввести данные с клавиатуры (но только строки)

if age >= 18:
    print(f'Имя пользователя: {name}, проход разрещен.')
else:
    print(f'Имя пользователя: {name}, проход запрещен.')
'''


# ВОПРОС В ЧАТ № 1:
'''
x = 7
x = str(x)
print(x * 2)
'''
# Ответ: 77


# ВОПРОС В ЧАТ № 2:
'''
a1 = '5'
a2 = 5
print(a1 == a2)
'''
# Ответ: False


# ВОПРОС В ЧАТ № 2:
'''
print(int(3.9))  # 3
# print(int('3.9'))  # 3
# ValueError: invalid literal for int() with base 10: '3.9'
print(round(3.9))  # 4
'''
# Ответ: 3


# f-строки
'''
age = int(input('Введите возраст пользователя: '))
name = input('Введите имя пользователя: ')

print('Привет', name, '! Тебе сейчас', age, 'лет?')

print(f'Привет {name}! Тебе сейчас {age} лет?')
'''


# Базовая арифметика
"""
a, b = 7, 2

print(f'{a} + {b} = {a + b} \n'  # \n - символ перехода на новую строку 
      f'{a} - {b} = {a - b} \n'
      f'{a} * {b} = {a * b} ')

print()  # В каждой функции print() есть переход на новую строку

# Три типа делений в python
print(f'{a} / {b} = {a / b}')  # 3.5 - обычное вещественное деление, то есть результат дробь
print(f'{a} // {b} = {a // b}')  # 3 - целоичисленное деление, то есть результат всегда int
print(f'{a} % {b} = {a % b}')  # 1 - взятие остатка от деления - тоже всегда int


n = 4387
print(n // 10)  # 438
print(n % 10)  # 7 - берет последнюю цифру числа

print(n // 100)  # 43
print(n % 100)  # 87 - берет последние две цифры числа

print(n % 1000)  # 387 - берет последние три цифры числда


x = 5
if n % 2 == 0:
    print('Делится на 2 | Кратно 2 | Четное')
if n % 2 != 0:
    print('Не делится на 2 | Не кратно 2 | Нечетное')



# мне просто попадалось задание, где надо было
# узнать последнюю цифру 10-ричного числа в 8-чной системе
'''
n = 1000
print(int(oct(n)[2:]) % 10)  # 1750 -> 0

print(n % 8)  # 0
'''


print(f'Возведение числа 4 в степень 2: {4 ** 2}')  # 16

print(f'Взять квадратный корень от числа 16: {16 ** (1 / 2)}')  # 4.0
print(f'Взять кубический корень от числа 27: {27 ** (1 / 3)}')  # 3.0

import math
print(f'Взять квадратный корень от числа 16: {math.sqrt(16)}')  # 4.0
"""


# Несколько спосбов подключения библиотек


# ctrl + B - показывает документацию по библиотекам/фукциям
'''
import math  # Самое базовое подключение библиотеки
print(math.sqrt(16))


import math as m  # Подключение библиотеки с коротким именем
print(m.sqrt(16))


from math import sqrt, factorial, prod  # Подключаем только необходимые функции/константы
print(sqrt(16))
print(factorial(5))


from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(factorial(5))
print(prod([1, 2, 3, 4, 5]))
'''


# Несколько библиотек, которые используются на ЕГЭ
"""
# 1.  itertools - для решения 8 и 1 номера, а так же пригождается в 9, 17, 24, 25
count = 0
from itertools import permutations
for p in permutations('abc'):
    count += 1
    print(count, p)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')

'''
count = 0
from itertools import *
for p in permutations('abc'):
    count += 1
    print(count, p)
    # TypeError: unsupported operand type(s) for +=: 'type' and 'int'
'''

# 2. turtle - для решения 6 номера ЕГЭ

import turtle as t


# 3. ipaddress - для решения 10 номера

from ipaddress import *


# 4. Обе библиотеки решают 25 номер на маски и помогают решать 24 номер

from fnmatch import *
from re import *


# 5. Помогают решать 16 номер

import sys
from functools import *

# 6. Библиотека math - для решения 19-21 и 27 номера

from math import ceil, floor, dist

# 7. Библиотека string - просто полезно

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']


from string import *

alp = digits + ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(alp[:2])  # 01
print(alp[:8])  # 01234567
"""



# Условные операторы: if, elif, else
'''
n = int(input('n: '))
if n > 0:  # - если 
    print('Число положительное')
elif n < 0:  # иначе если 
    print('Число отрицательное')
else:  # иначе 
    print('Число равно 0')
'''

'''
x, y = -4, 5
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертя четверть')
else:
    print('Лежит на осях')
print('Конец программы. ')
'''



# Логические связки: and, or, not, in, not in

a, b, c = 4, -5, -6

if a > 0 and b > 0 and c > 0:
    print('AND - Все три условия выполнились. ')
if a > 0 or b > 0 or c > 0:
    print('OR - Проверяет, что хотя бы одно условие выполняется')
if (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or ( a < 0 and b < 0 and c > 0):
    print('Выполняется только одно условие ')


print(True + True + True + False)  # 3
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Выполняеются все три условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Выполняется не более двух условий')


s = '5k34j54k3lj5kl34'

for x in s:
    print(x, end=' ')  # 5 k 3 4 j 5 4 k 3 l j 5 k l 3 4
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 5 3 4 5 4 3 5 3 4
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # k j k l j k l
print()


s = '254435435'
summa = 0
for x in s:
    summa += int(x)
print(summa)  # 35

s = '25a443x5.43 5'
summa = 0
for x in s:
    if x in '0123456789':
        summa += int(x)
print(summa)  # 35
# ValueError: invalid literal for int() with base 10: 'a'










