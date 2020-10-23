#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input("Введите арифметическое выражение: ")

    left = 0
    right = 0
    rightscob = -1

    for i in range(len(a)):
        if a[i] == "(":
            left += 1

        if a[i] == ")":
            right += 1

        if right > left:
            rightscob = i
            break

    if a.count("(") == a.count(")"):
        print("Скобки расставлены правильно")
    elif rightscob != -1:
        print(f"Лишняя правая скобка на позиции: {rightscob}")
    elif a.count("(") > a.count(")"):
        print(f"Колличество лишних левых скобок: {a.count('(') - a.count(')')}")