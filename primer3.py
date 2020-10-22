#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение: ")
    n = int(input("Введите длину: "))
    if len(s) >= n:
        print(
            "Заданная длина должна быть больше длины предложения",
            file=sys.stderr
        )
        exit(1)

    words = s.split(' ')

    if len(words) < 2:
        print(
            "Предложение должно содержать несколько слов",
            file=sys.stderr
        )
        exit(1)

    delta = n
    for word in words:
        delta -= len(word)

    w, r = delta // (len(words) - 1), delta % (len(words) - 1)

    lst = []

    for i, word in enumerate(words):
        lst.append(word)

        if i < len(words) - 1:

            width = w
            if r > 0:
                width += 1
                r -= 1

            if width > 0:
                lst.append(' ' * width)

    print(''.join(lst))