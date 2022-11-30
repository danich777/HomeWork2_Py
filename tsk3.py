#3.Реализуйте алгоритм перемешивания списка. Встроенный
# алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

def my_shuffle(list):
    m = len(list)
    while (m):
        m -= 1
        i = rnd(0, m)
        list[m], list[i] = list[i], list[m]
    return list

size = int(input('Введите размер списка: '))
rnd_list = []

for i in range (size):
    rnd_list.append(rnd(0,100))

print(rnd_list)
my_shuffle(rnd_list)
print(rnd_list)
