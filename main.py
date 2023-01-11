#!/usr/bin/env python3
# coding=utf-8

# Имеется двухмерный массив 4x5 в виде списка в списке. Сделать консольную программу, которая
# осуществляет заданный вариантом алгоритм обработки данных.

# ИСКАКОВ МАНСУР
# ВАРИАНТ 4

# Определить, имеется ли в таблице хотя бы один нулевой элемент. Если такой элемент есть, то заменить все
# вещественные значения таблицы единицами

import random  # импортируем модуль random для генерации случайных чисел


def random_array(n, m, max_value=2.5): # значение лишь до 2.5 чтобы увеличить вероятность получить 0 в массиве
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = round(random.uniform(0, max_value), 1) # изменил, чтобы получить вещественное число
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%.2f\t" % j, end='')
        print()


def main():
    array = random_array(4, 5)
    print_array(array)
    while True:
        print
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':
            array = random_array(4, 5)
            print_array(array)
        elif key == '2':
            print()
            zero_count = 0
            for i in array:  # перебираем каждую строку
                for j in i:  # если есть хотя бы один нулевой элемент
                    if j == 0:
                        zero_count += 1  # ведем подсчет нулей
            if zero_count == 0:  # если число нулей равно нулю
                print("Не найдены нулевые элементы")
                print("Задание задание не выполнится.")
                # Далее цикл начнется сначала
            else:
                print("Найден нулевой элемент, задание выполнится.")

                i = 0
                for ar1 in array:
                    j = 0
                    for ar2 in ar1:
                        if not float.is_integer(array[i][j]): # проверяем, вещественная ли переменная
                            array[i][j] = 1
                        j += 1
                    i += 1

                # Выводим на экран результаты
                print("")
                print("Все вещественные числа были заменены на единицы.")
                print_array(array)
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выходим из программы


if __name__ == '__main__':
    main()
