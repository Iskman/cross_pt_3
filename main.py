#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если во втором столбце стоят две единицы, то уменьшить макс. элемент первой
# строки в два раза, а все единицы в таблице заменить нулями.

import random  # импортируем модуль random для генерации случайных чисел


def random_array(n, m, max_value=20):
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = random.randint(0, max_value)
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
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
            one_count = 0
            for i in array:  # перебираем каждую строку
                for j in i:  # если есть хотя бы один нулевой элемент
                    if j == 0:
                        one_count += 1  # ведем подсчет нулей
            if one_count == 0:  # если число нулей равно нулю
                print("Не найдены нулевые элементы")
                print("Задание задание не выполнится.")
                # Далее цикл начнется сначала
            else:
                print("Найден нулевой элемент, задание выполнится.")

                i = 0
                for ar1 in array:
                    j = 0
                    for ar2 in ar1:
                        array[i][j] = 0
                        j += 1
                    i += 1

                # Выводим на экран результаты
                print("")
                print("Все единицы были заменены на нули.")
                print_array(array)
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выходим из программы


if __name__ == '__main__':
    main()
