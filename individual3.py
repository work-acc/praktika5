#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input('Введите слово: ')
    s = s[-1:] + s[0] + s[1:-1]
    print(s)
