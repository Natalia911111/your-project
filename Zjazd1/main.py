# This is a sample Python script.
from random import randint, random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

temp = 15
temp_2 = '15'
'''
type(temp)
type(temp_2)

if type(temp)==int:
    temp = temp*5
    print(temp)
elif type(temp)==float:
    temp = temp/5
    print(temp)
elif type(temp)==str:
    print(temp)
'''

def rps():
    l = input("Podaj liczbę:")
    l = int(l)

    if l > 0 and l < 4:
        pass
    else:
        raise Exception("Zły zakres")

    comp = randint(1,3)
    print(comp)

    if l == comp:
        return "Remis"
    elif (l == 1 and comp ==2) \
            or (l== 3 and comp ==1) \
            or (l==2 and comp ==3):
        return "człowiek wygrał"
    else:
        return "Komputer wygrał"

'''
print(rps())
#z = rsp()
#print(z)
'''
'''
no_of_stars = randint(1,20)
print("Wylosowana liczba gwiazek", no_of_stars * '*')
'''
def zadanie1():
    rows = randint(5,15)
    columns = randint(5,15)

    print(f'Wylosowana liczba rows: {rows}')
    print(f'Wylosowana liczba kolumn: {columns}')

    for i in range(rows):
        print(columns * '*')

#zadanie1()

def zadanie3():
    size = randint(3,9)
    print(f'Wielkość choinki: {size}')

    for i in range(size+1):
        print(i * '*')

#zadanie3()

def zadanie3_1():
    size = randint(3, 9)
    print(f'Wielkość choinki: {size}')

    for i in range(size+1):
        gwiazdka = ''
        for z in range(i):
            gwiazdka += '*'
        print(gwiazdka)

#zadanie3_1()

def square(num):
    return num * num

def square_print(num):
    print(num * num)

#a = square(10) + 10
#print(a)

#b = square_print(10) + 10
#print(b)

def multiply(subject, times):
    return subject * times

#print(multiply(2,3))
#print(multiply('6',3))

def power(base,exponent=2):
    wynik = 1
    for i in range(exponent):
        wynik *= base

    return wynik

#print(power(2,4))

def convert_to_usd(zlotys):
    return round(zlotys / 3.85,2)

#print(convert_to_usd(10))

def to_celsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9

#print(to_celsius(100))

def calculate_net(gross,vat=random()):
    print(vat)
    if vat>1 or vat <0:
        raise Exception("Vat tooooo big")
    else:
        return gross / (1+vat)

#print(calculate_net(100,2))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#print(is_even(3))

def iterate_through(number):
    for i in range(1,number+1):
        if is_even(i):
            print(i, is_even(i))

iterate_through(6)


