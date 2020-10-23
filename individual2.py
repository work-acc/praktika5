#!/usr/bin/env python3
# -- coding: utf-8 --

if __name__ == '__main__':
    s1 = input("Введите первое слово: ")
    s2 = input("Введите второе слово: ")
    z = 0
    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            z += 1
    if z:
        print(f"{z} начальные буквы первого слова, совпадают со вторым")
    else:
        print("Совпадений нет")







