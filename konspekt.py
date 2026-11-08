
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
'''
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
'''


# УРОК 02. ОСНОВЫ PYTHON. ЧАСТЬ 2


# Цикл while отвечат на запросы: "выполняй действие ПОКА условие верно", "бесконечные циклы"


'''
i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
print('Выход из цикла while')
'''


# Бесконечные циклы и операторы break, continue и функция exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # - прерывает итеррацию цикла (шаг)
    if k == 50_000:
        break  # - прерывает выполнение цикла в котором лежит
    if k == 50_000:
        exit()  # - прерывает выполнение всей программы
    print(k)
print('Выход из программы.')
'''


# Пример номер 1:
'''
x = 5
while x > 0:
    x -= 2  # x = x - 2
    print(x, end=' ')  # 3 1 -1 
'''

# Пример номер 2:
'''
n = 204
while n > 0:
    print(n % 10, end=' ')  # 4 0 2 
    n //= 10
'''


# Переводы в различные системы счисления
'''
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)  # 1000
'''

# 0 1 2 3 4 5 6 7 8 9 A B
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']
'''

# Универсальная функция перевода в различные системы счисления
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(8, 2))  # 1000
print(convert(8, 3))  # 22
print(convert(10**8, 16))  # 5F5E100

print(int('1000', 2))  # 8
print(int('5F5E100', 16))  # 100000000
'''


'''
print(bin(8)[2:])
print(f'{8:b}')

print(oct(8)[2:])
print(f'{8:o}')

print(hex(8)[2:])
print(f'{8:x}')
'''


# Цикл for отвечает на запросы: "повтори n раз", "пробеги числа от А до В"

# Работа цикла for с функцией range

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

'''
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(5, 30, 5):
    print(i, end=' ')  # 5 10 15 20 25 
print()

for i in range(1, 10, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):
    print(i, end=' ')  #
print()

for i in range(10-1, 0-1, -1):
    print(i, end=' ')  # 9 8 7 6 5 4 3 2 1 0
print()
'''


# Пример номер 3:
'''
s = 0
for i in range(4):
    s += i
print(s)  # 6
'''


# Цикл for в том числе может работать с последовательностями
'''
# i  01234567
s = 'a0b2cd3e'


for x in s:
    print(x, end=' ')  # a 0 b 2 c d 3 e
print()

summa = 0
for x in s:
    if x in '0123456789':
        summa += int(x)  
print(summa)  # 5
'''


# Типы данных коллекций (последовательностей)
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']  # list (список)
# -i -5   -4   -3   -2   -1

# 1. Могут в себе хранить неограниченное кол-во элементов
# 2. Элементы могут быть в различных типах данных
# 3. Каждый элемент списка имеет свой порядковый номер: индекс
# 4. Индексы могут считаться слева направо начиная с 0 или справа налево начиная с -1
# 5. Мы можем через индексы изменять значение элементов списка

L[0], L[-1] = L[-1], L[0]
print(L)  # ['e', 'b', 'c', 'd', 'a']

L[0] = L[0].upper()
L[-1] = 'A'
print(L)  # ['E', 'b', 'c', 'd', 'A']


L = ['a', 'b', 'c', 'd', 'e']
print(f'Первый элемент списка L: {L[0]}')  # a
print(f'Последний элемент списка L: {L[-1]}')  # e


M = [2, 'True', True, 4/2, [1, 2, 3]]
for x in M:
    print(type(x), x)
    # <class 'int'> 2
    # <class 'str'> True
    # <class 'bool'> True
    # <class 'float'> 2.0
    # <class 'list'> [1, 2, 3]


T = ('a', 'b', 'c', 'd', 'e')  # tuple (кортеж)
# 1. Все тоже самое, что списки, но не может изменять элементы кортежа

S = {'a', 'b', 'c', 'd', 'e'}  # set (множество)
# 1. Не могут хранить копии элементов

M = [1, 2, 132, 312, 3, 12, 123, 123, 12, 3, 12]
print(len(M))  # 11 - всего элементов 
print(len(set(M)))  # 7 - кол-во различных элементов 
'''


# Пример номер 4
'''
a = [1, 2, 3]

for x in a:
    x *= 2

print(a)  # [1, 2, 3]

a = [1, 2, 3]
print(len(a))  # возвращает кол-во элементов в последовательности
for i in range(len(a)):
    # print(i, end=' ')  # 0 1 2
    print(a[i], end=' ')  # 1 2 3
print()

for i in range(len(a)):
    a[i] = a[i] * 2
print(a)  # [2, 4, 6]
'''


# Срезы списков и строк (последовательностей)
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

# СРЕЗ[:STOP-1]
# СРЕЗ[START:STOP-1]
# СРЕЗ[START:STOP-1:STEP]

print(L[0])  # a

print(L[1:4])  # ['b', 'c', 'd']
print(L[:4])  # ['a', 'b', 'c', 'd']
print(L[1:])  # ['b', 'c', 'd', 'e']

print(L[2:])  # ['c', 'd', 'e'] - все элементы кроме первых двух
print(L[1:-1])  # ['b', 'c', 'd'] - все элементы кроме первого и последнего

print(L[0::2])  # ['a', 'c', 'e'] - все четные индексы
print(L[1::2])  # ['b', 'd'] - все нечетные индексы

print(L[:])  # ['a', 'b', 'c', 'd', 'e']
print(L[::])  # ['a', 'b', 'c', 'd', 'e']

print(L[::-1])  # ['e', 'd', 'c', 'b', 'a'] - все элементы в обратном порядке

# i  0123456789
s = '111122223333'
s = s[:4] + s[8:]
print(s)  # 11113333

# i  0123456789
s = '111122223333'
s = s[:4] + '0000' + s[8:]
print(s)  # 111100003333
'''


# Функции списков и строк
'''
M = [1, 3, 2, 3, 3, 2]
s = '132332'

print(len(M), len(s))  # 6 6
print(sum(M))  # 14
print(min(M), max(M))  # 1 3
print(min(s), max(s))  # 1 3

print(set(M), set(s))  # {1, 2, 3} {'1', '3', '2'}

print(sorted(M))  # [1, 2, 2, 3, 3, 3]
print(sorted(s))  # ['1', '2', '2', '3', '3', '3']

print(sorted(M)[::-1])  # [3, 3, 3, 2, 2, 1]
print(sorted(s)[::-1])  # ['3', '3', '3', '2', '2', '1']

print(eval('2 + 2'))  # 4
print(eval('3 * 2 + 2'))  # 8
print(eval('3 * (2 + 2)'))  # 12
'''


# Методы списков и строк
'''
s = '12121212'
print(s.count('2'))  # 4


M = ['1', 2, '1', '2', 1, 2, 1, 2]
print(M.count('2'))  # 1
print(M.count(2))  # 3


s = '12121212'
s = s.replace('2', '*')
print(s)  # 1*1*1*1*

s = s.replace('*', '+', 2)
print(s)  # 1+1+1*1*

# i  01234567
s = 'feshjfEKLIJRLWKER'
print(s.upper())  # FESHJFEKLIJRLWKER
print(s.lower())  # feshjfeklijrlwker

s = s[:6].upper() + s[6:].lower()
print(s)  # FESHJFeklijrlwker


id = '123.43.255.0'
print(id.split('.'))  # ['123', '43', '255', '0']

p = ['123', '43', '255', '0']
new_id = ' * '.join(p)
print(new_id)  # 123 * 43 * 255 * 0
'''

'''
M = [2, 2, 1, 1, 3, 2, 3]

M.sort()
print(M)  # [1, 1, 2, 2, 2, 3, 3]

M.reverse()
print(M)  # [3, 3, 2, 2, 2, 1, 1]


M = [2, 2, 1, 1, 3, 2, 3]
M = sorted(M)
print(M)  # [1, 1, 2, 2, 2, 3, 3]
M = M[::-1]
print(M)  # [3, 3, 2, 2, 2, 1, 1]


M = [1, 2, 3]
M.append(4)
M.append(5)
print(M)  # [1, 2, 3, 4, 5]
M.reverse()
M.append(0)
M.reverse()
print(M)  # [0, 1, 2, 3, 4, 5]


M = [1, 2, 3]
M = [0] + M + [4, 5]
print(M)  # [0, 1, 2, 3, 4, 5]
'''


# Генераторы списков

N = []
n = 23487
while n > 0:
    x = n % 10
    N.append(x)
    n //= 10
N = N[::-1]
print(N)  # [2, 3, 4, 8, 7]


N = []
n = 23487
n = str(n)
for x in n:
    N.append(int(x))
print(N)  # [2, 3, 4, 8, 7]


# генартор[что_кладем откуда_берем]
# генартор[что_кладем откуда_берем при_каком_условии]

print([int(x) for x in str(23487)])  # [2, 3, 4, 8, 7]

print([i for i in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print([i for i in range(10) if i % 2 == 0])  # [0, 2, 4, 6, 8]


print([i ** 2 for i in range(10) if i % 2 == 0])  # [0, 4, 16, 36, 64]

from random import randint
N = [randint(0, 10000) for _ in range(100)]

print([x for x in N if x % 2 == 0])

print([x for x in N if N.count(x) == 2])  # [3320, 3320]

print([x for x in N if len(str(x)) == 3])  # [402, 651, 556, 552, 312, 372, 791]

print([x for x in N if len(str(x)) == 3 and x % 10 == 2])  # [402, 552, 312, 372]












